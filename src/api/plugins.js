const write = require("write");
const path = require("path");
const fs = require("fs");
const yaml = require("js-yaml");
const { gql } = require("graphql-tag");

const outputRoot = "dist/meltano/api/v1/plugins";

const dataRoot = "_data/meltano";

const baseurl = process.env.HUB_SITE_URL;

const toDelete = [
  "keywords",
  "maintenance_status",
  "domain_url",
  "definition",
  "next_steps",
  "settings_preamble",
  "usage",
  "prereq",
];

const fieldFragment = gql`
  fragment Fields on Node {
    name
    logo_url
    variant
    isDefault
  }
`;
const apiRoutes = [
  {
    query: gql`
      ${fieldFragment}
      {
        data: allExtractors {
          edges {
            node {
              ...Fields
            }
          }
        }
      }
    `,
    path: "extractors",
  },
  {
    query: gql`
      ${fieldFragment}
      {
        data: allLoaders {
          edges {
            node {
              ...Fields
            }
          }
        }
      }
    `,
    path: "loaders",
  },
  {
    query: gql`
      ${fieldFragment}
      {
        data: allFiles {
          edges {
            node {
              ...Fields
            }
          }
        }
      }
    `,
    path: "files",
  },
  {
    query: gql`
      ${fieldFragment}
      {
        data: allMappers {
          edges {
            node {
              ...Fields
            }
          }
        }
      }
    `,
    path: "mappers",
  },
  {
    query: gql`
      ${fieldFragment}
      {
        data: allOrchestrators {
          edges {
            node {
              ...Fields
            }
          }
        }
      }
    `,
    path: "orchestrators",
  },
  {
    query: gql`
      ${fieldFragment}
      {
        data: allTransformers {
          edges {
            node {
              ...Fields
            }
          }
        }
      }
    `,
    path: "transformers",
  },
  {
    query: gql`
      ${fieldFragment}
      {
        data: allTransforms {
          edges {
            node {
              ...Fields
            }
          }
        }
      }
    `,
    path: "transforms",
  },
  {
    query: gql`
      ${fieldFragment}
      {
        data: allUtilities {
          edges {
            node {
              ...Fields
            }
          }
        }
      }
    `,
    path: "utilities",
  },
];

module.exports = function buildJSONApi(gridsome) {
  gridsome.afterBuild(async () => {
    const allPluginsIndex = {};
    await Promise.all(
      apiRoutes.map(async (pluginType) => {
        try {
          // eslint-disable-next-line no-underscore-dangle
          const result = await gridsome._app.graphql(pluginType.query);
          const typeIndex = {};
          await Promise.all(
            result.data.data.edges.map(async ({ node: plugin }) => {
              // Clean up plugin object, create full log_url, add docs url
              const logoUrl = plugin.logo_url
                ? path.join(baseurl, plugin.logo_url)
                : undefined;
              const docs = path.join(
                baseurl,
                pluginType.path,
                plugin.name,
                plugin.variant
              );

              // Update plugin index
              const indexEntry = typeIndex[plugin.name] || { variants: {} };
              indexEntry.variants[plugin.variant] = {
                ref: path.join(
                  baseurl,
                  "meltano/api/v1/plugins",
                  pluginType.path,
                  `${plugin.name}--${plugin.variant}`
                ),
              };
              if (plugin.isDefault) {
                indexEntry.default_variant = plugin.variant;
                indexEntry.logo_url = logoUrl || null;
              }
              typeIndex[plugin.name] = indexEntry;

              // Read in the file (again 🙄)
              const filePath = path.join(
                dataRoot,
                pluginType.path,
                plugin.name,
                `${plugin.variant}.yml`
              );
              const fileContents = fs.readFileSync(filePath);
              const readPlugin = yaml.load(fileContents);
              readPlugin.logo_url = logoUrl;
              readPlugin.docs = docs;

              toDelete.forEach((field) => {
                delete readPlugin[field];
              });

              // Write plugin file
              return write(
                path.join(
                  outputRoot,
                  pluginType.path,
                  `${plugin.name}--${plugin.variant}`
                ),
                JSON.stringify(readPlugin)
              );
            })
          );

          // Add to top level index
          allPluginsIndex[pluginType.path] = typeIndex;

          // Write index for this plugin type
          return write(
            path.join(outputRoot, pluginType.path, "index"),
            JSON.stringify(typeIndex)
          );
        } catch (e) {
          // eslint-disable-next-line no-console
          console.error(e);
          throw e;
        }
      })
    );

    return write(
      path.join(outputRoot, "index"),
      JSON.stringify(allPluginsIndex)
    );
  });
};
