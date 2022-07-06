<template>
    <Layout>
        <div class="info">
            <div class="single-plugin-detail">
                <div class="single-plugin-top-bar">
                    <h4>{{ $page.extractors.name }}</h4>
                </div>
                <div class="single-plugin-main">
                    <h1>{{ $page.extractors.name }} - <p>{{ $page.extractors.variant }}</p>
                    </h1>
                    <p>{{ $page.extractors.description }}</p>
                    <p>{{ $page.extractors.namespace }}</p>
                    <p>{{ $page.extractors.pip_url }}</p>
                    <p>{{ $page.extractors.prereq }}</p>
                    <p>{{ $page.extractors.usage }}</p>
                </div>
                <div class="single-plugin-aside">
                    <span>Install</span>
                    <pre><code>meltano add {{ $page.extractors.name }}</code></pre>
                    <span>Homepage</span>
                    <div class="link-box">
                        <img class="aside-icon" src="../assets/images/link-solid.svg" /><span>{{
                                $page.extractors.domain_url
                        }}</span>
                    </div>
                    <span>Repo</span>
                    <div class="link-box">
                        <img class="aside-icon" src="../assets/images/git-alt-brands.svg" /><span>{{ $page.extractors.repo
                        }}</span>
                    </div>
                    <p>{{ $page.extractors.maintenance_status }}</p>
                    <p>{{ $page.extractors.keywords }}</p>
                </div>
            </div>
        </div>
    </Layout>
</template>

<script>
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

<style>
</style>