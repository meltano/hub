<template>
  <div>
    <div v-for="edge in $page.utilities.edges" :key="edge.node.name">
      <h2>{{ edge.node.name }}</h2>
    </div>
  </div>
</template>

<script>
export default {
    name: 'Utilities'
}
</script>

<page-query>
query {
	allFireUtilities {
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