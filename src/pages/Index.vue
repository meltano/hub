<template>
  <Layout>
    <div class="max-w-6xl w-full mx-auto py-16 md:py-16 px-4 lg:py-32">
      <div
        class="flex flex-wrap-reverse md:flex-wrap items-center justify-center md:justify-between -mx-4"
      >
        <div class="w-full md:w-1/2 lg:w-2/5 xl:w-7/12 px-4 md:text-left text-center">
          <h1 class="xl:text-7xl md:text-6xl text-5xl leading-tight font-pjs text-purple font-bold">
            The <span class="brackets">joy</span> of creating
          </h1>
          <p class="mt-6 font-light max-w-sm text-base lg:text-lg md:ml-0 mx-auto">
            Everything you need and more to move, transform, and explore your data
          </p>
        </div>
        <div class="w-10/12 md:w-1/2 lg:w-2/5 xl:5/12 px-4 mb-8 md:mb-0">
          <g-image
            src="../assets/images/hero-image.svg"
            alt="hero image"
            class="hero-image w-full"
          />
        </div>
      </div>

      <div
        class="flex flex-wrap items-center justify-center mt-12 md:mt-16 lg:mt-20 -mx-4 lg:space-y-0 space-y-4"
      >
        <div
          v-for="item in items"
          :key="item.name"
          class="w-full max-w-sm md:max-w-md lg:w-1/3 px-4"
        >
          <g-link
            :to="item.url"
            class="block text-white hover:bg-white bg-purple/5 border border-purple/15 rounded"
          >
            <g-image
              :src="require('!!assets-loader!~/assets/images/' + item.svg)"
              :alt="item.name"
              class="w-40 h-40 mx-auto mt-12 mb-8"
            />
            <span class="flex flex-row justify-center mb-12">
              <span
                class="bg-blue flex flex-row justify-center font-ibm items-center w-auto rounded-md px-4 py-2 leading-none"
              >
                <g-image
                  class="w-7 h-7 mr-3 inline"
                  :src="require('!!assets-loader!~/assets/images/' + item.icon)"
                  :alt="item.name"
                />
                {{ item.name }}
              </span>
            </span>
          </g-link>
        </div>
      </div>
    </div>
  </Layout>
</template>

<script>
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
