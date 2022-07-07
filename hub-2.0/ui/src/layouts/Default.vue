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

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 2px solid #f1f1f2;
  height: 80px;
  background: #fff;
  padding-left: 20px;
  padding-right: 20px;
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

header,
main,
footer {
  flex-shrink: 0;
}
</style>
