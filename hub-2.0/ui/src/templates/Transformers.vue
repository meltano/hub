<template>
  <Layout>
    <div class="info">
      <div class="single-plugin-detail">
        <div class="single-plugin-top-bar">
          <h4>{{ $page.transformers.name }}</h4>
        </div>
        <div class="single-plugin-main">
          <h1>
            {{ $page.transformers.name }} -
            <p>{{ $page.transformers.variant }}</p>
          </h1>
          <p>{{ $page.transformers.description }}</p>
          <p>{{ $page.transformers.namespace }}</p>
          <p>{{ $page.transformers.pip_url }}</p>
          <p>{{ $page.transformers.prereq }}</p>
          <p>{{ $page.transformers.usage }}</p>
        </div>
        <div class="single-plugin-aside">
          <span>Install</span>
          <pre><code>meltano add {{ $page.transformers.name }}</code></pre>
          <span>Homepage</span>
          <span>Repo</span>
          <div class="link-box">
            <img
              class="aside-icon"
              src="../assets/images/git-alt-brands.svg"
            /><span>{{ $page.transformers.repo }}</span>
          </div>
          <p>{{ $page.transformers.maintenance_status }}</p>
          <p>{{ $page.transformers.keywords }}</p>
        </div>
      </div>
    </div>
  </Layout>
</template>

<script></script>

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
    settings {
      name
      label
      description
    }
  }
}
</page-query>

<style></style>
