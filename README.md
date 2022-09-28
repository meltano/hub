[![Build Status](https://gitlab.com/meltano/hub/badges/main/pipeline.svg)](https://gitlab.com/meltano/hub/-/pipelines?ref=main)

---

## MeltanoHub

Source of MeltanoHub: [hub.meltano.com](https://hub.meltano.com/). The central place for any Meltano plugin.

*Not familiar with Meltano?* 
[Meltano](https://docs.meltano.com/getting-started/meltano-at-a-glance) is your DataOps infrastructure that: 

- **Starts simple**: Meltano is pip-installable and comes in a prepackaged docker container, you can have your first ELT pipeline running within minutes.
- **Has DataOps out-of-the-box**: Meltano provides tools that make DataOps best practices easy to use in every project.
- **Integrates with everything**: 300+ natively supported data sources & targets, as well as additional plugins like great expectations or dbt are natively available.
- **Is Easily customizable**: Meltano isn't just extensible, it's built to be extended! The SDK for Singer Connectors & EDK for Meltano Components are easy to use. Meltano Hub helps you find all of the connectors and components created across the data community.
- **Is a Mature system**: Developed since [2018](https://handbook.meltano.com/timeline), runs in production at large companies like GitLab, and currently powers over a million pipeline runs monthly.
- **Has first class ELT tooling built-in**: Extract data from any data source, load into any target, use inline maps to transform on data on the fly, and test the incoming data, all in one package.

If you want to get started with Meltano, we suggest you:
- head over to the [Installation](https://docs.meltano.com/getting-started/installation)
- or if you have it installed, go through the [Meltano Tutorial](https://docs.meltano.com/getting-started/part1).


---

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

## Meltano API

In addition to the Singer API that serves metadata about Singer taps and targets, theres also a Meltano API which serves all plugin types that are discoverable by Meltano.
This API will serve the front end client for the MeltanoHub 2.0 site and Meltano itself will use the API as a resource for discovering and installing plugin definitions, in exchange for the legacy discovery.yml file.

The API has the following endpoints:

- A top level index with references to the plugins details endpoints under each category: http://hub.meltano.com/meltano/api/v1/plugins/index

- A plugin category (extractors, loaders, utilities, transformers, etc.) level index: http://hub.meltano.com/meltano/api/v1/plugins/extractors/index

- The indexes contain plugins by name with `ref` references to their individual plugin definitions endpoints. For these, the plugin name plus the plugin variant is included in the path i.e. `../v1/extractors/{plugin_name}--{variant}`: https://hub.meltano.com/meltano/api/v1/plugins/extractors/tap-csv--meltanolabs
