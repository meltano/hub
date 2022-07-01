<template>
  <div class="search">
    <input type="text" placeholder="Search for a plugin..." class="search-bar" />
    <button class="search-button">Search</button>
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
  // to search all items, lump all results together and then filter those
  // computed: {
  //   searchResults() {
  //     return this.$static.allPlugin.edges.filter(plugin => {
  //       return plugin.node.name.toLowerCase().includes(this.search.toLowerCase().trim())
  //     })
  //   }
  // }
}
</script>

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