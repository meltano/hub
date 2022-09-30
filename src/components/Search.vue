<template>
  <div class="grid grid-col-1 px-20 py-8">
    <input
      type="text"
      name="search"
      id="search"
      placeholder="Search 300+ connectors and tools that work with Meltano…"
      class="text-black col-span-1 bg-slate-100 pl-4 border-solid border-black border-2 w-10/12 place-self-center"
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
        class="absolute overflow-scroll max-h-96 mt-12 mx-44 justify-self-center grid grid-cols-1 grid-span-1 w-9/12 bg-slate-100 z-40 shadow-lg pt-2"
        v-if="search != '' && (searchFocused || hoveringOnSearchOptions)"
      >
        <div
          v-if="searchResults.length > 0 && (searchFocused || hoveringOnSearchOptions)"
          class="grid grid-cols-1 grid-span-1 justify-self-center w-full shadow-lg rounded gap-2 px-3"
        >
          <div
            v-for="plugin in searchResults.slice(0, 10)"
            :key="plugin.node.id"
            class="grid grid-cols-1 grid-span-1 place-self-start w-full"
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
              class="grid grid-cols-12 bg-white rounded w-full align-self-center h-full hover:bg-slate-200"
            >
              <div class="grid h-full p-4 place-items-center">
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
              <div class="grid align-items-center grid-rows-3 col-span-10 p-3">
                <div class="flex space-x-3 pt-1">
                  <p class="font-bold text-black text-lg underline place-self-center">
                    {{ plugin.node.label }}
                  </p>
                  <div class="place-self-center">
                    <span
                      class="bg-sky-100 text-sm text-center rounded-lg place-self-center py-1 px-2"
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
  allPlugins(
    filter: { isDefault: { eq: true }, hidden: { ne: true }, pluginType: { ne: "transform" } }
  ) {
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
