<template>
  <Layout>
    <div class="single-plugin-overview">
      <div class="single-plugin-detail">
        <div class="single-plugin-top-bar">
          <table>
            <tr>
              <td style="padding: 25px">
                <g-image
                  v-if="$page.extractors.logo_url"
                  :src="
                    require(`!!assets-loader?width=250&height=200&fit=inside!@logos/${$page.extractors.logo_url.replace(
                      '/assets/logos/',
                      ''
                    )}`)
                  "
                />
              </td>
              <td>
                <h1>
                  {{ $page.extractors.label }}
                </h1>
                <h2>
                  <code>{{ $page.extractors.name }} from {{ $page.extractors.variant }}</code>
                </h2>
                <p>
                  <b>{{ $page.extractors.description }}</b>
                </p>
              </td>
            </tr>
          </table>
        </div>
        <div class="single-plugin-main">
          <p>
            The {{ $page.extractors.name }}
            <a href="https://docs.meltano.com/concepts/plugins#extractors">Meltano extractor</a>
            pulls data from
            <a :href="$page.extractors.domain_url">{{ $page.extractors.label }}</a> that can then be
            sent to a destination using a <g-link to="/loaders">loader</g-link>.
          </p>
          <h3>Other Available Variants</h3>
          <ul>
            <li v-for="(variant, index) in $page.variants.edges" v-bind:key="index">
              <g-link :to="variant.node.path" v-if="variant.node.path !== $page.extractors.path">{{
                variant.node.variant
              }}</g-link>
              <span v-else>{{ variant.node.variant }}</span>
              <span v-if="variant.node.isDefault"> (default)</span>
            </li>
          </ul>
          <h2 id="getting-started">Getting Started</h2>
          <h3 id="prereqs">Prerequisites</h3>
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
          <p>{{ $page.extractors.prereq }}</p>
          <h3 id="installation">Installation and configuration</h3>
          <ol>
            <li>
              Add the {{ $page.extractors.name }} extractor to your project using
              <pre class="inline-code-block"><code>meltano add</code></pre>
              :
            </li>
            <pre><code>meltano add extractor {{ $page.extractors.name }}</code></pre>
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
          <h2 id="capabilities">Capabilities</h2>
          <div>
            The current capabilities for
            <pre class="inline-code-block"><code>{{ $page.extractors.name }}</code></pre>
            may have been automatically set when originally added to the Hub. Please review the
            capabilities when using this extractor. If you find they are out of date, please
            consider updating them by making a pull request to the YAML file that defines the
            capabilities for this extractor.
          </div>
          <p>This plugin has the following capabilities:</p>
          <ul>
            <li v-for="(capability, index) in $page.extractors.capabilities" v-bind:key="index">
              {{ capability }}
            </li>
          </ul>
          <PluginSettingsSection
            :settings="$page.extractors.settings"
            :name="$page.extractors.name"
          />
          <h2 id="contribute">Something missing?</h2>
          <p>
            This page is generated from a YAML file that you can contribute changes to.
            <a
              :href="
                'https://github.com/meltano/hub/blob/main/_data/meltano/extractors/' +
                $page.extractors.name +
                '/' +
                $page.extractors.variant +
                '.yml'
              "
              >Edit it on GitHub!</a
            >
          </p>
          <h2 id="looking-for-help">Looking for help?</h2>
          <div>
            If you're having trouble getting the
            {{ $page.extractors.name }} extractor to work, look for an
            <a :href="$page.extractors.repo + '/issues'">existing issue in its repository</a>, file
            a <a :href="$page.extractors.repo + '/issues/new'">new issue</a>, or
            <a href="https://meltano.com/slack">join the Meltano Slack community</a>
            and ask for help in the
            <pre class="inline-code-block"><code>#plugins-general</code></pre>
            channel.
          </div>
        </div>
        <PluginSidebar
          :name="$page.extractors.name"
          :domain_url="$page.extractors.domain_url"
          :repo="$page.extractors.repo"
          :maintenance_status="$page.extractors.maintenance_status"
          :keywords="$page.extractors.keywords"
          :variant="$page.extractors.variant"
          plugin_type="extractor"
        />
      </div>
    </div>
  </Layout>
</template>

<script>
import PluginSidebar from "../components/PluginSidebar.vue";
import PluginSettingsSection from "../components/PluginSettingsSection.vue";

export default {
  metaInfo() {
    return {
      title: this.$page.extractors.name,
    };
  },
  name: "ExtractorsTemplate",
  components: { PluginSidebar, PluginSettingsSection },
};
</script>

<page-query lang="graphql">
query Extractors($path: String!, $name: String!) {
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
      kind
      placeholder
    }
    prereq
    usage
  }
  variants: allExtractors(filter: { name: { eq: $name } }) {
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

<style lang="scss"></style>
