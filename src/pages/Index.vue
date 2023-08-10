<template>
  <Layout>
    <div class="relative z-10 mx-auto overflow-hidden space-y-44 lg:space-y-56">
      <Hero />
      <HeroConnectors />
      <TextAndCode />
    </div>
  </Layout>
</template>

<script>
import Hero from "../components/home/Hero.vue";
import HeroConnectors from "../components/home/HeroConnectors.vue";
import TextAndCode from "../components/home/TextAndCode.vue";

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
    Hero,
    HeroConnectors,
    TextAndCode,
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
