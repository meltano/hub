<template>
  <Layout>
    <div class="single-plugin-overview">
      <div class="single-plugin-detail">
        <div class="single-plugin-top-bar">
          <h4>{{ $page.extractors.name }}</h4>
        </div>
        <div class="single-plugin-main">
          <h1>
            {{ $page.extractors.name }} //
            <span>{{ $page.extractors.variant }}</span>
          </h1>
          <p>{{ $page.extractors.description }}</p>
          <p>{{ $page.extractors.prereq }}</p>
          <p>{{ $page.extractors.usage }}</p>
          <h2>Getting Started</h2>
          <h3>Prerequisites</h3>
          <p>If you haven't already, follow the initial steps of the <a href="https://docs.meltano.com/getting-started.html">Getting Started guide</a>:</p>
          <ol>
            <li><a href="https://docs.meltano.com/getting-started.html#install-meltano">Install Meltano</a></li>
            <li><a href="https://docs.meltano.com/getting-started.html#create-your-meltano-project">Create your Meltano project</a></li>
          </ol>
          <h3>Installation and configuration</h3>
          <ol>
            <li>Add the {{ $page.extractors.name }} extractor to your project using <pre class="inline-code-block"><code>meltano add</code></pre>:</li>
            <pre><code>meltano add extractor {{ $page.extractors.name }}</code></pre>
          </ol>
          <h3>Next steps</h3>
          <p>Follow the remaining steps of the <a href="https://docs.meltano.com/getting-started.html">Getting Started guide</a>:</p>
          <ol>
            <li><a href="https://docs.meltano.com/getting-started.html#select-entities-and-attributes-to-extract">Select entities and attributes to extract</a></li>
            <li><a href="https://docs.meltano.com/getting-started.html#add-a-loader-to-send-data-to-a-destination">Add a loader to send data to a destination</a></li>
            <li><a href="https://docs.meltano.com/getting-started.html#run-a-data-integration-el-pipeline">Run a data integration (EL) pipeline</a></li>
          </ol>
          <p>If you run into any issues, learn how to get help.</p>
          <h2>Capabilities</h2>
          <p>The current capabilities for <pre class="inline-code-block"><code>{{ $page.extractors.name }}</code></pre> may have been automatically set when originally added to the Hub. Please review the capabilities when using this extractor. If you find they are out of date, please consider updating them by making a pull request to the YAML file that defines the capabilities for this extractor.</p>
          <ul>
            <li v-for="(capability, index) in $page.extractors.capibilities" v-bind:key="index">{{capability}}</li>
          </ul>
          <h2>Settings</h2>
          <h2>Looking for help?</h2>
        </div>
        <div class="single-plugin-aside">
          <h4>Install</h4>
          <pre><code>meltano add {{ $page.extractors.name }}</code></pre>
          <h4>Homepage</h4>
          <div class="link-box">
            <img
              class="aside-icon"
              src="../assets/images/link-solid.svg"
            /><a :href="$page.extractors.domain_url">{{ $page.extractors.domain_url }}</a>
          </div>
          <h4>Repo</h4>
          <div class="link-box">
            <img
              class="aside-icon"
              src="../assets/images/git-alt-brands.svg"
            /><a :href="$page.extractors.repo">{{ $page.extractors.repo }}</a>
          </div>
          <h4>Maintenance Status</h4>
          <p>{{ $page.extractors.maintenance_status }}</p>
          <h4>Keywords</h4>
          <p>{{ $page.extractors.keywords[0] }}</p>
        </div>
      </div>
    </div>
  </Layout>
</template>

<script>
export default {
  name: "ExtractorsTemplate",
};
</script>

<page-query lang="graphql">
query Extractors($path: String!) {
  extractors: extractors(path: $path) {
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
    capabilities
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
