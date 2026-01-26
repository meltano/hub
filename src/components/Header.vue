<script setup lang="ts">
import { ref, onMounted } from 'vue';
import Search from './Search.vue';

interface SearchPlugin {
  id: string;
  name: string;
  label: string;
  description?: string;
  path: string;
  logo_url?: string;
  pluginType: string;
  pluginTypePlural: string;
  keywords?: string[];
}

const showMobileMenu = ref(false);
const searchPlugins = ref<SearchPlugin[]>([]);

function toggleMenu() {
  showMobileMenu.value = !showMobileMenu.value;
}

// Load search data on client-side
onMounted(async () => {
  try {
    const response = await fetch('/api/search-index.json');
    if (response.ok) {
      searchPlugins.value = await response.json();
    }
  } catch (error) {
    console.error('Failed to load search index:', error);
  }
});
</script>

<template>
  <header class="header max-w-7xl w-full mx-auto">
    <div class="top-nav flex-wrap">
      <div class="py-5 lg:py-6 xl:py-7 lg:w-1/3 xl:w-1/4">
        <a href="/" class="block logo-wrap">
          <img src="/assets/images/meltano-logo.svg" alt="Meltano Hub" class="logo-img" />
        </a>
      </div>
      <div class="w-full px-4 hidden xl:block lg:w-1/3 xl:w-5/12">
        <Search :plugins="searchPlugins" />
      </div>

      <button class="hamburger block md:hidden" @click="toggleMenu"></button>
      <nav
        class="flex md:shrink md:flex md:flex-row w-full md:w-auto lg:w-auto xl:w-1/4 lg:justify-around justify-center"
        :class="showMobileMenu ? 'flex' : 'hidden'"
      >
        <div class="dropdown">
          <a class="page-link" href="#">Plugins</a>
          <div class="dropdown-content">
            <a class="nav__link" href="/extractors">
              <h3>Extractors</h3>
            </a>
            <a class="nav__link" href="/loaders/">
              <h3>Loaders</h3>
            </a>
            <a class="nav__link" href="/mappers/">
              <h3>Mappers</h3>
            </a>
            <a class="nav__link" href="/utilities/">
              <h3>Utilities</h3>
            </a>
            <a class="nav__link" href="/files/">
              <h3>Files</h3>
            </a>
          </div>
        </div>
        <div class="dropdown">
          <a class="page-link" href="#">Singer</a>
          <div class="dropdown-content">
            <a class="nav__link" href="/extractors">
              <h3>Taps</h3>
            </a>
            <a class="nav__link" href="/loaders">
              <h3>Targets</h3>
            </a>
            <a class="nav__link" href="https://sdk.meltano.com">
              <h3>SDK</h3>
            </a>
            <a class="nav__link" href="/singer/spec">
              <h3>Spec</h3>
            </a>
            <a class="nav__link" href="/singer/docs">
              <h3>Docs</h3>
            </a>
          </div>
        </div>
        <div class="dropdown">
          <a class="page-link" href="#">Documentation</a>
          <div class="dropdown-content">
            <a class="nav__link" href="/add-a-tap">
              <h3>Add a Tap/Target</h3>
            </a>
            <a class="nav__link" href="/tap-target-maintenance">
              <h3>Tap/Target Maintenance</h3>
            </a>
          </div>
        </div>
      </nav>
    </div>
    <div class="bottom-search block xl:hidden px-4 mt-4 max-w-2xl mx-auto">
      <Search :plugins="searchPlugins" />
    </div>
  </header>
</template>

<style scoped>
.logo-wrap {
  display: block;
  flex-grow: 1;
}

.logo-img,
.logo-wrap {
  width: 135px;
}

@media (min-width: 768px) {
  .logo-img,
  .logo-wrap {
    width: 200px;
  }
}

.header {
  position: relative;
  z-index: 20;
  display: flex;
  background: transparent;
  flex-wrap: wrap;
}

.header .top-nav {
  width: 100%;
  display: flex;
  justify-content: space-between;
  padding: 0 20px;
  align-items: center;
}

.header .top-nav nav {
  align-items: center;
}

.header .top-nav nav span:first-of-type {
  height: 28px;
}

.header .bottom-search {
  width: 100%;
}

.header a {
  color: #080216;
  font-weight: 500;
  text-decoration: none;
}

.header .hamburger {
  background: url('/assets/images/bars-solid.svg') no-repeat;
  width: 40px;
  height: 40px;
  color: #3438bf;
  border: none;
  background-position: center;
}

.dropdown {
  cursor: pointer;
  position: relative;
  padding: 16px 8px;
  font-family: 'IBM Plex Mono', monospace;
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
}

.dropdown-content::after {
  position: absolute;
  width: 14px;
  height: 14px;
  left: 50%;
  margin-left: -14px;
  content: '';
  display: block;
  transform: rotate(45deg) translateY(-10px);
  background-color: #1e1e1e;
  z-index: 0;
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
}

@media (min-width: 640px) {
  .dropdown {
    display: inline-block;
  }
}

@media (min-width: 1000px) {
  .header .dropdown {
    padding: 12px 8px;
  }

  .header .dropdown .page-link {
    margin: 0 10px;
  }
}
</style>
