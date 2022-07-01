<template>
    <Layout>
      <div class="info">
        <h1>{{$page.extractors.name}}</h1>
        <p>{{$page.extractors.description}}</p>
      </div>
    </Layout>
</template>

<script>
// export default {
//     name: 'Extractors'
// }
</script>

<page-query>
query Extractors ($path: String!) {
  extractors: extractors (path: $path) {
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