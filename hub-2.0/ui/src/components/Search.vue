<template>

<div>
  <div class="search">
      <input type="text" name="search" id="search" placeholder="Search for a plugin..." class="search-bar" v-model="search" />
      <button class="search-button">Search</button>
  </div>
<div class="results">
  <!-- <p>results!</p> -->
      <!-- <div v-if="searchResults.length > 0">
        <article v-for="extractor in searchResults" :key="extractor.node.id">
          <h1><g-link :to="extractor.node.path">{{ extractor.node.name }}</g-link></h1>
        </article>
    </div>
    <div v-else>
      <p>Your search didn't return any results. Please try again.</p>
    </div> -->
</div>
</div>
</template>

data() {

}

<script>
export default {
  name: 'Search',
  data() {
    return {
      search: ''
    }
  },
  computed: {
    searchResults() {
      // return this.$static.allExtractors.edges.filter(extractor => {
      //   return extractor.node.name.toLowerCase().includes(this.search.toLowerCase().trim())
      // })
    }
  }
}
</script>

<page-query>
query {
	allExtractors{
		edges {
      node {
        id
				description
        path
				label
				name
				logo_url
				namespace
				variant
				pip_url
				repo
				maintenance_status
				keywords
      }
    }
  }
}
</page-query>

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
}
</style>