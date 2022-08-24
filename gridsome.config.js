// This is where project configuration and plugin options are located.
// Learn more: https://gridsome.org/docs/config

// Changes here require a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`

module.exports = {
  siteName: "Meltano Hub",
  icon: "./src/meltano-favicon-192x192.png",
  plugins: [],
  chainWebpack: (config) => {
    config.resolve.alias.set("@logos", "@/assets/logos");
  },
  templates: {
    Extractors: [
      {
        path: "/extractors/:name/:variant",
        component: "./src/templates/Extractors.vue",
      },
    ],
    Loaders: [
      {
        path: "/loaders/:name/:variant",
        component: "./src/templates/Loaders.vue",
      },
    ],
    Orchestrators: [
      {
        path: "/orchestrators/:name/:variant",
        component: "./src/templates/Orchestrators.vue",
      },
    ],
    Transformers: [
      {
        path: "/transformers/:name/:variant",
        component: "./src/templates/Transformers.vue",
      },
    ],
    Utilities: [
      {
        path: "/utilities/:name/:variant",
        component: "./src/templates/Utilities.vue",
      },
    ],
    Files: [
      {
        path: "/files/:name/:variant",
        component: "./src/templates/Files.vue",
      },
    ],
    Maintainers: [
      {
        path: "/maintainers/:name",
        component: ".src/templates/Maintainers.vue",
      },
    ],
  },
};
