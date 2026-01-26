<script>
import Search from "../components/Search.vue";

export default {
  name: "HeaderLayout",
  components: {
    Search,
  },
  data() {
    return {
      showMobileMenu: false,
    };
  },
  methods: {
    showMenu() {
      this.showMobileMenu = !this.showMobileMenu;
    },
  },
};
</script>
<template>
  <header class="header max-w-7xl w-full mx-auto">
    <div class="top-nav flex-wrap">
      <div class="py-5 lg:py-6 xl:py-7 lg:w-1/3 xl:w-1/4">
        <g-link to="/" class="block logo-wrap">
          <g-image src="../assets/images/meltano-logo.svg" class="logo-img" />
        </g-link>
      </div>
      <div class="w-full px-4 hidden xl:block lg:w-1/3 xl:w-5/12">
        <Search />
      </div>

      <!-- <div class="mx-2">
        <a href="https://github.com/meltano/meltano"
          ><img
            alt="Forks"
            :src="`https://img.shields.io/github/stars/meltano/meltano?style=social`"
        /></a>
      </div> -->
      <button class="hamburger block md:hidden" @click="showMenu()"></button>
      <nav
        class="flex md:shrink md:flex md:flex-row w-full md:w-auto lg:w-auto xl:w-1/4 justify-around"
        :class="this.showMobileMenu ? 'flex' : 'hidden'"
      >
        <div class="dropdown">
          <a class="page-link" href="#">Plugins</a>
          <div class="dropdown-content">
            <g-link class="nav__link" to="/extractors">
              <h3>Extractors</h3>
            </g-link>
            <g-link class="nav__link" to="/loaders/">
              <h3>Loaders</h3>
            </g-link>
            <g-link class="nav__link" to="/mappers/">
              <h3>Mappers</h3>
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
        <div class="dropdown">
          <a class="page-link" href="#">Documentation</a>
          <div class="dropdown-content">
            <g-link class="nav__link" to="/add-a-tap">
              <h3>Add a Tap/Target</h3>
            </g-link>
            <g-link class="nav__link" to="/tap-target-maintenance">
              <h3>Tap/Target Maintenance</h3>
            </g-link>
          </div>
        </div>
      </nav>
    </div>
    <div class="bottom-search block xl:hidden px-4 mt-4 max-w-2xl mx-auto">
      <Search />
    </div>
  </header>
</template>

<style lang="scss">
.logo-wrap {
  display: block;
  flex-grow: 1;
}

.logo-img,
.logo-wrap {
  width: 135px;
  @media (min-width: 768px) {
    width: 200px;
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
  position: relative;
  z-index: 20;
  display: flex;
  background: transparent;
  flex-wrap: wrap;

  .top-nav {
    width: 100%;
    display: flex;
    justify-content: space-between;
    padding: 0 20px;
    align-items: center;

    nav {
      // display: flex;
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
    color: #080216;
    font-weight: 500;
    text-decoration: none;
  }

  .hamburger {
    background: url("../assets/images/bars-solid.svg") no-repeat;
    width: 40px;
    height: 40px;
    color: #3438bf;
    border: none;
    background-position: center;
  }
}

.dropdown {
  cursor: pointer;
  position: relative;
  padding: 16px 4px;
  font-family: "IBM Plex Mono", monospace;
  font-weight: 500;
}

.dropdown-content {
  display: none;
  position: absolute;
  border-radius: 5px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  justify-content: center;
  width: auto;
  height: auto;
  top: 48px;
  right: 50%;
  flex-wrap: wrap;
  z-index: 10;

  &::after {
    position: absolute;
    width: 14px;
    height: 14px;
    left: 50%;
    margin-left: -14px;
    content: "";
    display: block;
    transform: rotate(45deg) translateY(-10px);
    background-color: #1e1e1e;
    z-index: 0;
  }
}

.dropdown-content a {
  display: flex;
  color: #ffffff;
  text-decoration: none;
  width: 180px;
  padding: 10px 16px;
  flex-direction: column;
}

.dropdown:hover .dropdown-content {
  display: flex;
  transform: translateX(50%);
  margin-left: 60px;
  background: #1e1e1e;
}

.dropdown-content a:hover {
  color: #18c3fa;
  // background-color: #3438bf;
}

@media (min-width: 640px) {
  .dropdown {
    display: inline-block;
  }
  // .hamburger {
  //   display: none;
  // }
}

@media (min-width: 1000px) {
  .header {
    .dropdown {
      padding: 12px 8px;
      .page-link {
        margin: 0 10px;
      }
    }
  }
}
</style>
