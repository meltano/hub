<template>
  <Layout>
    <div class="info">
      <div class="single-plugin-detail">
        <div class="single-plugin-top-bar">
          <h4>{{ $page.utilities.name }}</h4>
        </div>
        <div class="single-plugin-main">
          <h1>
            {{ $page.utilities.name }} -
            <p>{{ $page.utilities.variant }}</p>
          </h1>
          <p>{{ $page.utilities.description }}</p>
          <p>{{ $page.utilities.namespace }}</p>
          <p>{{ $page.utilities.pip_url }}</p>
          <p>{{ $page.utilities.prereq }}</p>
          <p>{{ $page.utilities.usage }}</p>
        </div>
        <div class="single-plugin-aside">
          <span>Install</span>
          <pre><code>meltano add {{ $page.utilities.name }}</code></pre>
          <span>Homepage</span>
          <div class="link-box">
            <img
              class="aside-icon"
              src="../assets/images/link-solid.svg"
            /><span>{{ $page.utilities.domain_url }}</span>
          </div>
          <span>Repo</span>
          <div class="link-box">
            <img
              class="aside-icon"
              src="../assets/images/git-alt-brands.svg"
            /><span>{{ $page.utilities.repo }}</span>
          </div>
          <p>{{ $page.utilities.maintenance_status }}</p>
          <p>{{ $page.utilities.keywords }}</p>
        </div>
      </div>
    </div>
  </Layout>
</template>

<script>
export default {
  name: "UtilitiesTemplate",
};
</script>

<page-query lang="graphql">
query Utilities($path: String!) {
  utilities: utilities(path: $path) {
    id
    description
    path
    label
    logo_url
    namespace
    variant
    pip_url
    repo
    maintenance_status
    keywords
    settings {
      name
      label
      description
    }
    prereq
    usage
  }
}
</page-query>

<style></style>
