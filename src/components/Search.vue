<template>
  <div class="search">
    <input
      type="text"
      name="search"
      id="search"
      placeholder="Search 300+ connectors and tools that work with Meltano…"
      class="search-bar"
      ref="searchBar"
      v-model="search"
      @focus="searchFocused = true"
      @blur="searchFocused = false"
      v-focus="searchFocused"
    />
    <div class="results" v-if="search != '' && (searchFocused || hoveringOnSearchOptions)">
      <div v-if="searchResults.length > 0 && (searchFocused || hoveringOnSearchOptions)">
        <article
          v-for="plugin in searchResults.slice(0, 10)"
          :key="plugin.node.id"
          class="result-item"
          @mouseover="hoveringOnSearchOptions = true"
          @mouseleave="hoveringOnSearchOptions = false"
          @click="
            hoveringOnSearchOptions = false;
            searchFocused = false;
            this.$refs.searchBar.reset();
          "
        >
          <g-link :to="plugin.node.path.split('--')[0]">
            <div class="result-left">
              <g-image
                v-if="plugin.node.logo_url"
                class="result-logo"
                :src="
                  require(`!!assets-loader?width=75!@logos/${plugin.node.logo_url.replace(
                    '/assets/logos/',
                    ''
                  )}`)
                "
              />
              <h1>
                {{ plugin.node.label }}
                J
              </h1>
              <span>{{ plugin.node.description || "No description" }}</span>
            </div>

            <span class="result-right plugin-type">{{ plugin.node.pluginType }}</span>
          </g-link>
        </article>
      </div>
      <div v-else>
        <p>Your search didn't return any results. Please try again.</p>
      </div>
    </div>
    o
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
  allPlugins(filter: { isDefault: { eq: true } }) {
    edges {
      node {
        id
        description
        path
        label
        name
        logo_url
        pluginType
        keywords
      }
    }
  }
}
</static-query>

<style lang="scss">
.search {
  height: 80px;
  background: #fff;
  padding: 20px;
  display: flex;
  justify-content: center;

  .search-bar {
    border: 2px solid #3438bf;
    width: 90%;
    border-radius: 0;
    font-size: 20px;
    background: #f1f1f2;
    padding-left: 20px;
  }

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
