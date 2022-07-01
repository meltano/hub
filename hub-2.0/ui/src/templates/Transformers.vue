<template>
    <Layout>
      <div class="info">
        <h1>{{$page.transformers.name}}</h1>
        <p>{{$page.transformers.description}}</p>
      </div>
    </Layout>
</template>

<script>
export default {
    name: 'Transformers'
}
</script>

<page-query>
query Transformers ($path: String!) {
  transformers: transformers (path: $path) {
    id
    path
		label
		name
		logo_url
		namespace
		variant
		pip_url
		repo
		maintenance_status
  }
}
</page-query>

<style>

</style>