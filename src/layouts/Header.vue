<script>
import Search from "../components/Search.vue";

export default {
  name: "HeaderLayout",
  components: {
    Search,
  },
};
</script>
<template>
  <header class="header">
    <div class="top-nav">
      <div class="py-3">
        <g-link to="/" class="flex">
          <g-image src="../assets/images/meltano-logo.svg" class="logo-img" />
        </g-link>
      </div>
      <nav class="nav">
        <button class="hamburger"></button>
        <div class="mx-2">
          <a href="https://github.com/meltano/meltano"
            ><img
              alt="Forks"
              :src="`https://img.shields.io/github/stars/meltano/meltano?style=social`"
          /></a>
        </div>
        <div class="dropdown">
          <a class="page-link" href="#">Plugins</a>
          <div class="dropdown-content">
            <g-link class="nav__link" to="/extractors">
              <h3>Extractors</h3>
            </g-link>
            <g-link class="nav__link" to="/loaders/">
              <h3>Loaders</h3>
            </g-link>
            <g-link class="nav__link" to="/transformers/">
              <h3>Transformers</h3>
            </g-link>
            <g-link class="nav__link" to="/orchestrators">
              <h3>Orchestrators</h3>
            </g-link>
            <g-link class="nav__link" to="/utilities/">
              <h3>Utilities</h3>
            </g-link>
            <g-link class="nav__link" to="/files/">
              <h3>Files</h3>
            </g-link>
          </div>
        </div>
        <div class="dropdown">
          <a class="page-link" href="#">Singer</a>
          <div class="dropdown-content">
            <g-link class="nav__link" to="/extractors">
              <h3>Taps</h3>
            </g-link>
            <g-link class="nav__link" to="/loaders">
              <h3>Targets</h3>
            </g-link>
            <a class="nav__link" href="https://sdk.meltano.com">
              <h3>SDK</h3>
            </a>
            <g-link class="nav__link" to="/singer/spec">
              <h3>Spec</h3>
            </g-link>
            <g-link class="nav__link" to="/singer/docs">
              <h3>Docs</h3>
            </g-link>
          </div>
        </div>
      </nav>
    </div>
    <div class="bottom-search">
      <Search />
    </div>
  </header>
</template>

<style lang="scss">
.logo-img {
  width: 80px;
  @media (min-width: 768px) {
    width: 150px;
  }
}

.logo-text {
  font-family: "IBM Plex Sans", sans-serif;
  font-weight: 900;
  padding-top: 0.2rem;
  font-size: 0.9rem;
  @media (min-width: 768px) {
    font-weight: 900;
    padding-top: 0.59rem;
    font-size: 1.3rem;
  }
}
.header {
  display: flex;
  background: #fff;
  flex-wrap: wrap;

  .top-nav {
    width: 100%;
    display: flex;
    justify-content: space-between;
    padding: 0 20px;
    align-items: center;
    border-bottom: 2px solid #f1f1f2;

    nav {
      display: flex;
      align-items: center;
    }
    nav span:first-of-type {
      height: 28px;
    }
  }

  .bottom-search {
    width: 100%;
  }

  a {
    color: #3438bf;
    text-decoration: none;
  }

  .hamburger {
    background: url("../assets/images/bars-solid.svg") no-repeat;
    width: 40px;
    height: 40px;
    color: #3438bf;
    border: none;
  }
}

.dropdown {
  display: none;
  position: relative;
}

.dropdown-content {
  display: none;
  position: absolute;
  overflow: auto;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  text-align: center;
  justify-content: center;
  width: auto;
  height: auto;
  right: 0;
  flex-wrap: wrap;
}

.dropdown-content a {
  display: flex;
  color: #3438bf;
  text-decoration: none;
  width: 180px;
  padding: 10px 5px;
  text-align: center;
  flex-direction: column;
}

.dropdown:hover .dropdown-content {
  display: flex;
  background: #fff;
}

.dropdown-content a:hover {
  color: #fff;
  background-color: #3438bf;
}

@media (min-width: 391px) {
  .dropdown {
    display: inline-block;
  }
  .hamburger {
    display: none;
  }
}

@media (min-width: 1000px) {
  .header {
    .dropdown {
      .page-link {
        margin: 0 10px;
      }
    }
  }
}
</style>
