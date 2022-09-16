// This is where project configuration and plugin options are located.
// Learn more: https://gridsome.org/docs/config

// Changes here require a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`

module.exports = {
  siteName: "Meltano Hub",
  icon: "./src/meltano-favicon-192x192.png",
  plugins: [
    {
      use: "gridsome-plugin-tailwindcss",

      options: {
        tailwindConfig: "./tailwind.config.js",
      },
    },
  ],
  chainWebpack: (config) => {
    config.resolve.alias.set("@logos", "@/../assets/logos");
  },
  templates: {
    Plugins: [
      {
        path: "/:pluginTypePlural/:name--:variant",
        component: "./src/templates/Plugins.vue",
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
