<template>
    <Layout>
      <div class="info">
        <h1>{{$page.loaders.name}}</h1>
        <p>{{$page.loaders.description}}</p>
      </div>
    </Layout>
</template>

<script>
export default {
    name: 'Loaders'
}
</script>

<page-query>
query Loaders ($path: String!) {
  loaders: loaders (path: $path) {
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
</page-query>

<style>

</style>