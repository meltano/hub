const write = require("write");
const path = require("path");
const { gql } = require("graphql-tag");

const outputRoot = "dist/meltano/api/v1/plugins";

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
    const allPlugins = [];
    const promises = apiRoutes.map(async (item) => {
      try {
        // eslint-disable-next-line no-underscore-dangle
        const result = await gridsome._app.graphql(item.query);
        const allPluginsOfType = [];
        result.data.data.edges.map(async (edge) => {
          const plugin = removeEmpty(edge.node);
          allPluginsOfType.push(plugin);
          allPlugins.push(plugin);
          write(
            path.join(
              outputRoot,
              item.path,
              `${plugin.name}--${plugin.variant}`
            ),
            JSON.stringify(plugin)
          );
        });
        return write(
          path.join(outputRoot, item.path, "index"),
          JSON.stringify(allPluginsOfType)
        );
      } catch (e) {
        // eslint-disable-next-line no-console
        console.error(e);
        throw e;
      }
    });
    // wait for all promises to finish
    await Promise.all(promises);

    return write(path.join(outputRoot, "index"), JSON.stringify(allPlugins));
  });
};
