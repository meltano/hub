const c1 = () => import(/* webpackChunkName: "page--src--templates--utility-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/templates/Utility.vue")
const c2 = () => import(/* webpackChunkName: "page--src--templates--transformer-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/templates/Transformer.vue")
const c3 = () => import(/* webpackChunkName: "page--src--templates--orchestrator-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/templates/Orchestrator.vue")
const c4 = () => import(/* webpackChunkName: "page--src--templates--loader-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/templates/Loader.vue")
const c5 = () => import(/* webpackChunkName: "page--src--templates--file-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/templates/File.vue")
const c6 = () => import(/* webpackChunkName: "page--src--templates--extractor-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/templates/Extractor.vue")
const c7 = () => import(/* webpackChunkName: "page--src--pages--utilities-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/Utilities.vue")
const c8 = () => import(/* webpackChunkName: "page--src--pages--transformers-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/Transformers.vue")
const c9 = () => import(/* webpackChunkName: "page--src--pages--orchestrators-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/Orchestrators.vue")
const c10 = () => import(/* webpackChunkName: "page--src--pages--loaders-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/Loaders.vue")
const c11 = () => import(/* webpackChunkName: "page--src--pages--files-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/Files.vue")
const c12 = () => import(/* webpackChunkName: "page--src--pages--extractors-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/Extractors.vue")
const c13 = () => import(/* webpackChunkName: "page--node-modules--gridsome--app--pages--404-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/node_modules/gridsome/app/pages/404.vue")
const c14 = () => import(/* webpackChunkName: "page--src--pages--index-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/Index.vue")

export default [
  {
    path: "/utilities/:name/:variant/",
    component: c1
  },
  {
    path: "/transformers/:name/:variant/",
    component: c2
  },
  {
    path: "/orchestrators/:name/:variant/",
    component: c3
  },
  {
    path: "/loaders/:name/:variant/",
    component: c4
  },
  {
    path: "/files/:name/:variant/",
    component: c5
  },
  {
    path: "/extractors/:name/:variant/",
    component: c6
  },
  {
    path: "/utilities/",
    component: c7
  },
  {
    path: "/transformers/",
    component: c8
  },
  {
    path: "/orchestrators/",
    component: c9
  },
  {
    path: "/loaders/",
    component: c10
  },
  {
    path: "/files/",
    component: c11
  },
  {
    path: "/extractors/",
    component: c12
  },
  {
    name: "404",
    path: "/404/",
    component: c13
  },
  {
    name: "home",
    path: "/",
    component: c14
  },
  {
    name: "*",
    path: "*",
    component: c13
  }
]
