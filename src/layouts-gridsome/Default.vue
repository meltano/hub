<script>
import FooterLayout from "./Footer.vue";
import HeaderLayout from "./Header.vue";

export default {
  components: { FooterLayout, HeaderLayout },
  name: "DefaultLayout",
};
</script>

<template>
  <div>
    <div class="layout">
      <HeaderLayout />
      <main>
        <slot />
      </main>
      <FooterLayout />
      <div class="absolute hidden lg:block left-cloud left-0 top-0 z-0 w-1/12 max-w-xs">
        <g-image src="../assets/images/left-cloud.png" width="250" />
      </div>
      <div class="absolute hidden lg:block right-cloud right-0 top-0 z-0 w-1/5 mx-w-lg">
        <g-image src="../assets/images/right-cloud.png" class="float-right" width="350" />
      </div>
    </div>
  </div>
</template>

<static-query lang="graphql">
query {
  metadata {
    siteName
  }
}
</static-query>

<style lang="scss">
.layout {
  position: relative;
  z-index: 20;
  margin: 0 auto;
  min-height: 100%;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  background: linear-gradient(180deg, #dad1fe -39.21%, #dad1fe 500px, #e9e5fb 1500px);
}
.stripe {
  width: 100%;
  background: linear-gradient(90deg, #3438bf, #d9042b);
  height: 10px;
}
</style>
