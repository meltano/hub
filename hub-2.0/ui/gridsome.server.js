// Server API makes it possible to hook into various parts of Gridsome
// on server-side and add custom data to the GraphQL data layer.
// Learn more: https://gridsome.org/docs/server-api/

// Changes here require a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`

const fs = require("fs");
const yaml = require("js-yaml");
const path = require("path");

const dataRoot = "../../_data/";

const defaultVariantData = yaml.load(
  fs.readFileSync(path.join(dataRoot, "default_variants.yml"))
);

const readMaintainers = yaml.load(
  fs.readFileSync(path.join(dataRoot, "maintainers.yml"))
);

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
      const readPlugin = yaml.load(fileContents);
      readPlugin.isDefault =
        defaultVariantData[path.basename(dataPath)][currentFolder] ===
        readPlugin.variant;
      readPlugin.pluginType = path.basename(dataPath).slice(0, -1);
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
    buildData(path.join(dataRoot, "meltano/utilities"), utilitiesCollection);
    buildMaintainers(readMaintainers, maintainersCollection);
  });

  api.chainWebpack((config) => {
    config.resolve.alias.set("@logos", "@/assets/logos");
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
          path: path.normalize(path.join(node.path, "..")),
          // And send it to the same rendering template
          component: `./src/templates/${query.substring(3)}.vue`,
          context: {
            id: node.id,
            path: node.path,
          },
        });
      });
    });
  });
};
