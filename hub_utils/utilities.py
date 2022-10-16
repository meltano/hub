import typer
from enum import Enum
import json
from ruamel.yaml import YAML
import ast
from pathlib import Path
import os
from collections import OrderedDict
import shutil
import csv
from hub_utils.meltano_util import MeltanoUtil

class Kind(str, Enum):
    string = "string"
    boolean = "boolean"
    integer = "integer"
    object = "object"
    array = "array"

class Utilities:

    def __init__(self, auto_accept):
        self.yaml = YAML()
        self.auto_accept = auto_accept
        self.hub_root = '/Users/pnadolny/Documents/Git/GitHub/meltano/hub'
        self.default_variants_path = f'{self.hub_root}/_data/default_variants.yml'
        self.maintainers_path = f'{self.hub_root}/_data/maintainers.yml'

    def _prompt(self, question, default_val=None, type=None):
        if self.auto_accept:
            return default_val
        if default_val:
            return typer.prompt(question, default=default_val, type=type)
        else:
            return typer.prompt(question, type=type)

    def _write_yaml(self, path, content):
        with open(path, "w") as f:
            self.yaml.dump(content, f)

    def _read_yaml(self, path):
        with open(path, "r") as f:
            data = self.yaml.load(f)
        return data

    @staticmethod
    def _get_plugin_name(repo_url: str):
        return repo_url.split("/")[-1]

    @staticmethod
    def _get_plugin_variant(repo_url: str):
        return repo_url.split("/")[-2]

    @staticmethod
    def get_plugin_type(plugin_name: str):
        if 'tap' in plugin_name and 'target' in plugin_name:
            raise Exception(f'Type Unknown: {plugin_name}')
        if 'tap' in plugin_name:
            return 'extractors'
        if 'target' in plugin_name:
            return 'loaders'

    @staticmethod
    def _boilerplate_capabilities(plugin_type):
        if plugin_type == 'extractors':
            return [
                "catalog",
                "discover",
                "state"
            ]
        if plugin_type == 'loaders':
            return []

    @staticmethod
    def _scrape_keywords(meltano_sdk):
        if meltano_sdk:
            return f"['meltano_sdk']"
        return "[]"

    @staticmethod
    def _get_label(plugin_name, plugin_type=None):
        # TODO: not sure if this is the best place to do this
        name = plugin_name
        if plugin_type:
            if plugin_type == 'extractors':
                name = ''.join(plugin_name.split('tap-')[1:])
            elif plugin_type == 'loaders':
                name = ''.join(plugin_name.split('target-')[1:])
        return name.replace('_', ' ').replace('-', ' ').title()

    @staticmethod
    def _get_maintenance_status():
        return "active"

    def _build_settings(self, setting_list):
        settings = []
        settings_group_validation = []
        for setting in setting_list:
            label = self._prompt(f"[{setting}] `label`", default_val=self._get_label(setting))
            kind = self._prompt(f"[{setting}] `kind`", default_val="string")
            description = self._prompt(f"[{setting}] `description`")
            required = self._prompt(f"[{setting}] `required`", default_val=False, type=bool)
            setting_details = {
                'name': setting,
                'label': label,
                'description': description
            }
            if kind != 'string':
                setting_details['kind'] = kind
            settings.append(setting_details)
            if required:
                settings_group_validation.append(setting)
        return settings, [settings_group_validation]

    def _compile_settings(self):
        settings = []
        continue_prompts = True
        prompt_text = 'Lets collect all the settings, provide one at a time'
        while continue_prompts and not self.auto_accept:
            setting = self._prompt(f"{prompt_text}", default_val=settings)
            if str(setting) == str(settings):
                break
            settings.append(setting)
            prompt_text = 'Return an empty to end'
        return list(set(settings))

    @staticmethod
    def _string_to_literal(value):
        try:
            return ast.literal_eval(value)
        except:
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
        keywords
    ):
        label = self._get_label(name, plugin_type=plugin_type)
        logo_name = label.lower().replace(' ', '-')
        return {
            "name": name,
            "variant": self._prompt("plugin variant", self._get_plugin_variant(repo_url)),
            "label": self._prompt("label", label),
            "logo_url": f'/assets/logos/{plugin_type}/{logo_name}.png',
            "capabilities": self._string_to_literal(self._prompt("capabilities", self._boilerplate_capabilities(plugin_type))),
            "domain_url": "",
            "keywords": keywords,
            "maintenance_status": self._prompt("maintenance_status", self._get_maintenance_status()),
            "namespace": namespace,
            "next_steps": "",
            "pip_url": pip_url,
            "repo": repo_url,
            "settings": settings,
            "settings_group_validation": settings_group_validation,
            "settings_preamble": "",
            "usage": "",
        }

    def _write_definition(self, definition, plugin_type):
        dir_name = os.path.join(
            self.hub_root,
            '_data',
            'meltano',
            plugin_type,
            definition['name']
        )
        variant = definition['variant']
        Path(dir_name).mkdir(parents=True, exist_ok=True)
        yaml_path = Path(os.path.join(dir_name, f'{variant}.yml'))
        if not yaml_path.exists():
            self._write_yaml(
                os.path.join(dir_name, f'{variant}.yml'),
                definition
            )
            print(f'Definition: Updated')
        else:
            # TODO: show a diff or print
            overwrite = self._prompt(
                "Plugin definition already exists, overwrite it?",
                default_val=False,
                type=bool
            )
            if overwrite:
                self._write_yaml(
                    os.path.join(dir_name, f'{variant}.yml'),
                    definition
                )
            print(f'Definition: Skipping')
        return str(yaml_path)

    def _update_variant_file(self, plugin_type_defaults, plugin_name, plugin_variant, defaults, plugin_type):
        plugin_type_defaults[plugin_name] = plugin_variant
        defaults[plugin_type] = plugin_type_defaults
        self._write_yaml(self.default_variants_path, defaults)
        print(f'Default: Updated')

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
                type=bool
            )
            if overwrite:
                self._update_variant_file(plugin_type_defaults, plugin_name, plugin_variant, defaults, plugin_type)


    def _handle_maintainer(self, plugin_variant, repo_url):
        updated_maintainers = self._read_yaml(self.maintainers_path)
        if plugin_variant not in updated_maintainers:
            maintainer_name = plugin_variant
            updated_maintainers[plugin_variant] = {
                "label": maintainer_name,
                "url": "/".join(repo_url.split("/")[:-1]),
            }
            print(f'Maintainer: Updated')
            updated_maintainers = dict(OrderedDict(sorted(updated_maintainers.items())))
            self._write_yaml(self.maintainers_path, updated_maintainers)
        else:
            print(f'Maintainer: Skipping')

    def _handle_logo(self, definition, plugin_type):
        placeholder = self._prompt(
            f"Use placeholder logo?",
            default_val=False,
            type=bool
        )
        if placeholder:
            definition['logo_url'] = '/assets/logos/placeholder.png'
            print('Logo: Placeholder Used')
        image_path = self._prompt(
            "Path to image [.png] file"
        )
        logo_file_name = definition['logo_url'].split('/')[-1]
        shutil.copyfile(image_path, f'{self.hub_root}/static/assets/logos/{plugin_type}/{logo_file_name}')

    @staticmethod
    def _install_test(plugin_name, namespace, plugin_type, pip_url, is_meltano_sdk):
        MeltanoUtil.add(plugin_name, namespace, pip_url, plugin_type)
        MeltanoUtil.help_test(plugin_name)

    def _parse_sdk_about_settings(self, sdk_settings):
        settings_raw = sdk_settings.get('settings', {})
        properties = settings_raw.get('properties', {})
        reformatted_settings = []
        for setting_name, details in properties.items():
            setting_details = {
                'name': setting_name,
                'label': self._get_label(setting_name),
                'description': details.get('description')
            }
            kind = [s_type for s_type in details.get('type') if s_type != 'null'][0]
            if kind != 'string' and details.get('format') != 'date-time':
                if details.get('format') != 'date-time':
                    kind = 'date_iso8601'
                setting_details['kind'] = kind
            reformatted_settings.append(setting_details)

        return reformatted_settings, settings_raw.get('required', [])


    def add(self, repo_url: str, definition_seed: dict = None):
        plugin_name = self._prompt("plugin name", self._get_plugin_name(repo_url))
        plugin_type = self._prompt("plugin type", self.get_plugin_type(repo_url))
        pip_url = self._prompt("pip_url", f"git+{repo_url}.git")
        namespace = self._prompt("namespace", plugin_name.replace('-', '_'))
        is_meltano_sdk = self._prompt("is_meltano_sdk", True, type=bool)
        sdk_settings = None
        try:
            self._install_test(plugin_name, namespace, plugin_type, pip_url, is_meltano_sdk)
            if is_meltano_sdk:
                sdk_settings = MeltanoUtil.sdk_about(plugin_name)
        except Exception as e:
            print(e)
        finally:
            MeltanoUtil.remove(plugin_name, plugin_type)
        
        if sdk_settings:
            settings, settings_group_validation = self._parse_sdk_about_settings(sdk_settings)
        else:
            setting_list = self._compile_settings()
            settings, settings_group_validation = self._build_settings(setting_list)
        keywords = self._string_to_literal(self._prompt("keywords", self._scrape_keywords(is_meltano_sdk)))
        definition = self._boilerplate_definition(repo_url, plugin_type, settings, settings_group_validation, plugin_name, namespace, pip_url, keywords)
        definition_path = self._write_definition(definition, plugin_type)
        variant = definition['variant']
        self._handle_default_variant(plugin_name, definition['variant'], plugin_type)
        self._handle_maintainer(variant, repo_url)
        self._handle_logo(definition, plugin_type)
        print(definition_path)
        print(f'Adds {plugin_type} {plugin_name} ({variant})\n\n')

    def delete_rows(self, repo_urls_to_delete, edit_path, csv_path):
        with open(csv_path, 'r') as inp, open(edit_path, 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if row[0] in repo_urls_to_delete:
                    continue
                writer.writerow(row)

    def add_bulk(self, csv_path: str):
        edit_path = csv_path.split('.csv')[0] + '_edit.csv'
        csv_list = []
        repo_urls_to_delete = []
        with open(csv_path, 'r') as inp:
            csv_list = [row for row in csv.reader(inp)]
        for index, row in enumerate(csv_list):
            if index == 0:
                print(f"Skipping header {row}")
                continue
            repo_url = row[0]
            plugin_definition = json.loads(row[5])
            do_add = self._prompt(f'Add {repo_url}?', default_val=True, type=bool)
            if not do_add:
                continue
            self.add(repo_url, definition_seed=plugin_definition)
            repo_urls_to_delete.append(repo_url)
            self.delete_rows(repo_urls_to_delete, edit_path, csv_path)
            self._prompt('Pausing to commit changes...hit any key to continue')
