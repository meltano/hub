const c1 = () => import(/* webpackChunkName: "page--src--templates--utilities-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/templates/Utilities.vue")
const c2 = () => import(/* webpackChunkName: "page--src--templates--transformers-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/templates/Transformers.vue")
const c3 = () => import(/* webpackChunkName: "page--src--templates--orchestrators-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/templates/Orchestrators.vue")
const c4 = () => import(/* webpackChunkName: "page--src--templates--loaders-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/templates/Loaders.vue")
const c5 = () => import(/* webpackChunkName: "page--src--templates--files-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/templates/Files.vue")
const c6 = () => import(/* webpackChunkName: "page--src--templates--extractors-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/templates/Extractors.vue")
const c7 = () => import(/* webpackChunkName: "page--src--pages--utilities-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/Utilities.vue")
const c8 = () => import(/* webpackChunkName: "page--src--pages--transformers-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/Transformers.vue")
const c9 = () => import(/* webpackChunkName: "page--src--pages--orchestrators-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/Orchestrators.vue")
const c10 = () => import(/* webpackChunkName: "page--src--pages--loaders-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/Loaders.vue")
const c11 = () => import(/* webpackChunkName: "page--src--pages--files-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/Files.vue")
const c12 = () => import(/* webpackChunkName: "page--src--pages--extractors-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/Extractors.vue")
const c13 = () => import(/* webpackChunkName: "page--src--pages--404-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/404.vue")
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
    path: "/utilities/:page(\\d+)?/",
    component: c7
  },
  {
    path: "/transformers/:page(\\d+)?/",
    component: c8
  },
  {
    path: "/orchestrators/:page(\\d+)?/",
    component: c9
  },
  {
    path: "/loaders/:page(\\d+)?/",
    component: c10
  },
  {
    path: "/files/:page(\\d+)?/",
    component: c11
  },
  {
    path: "/extractors/:page(\\d+)?/",
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
