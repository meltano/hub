// This is the main.js file. Import global CSS and scripts here.
// The Client API can be used here. Learn more: gridsome.org/docs/client-api

import DefaultLayout from "./layouts/Default.vue";
import "./assets/css/main.css";
import "prismjs/themes/prism-tomorrow.css";

export default function main(Vue, { head }) {
  // Set default layout as a global component
  // eslint-disable-next-line vue/multi-word-component-names
  Vue.component("Layout", DefaultLayout);
  // Set font to IBM Plex Sans
  head.link.push({
    rel: "preconnect",
    href: "https://fonts.googleapis.com",
  });
  head.link.push({
    rel: "preconnect",
    href: "https://fonts.gstatic.com",
    crossorigin: true
  });
  head.link.push({
    rel: "stylesheet",
    href: "https://fonts.googleapis.com/css2?family=Hanken+Grotesk&family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700&display=swap",
  });
  head.script.push({
    src: "https://buttons.github.io/buttons.js",
  });
  head.meta.push({
    name: 'viewport',
    content: 'width=device-width, initial-scale=1'
  })
}
