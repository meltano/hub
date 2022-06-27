// This is where project configuration and plugin options are located.
// Learn more: https://gridsome.org/docs/config

// Changes here require a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`

module.exports = {
  siteName: "MeltanoHub",
  plugins: [],
  templates: {
    Extractors: [
      {
        path: "/extractors/:name/:variant",
        component: "./src/templates/Extractor.vue",
      },
    ],
    Loaders: [
      {
        path: "/loaders/:name/:variant",
        component: "./src/templates/Loader.vue",
      },
    ],
    Orchestrators: [
      {
        path: "/orchestrators/:name/:variant",
        component: "./src/templates/Orchestrator.vue",
      },
    ],
    Transformers: [
      {
        path: "/transformers/:name/:variant",
        component: "./src/templates/Transformer.vue",
      },
    ],
    Utilities: [
      {
        path: "/utilities/:name/:variant",
        component: "./src/templates/Utility.vue",
      },
    ],
    Files: [
      {
        path: "/files/:name/:variant",
        component: "./src/templates/File.vue",
      },
    ],
  },
};
