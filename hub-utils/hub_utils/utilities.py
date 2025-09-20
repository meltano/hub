import ast
import csv
import json
import os
import shutil
from collections import OrderedDict
from enum import Enum
from pathlib import Path
from typing import Any

import typer
from jsonpath_ng.ext import parse
from ruamel.yaml import YAML

from hub_utils.meltano_util import MeltanoUtil

from hub_utils.yaml_lint import (  # isort:skip
    fix_arrays,
    fix_yaml,
    fix_yaml_dict_format,
    run_yamllint,
)


OVERRIDES: dict[tuple[str, str], list[dict[str, Any]]] = {
    ("tap-mailchimp", "acarter24"): [
        {
            "jsonpath": parse("$.settings[?(@.name == 'dc')].label"),
            "value": "Data Center",
        }
    ],
    ("tap-totango", "edsoncezar16"): [
        {
            "jsonpath": parse("$.settings[?(@.name == 'api_url')].options[0].label"),
            "value": "US Endpoint",
        },
        {
            "jsonpath": parse("$.settings[?(@.name == 'api_url')].options[1].label"),
            "value": "EU Endpoint",
        },
        {
            "jsonpath": parse("$.settings[?(@.name == 'api_url')].options[1].value"),
            "value": "https://api-eu1.totango.com",
        },
    ],
}


class Kind(str, Enum):
    string = "string"
    boolean = "boolean"
    integer = "integer"
    object = "object"
    array = "array"


ALLOWED_CAPABILITIES_TAP = {
    "catalog",
    "properties",
    "discover",
    "state",
    "about",
    "stream-maps",
    "activate-version",
    "batch",
    "schema-flattening",
    "test",
    "log-based",
    "structured-logging",
}

ALLOWED_CAPABILITIES_TARGET = {
    "about",
    "stream-maps",
    "activate-version",
    "batch",
    "schema-flattening",
    "test",
    "soft-delete",
    "hard-delete",
    "datatype-failsafe",
    "structured-logging",
}


