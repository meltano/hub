const c1 = () => import(/* webpackChunkName: "page--src--pages--utilities-vue" */ "/Users/alexmarple/Meltano/meltano-hub-v2.0/src/pages/Utilities.vue")
const c2 = () => import(/* webpackChunkName: "page--src--pages--loaders-vue" */ "/Users/alexmarple/Meltano/meltano-hub-v2.0/src/pages/Loaders.vue")
const c3 = () => import(/* webpackChunkName: "page--src--pages--extractors-vue" */ "/Users/alexmarple/Meltano/meltano-hub-v2.0/src/pages/Extractors.vue")
const c4 = () => import(/* webpackChunkName: "page--src--pages--about-vue" */ "/Users/alexmarple/Meltano/meltano-hub-v2.0/src/pages/About.vue")
const c5 = () => import(/* webpackChunkName: "page--node-modules--gridsome--app--pages--404-vue" */ "/Users/alexmarple/Meltano/meltano-hub-v2.0/node_modules/gridsome/app/pages/404.vue")
const c6 = () => import(/* webpackChunkName: "page--src--pages--index-vue" */ "/Users/alexmarple/Meltano/meltano-hub-v2.0/src/pages/Index.vue")

export default [
  {
    path: "/utilities/",
    component: c1
  },
  {
    path: "/loaders/",
    component: c2
  },
  {
    path: "/extractors/",
    component: c3
  },
  {
    path: "/about/",
    component: c4
  },
  {
    name: "404",
    path: "/404/",
    component: c5
  },
  {
    name: "home",
    path: "/",
    component: c6
  },
  {
    name: "*",
    path: "*",
    component: c5
  }
]
