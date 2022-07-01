<template>
    <Layout>
      <div class="info">
        <h1>{{$page.utilities.name}}</h1>
        <p>{{$page.utilities.description}}</p>
      </div>
    </Layout>
</template>

<script>
// export default {
//     name: 'Utilities'
// }
</script>

<page-query>
query Utilities ($path: String!) {
  utilities: utilities (path: $path) {
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
  }
}
</page-query>

<style>

</style>