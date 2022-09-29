<template>
  <Layout>
    <div class="plugins-overview">
      <h3>{{ $page.maintainers.label }}</h3>
      <p>{{ $page.maintainers.name }}</p>
      <p>{{ $page.maintainers.url }}</p>
    </div>
  </Layout>
</template>

<script>
export default {
  metaInfo() {
    return {
      title: this.$page.maintainers.name,
    };
  },
  name: "MaintainersTemplate",
};
</script>
<page-query>
query Maintainers($path: String!) {
  maintainers: maintainers(path: $path) {
    name
    label
    url
  }
}
</page-query>
<style></style>
