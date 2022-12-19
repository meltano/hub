from os import stat
import subprocess
import pathlib
import json
import typer
class MeltanoUtil:

    def __init__(self):
        pass

    @staticmethod
    def get_cwd():
        return pathlib.Path(__file__).parent.resolve()

    @staticmethod
    def add(plugin_name, namespace, executable, pip_url, plugin_type):
        content = f"""{namespace}\n{pip_url}\n{executable}\n\n\n"""
        subprocess.run(
            f'poetry run meltano add {plugin_type} {plugin_name} --custom'.split(" "),
            cwd=str(MeltanoUtil.get_cwd()) + '/test_meltano_project/',
            stdout=subprocess.PIPE,
            universal_newlines=True,
            check=True,
            input=content
        )

    @staticmethod
    def command(command):
        subprocess.run(
            f'poetry run {command}'.split(" "),
            cwd=str(MeltanoUtil.get_cwd()) + '/test_meltano_project/',
            stdout=subprocess.PIPE,
            universal_newlines=True,
            check=True,
        )

    @staticmethod
    def help_test(plugin_name):
        subprocess.run(
            f"poetry run meltano invoke {plugin_name} --help".split(" "),
            cwd=str(MeltanoUtil.get_cwd()) + '/test_meltano_project/',
            stdout=subprocess.PIPE,
            universal_newlines=True,
            check=True,
        )

    @staticmethod
    def sdk_about(plugin_name):
        about_content = subprocess.run(
            f"poetry run meltano invoke {plugin_name} --about --format=json".split(" "),
            cwd=str(MeltanoUtil.get_cwd()) + '/test_meltano_project/',
            stdout=subprocess.PIPE,
            universal_newlines=True,
            check=True,
        )
        return json.loads(about_content.stdout)

    @staticmethod
    def remove(plugin_name, plugin_type):
        subprocess.run(
            f"poetry run meltano remove {plugin_type} {plugin_name}".split(" "),
            cwd=str(MeltanoUtil.get_cwd()) + '/test_meltano_project/',
            stdout=subprocess.PIPE,
            universal_newlines=True,
            check=True
        )

    @staticmethod
    def _get_label(plugin_name, plugin_type=None):
        return plugin_name.replace('_', ' ').replace('-', ' ').replace('.', ' ').title()

    @staticmethod
    def _parse_kind(kind, setting, format=None):
        setting = setting.lower()
        if kind == 'string':
            if format == 'date-time' or setting in ('start_date', 'end_date'):
                return 'date_iso8601'
            if any(id_str.lower() in setting for id_str in ['password', 'id', 'token', 'key', 'secret']):
                return 'password'
            return 'string'
        if kind == 'number':
            return 'integer'
        else:
            return kind

    @staticmethod
    def _default_description(setting):
        setting = setting.lower()
        if setting == "start_date":
            return """Determines how much historical data will be extracted. Please be aware
that the larger the time period and amount of data, the longer the initial extraction
can be expected to take."""
        if setting == "end_date":
            return "Date up to when historical data will be extracted."
        else:
            return None

    @staticmethod
    def _parse_sdk_about_settings(sdk_about_dict, enforce_desc=False):
        settings_raw = sdk_about_dict.get('settings', {})
        reformatted_settings = []
        settings_group_validation = []
        base_required = settings_raw.get('required', [])
        for settings in MeltanoUtil._traverse_schema_properties(settings_raw):
            description = settings.get('description')
            if not settings.get('description') and enforce_desc:
                description = typer.prompt(f"[{settings.get('name')}] `description`", default=MeltanoUtil._default_description(settings.get('name')))
            setting_details = {
                'name': settings.get('name'),
                'label': MeltanoUtil._get_label(settings.get('name')),
                'description': description
            }
            if isinstance(settings.get('type'), list):
                kind = [s_type for s_type in settings.get('type') if s_type != 'null'][0]
            else:
                kind = settings.get('type')

            setting_details['kind'] = MeltanoUtil._parse_kind(kind, settings.get('name'))

            reformatted_settings.append(setting_details)
            if settings.get('required'):
                settings_group_validation.append(settings.get('name'))
        return reformatted_settings, [list(set(settings_group_validation + base_required))], sdk_about_dict.get('capabilities')

    @staticmethod
    def _traverse_schema_properties(schema, field_sep='.'):
        fields = []

        for key, value in schema.get('properties', {}).items():
            val_type = value.get('type')
            if val_type == 'object':
                for subfield in MeltanoUtil._traverse_schema_properties(value):
                    sub_name = subfield.get('name')
                    full_name = f'{key}{field_sep}{sub_name}'
                    reqs = value.get("required")
                    field = {
                        'name': full_name,
                        'description': subfield.get('description'),
                        'type': subfield.get('type'),
                    }
                    if 'required' in subfield:
                        # accept parent if it was set already
                        field['required'] = subfield['required']
                    else:
                        field['required'] = sub_name in reqs

                    fields.append(field)
            else:
                fields.append({
                    'name': key,
                    'description': value.get('description'),
                    'type': value.get('type')
                })
        return fields

if __name__ == '__main__':
    m = MeltanoUtil()

    # plugin_name = "tap-amazon-sp"
    # namespace = "tap_amazon_sp",
    # pip_url = "git+https://github.com/singer-io/tap-amazon-sp.git"
    # plugin_type = "extractors"
    # is_meltano_sdk = False

    plugin_name = "tap-cqc-org-uk"
    namespace = "tap_cqc_org_uk",
    pip_url = "git+https://github.com/birdiecare/tap-cqc-org-uk.git"
    plugin_type = "extractors"
    is_meltano_sdk = False

    MeltanoUtil.add(plugin_name, namespace, pip_url, plugin_type)
    MeltanoUtil.help_test(plugin_name)
    if is_meltano_sdk:
        MeltanoUtil.sdk_about(plugin_name)
    MeltanoUtil.remove(plugin_name, plugin_type)
