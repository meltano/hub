<script>
import Footer from './Footer.vue';
import Header from './Header.vue';
export default {
  components: { Footer, Header }
}
</script>

<template>
  <div class="layout">
    <div class="stripe" />
    <Header />
    <main>
      <slot />
    </main>
    <Footer />
    <div class="stripe" />
  </div>
</template>

<static-query>
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
