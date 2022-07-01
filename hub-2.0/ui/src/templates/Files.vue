<template>
    <Layout>
      <div class="info">
        <h1>{{$page.files.name}}</h1>
        <p>{{$page.files.description}}</p>
      </div>
    </Layout>
</template>

<script>
// export default {
//     name: 'Files'
// }
</script>

<page-query>
query Files ($path: String!) {
  files: files (path: $path) {
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