// Server API makes it possible to hook into various parts of Gridsome
// on server-side and add custom data to the GraphQL data layer.
// Learn more: https://gridsome.org/docs/server-api/

// Changes here require a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`

const fs = require("fs");
const yaml = require("js-yaml");
const path = require("path");
const marked = require("marked");
const buildJSONApi = require("./src/api/plugins");

const dataRoot = "_data/";

const defaultVariantData = yaml.load(
  fs.readFileSync(path.join(dataRoot, "default_variants.yml"))
);

const pluginMetricsData = yaml.load(
  fs.readFileSync(path.join(dataRoot, "variant_metrics.yml"))
).metrics;

const readMaintainers = yaml.load(
  fs.readFileSync(path.join(dataRoot, "maintainers.yml"))
);

function renderMarkdownSections(pluginData) {
  return {
    ...pluginData,
    // Common
    settings:
      pluginData.settings &&
      pluginData.settings.map((setting) => ({
        ...setting,
        description_rendered:
          setting.description && marked.marked(setting.description),
      })),
    // Rare
    settings_preamble_rendered: pluginData.settings_preamble
      ? marked.marked(pluginData.settings_preamble)
      : undefined,
    usage_rendered: pluginData.usage
      ? marked.marked(pluginData.usage)
      : undefined,
    prereq_rendered: pluginData.prereq
      ? marked.marked(pluginData.prereq)
      : undefined,
    next_steps_rendered: pluginData.next_steps
      ? marked.marked(pluginData.next_steps)
      : undefined,
  };
}

function addCommandNames(pluginData) {
  return {
    ...pluginData,
    // Common
    commands:
      pluginData.commands &&
      pluginData.commands.toArray(([commandName, command]) => ({
        ...command,
        name: commandName
      }))
  };
}

function buildData(dataPath, collection) {
  const currentCollection = dataPath;
  let collectionFolder = fs.readdirSync(dataPath);
  collectionFolder = collectionFolder.filter(
    (item) => !/(^|\/)\.[^/.]/g.test(item)
  );
  collectionFolder.forEach((folder) => {
    const currentFolder = folder;
    const subfolderPlugins = fs.readdirSync(`${currentCollection}/${folder}`);
    subfolderPlugins.forEach((plugin) => {
      const fileContents = fs.readFileSync(
        `${currentCollection}/${currentFolder}/${plugin}`
      );
      let readPlugin = yaml.load(fileContents);
      readPlugin = renderMarkdownSections(readPlugin);
      readPlugin = addCommandNames(readPlugin);

      readPlugin.isDefault =
        defaultVariantData[path.basename(dataPath)][currentFolder] ===
        readPlugin.variant;
      readPlugin.pluginType = path.basename(dataPath).slice(0, -1);

      // Include additional fields
      readPlugin.metrics = pluginMetricsData[readPlugin.repo];

      collection.addNode(readPlugin);
    });
  });
}

function buildMaintainers(datapath, collection) {
  Object.keys(datapath).forEach((key) => {
    collection.addNode({
      name: datapath[key].name,
      label: datapath[key].label,
      url: datapath[key].url,
    });
  });
}

module.exports = function main(api) {
  api.loadSource(async (actions) => {
    const extractorsCollection = actions.addCollection({
      typeName: "Extractors",
    });
    const loadersCollection = actions.addCollection({
      typeName: "Loaders",
    });
    const filesCollection = actions.addCollection({
      typeName: "Files",
    });
    const orchestratorsCollection = actions.addCollection({
      typeName: "Orchestrators",
    });
    const transformersCollection = actions.addCollection({
      typeName: "Transformers",
    });
    const transformsCollection = actions.addCollection({
      typeName: "Transforms",
    });
    const mappersCollection = actions.addCollection({
      typeName: "Mappers",
    });
    const utilitiesCollection = actions.addCollection({
      typeName: "Utilities",
    });
    const maintainersCollection = actions.addCollection({
      typeName: "Maintainers",
    });

    buildData(path.join(dataRoot, "meltano/extractors"), extractorsCollection);
    buildData(path.join(dataRoot, "meltano/loaders"), loadersCollection);
    buildData(path.join(dataRoot, "meltano/files"), filesCollection);
    buildData(
      path.join(dataRoot, "meltano/orchestrators"),
      orchestratorsCollection
    );
    buildData(
      path.join(dataRoot, "meltano/transformers"),
      transformersCollection
    );
    buildData(path.join(dataRoot, "meltano/transforms"), transformsCollection);
    buildData(path.join(dataRoot, "meltano/mappers"), mappersCollection);
    buildData(path.join(dataRoot, "meltano/utilities"), utilitiesCollection);
    buildMaintainers(readMaintainers, maintainersCollection);
  });

  // Create default variant pages
  api.createPages(async ({ createPage, graphql }) => {
    const defaultPlugins = await graphql(`
      {
        allExtractors(filter: { isDefault: { eq: true } }) {
          edges {
            node {
              id
              path
              name
            }
          }
        }
        allLoaders(filter: { isDefault: { eq: true } }) {
          edges {
            node {
              id
              path
              name
            }
          }
        }
        allFiles(filter: { isDefault: { eq: true } }) {
          edges {
            node {
              id
              path
              name
            }
          }
        }
        allOrchestrators(filter: { isDefault: { eq: true } }) {
          edges {
            node {
              id
              path
              name
            }
          }
        }
        allTransformers(filter: { isDefault: { eq: true } }) {
          edges {
            node {
              id
              path
              name
            }
          }
        }
        allUtilities(filter: { isDefault: { eq: true } }) {
          edges {
            node {
              id
              path
              name
            }
          }
        }
      }
    `);

    Object.keys(defaultPlugins.data).forEach((query) => {
      // For each default plugin we create an extra page one-level up
      defaultPlugins.data[query].edges.forEach(({ node }) => {
        createPage({
          // Remove the variant part of the path
          path: node.path.split("--")[0],
          // And send it to the same rendering template
          component: `./src/templates/${query.substring(3)}.vue`,
          context: {
            id: node.id,
            path: node.path,
            name: node.name,
          },
        });
      });
    });
  });

  // Build JSON files to serve the static Meltano API
  buildJSONApi(api);
};
