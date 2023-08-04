<template>
  <Layout>
    <div class="w-full max-w-6xl px-4 py-16 mx-auto md:py-16 lg:py-32">
      <div
        class="flex flex-wrap-reverse items-center justify-center -mx-4 md:flex-wrap md:justify-between"
      >
        <div class="w-full px-4 text-center md:w-1/2 lg:w-2/5 xl:w-7/12 md:text-left">
          <h1 class="text-5xl font-bold leading-tight xl:text-7xl md:text-6xl font-pjs text-purple">
            The <span class="brackets">joy</span> of creating
          </h1>
          <p class="max-w-sm mx-auto mt-6 text-base font-light lg:text-lg md:ml-0">
            Everything you need and more to move, transform, and explore your data
          </p>
        </div>
        <div class="w-10/12 px-4 mb-8 md:w-1/2 lg:w-2/5 xl:5/12 md:mb-0">
          <g-image
            src="../assets/images/hero-image.svg"
            alt="hero image"
            class="w-full hero-image"
          />
        </div>
      </div>

      <div class="flex flex-wrap items-center justify-center mt-12 -mx-3 md:mt-16 lg:mt-20">
        <div
          v-for="item in items"
          :key="item.name"
          class="w-full max-w-sm px-3 my-4 md:w-1/3 lg:my-0"
        >
          <g-link
            :to="item.url"
            class="block text-white border rounded hover:bg-white bg-purple/5 border-purple/15"
          >
            <g-image
              :src="require('!!assets-loader!~/assets/images/' + item.svg)"
              :alt="item.name"
              class="w-40 h-40 mx-auto mt-12 mb-8"
            />
            <span class="flex flex-row justify-center mb-12">
              <span
                class="flex flex-row items-center justify-center w-auto px-4 py-2 leading-none rounded-md bg-blue font-ibm"
              >
                <g-image
                  class="inline mr-3 w-7 h-7"
                  :src="require('!!assets-loader!~/assets/images/' + item.icon)"
                  :alt="item.name"
                />
                {{ item.name }}
              </span>
            </span>
          </g-link>
        </div>
      </div>
      <section class="mt-24">
        <HeroConnectors />
      </section>
    </div>
  </Layout>
</template>

<script>
import HeroConnectors from "../components/home/HeroConnectors.vue";

const items = [
  { name: "Browse Extractors", url: "/extractors", svg: "cyl.svg", icon: "Extractor.svg" },
  { name: "Browse Loaders", url: "/loaders", svg: "cube.svg", icon: "Loader.svg" },
  { name: "Browse Tools", url: "/utilities", svg: "cone.svg", icon: "Tool.svg" },
];

export default {
  metaInfo: {
    title: "Home",
  },
  name: "HomePage",
  components: {
    HeroConnectors,
  },
  data() {
    return {
      items,
    };
  },
};
</script>

<style lang="scss">
.home-details {
  font-family: "Hanken Grotesk";
}
</style>
