const write = require("write");
const path = require("path");
const { gql } = require("graphql-tag");

const outputRoot = "dist/meltano/api/v1/plugins";
const baseurl = "https://hub.meltano.com";

const fieldFragment = gql`
  fragment Fields on Node {
    description
    label
    name
    namespace
    logo_url
    variant
    pip_url
    repo
    settings {
      name
      kind
      label
      description
      value
      env
      options {
        label
        value
      }
      aliases
      value_post_processor
      value_processor
      placeholder
    }
    capabilities
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

const removeEmpty = (obj) => {
  Object.entries(obj).forEach(
    ([key, val]) =>
      (val && typeof val === "object" && removeEmpty(val)) ||
      // eslint-disable-next-line no-param-reassign
      ((val === null || val === "") && delete obj[key])
  );
  return obj;
};

module.exports = function buildJSONApi(gridsome) {
  gridsome.afterBuild(async () => {
    const allPluginsIndex = {};
    await Promise.all(
      apiRoutes.map(async (item) => {
        try {
          // eslint-disable-next-line no-underscore-dangle
          const result = await gridsome._app.graphql(item.query);
          const typeIndex = {};
          await Promise.all(
            result.data.data.edges.map(async (edge) => {
              const plugin = removeEmpty(edge.node);

              // Update plugin index
              const indexEntry = typeIndex[plugin.name] || { variants: {} };
              indexEntry.variants[plugin.variant] = {
                ref: `${baseurl}/meltano/api/v1/plugins/${plugin.name}--${plugin.variant}`,
              };
              if (plugin.isDefault) {
                indexEntry.default_variant = plugin.variant;
                indexEntry.logo_url = plugin.logo_url || null;
              }
              typeIndex[plugin.name] = indexEntry;
              delete plugin.isDefault;

              // Write plugin file
              return write(
                path.join(
                  outputRoot,
                  item.path,
                  `${plugin.name}--${plugin.variant}`
                ),
                JSON.stringify(plugin)
              );
            })
          );

          // Add to top level index
          allPluginsIndex[item.path] = typeIndex;

          // Write index for this plugin type
          return write(
            path.join(outputRoot, item.path, "index"),
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
