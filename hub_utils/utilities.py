import typer
from enum import Enum
import json
from ruamel.yaml import YAML
import ast

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
        self.file_path = f'{self.hub_root}/utility_scripts/hub_bot/export.csv'
        self.default_path = f'{self.hub_root}/_data/default_variants.yml'
        self.maintainers_path = f'{self.hub_root}/_data/maintainers.yml'

    def _prompt(self, question, default_val=None, type=None):
        if self.auto_accept:
            return default_val
        if default_val:
            return typer.prompt(question, default=default_val, type=type)
        else:
            return typer.prompt(question, type=type)

   
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
    def _scrape_keywords():
        return [
            # "meltano_sdk"
        ]

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

    def _boilerplate_definition(self, repo_url, plugin_type, settings, settings_group_validation):
        name = self._prompt("plugin name", self._get_plugin_name(repo_url))
        return {
            "name": name,
            "variant": self._prompt("plugin variant", self._get_plugin_variant(repo_url)),
            "label": self._prompt("label", self._get_label(name, plugin_type=plugin_type)),
            "capabilities": self._string_to_literal(self._prompt("capabilities", self._boilerplate_capabilities(plugin_type))),
            "domain_url": "",
            "keywords": self._prompt("keywords", self._scrape_keywords()),
            "maintenance_status": self._prompt("maintenance_status", self._get_maintenance_status()),
            "namespace": name.replace('-', '_'),
            "next_steps": "",
            "pip_url": f"git+{repo_url}.git",
            "repo": repo_url,
            "settings": settings,
            "settings_group_validation": settings_group_validation,
            "settings_preamble": "",
            "usage": "",
        }

    # def _assert_enum(self, value):
    #     if value not in list(Kind):
    #         raise Exception()

    def add(self, repo_url: str):
        # typer.prompt("test", default="a", value_proc=self._assert_enum)
        setting_list = self._compile_settings()
        settings, settings_group_validation = self._build_settings(setting_list)
        plugin_type = self._prompt("plugin type", self.get_plugin_type(repo_url))
        with open('/Users/pnadolny/Documents/Git/GitHub/pnadolny/hub-utils/hub_utils/output.yml', 'w') as f:
            self.yaml.dump(self._boilerplate_definition(repo_url, plugin_type, settings, settings_group_validation), f)
