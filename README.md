[![Build Status](https://gitlab.com/meltano/hub/badges/main/pipeline.svg)](https://gitlab.com/meltano/hub/-/pipelines?ref=main)

---

## MeltanoHub

Source of MeltanoHub <https://hub.meltano.com/>.

## Development

To work locally with this project, you'll have to follow the steps below:

1. Fork this project
2. Install Ruby 3.1.2+ (via rbenv or some other method)
2. Install dependencies: `bundle install`
3. Build and preview: `bundle exec jekyll serve --livereload`
4. Add content
5. Push the commit(s) you made
6. Make an MR

The above commands should be executed from the root directory of this project.

Read more at Jekyll's [documentation][].

[documentation]: https://jekyllrb.com/docs/home/

## API 2.0 (Alpha)

In addition to the Singer API that serves metadata about Singer taps and targets, theres also an (Alpha) Meltano 2.0 API which serves all plugin types.
This API will serve the front end client for the MeltanoHub 2.0 site and Meltano itself will use the API as a resource for discovering and installing plugin definitions, in exchange for the legacy discovery.yml file.

The API has the following endpoints:

- A top level index with references to the plugins details endpoints under each category: http://hub.meltano.com/meltano/api/v1/plugins/index

- A plugin category (extractors, loaders, utilities, transformers, etc.) level index: http://hub.meltano.com/meltano/api/v1/plugins/extractors/index

- The indexes contain plugins by name with `ref` references to their individual plugin definitions endpoints. For these, the plugin name plus the plugin variant is included in the path i.e. `../v1/extractors/{plugin_name}--{variant}`: https://hub.meltano.com/meltano/api/v1/plugins/extractors/tap-csv--meltanolabs