class Utilities:
    def __init__(self, auto_accept=False):
        self.yaml = YAML()
        self.auto_accept = auto_accept
        self.hub_root = os.getenv("HUB_ROOT_PATH", ".")
        self.default_variants_path = f"{self.hub_root}/_data/default_variants.yml"
        self.maintainers_path = f"{self.hub_root}/_data/maintainers.yml"

    def get_variant_names(self, plugin_type, metadata_type, skip=0, limit=10000):
        from hub_utils.yaml_lint import find_all_yamls

        formatted_output = []
        for yaml_file in find_all_yamls(f_path=f"{self.hub_root}/_data/meltano/"):
            # Pagination mechanism
            if len(formatted_output) == skip:
                # Clear list and continue iterating
                formatted_output = []
            if len(formatted_output) == limit:
                break
            data = self._read_yaml(yaml_file)
            if plugin_type and yaml_file.split("/")[-3] not in plugin_type.split(","):
                continue

            if metadata_type == "sdk":
                if "meltano_sdk" not in data.get("keywords", []) or "airbyte_protocol" in data.get("keywords", []):
                    continue
                suffix = "/".join(yaml_file.split("/")[-3:])
                formatted_output.append({"plugin-name": suffix})

            if metadata_type == "airbyte":
                if "airbyte_protocol" not in data.get("keywords", []):
                    continue
                suffix = "/".join(yaml_file.split("/")[-3:])
                image_name = next(
                    setting.get("value")
                    for setting in data.get("settings")
                    if setting.get("name") == "airbyte_spec.image"
                )
                if not image_name:
                    continue
                formatted_output.append(
                    {
                        "plugin-name": suffix,
                        "source-name": image_name.replace("airbyte/", ""),
                    }
                )
        return formatted_output

    def _prompt(self, question, default_val=None, type=None):
        if self.auto_accept:
            return default_val
        if default_val:
            return typer.prompt(question, default=default_val, type=type)
        else:
            return typer.prompt(question, type=type)

    def _write_yaml(self, path, content, reformat=False):
        with open(path, "w") as f:
            self.yaml.dump(content, f)
            if reformat:
                self._reformat(path)

    def _write_dict(self, path, content):
        Path(os.path.dirname(path)).mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(content, f)

    def _read_yaml(self, path):
        with open(path) as f:
            data = self.yaml.load(f)
        return data

    def _read_json(self, path):
        with open(path) as f:
            data = json.load(f)
        return data

    @staticmethod
    def _get_plugin_name(repo_url: str):
        return repo_url.split("/")[-1]

    @staticmethod
    def _get_plugin_variant(repo_url: str):
        return repo_url.split("/")[-2].lower()

    @staticmethod
    def get_plugin_type(plugin_name: str):
        plugin_name = plugin_name.lower()
        if "tap-" in plugin_name and "target-" in plugin_name:
            raise Exception(f"Type Unknown: {plugin_name}")
        if "tap-" in plugin_name:
            return "extractors"
        if "target-" in plugin_name:
            return "loaders"

    @staticmethod
    def get_plugin_type_from_suffix(suffix: str):
        return suffix.split("/")[0]

    @staticmethod
    def get_plugin_variant_from_suffix(suffix: str):
        return suffix.split("/")[2]

    @staticmethod
    def _boilerplate_capabilities(plugin_type):
        if plugin_type == "extractors":
            return ["catalog", "discover", "state"]
        if plugin_type == "loaders":
            return []

    @staticmethod
    def _scrape_keywords(meltano_sdk, existing=None):
        if existing:
            return str(existing)
        if meltano_sdk:
            return "['meltano_sdk']"
        return "[]"

    @staticmethod
    def _get_label(plugin_name, plugin_type=None):
        # TODO: not sure if this is the best place to do this
        name = plugin_name
        if plugin_type:
            if plugin_type == "extractors":
                name = "".join(plugin_name.split("tap-")[1:])
            elif plugin_type == "loaders":
                name = "".join(plugin_name.split("target-")[1:])
        return name.replace("_", " ").replace("-", " ").title()

    @staticmethod
    def _get_maintenance_status(existing=None):
        if existing:
            return existing
        return "active"

    def _build_settings(self, setting_list):
        settings = []
        settings_group_validation = []
        for setting in setting_list:
            label = self._prompt(f"[{setting}] `label`", default_val=self._get_label(setting))
            kind = self._prompt(
                f"[{setting}] `kind`",
                default_val=MeltanoUtil._parse_kind("string", {"name": setting})[0],
            )
            description = self._prompt(
                f"[{setting}] `description`",
                default_val=MeltanoUtil._default_description(setting),
            )
            required = self._prompt(f"[{setting}] `required`", default_val=False, type=bool)
            setting_details = {
                "name": setting,
                "label": label,
                "description": description,
            }
            setting_details["kind"] = kind
            settings.append(setting_details)
            if required:
                settings_group_validation.append(setting)
        return settings, [settings_group_validation]

    def _compile_settings(self, seed=[]):
        settings = seed
        continue_prompts = True
        prompt_text = "Lets collect all the settings, provide one at a time"
        while continue_prompts and not self.auto_accept:
            setting = self._prompt(f"{prompt_text}", default_val=settings)
            if str(setting) == str(settings):
                break
            settings.append(setting)
            prompt_text = "Return an empty to end"
        return list(set(settings))

    @staticmethod
    def _string_to_literal(value):
        try:
            return ast.literal_eval(value)
        except Exception:
            return value

    def _boilerplate_definition(
        self,
        repo_url,
        plugin_type,
        settings,
        settings_group_validation,
        name,
        namespace,
        pip_url,
        keywords,
        capabilities,
        executable,
        variant,
    ):
        label = self._get_label(name, plugin_type=plugin_type)
        logo_name = label.lower().replace(" ", "-")
        plugin_def = {
            "name": name,
            "variant": variant,
            "label": self._prompt("label", label),
            "logo_url": f"/assets/logos/{plugin_type}/{logo_name}.png",
            "capabilities": capabilities,
            "description": self._prompt("description", ""),
            "domain_url": self._prompt("domain_url", ""),
            "keywords": keywords,
            "maintenance_status": self._prompt("maintenance_status", self._get_maintenance_status()),
            "namespace": namespace,
            "next_steps": "",
            "pip_url": pip_url,
            "quality": self._prompt("quality", "unknown"),
            "repo": repo_url,
            "settings": settings,
            "settings_group_validation": settings_group_validation,
            "settings_preamble": "",
            "usage": "",
        }
        if executable:
            plugin_def["executable"] = executable

        # Add log_parser property if plugin supports structured logging
        if "structured-logging" in capabilities:
            plugin_def["log_parser"] = "singer-sdk"

        return plugin_def

    def _apply_overrides(self, definition: dict[str, Any]) -> dict[str, Any]:
        for override in OVERRIDES.get((definition["name"], definition["variant"]), []):
            expr = override["jsonpath"]
            value = override["value"]
            definition = expr.update(definition, value)

        return definition

    def _write_definition(self, definition, plugin_type):
        dir_name = os.path.join(self.hub_root, "_data", "meltano", plugin_type, definition["name"])
        variant = definition["variant"]

        # Apply overrides
        definition = self._apply_overrides(definition)

        Path(dir_name).mkdir(parents=True, exist_ok=True)
        yaml_path = Path(os.path.join(dir_name, f"{variant}.yml"))
        if not yaml_path.exists():
            self._write_yaml(os.path.join(dir_name, f"{variant}.yml"), definition)
            print("Definition: Updated")
        else:
            # TODO: show a diff or print
            overwrite = self._prompt(
                "Plugin definition already exists, overwrite it?",
                default_val=False,
                type=bool,
            )
            if overwrite:
                self._write_yaml(os.path.join(dir_name, f"{variant}.yml"), definition)
            else:
                print("Definition: Skipping")
        return str(yaml_path)

    def _update_variant_file(self, plugin_type_defaults, plugin_name, plugin_variant, defaults, plugin_type):
        plugin_type_defaults[plugin_name] = plugin_variant
        defaults[plugin_type] = plugin_type_defaults
        self._write_yaml(self.default_variants_path, defaults)
        print("Default: Updated")

    def _handle_default_variant(self, plugin_name, plugin_variant, plugin_type):
        defaults = self._read_yaml(self.default_variants_path)
        plugin_type_defaults = defaults[plugin_type]
        if plugin_name not in plugin_type_defaults:
            self._update_variant_file(plugin_type_defaults, plugin_name, plugin_variant, defaults, plugin_type)
        else:
            current_default = plugin_type_defaults[plugin_name]
            overwrite = self._prompt(
                f"Default variant already exists [{current_default}], overwrite it?",
                default_val=False,
                type=bool,
            )
            if overwrite:
                self._update_variant_file(
                    plugin_type_defaults,
                    plugin_name,
                    plugin_variant,
                    defaults,
                    plugin_type,
                )
            return True

    def _handle_maintainer(self, plugin_variant, repo_url):
        updated_maintainers = self._read_yaml(self.maintainers_path)
        if plugin_variant not in updated_maintainers:
            maintainer_name = plugin_variant
            updated_maintainers[plugin_variant] = {
                "label": maintainer_name,
                "url": "/".join(repo_url.split("/")[:-1]),
                "name": maintainer_name,
            }
            print("Maintainer: Updated")
            updated_maintainers = dict(OrderedDict(sorted(updated_maintainers.items())))
            self._write_yaml(self.maintainers_path, updated_maintainers)
        else:
            print("Maintainer: Skipping")

    def _handle_logo(self, definition, plugin_type, variant_exists):
        if variant_exists and self._prompt("Use current variant's logo?", default_val=True, type=bool):
            return

        image_path = self._prompt("Path to image [.png] file, leave blank to skip", "skip")
        # TODO: kind of a hack, not sure how to accept an empty string to skip properly
        if image_path == "skip":
            logo_file_name = definition["logo_url"].split("/")[-1]
            print("Logo: Placeholder Used")
        else:
            logo_file_name = definition["logo_url"].split("/")[-1]
            shutil.copyfile(
                image_path,
                f"{self.hub_root}/static/assets/logos/{plugin_type}/{logo_file_name}",
            )

    def _reformat(self, file_path):
        fix_yaml(file_path)
        run_yamllint(file_path)

    def _reformat_all(self, plugin_type, plugin_name, variant):
        for file_path in [
            "_data/default_variants.yml",
            "_data/maintainers.yml",
            f"_data/meltano/{plugin_type}/{plugin_name}/{variant}.yml",
        ]:
            self._reformat(f"{self.hub_root}/{file_path}")

    @staticmethod
    def _install_test(
        plugin_name,
        plugin_type,
        pip_url,
        namespace,
        executable,
        python: str | None = None,
    ):
        MeltanoUtil.add(plugin_name, pip_url, plugin_type, python=python)
        MeltanoUtil.help_test(plugin_name, executable, plugin_type)

    def add(
        self,
        repo_url: str | None = None,
        definition_seed: dict | None = None,
        python: str | None = None,
    ):
        plugin_name = self._prompt("plugin name", self._get_plugin_name(repo_url))
        plugin_type = self._prompt("plugin type", self.get_plugin_type(repo_url))
        pip_url = self._prompt("pip_url", f"git+{repo_url}.git")
        namespace = self._prompt("namespace", plugin_name.replace("-", "_"))
        executable = self._prompt("executable", plugin_name)
        is_meltano_sdk = self._prompt("is_meltano_sdk", True, type=bool)
        sdk_about_dict = None
        sdk_about_dict = self._test(
            plugin_name,
            plugin_type,
            pip_url,
            namespace,
            executable,
            is_meltano_sdk,
            python=python,
        )
        if sdk_about_dict:
            (
                settings,
                settings_group_validation,
                capabilities,
            ) = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict, enforce_desc=not self.auto_accept)
        else:
            setting_list = self._compile_settings()
            settings, settings_group_validation = self._build_settings(setting_list)
            capabilities = self._string_to_literal(
                self._prompt("capabilities", self._boilerplate_capabilities(plugin_type))
            )
        keywords = self._string_to_literal(self._prompt("keywords", self._scrape_keywords(is_meltano_sdk)))
        definition = self._boilerplate_definition(
            repo_url,
            plugin_type,
            settings,
            settings_group_validation,
            plugin_name,
            namespace,
            pip_url,
            keywords,
            capabilities,
            executable,
            self._prompt("plugin variant", self._get_plugin_variant(repo_url)),
        )
        definition_path = self._write_definition(definition, plugin_type)
        variant = definition["variant"]
        variant_exists = self._handle_default_variant(plugin_name, definition["variant"], plugin_type)
        self._handle_maintainer(variant, repo_url)
        self._handle_logo(definition, plugin_type, variant_exists)
        self._reformat_all(plugin_type, plugin_name, variant)
        print(definition_path)
        print(f"Adds {plugin_type} {plugin_name} ({variant})\n\n")

    def add_airbyte(
        self,
        definition_seed: dict | None = None,
        enforce_desc: bool = True,
        python: str | None = None,
    ):
        repo_url = "https://github.com/meltanolabs/tap-airbyte-wrapper"
        plugin_name = self._prompt("plugin name", "tap-<source/x>")
        plugin_type = "extractors"
        pip_url = f"git+{repo_url}.git"
        namespace = "tap_airbyte"
        executable = "tap-airbyte"
        variant = "airbyte"
        sdk_about_dict = None
        sdk_about_dict = self._test_airbyte(
            plugin_name,
            plugin_type,
            pip_url,
            namespace,
            executable,
            python=python,
        )
        if sdk_about_dict:
            (
                settings,
                settings_group_validation,
                capabilities,
            ) = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict, enforce_desc=enforce_desc)
        else:
            setting_list = self._compile_settings()
            settings, settings_group_validation = self._build_settings(setting_list)
            capabilities = self._string_to_literal(
                self._prompt("capabilities", self._boilerplate_capabilities(plugin_type))
            )
        keywords = ["airbyte_protocol"]
        definition = self._boilerplate_definition(
            repo_url,
            plugin_type,
            settings,
            settings_group_validation,
            plugin_name,
            namespace,
            pip_url,
            keywords,
            capabilities,
            executable,
            variant,
        )
        definition_path = self._write_definition(definition, plugin_type)
        definition["variant"] = variant
        variant_exists = self._handle_default_variant(plugin_name, variant, plugin_type)
        self._handle_maintainer(variant, repo_url)
        self._handle_logo(definition, plugin_type, variant_exists)
        self._reformat_all(plugin_type, plugin_name, variant)
        print(definition_path)
        print(f"Adds {plugin_type} {plugin_name} ({variant})\n\n")

    def delete_rows(self, repo_urls_to_delete, edit_path, csv_path):
        with open(csv_path) as inp, open(edit_path, "w") as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if row[0] in repo_urls_to_delete:
                    continue
                writer.writerow(row)

    def _retrieve_def(self, plugin_name, plugin_variant, plugin_type):
        def_path = f"{self.hub_root}/_data/meltano/{plugin_type}/{plugin_name}/{plugin_variant}.yml"
        return self._read_yaml(def_path)

    def _write_updated_def(self, plugin_name, plugin_variant, plugin_type, definition):
        def_path = f"{self.hub_root}/_data/meltano/{plugin_type}/{plugin_name}/{plugin_variant}.yml"
        self._write_yaml(def_path, definition, reformat=True)

    def _iterate_existing_settings(self, plugin_name, plugin_variant, plugin_type):
        def_path = f"{self.hub_root}/_data/meltano/{plugin_type}/{plugin_name}/{plugin_variant}.yml"
        return self._read_yaml(def_path)

    @staticmethod
    def _merge_capabilities(existing_caps, capabilities):
        new_caps = capabilities
        if not capabilities:
            new_caps = existing_caps
        return [cap for cap in new_caps if cap in ALLOWED_CAPABILITIES_TAP.union(ALLOWED_CAPABILITIES_TARGET)]

    @staticmethod
    def _merge_settings(existing_settings, settings):
        new_settings = []
        name_lookup = {setting.get("name"): setting for setting in settings}
        name_lookup_existing = {setting.get("name"): setting for setting in existing_settings}
        for name, setting in name_lookup.items():
            existing_desc = name_lookup_existing.get(name, {}).get("description", "")
            if not setting.get("description") or (
                len(existing_desc) > len(setting.get("description")) and "\n" in existing_desc
            ):
                # If the --about description is null, keep existing.
                # If the existing description is longer and has new line characters
                # then its probably a custom/manual override so keep it.
                setting["description"] = existing_desc
            else:
                setting["description"] = MeltanoUtil._clean_description(setting["description"])
            # TODO: if existing is much longer we might want to keep it
            existing_value = name_lookup_existing.get(name, {}).get("value", "")
            if str(existing_value).startswith("$MELTANO"):
                setting["value"] = existing_value
            for attrib in ["placeholder", "documentation"]:
                attrib_value = name_lookup_existing.get(name, {}).get(attrib, "")
                if attrib_value:
                    setting[attrib] = attrib_value
            new_settings.append(setting)
        return settings

    def _merge_definitions(self, existing_def, settings, keywords, m_status, caps, sgv):
        new_def = existing_def.copy()
        new_def["settings"] = self._merge_settings(existing_def.get("settings"), settings)
        new_def["keywords"] = keywords
        new_def["maintenance_status"] = m_status
        new_def["capabilities"] = self._merge_capabilities(existing_def.get("capabilities"), caps)
        if len(str(sgv)) > len(str(existing_def.get("settings_group_validation"))):
            if sgv and sgv[0]:
                new_def["settings_group_validation"] = sgv
        return new_def

    def _test_exception(
        self,
        plugin_name,
        plugin_type,
        pip_url,
        namespace,
        executable,
        *,
        is_meltano_sdk: bool,
        python: str | None = None,
    ):
        if self._prompt("Run install test?", True, type=bool):
            self._install_test(
                plugin_name,
                plugin_type,
                pip_url,
                namespace,
                executable,
                python=python,
            )
        if is_meltano_sdk:
            if self._prompt("Scrape SDK --about settings?", True, type=bool):
                try:
                    return MeltanoUtil.sdk_about(
                        plugin_name,
                        executable,
                        plugin_type,
                    )
                except Exception:
                    if self._prompt("Scrape failed! Provide as json?", True, type=bool):
                        return json.loads(self._prompt("Provide --about output"))

    def _test(
        self,
        plugin_name,
        plugin_type,
        pip_url,
        namespace,
        executable,
        is_meltano_sdk,
        python: str | None = None,
    ):
        try:
            return self._test_exception(
                plugin_name,
                plugin_type,
                pip_url,
                namespace,
                executable,
                is_meltano_sdk=is_meltano_sdk,
                python=python,
            )
        except Exception as e:
            print(e)

    def _test_airbyte(
        self,
        plugin_name,
        plugin_type,
        pip_url,
        namespace,
        executable,
        python: str | None = None,
    ):
        try:
            airbyte_name = self._prompt("airbyte_name (e.g. source-s3)")
            MeltanoUtil.add(plugin_name, pip_url, plugin_type, python=python)
            airbyte_config = {"airbyte_spec": {"image": f"airbyte/{airbyte_name}", "tag": "latest"}}
            MeltanoUtil.help_test(
                plugin_name,
                executable,
                plugin_type,
                config=airbyte_config,
            )
            try:
                return MeltanoUtil.sdk_about(
                    plugin_name,
                    executable,
                    plugin_type,
                    config=airbyte_config,
                )
            except Exception as e:
                print(e)
                if self._prompt("Scrape failed! Provide as json?", True, type=bool):
                    return json.loads(self._prompt("Provide --about output"))
        except Exception as e:
            print(e)

    def _update_base(
        self,
        repo_url,
        plugin_name,
        is_meltano_sdk=False,
        python: str | None = None,
    ):
        if not repo_url:
            repo_url = self._prompt("repo_url")
        plugin_name = self._prompt("plugin name", plugin_name or self._get_plugin_name(repo_url))
        plugin_type = self._prompt("plugin type", self.get_plugin_type(repo_url))
        plugin_variant = self._prompt("plugin variant", self._get_plugin_variant(repo_url))
        existing_def = self._retrieve_def(plugin_name, plugin_variant, plugin_type)
        sdk_def = self._test(
            plugin_name,
            plugin_type,
            existing_def["pip_url"],
            existing_def["namespace"],
            existing_def.get("executable", plugin_name),
            is_meltano_sdk,
            python=python,
        )
        return repo_url, plugin_name, plugin_type, plugin_variant, existing_def, sdk_def

    def update(
        self,
        repo_url: str | None = None,
        plugin_name: str | None = None,
        python: str | None = None,
    ):
        (
            repo_url,
            plugin_name,
            plugin_type,
            plugin_variant,
            existing_def,
            sdk_def,
        ) = self._update_base(repo_url, plugin_name, python=python)
        setting_names = [setting.get("name") for setting in existing_def.get("settings", [])]
        caps = self._string_to_literal(self._prompt("capabilities", existing_def.get("capabilities")))
        m_status = self._prompt("maintenance_status", existing_def.get("maintenance_status"))
        keywords = self._string_to_literal(self._prompt("keywords", existing_def.get("keywords")))
        settings, sgv = self._build_settings(self._compile_settings(setting_names))
        new_def = self._merge_definitions(
            existing_def,
            settings,
            keywords,
            m_status,
            caps,
            sgv,
        )
        self._write_updated_def(plugin_name, plugin_variant, plugin_type, new_def)
        print(f"\nUpdates {plugin_type} {plugin_name} ({plugin_variant})\n\n")

    def update_sdk(
        self,
        repo_url: str | None = None,
        plugin_name: str | None = None,
        python: str | None = None,
    ):
        (
            repo_url,
            plugin_name,
            plugin_type,
            plugin_variant,
            existing_def,
            sdk_def,
        ) = self._update_base(repo_url, plugin_name, is_meltano_sdk=True, python=python)
        (
            settings,
            settings_group_validation,
            capabilities,
        ) = MeltanoUtil._parse_sdk_about_settings(sdk_def)
        new_def = self._merge_definitions(
            existing_def,
            settings,
            self._string_to_literal(
                self._prompt(
                    "keywords",
                    self._scrape_keywords(True, existing_def.get("keywords")),
                )
            ),
            self._prompt("maintenance_status", existing_def.get("maintenance_status")),
            capabilities,
            settings_group_validation,
        )
        self._write_updated_def(plugin_name, plugin_variant, plugin_type, new_def)
        print(f"\nUpdates {plugin_type} {plugin_name} (SDK based - {plugin_variant})\n\n")

    def merge_and_update(
        self,
        existing_def,
        plugin_name,
        plugin_type,
        plugin_variant,
        new_settings,
        new_capabilities,
        new_settings_group_validation,
    ):
        merged_def = self._merge_definitions(
            existing_def,
            new_settings,
            existing_def.get("keywords"),
            existing_def.get("maintenance_status"),
            new_capabilities,
            new_settings_group_validation,
        )
        merged_def_formatted = fix_arrays(fix_yaml_dict_format(merged_def))
        self._write_updated_def(plugin_name, plugin_variant, plugin_type, merged_def_formatted)

    @staticmethod
    def get_suffix(yaml_file):
        p_type, p_name, p_variant = os.path.splitext(yaml_file)[0].split("/")[-3:]
        return f"{p_type}/{p_name}/{p_variant}"
