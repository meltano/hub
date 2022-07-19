<template>
  <div class="search">
    <input
      type="text"
      name="search"
      id="search"
      placeholder="Search for a plugin..."
      class="search-bar"
      v-model="search"
    />
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
            <span class="plugin-type">{{ plugin.node.pluginType }}</span>
          </g-link>
        </article>
      </div>
      <div v-else>
        <p>Your search didn't return any results. Please try again.</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchBar",
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
  allExtractors(filter: { isDefault: { eq: true } }) {
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
  allLoaders(filter: { isDefault: { eq: true } }) {
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
  allOrchestrators(filter: { isDefault: { eq: true } }) {
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
  allTransformers(filter: { isDefault: { eq: true } }) {
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
  allUtilities(filter: { isDefault: { eq: true } }) {
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
  allFiles(filter: { isDefault: { eq: true } }) {
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
    width: 90%;
    border-radius: 0;
    font-size: 20px;
    background: #f1f1f2;
    padding-left: 20px;
    &:focus-visible {
      outline: 3px solid #3438bf;
      border: 0;
    }
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
      }

      .plugin-type {
        float: right;
      }
    }
  }
}
</style>
