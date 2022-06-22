<template>
  <div class="search">
    <input type="text" placeholder="Search for an extractor, loader, or utility" class="search-bar"/>
    <button class="search-button">Search</button>
  </div>
</template>

<script>
export default {
    name: 'Search'
}
</script>

<style>
.search {
  height: 80px;
  /* width: 100%; */
  background: #fff;
  padding: 20px;
  display: flex;
  justify-content: center;
}
.search-bar {
    border: 2px solid red;
    width: calc(100% - 300px);
    border-radius: none;
    font-size: 20px;
    background: #f1f1f2;
    padding-left: 20px;
}
/* .search-bar:active, .search-bar:focus {
  border-radius: 0;
} */
.search-button {
  background: #d9042b;
  border: none;
  color: #fff;
  padding: 20px;
  font-size: 16px;
}
</style>