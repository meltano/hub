<template>
  <Layout>
    <div class="info">
      <div class="single-plugin-detail">
        <div class="single-plugin-top-bar">
          <h4>{{ $page.loaders.name }}</h4>
        </div>
        <div class="single-plugin-main">
          <h1>
            {{ $page.loaders.name }} -
            <p>{{ $page.loaders.variant }}</p>
          </h1>
          <p>{{ $page.loaders.description }}</p>
          <p>{{ $page.loaders.namespace }}</p>
          <p>{{ $page.loaders.pip_url }}</p>
          <p>{{ $page.loaders.prereq }}</p>
          <p>{{ $page.loaders.usage }}</p>
        </div>
        <div class="single-plugin-aside">
          <span>Install</span>
          <pre><code>meltano add {{ $page.loaders.name }}</code></pre>
          <span>Homepage</span>
          <div class="link-box">
            <img
              class="aside-icon"
              src="../assets/images/link-solid.svg"
            /><span>{{ $page.loaders.domain_url }}</span>
          </div>
          <span>Repo</span>
          <div class="link-box">
            <img
              class="aside-icon"
              src="../assets/images/git-alt-brands.svg"
            /><span>{{ $page.loaders.repo }}</span>
          </div>
          <p>{{ $page.loaders.maintenance_status }}</p>
          <p>{{ $page.loaders.keywords }}</p>
        </div>
      </div>
    </div>
  </Layout>
</template>

<script>
export default {
  name: "LoadersTemplate",
};
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
    domain_url
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

<style lang="scss"></style>
