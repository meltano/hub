// Server API makes it possible to hook into various parts of Gridsome
// on server-side and add custom data to the GraphQL data layer.
// Learn more: https://gridsome.org/docs/server-api/

// Changes here require a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`

const fs = require("fs");
const yaml = require("js-yaml");

function buildData(path, collection) {
  let currentCollection = path;
  let collectionFolder = fs.readdirSync(path);
  collectionFolder = collectionFolder.filter(
    (item) => !/(^|\/)\.[^\/\.]/g.test(item)
  );
  collectionFolder.forEach((folder) => {
    let currentFolder = folder;
    let subfolderPlugins = fs.readdirSync(`${currentCollection}/${folder}`);
    subfolderPlugins.forEach((plugin) => {
      const fileContents = fs.readFileSync(
        `${currentCollection}/${currentFolder}/${plugin}`
      );
      console.log(`${currentCollection}/${currentFolder}/${plugin}`);
      const readPlugin = yaml.load(fileContents);
      collection.addNode(readPlugin);
    });
  });
}

module.exports = function(api) {
  // api.loadSource(({ addCollection }) => {
  //   // Use the Data Store API here: https://gridsome.org/docs/data-store-api/
  // });

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

    buildData("../../_data/meltano/extractors", extractorsCollection);
    buildData("../../_data/meltano/loaders", loadersCollection);
    buildData("../../_data/meltano/files", filesCollection);
    buildData("../../_data/meltano/orchestrators", orchestratorsCollection);
    buildData("../../_data/meltano/transformers", transformersCollection);
    buildData("../../_data/meltano/utilities", utilitiesCollection);
  });

  api.createPages(({ createPage }) => {
    // Use the Pages API here: https://gridsome.org/docs/pages-api/
  });
};
