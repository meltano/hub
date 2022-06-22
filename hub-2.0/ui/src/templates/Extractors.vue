<template>
  <div>
    <div v-for="edge in $page.extractors.edges" :key="edge.node.name">
      <h2>{{ edge.node.name }}</h2>
    </div>
  </div>
</template>

<script>
export default {
    name: 'Extractors'
}
</script>

<page-query>
query {
	allFireExtractors {
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