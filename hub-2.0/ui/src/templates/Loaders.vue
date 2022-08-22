<template>
  <Layout>
    <div class="single-plugin-overview">
      <div class="single-plugin-detail">
        <div class="single-plugin-top-bar">
          <h4>
            {{ $page.loaders.label }} -
            <span>{{ $page.loaders.description }}</span>
          </h4>
        </div>
        <div class="single-plugin-main">
          <g-image
            v-if="$page.loaders.logo_url"
            :src="
              require(`!!assets-loader?width=250!@logos/${$page.loaders.logo_url.replace(
                '/assets/logos/',
                ''
              )}`)
            "
          />
          <h1>
            {{ $page.loaders.name }} //
            <span>{{ $page.loaders.variant }}</span>
          </h1>

          <p>{{ $page.loaders.usage }}</p>
          <p>
            The {{ $page.loaders.name }}
            <a href="https://docs.meltano.com/concepts/plugins#loaders">Meltano loader</a>
            sends data into
            <a :href="$page.loaders.domain_url">{{ $page.loaders.label }}</a>
            after it was pulled from a source using an
            <g-link to="/extractors">extractor</g-link>.
          </p>
          <h3>Available Variants</h3>
          <ul>
            <li v-for="(variant, index) in $page.variants.edges" v-bind:key="index">
              <g-link :to="variant.node.path" v-if="variant.node.path !== $page.loaders.path">{{
                variant.node.variant
              }}</g-link>
              <span v-else>{{ variant.node.variant }}</span>
              <span v-if="variant.node.isDefault"> (default)</span>
            </li>
          </ul>
          <h2>Getting Started</h2>
          <h3>Prerequisites</h3>
          <p>
            If you haven't already, follow the initial steps of the
            <a href="https://docs.meltano.com/getting-started.html">Getting Started guide</a>:
          </p>
          <ol>
            <li>
              <a href="https://docs.meltano.com/getting-started.html#install-meltano"
                >Install Meltano</a
              >
            </li>
            <li>
              <a href="https://docs.meltano.com/getting-started.html#create-your-meltano-project"
                >Create your Meltano project</a
              >
            </li>
          </ol>
          <p>{{ $page.loaders.prereq }}</p>
          <h3>Installation and configuration</h3>
          <ol>
            <li>
              Add the {{ $page.loaders.name }} extractor to your project using
              <pre class="inline-code-block"><code>meltano add</code></pre>
              :
            </li>
            <pre><code>meltano add loader {{ $page.loaders.name }}</code></pre>
          </ol>
          <h3>Next steps</h3>
          <p>
            Follow the remaining steps of the
            <a href="https://docs.meltano.com/getting-started.html">Getting Started guide</a>:
          </p>
          <ol>
            <li>
              <a
                href="https://docs.meltano.com/getting-started.html#select-entities-and-attributes-to-extract"
                >Select entities and attributes to extract</a
              >
            </li>
            <li>
              <a
                href="https://docs.meltano.com/getting-started.html#add-a-loader-to-send-data-to-a-destination"
                >Add a loader to send data to a destination</a
              >
            </li>
            <li>
              <a
                href="https://docs.meltano.com/getting-started.html#run-a-data-integration-el-pipeline"
                >Run a data integration (EL) pipeline</a
              >
            </li>
          </ol>
          <p>If you run into any issues, learn how to get help.</p>
          <h2 v-if="$page.loaders.capabilities">Capabilities</h2>
          <div v-if="$page.loaders.capabilities">
            The current capabilities for
            <pre class="inline-code-block"><code>{{ $page.loaders.name }}</code></pre>
            may have been automatically set when originally added to the Hub. Please review the
            capabilities when using this extractor. If you find they are out of date, please
            consider updating them by making a pull request to the YAML file that defines the
            capabilities for this extractor.
          </div>
          <p v-if="$page.loaders.capabilities">This plugin has the following capabilities:</p>
          <ul v-if="$page.loaders.capabilities">
            <li v-for="(capability, index) in $page.loaders.capabilities" v-bind:key="index">
              {{ capability }}
            </li>
          </ul>
          <h2>Settings</h2>
          <p>{{ $page.loaders.name }} requires the configuration of the following settings:</p>
          <ul>
            <li v-for="(setting, index) in $page.loaders.settings" v-bind:key="index">
              {{ setting.name }}
            </li>
          </ul>
          <p>
            The settings for extractor tap-github that are known to Meltano are documented below. To
            quickly find the setting you're looking for, use the Table of Contents at the top of the
            page.
          </p>
          <p class="add-more-info">Account ID</p>
          <p class="add-more-info">Personal Access Token</p>
          <p class="add-more-info">Start Date</p>
          <p class="add-more-info">End Date</p>
          <p class="add-more-info">Anything else</p>
          <h2>Looking for help?</h2>
          <div>
            If you're having trouble getting the {{ $page.loaders.name }} loader to work, look for
            an <a :href="$page.loaders.domain_url">existing issue in its repository</a>, file a
            <a href="https://github.com/singer-io/tap-github/issues/new">new issue</a>, or
            <a href="https://meltano.com/slack">join the Meltano Slack community</a>
            and ask for help in the
            <pre class="inline-code-block"><code>#plugins-general channel</code></pre>
            .
          </div>
          <h3>Found an issue on this page?</h3>
          <p>
            This page is generated from a YAML file that you can contribute changes to.
            <a
              href="https://github.com/meltano/hub/blob/main/_data/meltano/extractors/tap-github/singer-io.yml"
              >Edit it on GitHub!</a
            >
          </p>
        </div>
        <PluginSidebar
          :name="$page.loaders.name"
          :domain_url="$page.loaders.domain_url"
          :repo="$page.loaders.repo"
          :maintenance_status="$page.loaders.maintenance_status"
          :keywords="$page.loaders.keywords"
          :variant="$page.loaders.variant"
        />
      </div>
    </div>
  </Layout>
</template>

<script>
import PluginSidebar from "../components/PluginSidebar.vue";

export default {
  metaInfo() {
    return {
      title: this.$page.loaders.name,
    };
  },
  name: "LoadersTemplate",
  components: { PluginSidebar },
};
</script>

<page-query lang="graphql">
query Loaders($path: String!, $name: String!) {
  loaders: loaders(path: $path) {
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
  variants: allLoaders(filter: { name: { eq: $name } }) {
    edges {
      node {
        name
        variant
        path
        isDefault
      }
    }
  }
}
</page-query>

<style lang="scss">
.add-more-info {
  color: red;
  border: 1px solid red;
}
</style>
