import itertools
import json
import pathlib
import shlex
import shutil
import subprocess
import tempfile

import typer
import uv


class MeltanoUtil:
    def __init__(self):
        pass

    @staticmethod
    def get_cwd():
        return pathlib.Path(__file__).parent.resolve()

    @staticmethod
    def run_uv(*args: str, **kwargs) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            (
                uv.find_uv_bin(),
                *args,
            ),
            stdout=subprocess.PIPE,
            text=True,
            **kwargs,
        )

    @staticmethod
    def plugin_venv(plugin_name: str, plugin_type: str) -> pathlib.Path:
        dot_hub_utils = pathlib.Path(".hub_utils")
        dot_hub_utils.mkdir(parents=True, exist_ok=True)
        return dot_hub_utils / plugin_type / plugin_name / "venv"

    @staticmethod
    def add(
        plugin_name: str,
        pip_url: str,
        plugin_type: str,
        *,
        python: str | None = None,
    ):
        venv_path = MeltanoUtil.plugin_venv(plugin_name, plugin_type)

        python = python or shutil.which("python")
        if not python:
            raise ValueError("Python not found in PATH")

        MeltanoUtil.run_uv("venv", venv_path.as_posix())
        MeltanoUtil.run_uv("pip", "install", *shlex.split(pip_url), "--prefix", venv_path.as_posix())

    @staticmethod
    def _base_plugin_command(
        plugin_name: str,
        executable: str,
        plugin_type: str,
    ) -> str:
        return MeltanoUtil.plugin_venv(plugin_name, plugin_type).joinpath("bin", executable).as_posix()

    @staticmethod
    def help_test(
        plugin_name: str,
        executable: str,
        plugin_type: str,
        config: dict | None = None,
    ):
        base_command: tuple[str, ...] = (
            MeltanoUtil._base_plugin_command(
                plugin_name,
                executable,
                plugin_type,
            ),
            "--help",
        )

        if config:
            with tempfile.NamedTemporaryFile(mode="w+") as tmp:
                json.dump(config, tmp)
                tmp.flush()
                subprocess.run(
                    (
                        *base_command,
                        "--config",
                        tmp.name,
                    ),
                    stdout=subprocess.PIPE,
                    text=True,
                    check=True,
                )
        else:
            subprocess.run(
                base_command,
                stdout=subprocess.PIPE,
                text=True,
                check=True,
            )

    @staticmethod
    def sdk_about(
        plugin_name: str,
        executable: str,
        plugin_type: str,
        config: dict | None = None,
    ):
        base_command: tuple[str, ...] = (
            MeltanoUtil._base_plugin_command(
                plugin_name,
                executable,
                plugin_type,
            ),
            "--about",
            "--format",
            "json",
        )

        if config:
            with tempfile.NamedTemporaryFile(mode="w+") as tmp:
                json.dump(config, tmp)
                tmp.flush()
                about_content = subprocess.run(
                    (
                        *base_command,
                        "--config",
                        tmp.name,
                    ),
                    stdout=subprocess.PIPE,
                    text=True,
                    check=True,
                )
                about_json_str = about_content.stdout.split("Setup Instructions:")[0]
                return json.loads(about_json_str)
        else:
            about_content = subprocess.run(
                base_command,
                stdout=subprocess.PIPE,
                text=True,
                check=True,
            )
            return json.loads(about_content.stdout)

    @staticmethod
    def _get_maintainer(
        variant,
    ):
        maintainer = "community"
        if variant in ["meltano", "meltanolabs"]:
            maintainer = "official"
        elif variant in ["matatika", "autoidm", "hotglue", "hotgluexyz"]:
            maintainer = "partner"
        return maintainer

    @staticmethod
    def _evaluate_official(is_sdk_based, usage_count, responsiveness) -> str:
        quality = "bronze"
        if is_sdk_based:
            quality = "gold"
        elif usage_count >= 1 and responsiveness != "low":
            quality = "silver"
        return quality

    @staticmethod
    def _evaluate_partner(is_sdk_based, usage_count, responsiveness) -> str:
        quality = "bronze"
        if is_sdk_based:
            quality = "gold"
        elif usage_count >= 1 and responsiveness != "low":
            quality = "silver"
        return quality

    @staticmethod
    def _evaluate_community(variant, is_sdk_based, usage_count, responsiveness) -> str:
        legacy_partners = ["singer-io", "airbyte", "transferwise"]
        quality = "unknown"
        if is_sdk_based and usage_count >= 6 and responsiveness != "low":
            quality = "gold"
        elif is_sdk_based:
            quality = "silver"
        elif usage_count >= 1 and responsiveness != "low":
            quality = "silver"
        elif usage_count >= 6 and variant in legacy_partners:
            quality = "silver"
        elif usage_count >= 1:
            quality = "bronze"
        elif variant in legacy_partners:
            quality = "bronze"
        return quality

    @staticmethod
    def get_quality(variant, is_sdk_based, usage_count, responsiveness):
        maintainer = MeltanoUtil._get_maintainer(variant)
        if maintainer == "official":
            quality = MeltanoUtil._evaluate_official(is_sdk_based, usage_count, responsiveness)
        elif maintainer == "partner":
            quality = MeltanoUtil._evaluate_partner(is_sdk_based, usage_count, responsiveness)
        elif maintainer == "community":
            quality = MeltanoUtil._evaluate_community(variant, is_sdk_based, usage_count, responsiveness)
        return quality

    @staticmethod
    def _get_label(name):
        new_label = []
        for label_word in name.replace("_", " ").replace("-", " ").replace(".", " ").split(" "):
            label_word = label_word.title()
            new_label.append(
                label_word.replace("Aws", "AWS")
                .replace("Url", "URL")
                .replace("Id", "ID")
                .replace("Db", "Database")
                .replace("Api", "API")
                .replace("Oauth", "OAuth")
                .replace("Ssh", "SSH")
                .replace("Ssl", "SSL")
                .replace("Gzip", "GZIP")
                .replace("Jsonl", "JSONL")
                .replace("Sqlalchemy", "SQLAlchemy")
            )
        return " ".join(new_label)

    @staticmethod
    def _parse_kind(kind, settings, format=None):
        setting = settings.get("name")
        setting = setting.lower()
        if kind == "string":
            if format in ("date-time", "date") or setting in ("start_date", "end_date"):
                return "date_iso8601", None
            if (
                any(id_str.lower() in setting for id_str in ["password", "id", "token", "key", "secret"])
                or format == "airbyte_secret"
            ):
                return "password", None
            if allowed_values := settings.get("enum"):
                option_parsed = [{"label": MeltanoUtil._get_label(val), "value": val} for val in allowed_values]
                return "options", option_parsed
            return "string", None
        if kind == "number":
            return "integer", None
        # TODO: Meltano doesnt support array enums as of today
        # if kind == 'array':
        #     enum = settings.get('items', {}).get('enum')
        #     if enum:
        # option_parsed = [
        #     {'label': MeltanoUtil._get_label(val), 'value': val}
        #      for val in enum
        # ]
        #         return 'options', option_parsed
        #     return 'array', None
        else:
            return kind, None

    @staticmethod
    def _default_description(setting):
        setting = setting.lower()
        if setting == "start_date":
            return (
                "Determines how much historical data will be extracted. "
                "Please be aware that the larger the time period and amount "
                "of data, the longer the initial extraction can be expected "
                "to take."
            )
        if setting == "end_date":
            return "Date up to when historical data will be extracted."
        elif setting == "batch_config.encoding.format":
            return "Format to use for batch files."
        elif setting == "batch_config.encoding.compression":
            return "Compression format to use for batch files."
        elif setting == "batch_config.storage.root":
            return "Root path to use when writing batch files."
        elif setting == "batch_config.storage.prefix":
            return "Prefix to use when writing batch files."
        else:
            return None

    @staticmethod
    def _dedup_settings(reformatted_settings):
        reformatted_settings_2 = {}
        for setting in reformatted_settings:
            name = setting.get("name")
            if name in reformatted_settings_2:
                existing_setting = reformatted_settings_2.get(name)
                existing_setting["description"] = ", ".join(
                    [
                        existing_setting["description"],
                        MeltanoUtil._clean_description(setting.get("description")),
                    ]
                )
            else:
                reformatted_settings_2[name] = setting
        return [value for key, value in reformatted_settings_2.items()]

    @staticmethod
    def _handle_description(description, name, enforce_desc):
        if not description:
            if enforce_desc:
                description = typer.prompt(
                    f"[{name}] `description`",
                    default=MeltanoUtil._default_description(name),
                )
            else:
                if name == "tag":
                    description = "Airbyte image tag"
                else:
                    description = ""
        return description

    @staticmethod
    def _get_kind_from_type(type, name, enforce_desc):
        if isinstance(type, list):
            kind = next(s_type for s_type in type if s_type != "null")
        else:
            kind = type

        if not kind:
            if name == "faker_config.locale":
                kind = "array"
            elif enforce_desc:
                kind = typer.prompt(f"[{name}] `kind`", default="string")
            else:
                name = name
                print(f"No type found for: {name}. Defaulting to string")
                kind = "string"
        return kind

    @staticmethod
    def _parse_sdk_about_settings(sdk_about_dict, enforce_desc=False):
        """Parse SDK about settings into a format suitable for Meltano.

        Args:
            sdk_about_dict: Dictionary containing SDK about information
            enforce_desc: Whether to enforce descriptions for settings

        Returns:
            Tuple of (settings, validation_groups, capabilities)
        """
        settings_raw = sdk_about_dict.get("settings", {})
        reformatted_settings = []
        settings_group_validation = []
        base_required = settings_raw.get("required", [])

        # Process dependent required fields
        dependent_required_groups = []

        # First collect all settings
        for settings in MeltanoUtil._traverse_schema_properties(settings_raw):
            name = settings.get("name")
            title = settings.get("title")
            description = MeltanoUtil._handle_description(
                MeltanoUtil._clean_description(settings.get("description")),
                name,
                enforce_desc,
            )
            setting_details = {
                "name": name,
                "label": title or MeltanoUtil._get_label(name),
                "description": description,
            }
            kind = MeltanoUtil._get_kind_from_type(settings.get("type"), name, enforce_desc)

            kind, options = MeltanoUtil._parse_kind(kind, settings)
            setting_details["kind"] = kind
            if options:
                setting_details["options"] = options
            if settings.get("default") is not None:
                if kind != "date_iso8601":
                    setting_details["value"] = settings.get("default")
            if kind == "password":
                setting_details["sensitive"] = True
            reformatted_settings.append(setting_details)
            if settings.get("required"):
                settings_group_validation.append(settings.get("name"))

        # Process top-level dependentRequired
        if "dependentRequired" in settings_raw:
            for field, required_fields in settings_raw.get("dependentRequired", {}).items():
                if required_fields:
                    dependent_required_groups.append([field, *required_fields])

        # Process nested dependentRequired by traversing the schema again
        MeltanoUtil._collect_nested_dependent_required(settings_raw, "", dependent_required_groups)

        deduped_settings = MeltanoUtil._dedup_settings(reformatted_settings)

        # Add base required fields and dependent required groups to settings_group_validation
        validation_groups = [list(set(settings_group_validation + base_required))]
        validation_groups.extend(dependent_required_groups)

        return (
            deduped_settings,
            [group for group in validation_groups if group],
            sdk_about_dict.get("capabilities"),
        )

    @staticmethod
    def _collect_nested_dependent_required(schema, parent_path, dependent_groups, field_sep="."):
        """Collect nested dependentRequired fields and add them to dependent_groups."""
        for key, value in schema.get("properties", {}).items():
            current_path = key if not parent_path else f"{parent_path}{field_sep}{key}"

            # Check if this object has dependentRequired
            if isinstance(value, dict) and "dependentRequired" in value:
                for dep_field, dep_required_fields in value.get("dependentRequired", {}).items():
                    if dep_required_fields:
                        # Create full paths for dependent fields
                        full_path_field = f"{current_path}{field_sep}{dep_field}"
                        full_path_required = [f"{current_path}{field_sep}{req}" for req in dep_required_fields]
                        dependent_groups.append([full_path_field, *full_path_required])

            # Recursively check nested objects
            if isinstance(value, dict) and "properties" in value:
                MeltanoUtil._collect_nested_dependent_required(value, current_path, dependent_groups, field_sep)

    @staticmethod
    def _traverse_schema_properties(schema, field_sep=".", parent_path=""):
        fields = []
        for key, value in schema.get("properties", {}).items():
            val_type = value.get("type", "string")
            reqs = value.get("required", [])
            if (val_type == "object" or "object" in val_type) and (value.get("properties") or value.get("oneOf")):
                for subfield in MeltanoUtil._traverse_schema_properties(value):
                    sub_name = subfield.get("name")
                    full_name = f"{key}{field_sep}{sub_name}"
                    field = {
                        "name": full_name,
                        "description": MeltanoUtil._clean_description(subfield.get("description")),
                        "default": subfield.get("default"),
                        "type": subfield.get("type"),
                        "title": subfield.get("title"),
                        "const": subfield.get("const"),
                        "items": subfield.get("items"),
                        "enum": subfield.get("enum"),
                    }
                    if "required" in subfield:
                        # accept parent if it was set already
                        field["required"] = subfield["required"]
                    else:
                        field["required"] = sub_name in reqs

                    fields.append(field)
            else:
                fields.append(
                    {
                        "name": key,
                        "description": MeltanoUtil._clean_description(value.get("description")),
                        "default": value.get("default"),
                        "type": value.get("type"),
                        "title": value.get("title"),
                        "const": value.get("const"),
                        "items": value.get("items"),
                        "enum": value.get("enum"),
                    }
                )
        for item in schema.get("oneOf", []):
            for i in MeltanoUtil._traverse_schema_properties(item):
                if i.get("const"):
                    i["description"] = i.get("const") or item.get("title")
                fields.append(i)
        return fields

    @staticmethod
    def _split_sentence_endings(word_list):
        desc_list_clean = []
        for word in word_list:
            if any(i in word for i in ["i.e.", "e.g."]):
                desc_list_clean.append(word)
                continue
            elif len(word.split(".")) > 1 and not word.startswith("."):
                if word.split(".")[0][-1].isnumeric() and word.split(".")[1] and word.split(".")[1][0].isnumeric():
                    # its numeric
                    desc_list_clean.append(word)
                    continue
                if not any(
                    keyword in word
                    for keyword in (
                        "http",
                        "ssh",
                        "ssl",
                        "e.g.",
                        '"',
                        "`",
                        "()",
                        ".com",
                    )
                ):
                    desc_list_clean.extend(word.replace(".", ". ").split())
                    continue
            desc_list_clean.append(word)
        return " ".join(desc_list_clean)

    @staticmethod
    def _last_element(lst):
        if lst:
            return lst[-1]
        else:
            return ""

    @staticmethod
    def _capitalize(cleaned_sentence):
        capital_list = cleaned_sentence.split(". ")
        clean_capital_list = []
        for elem in capital_list:
            sentence_list = elem.split()
            last_elem = MeltanoUtil._last_element(clean_capital_list)
            if (
                sentence_list[0][0].isupper()
                or sentence_list[0][0] == "'"
                or last_elem.endswith("e.g")
                or last_elem.endswith("i.e")
                or sentence_list[0].startswith("tap-")
                or sentence_list[0].startswith("target-")
                or sentence_list[0].startswith("http")
            ):
                clean_capital_list.append(" ".join(sentence_list))
            else:
                sentence_list[0] = sentence_list[0].capitalize()
                clean_capital_list.append(" ".join(sentence_list))

        return ". ".join(clean_capital_list)

    @staticmethod
    def _clean_description(description):
        if not description:
            return description
        if not isinstance(description, str):
            return ""

        # Add a space after sentence ending periods
        desc_list = description.split()
        cleaned_sentence = MeltanoUtil._split_sentence_endings(desc_list)
        cleaned_description = MeltanoUtil._capitalize(cleaned_sentence)
        cleaned_description = cleaned_description.replace("Dbt", "dbt")
        return cleaned_description
