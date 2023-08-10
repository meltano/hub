<script setup>
import HeroCard from "./HeroCard.vue";
</script>

<template>
  <header>
    <div class="w-full max-w-5xl px-4 pt-16 mx-auto md:pt-16 lg:pt-32">
      <div
        class="flex flex-wrap-reverse items-center justify-center -mx-4 md:flex-wrap md:justify-between"
      >
        <div class="w-full px-4 text-center md:w-1/2 lg:w-2/5 xl:w-7/12 md:text-left">
          <h1
            class="text-5xl font-bold leading-tight xl:text-7xl md:text-6xl font-pjs text-purple lg:max-w-lg"
          >
            The <span class="brackets brackets-pink">joy</span> of creating
          </h1>
          <p
            class="max-w-sm mx-auto mt-6 text-base leading-relaxed font-grotesk lg:text-xl md:ml-0 text-black/75"
          >
            Everything you need and more to move, transform, and explore your data
          </p>
        </div>

        <div class="w-10/12 px-4 mb-8 md:w-1/2 lg:w-2/5 xl:5/12 md:mb-0">
          <img src="@/assets/images/hero-image.svg" alt="hero image" class="w-full hero-image" />
        </div>
      </div>

      <div class="flex flex-wrap items-center justify-center mt-12 -mx-3 md:mt-16 lg:mt-20">
        <div
          v-for="item in items"
          :key="item.name"
          class="w-full max-w-sm px-3 my-4 md:w-1/3 lg:my-0"
        >
          <HeroCard :item="item" />
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import IconArrowFrom from "../icons/IconArrowFrom.vue";
import IconArrowTo from "../icons/IconArrowTo.vue";
import IconWrench from "../icons/IconWrench.vue";

import cyl from "../../assets/images/cyl.svg";
import cube from "../../assets/images/cube.svg";
import cone from "../../assets/images/cone.svg";

const items = [
  { name: "Browse Extractors", url: "/extractors", icon: IconArrowFrom, svg: cyl },
  { name: "Browse Loaders", url: "/loaders", icon: IconArrowTo, svg: cube },
  { name: "Browse Tools", url: "/utilities", icon: IconWrench, svg: cone },
];
export default {
  metaInfo: {
    title: "Home",
  },
  name: "HomePage",
  data() {
    return {
      items,
    };
  },
};
</script>
