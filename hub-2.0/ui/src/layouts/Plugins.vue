<script>
  import Search from '../components/Search.vue';
  import Footer from './Footer.vue';
  export default {
    components: { Search, Footer }
  }
</script>

<template>
  <div class="template-plugins">
    <div class="stripe" />
    <Header />
    <main>
      <Search />
      <slot/>
    </main>
    <Footer />
    <div class="stripe" />
  </div>
</template>

<script>
export default {
    name: "Plugins"
}
</script>

<style>
  .templates-plugins {
    background: #e8f0ff;
  }
</style>