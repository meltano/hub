<template>
  <div class="grid-col-1 grid px-20 py-8">
    <input
      type="text"
      name="search"
      id="search"
      placeholder="Search 300+ connectors and tools that work with Meltano…"
      class="col-span-1 w-10/12 place-self-center border-2 border-solid border-black bg-slate-100 pl-4 text-black"
      ref="searchBar"
      v-model="search"
      @focus="searchFocused = true"
      @blur="searchFocused = false"
      v-focus="searchFocused"
    />
    <transition
      enter-active-class="transform transition duration-200 ease-custom"
      enter-class="-translate-y-1/2 scale-y-0 opacity-0"
      enter-to-class="translate-y-0 scale-y-100 opacity-100"
      leave-active-class="transform transition duration-300 ease-custom"
      leave-class="translate-y-0 scale-y-100 opacity-100"
      leave-to-class="-translate-y-1/2 scale-y-0 opacity-0"
    >
      <div
        class="grid-span-1 absolute z-40 mx-44 mt-12 grid max-h-96 w-9/12 grid-cols-1 justify-self-center overflow-scroll bg-slate-100 pt-2 shadow-lg"
        v-if="search != '' && (searchFocused || hoveringOnSearchOptions)"
      >
        <div
          v-if="searchResults.length > 0 && (searchFocused || hoveringOnSearchOptions)"
          class="grid-span-1 grid w-full grid-cols-1 gap-2 justify-self-center rounded px-3 shadow-lg"
        >
          <div
            v-for="plugin in searchResults.slice(0, 10)"
            :key="plugin.node.id"
            class="grid-span-1 grid w-full grid-cols-1 place-self-start"
            @mouseover="hoveringOnSearchOptions = true"
            @mouseleave="hoveringOnSearchOptions = false"
            @click="
              hoveringOnSearchOptions = false;
              searchFocused = false;
              this.$refs.searchBar.reset();
            "
          >
            <g-link
              :to="plugin.node.path.split('--')[0]"
              class="align-self-center grid h-full w-full grid-cols-12 rounded bg-white hover:bg-slate-200"
            >
              <div class="grid h-full place-items-center p-4">
                <g-image
                  v-if="plugin.node.logo_url"
                  :src="
                    require(`!!assets-loader?width=75!@logos/${plugin.node.logo_url.replace(
                      '/assets/logos/',
                      ''
                    )}`)
                  "
                />
                <g-image
                  v-else
                  :src="
                    require(`!!assets-loader?width=75!@logos/${plugin.node.pluginTypePlural}/${plugin.node.name}.png`)
                  "
                />
              </div>
              <div class="align-items-center col-span-10 grid grid-rows-3 p-3">
                <div class="flex space-x-3 pt-1">
                  <p class="place-self-center text-lg font-bold text-black underline">
                    {{ plugin.node.label }}
                  </p>
                  <div class="place-self-center">
                    <span
                      class="place-self-center rounded-lg bg-sky-100 py-1 px-2 text-center text-sm"
                    >
                      {{ plugin.node.pluginType }}
                    </span>
                  </div>
                </div>
                <span class="text-black">{{ plugin.node.description || "No description" }}</span>
              </div>
            </g-link>
          </div>
        </div>

        <div v-else>
          <p class="text-amber-800">Your search didn't return any results. Please try again.</p>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  data() {
    return {
      search: "",
      searchFocused: false,
      hoveringOnSearchOptions: false,
    };
  },
  computed: {
    searchResults() {
      const pluginCollections = [this.$static.allPlugins];
      return pluginCollections.flatMap((coll) =>
        coll.edges.filter((plugin) => {
          const pluginTextFields = [
            plugin.node.name,
            plugin.node.description,
            plugin.node.label,
            plugin.node.keywords?.join(" "),
          ];
          return pluginTextFields
            .join(" ")
            .toLowerCase()
            .includes(this.search.toLowerCase().trim());
        })
      );
    },
  },
};
</script>

<static-query lang="graphql">
query {
  allPlugins(filter: { isDefault: { eq: true }, hidden: { ne: true } }) {
    edges {
      node {
        id
        description
        path
        label
        name
        logo_url
        pluginType
        pluginTypePlural
        keywords
      }
    }
  }
}
</static-query>

<style lang="scss">
.search {
  .results {
    box-shadow: 1px 2px 4px rgba(0, 0, 0, 0.3);
    position: absolute;
    width: 75%;
    align-content: left;
    margin-top: 80px;
    background: white;
    line-height: 1rem;

    .result-item {
      color: black;
      padding: 0.5rem;
      border-bottom: 2px solid black;

      a {
        text-decoration: none;
        display: flex;
        justify-content: space-between;
      }
    }
  }
}
</style>
