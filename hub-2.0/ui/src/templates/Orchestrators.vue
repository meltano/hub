<template>
  <Layout>
    <div class="info">
      <div class="single-plugin-detail">
        <div class="single-plugin-top-bar">
          <h4>{{ $page.orchestrators.name }}</h4>
        </div>
        <div class="single-plugin-main">
          <h1>
            {{ $page.orchestrators.name }} -
            <p>{{ $page.orchestrators.variant }}</p>
          </h1>
          <p>{{ $page.orchestrators.description }}</p>
          <p>{{ $page.orchestrators.namespace }}</p>
          <p>{{ $page.orchestrators.pip_url }}</p>
          <p>{{ $page.orchestrators.prereq }}</p>
          <p>{{ $page.orchestrators.usage }}</p>
        </div>
        <div class="single-plugin-aside">
          <span>Install</span>
          <pre><code>meltano add {{ $page.orchestrators.name }}</code></pre>
          <span>Homepage</span>
          <span>Repo</span>
          <div class="link-box">
            <img
              class="aside-icon"
              src="../assets/images/git-alt-brands.svg"
            /><span>{{ $page.orchestrators.repo }}</span>
          </div>
          <p>{{ $page.orchestrators.maintenance_status }}</p>
          <p>{{ $page.orchestrators.keywords }}</p>
        </div>
      </div>
    </div>
  </Layout>
</template>

<script></script>

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
    settings {
      name
      label
    }
  }
}
</page-query>

<style></style>
