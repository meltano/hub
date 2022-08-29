// This is the main.js file. Import global CSS and scripts here.
// The Client API can be used here. Learn more: gridsome.org/docs/client-api

import DefaultLayout from "./layouts/Default.vue";
import "./assets/css/main.css";

export default function main(Vue, { head }) {
  // Set default layout as a global component
  // eslint-disable-next-line vue/multi-word-component-names
  Vue.component("Layout", DefaultLayout);
  // Set font to IBM Plex Sans
  head.link.push({
    rel: "stylesheet",
    href: "https://fonts.googleapis.com/css?family=IBM+Plex+Mono|IBM+Plex+Sans&display=swap",
  });
  head.script.push({
    src: "https://buttons.github.io/buttons.js",
  });
}
