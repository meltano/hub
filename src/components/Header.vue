<script>
import Search from "./Search.vue";
import Dropdown from "./Dropdown.vue";

const dropdownItems = [
  {
    name: "Main",
    path: "/maintainers",
  },
  {
    name: "Single",
    path: "/single",
  },
  {
    name: "Extr",
    path: "/extractor-loader",
  },
  {
    name: "Dbt",
    path: "/dbt-tool-toopic",
  },
  {
    name: "WHouse",
    path: "/warehouse-topic",
  },
  {
    name: "Explore",
    path: "/hub-explore",
  },
];

const dropdownItemsRight = [
  {
    name: "Extr",
    path: "/extractor-loader",
  },
  {
    name: "Dbt",
    path: "/dbt-tool-toopic",
  },
  {
    name: "WHouse",
    path: "/warehouse-topic",
  },
  {
    name: "Explore",
    path: "/hub-explore",
  },
];
const dropdownItemsLeft = [
  {
    name: "Main",
    path: "/maintainers",
  },
  {
    name: "Single",
    path: "/single",
  },
  {
    name: "Extr",
    path: "/extractor-loader",
  },
  {
    name: "Dbt",
    path: "/dbt-tool-toopic",
  },
];

const navbarItems = [
  // {
  //   name: 'Main',
  //   path: '/maintainers'
  // }
];

