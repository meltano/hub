<template>
  <Layout>
    <div class="single-plugin-overview">
      <div class="single-plugin-detail">
        <div class="single-plugin-top-bar">
          <table>
            <tr>
              <td style="padding: 25px">
                <g-image
                  v-if="$page.loaders.logo_url"
                  :src="
                    require(`!!assets-loader?width=250&height=200&fit=inside!@logos/${$page.loaders.logo_url.replace(
                      '/assets/logos/',
                      ''
                    )}`)
                  "
                />
              </td>
              <td>
                <h1>
                  {{ $page.loaders.label }}
                </h1>
                <h2>
                  <code>{{ $page.loaders.name }} from {{ $page.loaders.variant }}</code>
                </h2>
                <p>
                  <b>{{ $page.loaders.description }}</b>
                </p>
              </td>
            </tr>
          </table>
        </div>
        <div class="single-plugin-main">
          <p>
            The {{ $page.loaders.name }}
            <a href="https://docs.meltano.com/concepts/plugins#loaders">Meltano loader</a>
            sends data into
            <a :href="$page.loaders.domain_url">{{ $page.loaders.label }}</a>
            after it was pulled from a source using an
            <g-link to="/extractors">extractor</g-link>.
          </p>
          <h3>Other Available Variants</h3>
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
          <PluginPrereqSection :plugin="$page.loaders" plugin_type="loader" />
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
          <PluginCapabilitiesSection
            :capabilities="$page.loaders.capabilities"
            :name="$page.loaders.name"
            plugin_type="loader"
          />
          <PluginSettingsSection :settings="$page.loaders.settings" :name="$page.loaders.name" />
          <PluginHelpSection
            :name="$page.loaders.name"
            :variant="$page.loaders.variant"
            :repo="$page.loaders.repo"
            plugin_type="loaders"
          />
        </div>
        <PluginSidebar
          :name="$page.loaders.name"
          :domain_url="$page.loaders.domain_url"
          :repo="$page.loaders.repo"
          :maintenance_status="$page.loaders.maintenance_status"
          :keywords="$page.loaders.keywords"
          :variant="$page.loaders.variant"
          plugin_type="loader"
        />
      </div>
    </div>
  </Layout>
</template>

<script>
import PluginSidebar from "../components/PluginSidebar.vue";
import PluginSettingsSection from "../components/PluginSettingsSection.vue";
import PluginHelpSection from "../components/PluginHelpSection.vue";
import PluginCapabilitiesSection from "../components/PluginCapabilitiesSection.vue";
import PluginPrereqSection from "../components/PluginPrereqSection.vue";

export default {
  metaInfo() {
    return {
      title: this.$page.loaders.name,
    };
  },
  name: "LoadersTemplate",
  components: {
    PluginSidebar,
    PluginSettingsSection,
    PluginHelpSection,
    PluginCapabilitiesSection,
    PluginPrereqSection,
  },
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
    capabilities
    settings {
      name
      label
      description
      descriptionRendered
    }
    prereq
    prereqRendered
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

<style lang="scss"></style>
