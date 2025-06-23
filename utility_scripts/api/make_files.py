from __future__ import annotations

import enum
import json
import logging
import sys
from pathlib import Path
from typing import Any, Generator

from ruamel.yaml import YAML

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger("make_api_files")

DATA_PATH = Path("_data")
BASE_HUB_URL = "https://hub.meltano.com"
BASE_API_URL = "https://hub.meltano.com/meltano/api/v1/plugins"
SKIP_FIELDS = [
    "keywords",
    "maintenance_status",
    "domain_url",
    "definition",
    "next_steps",
    "settings_preamble",
    "usage",
    "prereq",
    "quality",
]

SKIP_FIELDS_BY_TYPE = {
    "extractors": SKIP_FIELDS + [],
    "loaders": SKIP_FIELDS + [],
    "transformers": SKIP_FIELDS + ["hidden"],
    "utilities": SKIP_FIELDS + ["hidden"],
    "transforms": SKIP_FIELDS + ["hidden"],
    "orchestrators": SKIP_FIELDS + ["hidden"],
    "mappers": SKIP_FIELDS + ["hidden"],
    "files": SKIP_FIELDS + ["hidden"],
}


class PluginType(str, enum.Enum):
    """Plugin types."""

    EXTRACTORS = "extractors"
    LOADERS = "loaders"
    TRANSFORMERS = "transformers"
    UTILITIES = "utilities"
    TRANSFORMS = "transforms"
    ORCHESTRATORS = "orchestrators"
    MAPPERS = "mappers"
    FILES = "files"

    def __str__(self) -> str:
        return self.value


class ApiBuilder:
    def __init__(
        self,
        base_hub_url: str = BASE_HUB_URL,
        base_api_url: str = BASE_API_URL,
        data_path: Path = DATA_PATH,
    ):
        """Initialize ApiBuilder.

        Args:
            data_path: Path to source plugin YAML files.
            base_hub_url: Base URL for Meltano Hub.
            base_api_url: Base URL for Meltano Hub API.
        """
        self.data_path = data_path
        self.base_api_url = base_api_url
        self.base_hub_url = base_hub_url
        self.yaml = YAML()

        self.default_variants_path = self.data_path.joinpath("default_variants.yml")

    def get_default_variants(self) -> dict:
        """Get default variants of a given plugin.

        Returns:
            Mapping of plugin to default variant.
        """
        with self.default_variants_path.open("r") as f:
            return self.yaml.load(f)

    def get_plugin_variants(
        self,
        plugin_path: Path,
    ) -> Generator[tuple[str, dict[str, Any]], None, None]:
        """Get plugin variants of a given type.

        Args:
            plugin_path: Path to plugin directory.

        Yields:
            Tuple of plugin name and variant dictionary.
        """
        for plugin_file in plugin_path.glob("*.yml"):
            with open(plugin_file, "r") as f:
                yield plugin_file.stem, self.yaml.load(f)

    def write_files(self, output_dir: Path, create: bool = True):
        """Write API files to output directory.

        Args:
            output_dir: Path to output directory.
            create: Whether to create the output directory if it doesn't exist.
        """
        plugins_dir = output_dir.joinpath("plugins")

        if not plugins_dir.exists() and create:
            plugins_dir.mkdir(parents=True)

        default_variants = self.get_default_variants()
        global_index = {}

        for plugin_type in PluginType:
            source_type_path = self.data_path.joinpath("meltano", plugin_type.value)
            output_type_path = plugins_dir.joinpath(plugin_type.value)
            plugin_type_index = {}

            if not output_type_path.exists() and create:
                output_type_path.mkdir(parents=True)

            for plugin_path in source_type_path.glob("*"):
                plugin_name = plugin_path.name
                default_variant = default_variants[plugin_type.value].get(plugin_name)
                variants = {}
                default_variant_logo = None

                for variant, definition in self.get_plugin_variants(plugin_path):
                    plugin_full_name = f"{plugin_name}--{variant}"

                    # -- Start plugin definition cleanup
                    if "logo_url" in definition:
                        logo_url = f"{self.base_hub_url}{definition['logo_url']}"
                        definition["logo_url"] = logo_url

                    # Point plugin docs to Meltano Hub
                    definition["docs"] = (
                        f"{self.base_hub_url}/{plugin_type}/{plugin_full_name}"
                    )

                    for field in SKIP_FIELDS_BY_TYPE.get(plugin_type):
                        definition.pop(field, None)

                    # -- End plugin definition cleanup

                    # Write plugin definition
                    plugin_definition_path = output_type_path.joinpath(plugin_full_name)
                    with plugin_definition_path.open("w") as f:
                        json.dump(definition, f, separators=(",", ":"))

                    logger.info("Wrote %s", plugin_definition_path)

                    # Add to plugin variants
                    variants[variant] = {
                        "ref": (
                            f"{self.base_api_url}/plugins"
                            f"/{plugin_type}/{plugin_full_name}"
                        ),
                    }

                    # Set default variant logo
                    if variant == default_variant:
                        default_variant_logo = definition.get("logo_url")

                if plugin_name.startswith("."):
                    continue
                # Add to plugin type index
                plugin_type_index[plugin_name] = {
                    "default_variant": default_variant,
                    "variants": variants,
                    "logo_url": default_variant_logo,
                }

            # Write plugin type index
            global_index[plugin_type.value] = plugin_type_index
            plugin_index_path = output_type_path.joinpath("index")
            with plugin_index_path.open("w") as f:
                json.dump(plugin_type_index, f, separators=(",", ":"))

            logger.info("Wrote %s", plugin_index_path)

        # Write global index
        global_index_path = plugins_dir.joinpath("index")
        with global_index_path.open("w") as f:
            json.dump(global_index, f, separators=(",", ":"))

        logger.info("Wrote %s", global_index_path)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        help="Path to output directory for API files.",
    )
    parser.add_argument(
        "--hub-url",
        type=str,
        default=BASE_HUB_URL,
        help="Base URL for Meltano Hub.",
    )
    parser.add_argument(
        "--api-url",
        type=str,
        default=BASE_API_URL,
        help="Base URL for Meltano Hub API.",
    )

    args = parser.parse_args()
    builder = ApiBuilder(base_hub_url=args.hub_url, base_api_url=args.api_url)
    builder.write_files(output_dir=args.output_dir)