export default {
  name: "HeaderLayout",
  components: {
    Search,
    Dropdown,
  },
  data() {
    return {
      showMobileMenu: false,
      showMobileSearchBar: false,
      scrolled: false,
      navbarItems,
      dropdownItems,
      dropdownItemsLeft,
      dropdownItemsRight,
    };
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  methods: {
    showMenu() {
      if (this.showMobileSearchBar) {
        this.showMobileSearchBar = false;
      }
      this.showMobileMenu = !this.showMobileMenu;
    },
    showSearchBar() {
      if (this.showMobileMenu && !this.showMobileSearchBar) {
        this.showMobileMenu = false;
      }

      if (!this.showMobileSearchBar) {
        document.querySelector(".mobile-search .search-bar").focus();
      }

      this.showMobileSearchBar = !this.showMobileSearchBar;
    },
    handleScroll() {
      if (window.scrollY > 10) {
        this.scrolled = true;
      } else {
        this.scrolled = false;
      }
    },
  },
};
</script>
<template>
  <span>
    <div
      :class="[
        scrolled
          ? 'h-16 xl:h-20 bg-purple-10 md:bg-purple-10 backdrop backdrop-blur-md'
          : 'h-16 lg:h-24 xl:h-28 bg-purple-10 md:bg-transparent',
        ' z-50 fixed top-0 w-full transition-all duration-500 flex items-center',
      ]"
    >
      <header class="container relative z-20 w-full max-w-6xl mx-auto header">
        <div class="flex flex-wrap items-center justify-between w-full top-nav">
          <div :class="['xl:w-auto flex-1 xl:flex-none px-4']">
            <a href="/" :class="['nav-logo block grow transition-all duration-200']">
              <img src="../assets/images/meltano-logo.svg" class="w-full" />
            </a>
          </div>
          <div class="order-last hidden max-w-xl px-4 md:order-none md:w-auto grow lg:block">
            <Search />
          </div>
          <div class="flex items-center w-auto px-0 shrink lg:hidden">
            <!-- search toggle -->
            <button class="text-purple" @click="showSearchBar()">
              <div class="relative flex flex-col justify-between w-4 h-4">
                <svg
                  v-if="!showMobileSearchBar"
                  class="block w-4 h-4"
                  width="12"
                  height="15"
                  viewBox="0 0 12 15"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fill-rule="evenodd"
                    clip-rule="evenodd"
                    d="M10 6.59998C10 8.80911 8.20914 10.6 6 10.6C3.79086 10.6 2 8.80911 2 6.59998C2 4.39084 3.79086 2.59998 6 2.59998C8.20914 2.59998 10 4.39084 10 6.59998ZM8.38157 12.1087C7.65149 12.4248 6.8462 12.6 6 12.6C2.68629 12.6 0 9.91368 0 6.59998C0 3.28627 2.68629 0.599976 6 0.599976C9.31371 0.599976 12 3.28627 12 6.59998C12 8.34688 11.2534 9.91942 10.062 11.0159L11.4 12.8C11.7314 13.2418 11.6418 13.8686 11.2 14.2C10.7582 14.5313 10.1314 14.4418 9.8 14L8.38157 12.1087Z"
                    fill="#080216"
                  />
                </svg>

                <svg
                  v-if="showMobileSearchBar"
                  class="block w-4 h-4"
                  width="12"
                  height="13"
                  viewBox="0 0 12 13"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fill-rule="evenodd"
                    clip-rule="evenodd"
                    d="M11.7073 10.3762C12.0978 10.7667 12.0978 11.3999 11.7073 11.7904C11.3167 12.1809 10.6836 12.1809 10.2931 11.7904L6.41685 7.91419L2.5406 11.7904C2.15008 12.181 1.51691 12.181 1.12639 11.7904C0.735865 11.3999 0.735865 10.7668 1.12639 10.3762L5.00264 6.49998L1.12639 2.62373C0.735865 2.23321 0.735865 1.60004 1.12639 1.20952C1.51691 0.818995 2.15008 0.818995 2.5406 1.20952L6.41685 5.08577L10.2931 1.20956C10.6836 0.819035 11.3167 0.819035 11.7073 1.20956C12.0978 1.60008 12.0978 2.23325 11.7073 2.62377L7.83106 6.49998L11.7073 10.3762Z"
                    fill="black"
                  />
                </svg>
              </div>
            </button>
          </div>
          <div class="flex items-center w-auto px-4 shrink md:hidden">
            <!-- hamburger -->
            <button class="text-purple" @click="showMenu()">
              <div class="relative flex flex-col justify-between w-5 h-4">
                <div
                  :class="[
                    this.showMobileMenu ? 'translate-y-2 origin-center opacity-0' : 'opacity-100',
                    'w-5 h-0.5 duration-100 delay-200 bg-purple',
                  ]"
                />
                <div class="relative h-0.5">
                  <div
                    :class="[
                      this.showMobileMenu ? 'rotate-45 ' : 'rotate-180',
                      'w-5 h-0.5 duration-500 delay-200 origin-center bg-purple absolute',
                    ]"
                  />
                  <div
                    :class="[
                      this.showMobileMenu ? '-rotate-45 ' : 'rotate-180',
                      'w-5 h-0.5 duration-500 delay-200 origin-center bg-purple absolute',
                    ]"
                  />
                </div>
                <div
                  :class="[
                    this.showMobileMenu ? '-translate-y-2 origin-center opacity-0' : 'opacity-100',
                    'w-5 h-0.5 duration-100 delay-200 bg-purple',
                  ]"
                />
              </div>
            </button>
          </div>
          <nav
            :class="[
              this.showMobileMenu
                ? 'md:max-h-screen flex bg-purple-10 pb-4 md:pb-0 opacity-100'
                : 'max-h-0 overflow-hidden opacity-0',
              'flex absolute inset-x-0 px-4 top-10 md:bg-transparent md:relative md:top-auto md:overflow-visible md:opacity-100 md:max-h-none space-y-3 md:space-y-0 md:shrink md:flex md:flex-row w-full flex-col md:w-auto shrink md:justify-end justify-center items-center font-medium transition-all duration-200',
            ]"
          >
            <span v-for="(item, index) in navbarItems" :key="index + '-navbar-item'">
              <RouterLink
                :to="item.path"
                @click="showMenu()"
                class="whitespace-nowrap rounded-md px-4 md:px-1.5 lg:px-4 w-full backdrop-blur-md md:backdrop-blur-none bg-purple/5 md:bg-transparent md:w-auto md:border-transparent py-3 md:py-2 border md:border-2 border-black/15 text-[15px] mx-1 font-ibm"
              >
                {{ item.name }}
              </RouterLink>
            </span>

            <!-- <Dropdown item="Explore" :items="dropdownItems" alignment="left" />
          <Dropdown item="Explore" :items="dropdownItems" alignment="center" /> -->
            <Dropdown item="Explore" :items="dropdownItems" alignment="right" />

            <a
              href="#"
              class="rounded-md px-4 w-full backdrop-blur-md md:backdrop-blur-none bg-purple/5 md:bg-transparent md:w-auto py-3 md:py-2 border md:border-2 border-black/15 md:border-black text-[15px] mx-1 font-ibm"
              >Publish</a
            >
          </nav>
        </div>
      </header>
    </div>
    <div class="relative z-20 block w-full lg:hidden top-16 mobile-search">
      <div
        :class="[
          showMobileSearchBar ? 'max-h-screen pt-1 pb-4' : 'max-h-0 overflow-hidden',
          'bottom-search px-4 max-w-2xl mx-auto duration-500',
        ]"
      >
        <Search />
      </div>
    </div>
  </span>
</template>

<style lang="scss">
.nav-logo {
  width: 186px;
  @media (min-width: 768px) {
    width: 230px;
  }
}

.dropdown {
  cursor: pointer;
  position: relative;
  padding: 16px 8px;
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
</style>
