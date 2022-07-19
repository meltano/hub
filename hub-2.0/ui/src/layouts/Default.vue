<script>
import FooterLayout from "./Footer.vue";
import HeaderLayout from "./Header.vue";

export default {
  components: { FooterLayout, HeaderLayout },
  name: "DefaultLayout",
};
</script>

<template>
  <div class="layout">
    <div class="stripe" />
    <HeaderLayout />
    <main>
      <slot />
    </main>
    <FooterLayout />
    <div class="stripe" />
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
  margin: 0 auto;
  min-height: 100%;
  display: flex;
  flex-direction: column;
  align-items: stretch;
}

.stripe {
  width: 100%;
  background: linear-gradient(90deg, #3438bf, #d9042b);
  height: 10px;
}
</style>
