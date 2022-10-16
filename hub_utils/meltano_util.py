from os import stat
import subprocess
import pathlib
import json

class MeltanoUtil:

    def __init__(self):
        pass

    @staticmethod
    def get_cwd():
        return pathlib.Path(__file__).parent.resolve()

    @staticmethod
    def add(plugin_name, namespace, pip_url, plugin_type):
        content = f"""{namespace}\n{pip_url}\n{plugin_name}\n\n\n"""
        subprocess.run(
            f'poetry run meltano add {plugin_type} {plugin_name} --custom'.split(" "),
            cwd=str(MeltanoUtil.get_cwd()) + '/test_meltano_project/',
            stdout=subprocess.PIPE,
            universal_newlines=True,
            check=True,
            input=content
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
