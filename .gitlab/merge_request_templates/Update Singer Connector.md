<!---
Use this template when updating the YAML file or logo of an existing Singer tap or target. 
--->

## Checklist

- [ ] Update the file in the appropriate folder (/taps or /targets). The name of the file should match the name of the tap. If there is already one, add a descriptor to the name such as `-search`.
- [ ] If necessary, update the png logo image in `/assets/<taps/targets>`. The image name must match the YAML file name.
- [ ] Tag `@tayloramurphy` or `@aaronsteers` to flag it for review. Or post to the hub channel on Meltano slack.

## Reviewer Checklist

- [ ] Validate file against JSON Schema. https://www.jsonschema.net/home is an option.
- [ ] Build website locally and validate everything works.
