<template>
  <div>
    <div v-for="edge in $page.loaders.edges" :key="edge.node.name">
      <h2>{{ edge.node.name }}</h2>
    </div>
  </div>
</template>

<script>
export default {
    name: 'Loaders'
}
</script>

<page-query>
query {
	allFireLoaders {
  	    edges {
    	    node {
      	        name
    	    }
  	    }
	}
}
</page-query>

<style>

</style>