<template>
  <Layout>
    <div class="info">
      <div class="single-plugin-detail">
        <div class="single-plugin-top-bar">
          <h4>{{ $page.files.name }}</h4>
        </div>
        <div class="single-plugin-main">
          <h1>
            {{ $page.files.name }} -
            <p>{{ $page.files.variant }}</p>
          </h1>
          <p>{{ $page.files.description }}</p>
          <p>{{ $page.files.namespace }}</p>
          <p>{{ $page.files.pip_url }}</p>
          <p>{{ $page.files.prereq }}</p>
          <p>{{ $page.files.usage }}</p>
        </div>
        <div class="single-plugin-aside">
          <span>Install</span>
          <pre><code>meltano add {{ $page.files.name }}</code></pre>
          <span>Homepage</span>
          <span>Repo</span>
          <div class="link-box">
            <img
              class="aside-icon"
              src="../assets/images/git-alt-brands.svg"
            /><span>{{ $page.files.repo }}</span>
          </div>
          <p>{{ $page.files.maintenance_status }}</p>
          <p>{{ $page.files.keywords }}</p>
        </div>
      </div>
    </div>
  </Layout>
</template>

<script></script>

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

<style></style>
