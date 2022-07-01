<template>
    <Layout>
      <div class="info">
        <h1>{{$page.orchestrators.name}}</h1>
        <p>{{$page.orchestrators.description}}</p>
      </div>
    </Layout>
</template>

<script>
export default {
    name: 'Orchestrators'
}
</script>

<page-query>
query Orchestrators ($path: String!) {
  orchestrators: orchestrators (path: $path) {
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