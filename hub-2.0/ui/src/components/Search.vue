<template>
  <div>
    <div class="search">
      <input
        type="text"
        name="search"
        id="search"
        placeholder="Search for a plugin..."
        class="search-bar"
        v-model="search"
      />
      <button class="search-button">Search</button>
      <div class="results" v-if="search != ''">
        <div v-if="searchResults.length > 0">
          <article
            v-for="plugin in searchResults.slice(0, 10)"
            :key="plugin.node.id"
            class="result-item"
          >
            <g-link :to="plugin.node.path">
              <h1>
                {{ plugin.node.label }}
              </h1>

              <span>{{ plugin.node.description || "No description" }}</span>
              <span class="plugin-type">{{
                plugin.node.pluginType
              }}</span></g-link
            >
          </article>
        </div>
        <div v-else>
          <p>Your search didn't return any results. Please try again.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Search",
  data() {
    return {
      search: "",
    };
  },
  computed: {
    searchResults() {
      const pluginCollections = [
        this.$static.allExtractors,
        this.$static.allLoaders,
        this.$static.allFiles,
        this.$static.allOrchestrators,
        this.$static.allUtilities,
        this.$static.allTransformers,
      ];
      console.log(pluginCollections);
      return pluginCollections.flatMap((coll) => {
        return coll.edges.filter((plugin) => {
          const pluginText =
            plugin.node.name + plugin.node.description + plugin.node.label;
          return pluginText
            .toLowerCase()
            .includes(this.search.toLowerCase().trim());
        });
      });
    },
  },
};
</script>

<static-query>
query {
	allExtractors (filter: {isDefault: {eq: true}}){
		edges {
      node {
        id
				description
        path
				label
				name
				logo_url
        pluginType
      }
    }
  }
  allLoaders (filter: {isDefault: {eq: true}}){
		edges {
      node {
        id
				description
        path
				label
				name
				logo_url
        pluginType
      }
    }
  }
  allOrchestrators (filter: {isDefault: {eq: true}}){
		edges {
      node {
        id
        path
				label
				name
				logo_url
        pluginType
      }
    }
  }
  allTransformers (filter: {isDefault: {eq: true}}){
		edges {
      node {
        id
        path
				label
				name
				logo_url
        pluginType
      }
    }
  }
  allUtilities (filter: {isDefault: {eq: true}}){
		edges {
      node {
        id
				description
        path
				label
				name
				logo_url
        pluginType
      }
    }
  }
  allFiles (filter: {isDefault: {eq: true}}){
		edges {
      node {
        id
        path
				label
				name
				logo_url
        pluginType
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
    border: 2px solid red;
    width: calc(100% - 300px);
    border-radius: none;
    font-size: 20px;
    background: #f1f1f2;
    padding-left: 20px;
  }

  .search-button {
    background: #d9042b;
    border: none;
    color: #fff;
    padding: 20px;
    font-size: 16px;
  }

  .results {
    // display: none;
    box-shadow: 1px 2px 4px rgba(0, 0, 0, 0.3);
    position: absolute;
    width: 75%;
    align-content: left;
    margin-top: 80px;
    background: white;
    .result-item {
      color: black;
      padding: 0.5rem;
      border-bottom: 2px solid black;
      .plugin-type {
        float: right;
      }
    }
  }
}
</style>