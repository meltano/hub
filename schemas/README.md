# Schemas

## Overview

These JSON schemas are used to validate both the plugin definition yaml files and the Meltano API static files used for serving Meltano plugin definitions.
The two uses are very similar but have a few slight differences that make it better for us to split them up.

## Conventions

The pattern that we use is the `allOf` key which lets us validate against a list of schemas separately, each doing only a piece of the validation but together covering all requirements.
This is useful because it lets us be more DRY by moving things like `pip_url` out into a `common/common.schema.json` schema where it only needs to be defined once and can be referenced multiple times.
Then at the top level, say `plugin_definitions/extractors.schema.json` we can include a reference to validate against that common schema.
We can use this pattern to share schemas for other uses too like extractor specific keys that are used by both the API validation and the plugin definition yaml file validation.

At the top level e.g. `plugin_definitions/extractors.schema.json` we also define a schema of only the top level keys that are allowed for that particular schema with `"additionalProperties": false`.
This allows us to catch any misspelled keys or additional keys that aren't allowed.
By only defining the keys it saves us from having to re-define the content validation in multiple places, thats taken care of by the other shared schemas.
