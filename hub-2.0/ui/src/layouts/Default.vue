<script>
  import Search from '../components/Search.vue';
  import Footer from './Footer.vue';
  import Header from './Header.vue';
  export default {
    components: { Search, Footer, Header }
  }
</script>

<template>
  <div class="layout">
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

<static-query>
query {
  metadata {
    siteName
  }
}
</static-query>

<style>
html, body {
  width: 100%;
  height: 100%;
}
body {
  /* font-family: -apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif; */
  font-family: IBM Plex Sans;
  margin:0;
  padding:0;
  line-height: 1.5;
  background: #fff;
  background: url('../images/meltano-background.jpeg');
  /* background: #2126A4; */
  color: #fff;
  /* color: #2126A4; */
}

.layout {
  /* max-width: 760px; */
  margin: 0 auto;
  /* padding-left: 20px; */
  /* padding-right: 20px; */
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

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  /* margin-bottom: 20px; */
  border-bottom: 2px solid #f1f1f2;
  height: 80px;
  /* background: #2126A4; */
  background: #fff;
  padding-left: 20px; 
  padding-right: 20px;
  /* color: #fff; */
}

.header a {
  color: #3438bf;
  text-decoration: none;
  margin-left: 20px;
}

.nav__link {
  color: #3438bf;
  text-decoration: none;
}

.footer a {
  margin: 10px 0 10px 0;
}

main {
  flex-grow: 1;
}

header, main, footer {
  flex-shrink: 0;
}
</style>
