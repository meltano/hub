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

const pluginTypeSingulars = {
  extractors: "extractor",
  loaders: "loader",
  mappers: "mapper",
  transforms: "transform",
  transformers: "transformer",
  orchestrators: "orchestrator",
  utilities: "utility",
  files: "file",
};

function renderDefinition(definition) {
  let rendered = marked.marked(definition);
  rendered = rendered.replace(/<p>|<\/p>/gi, "");
  return " " + rendered.charAt(0).toLowerCase() + rendered.slice(1);
}

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
    definition_rendered: pluginData.definition
      ? renderDefinition(pluginData.definition)
      : undefined,
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

function addLowercaseLabel(pluginData) {
  return {
    ...pluginData,
    label_lowercase: pluginData.label
      ? pluginData.label.toLowerCase()
      : undefined,
  };
}
function addCommandNames(pluginData) {
  if (!pluginData.commands) {
    return;
  }
  Object.keys(pluginData.commands).forEach((commandName) => {
    const command = pluginData.commands[commandName];
    command.name = commandName;
  });
}

function buildData(dataPath, collections) {
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
      readPlugin = renderMarkdownSections(addLowercaseLabel(readPlugin));
      addCommandNames(readPlugin);

      readPlugin.isDefault =
        defaultVariantData[path.basename(dataPath)][currentFolder] ===
        readPlugin.variant;
      readPlugin.pluginTypePlural = path.basename(dataPath);
      readPlugin.pluginType = pluginTypeSingulars[readPlugin.pluginTypePlural];

      // Need to stringify default setting values due to limited gql type system
      readPlugin.settings =
        readPlugin.settings &&
        readPlugin.settings.map((setting) => ({
          ...setting,
          value: (function parseValue(s) {
            if (s.value === undefined) {
              return undefined;
            }
            if (typeof s.value === "string") {
              return s.value;
            }
            return JSON.stringify(s.value);
          })(setting),
        }));

      // Include additional fields
      readPlugin.metrics = pluginMetricsData[readPlugin.repo];
      readPlugin.maintainer = readMaintainers[readPlugin.variant];

      collections.forEach((collection) => {
        collection.addNode(readPlugin);
      });
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
    const pluginsCollection = actions.addCollection({
      typeName: "Plugins",
    });
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

    buildData(path.join(dataRoot, "meltano/extractors"), [
      extractorsCollection,
      pluginsCollection,
    ]);
    buildData(path.join(dataRoot, "meltano/loaders"), [
      loadersCollection,
      pluginsCollection,
    ]);
    buildData(path.join(dataRoot, "meltano/files"), [
      filesCollection,
      pluginsCollection,
    ]);
    buildData(path.join(dataRoot, "meltano/orchestrators"), [
      orchestratorsCollection,
      pluginsCollection,
    ]);
    buildData(path.join(dataRoot, "meltano/transformers"), [
      transformersCollection,
      pluginsCollection,
    ]);
    buildData(path.join(dataRoot, "meltano/transforms"), [
      transformsCollection,
      pluginsCollection,
    ]);
    buildData(path.join(dataRoot, "meltano/mappers"), [
      mappersCollection,
      pluginsCollection,
    ]);
    buildData(path.join(dataRoot, "meltano/utilities"), [
      utilitiesCollection,
      pluginsCollection,
    ]);
    buildMaintainers(readMaintainers, maintainersCollection);
  });

  // Create default variant pages
  api.createPages(async ({ createPage, graphql }) => {
    const defaultPlugins = await graphql(`
      {
        allPlugins(filter: { isDefault: { eq: true } }) {
          edges {
            node {
              id
              path
              name
              pluginType
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
          component: `./src/templates/Plugins.vue`,
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
