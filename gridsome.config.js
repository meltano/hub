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
    {
      use: '@gridsome/source-filesystem',
      options: {
        typeName: 'MarkdownDocs',
        baseDir: './static/markdown',
        path: './**/*.md',
        remark: {
          // remark options
        }
      },
      transformers: {
        remark: {
          // global remark options
          plugins: [
            // Place Remark markdown extensions here:
            // https://github.com/remarkjs/remark/blob/main/doc/plugins.md#list-of-plugins
            "remark-prism",
          ]
        }
      }
    }
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
    MarkdownDocs: [
      {
        path: (node) => node.path,
        component: ".src/templates/MarkdownDocs.vue"
      },
    ],
  },
};
