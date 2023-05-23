<template>
  <div class="relative">
    <input
      type="text"
      name="search"
      id="search"
      placeholder="Search 600+ connectors and tools"
      class="search-bar text-black text-sm bg-transparent pl-4 border-solid border-blue border rounded-[9999px] py-1.5 w-full placeholder:text-par placeholder:font-light font-ibm focus-visible:outline-0"
      ref="searchBar"
      :value="search"
      @input="search = $event.target.value"
      @focus="searchFocused = true"
      @blur="searchFocused = true"
      v-focus="searchFocused"
    />
    <div class="absolute right-2 top-1/4">
      <svg
        class="w-6 block mt-0.5"
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
    </div>
    <transition
      enter-active-class="transform transition duration-200 ease-custom"
      enter-class="-translate-y-1/2 scale-y-0 opacity-0"
      enter-to-class="translate-y-0 scale-y-100 opacity-100"
      leave-active-class="transform transition duration-300 ease-custom"
      leave-class="translate-y-0 scale-y-100 opacity-100"
      leave-to-class="-translate-y-1/2 scale-y-0 opacity-0"
    >
      <div
        class="absolute overflow-scroll max-h-96 mt-12 mx-auto justify-self-center grid grid-cols-1 grid-span-1 w-full bg-slate-100 z-40 shadow-lg py-2"
        v-if="search != '' && (searchFocused || hoveringOnSearchOptions)"
      >
        <div
          v-if="searchResults.length > 0 && (searchFocused || hoveringOnSearchOptions)"
          class="grid grid-cols-1 grid-span-1 justify-self-center w-full rounded gap-2 px-3"
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
              <div class="grid h-full col-span-3 p-4 place-items-center">
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
              <div class="grid align-items-center grid-rows-3 col-span-9 p-3">
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
          <p class="text-amber-800 p-4">Your search didn't return any results. Please try again.</p>
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
            plugin.node.name.replace("-", " "),
            plugin.node.description,
            plugin.node.label,
            plugin.node.keywords?.join(" "),
          ];
          return pluginTextFields
            .join(" ")
            .toLowerCase()
            .includes(this.search.toLowerCase().trim());
        }).sort((a, b) => a.node.name.localeCompare(b.node.name))
      );
    },
  },
};
</script>

<static-query lang="graphql">
query {
  allPlugins(
    filter: {
      isDefault: { eq: true }
      hidden: { ne: true }
      pluginType: { nin: ["transform", "orchestrator", "transformer"] }
      name: {
        nin: [
          "files-airflow"
          "files-dbt-snowflake"
          "files-dbt-redshift"
          "files-dbt-postgres"
          "files-dbt-duckdb"
          "files-dbt-bigquery"
          "files-dbt"
        ]
      }
    }
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
.search-bar {
  position: relative;
  &::before {
    content: "";
    display: block;
    top: 10px;
    right: 10px;
    width: 14px;
    height: 14px;
    position: absolute;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    background-image: url("/assets/icons/magnifier.svg");
  }
}
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
