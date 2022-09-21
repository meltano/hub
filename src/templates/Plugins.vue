<template>
  <Layout>
    <div class="single-plugin-overview">
      <div class="single-plugin-detail">
        <div class="single-plugin-top-bar">
          <table>
            <tr>
              <td style="padding: 25px">
                <g-image
                  v-if="$page.plugins.logo_url"
                  :src="
                    require(`!!assets-loader?width=250&height=200&fit=inside!@logos/${$page.plugins.logo_url.replace(
                      '/assets/logos/',
                      ''
                    )}`)
                  "
                />
              </td>
              <td>
                <p class="text-3xl py-8">
                  {{ $page.plugins.label }}
                </p>
                <p class="text-2xl">
                  <code>{{ $page.plugins.name }} from {{ $page.plugins.variant }}</code>
                </p>
                <p>
                  <b>{{ $page.plugins.description }}</b>
                </p>
              </td>
            </tr>
          </table>
        </div>
        <div class="single-plugin-main p-5 space-y-4">
          <p>
            The {{ $page.plugins.name }}
            <a :href="'https://docs.meltano.com/concepts/plugins#' + $page.plugins.pluginTypePlural"
              >Meltano {{ $page.plugins.pluginType }}</a
            >
            pulls data from
            <a :href="$page.plugins.domain_url">{{ $page.plugins.label }}</a> that can then be sent
            to a destination using a <g-link to="/loaders">loader</g-link>.
          </p>
          <p class="text-2xl">Other Available Variants</p>
          <ul class="list-disc list-inside pl-4">
            <li v-for="(variant, index) in $page.variants.edges" v-bind:key="index">
              <g-link :to="variant.node.path" v-if="variant.node.path !== $page.plugins.path">{{
                variant.node.variant
              }}</g-link>
              <span v-else>{{ variant.node.variant }}</span>
              <span v-if="variant.node.isDefault"> (default)</span>
              <span v-if="variant.node.keywords.includes('meltano_sdk')">
                <img
                  class="inline pl-2"
                  alt="Built with the Meltano SDK"
                  src="https://img.shields.io/badge/-Meltano%20SDK-blueviolet"
                />
              </span>
            </li>
          </ul>
          <div>
            <p class="text-3xl py-4" id="getting-started">Getting Started</p>
            <PluginPrereqSection :plugin="$page.plugins" :plugin_type="$page.plugins.pluginType" />
            <p class="text-xl py-3" id="installation">Installation and configuration</p>
            <ol class="list-decimal list-inside pl-4">
              <li>
                Add the {{ $page.plugins.name }} {{ $page.plugins.pluginType }} to your project
                using
                <pre class="inline-code-block"><code>meltano add</code></pre>
                :
              </li>
              <pre><code>meltano add {{ $page.plugins.pluginType }} {{ $page.plugins.name }}<span v-if="!$page.plugins.isDefault"> --variant {{ $page.plugins.variant }}</span></code></pre>
            </ol>
            <p class="text-xl py-3">Next steps</p>
            <div
              v-if="$page.plugins.next_steps_rendered"
              v-html="$page.plugins.next_steps_rendered"
              class="prose"
            ></div>
            <!-- extractors default next steps -->
            <div v-else-if="$page.plugins.pluginType == 'extractor'">
              <p>
                Follow the remaining steps of the
                <a href="https://docs.meltano.com/getting-started.html">Getting Started guide</a>:
              </p>
              <ol class="list-decimal list-inside pl-4">
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
            </div>

            <!-- loaders default next steps -->
            <div v-else-if="$page.plugins.pluginType == 'loader'">
              <p>
                Follow the remaining steps of the
                <a href="https://docs.meltano.com/getting-started.html">Getting Started guide</a>:
              </p>
              <ol class="list-decimal list-inside pl-4">
                <li>
                  <a
                    href="https://docs.meltano.com/getting-started.html#run-a-data-integration-el-pipeline"
                    >Run a data integration (EL) pipeline</a
                  >
                </li>
              </ol>
            </div>

            <!-- Default transformers next steps -->
            <div v-else-if="$page.plugins.pluginType == 'transformer'">
              <p>
                Follow the remaining steps of the
                <a href="https://docs.meltano.com/getting-started.html">Getting Started guide</a>:
              </p>
              <ol class="list-decimal list-inside pl-4">
                <li>
                  <a
                    href="https://docs.meltano.com/getting-started.html#transform-loaded-data-for-analysis"
                  >
                    Transform loaded data for analysis
                  </a>
                </li>
              </ol>
            </div>
            <!-- No next steps defined for this plugin. -->
            <div v-else></div>

            <!-- Help section -->
            <p>If you run into any issues, learn how to get help.</p>
            <div
              class="prose mt-3 p-2"
              v-if="$page.plugins.usage"
              v-html="$page.plugins.usage_rendered"
            ></div>
          </div>
          <div>
            <PluginCapabilitiesSection
              :capabilities="$page.plugins.capabilities"
              :name="$page.plugins.name"
              :plugin_type="$page.plugins.pluginType"
            />
            <PluginSettingsSection :settings="$page.plugins.settings" :name="$page.plugins.name" />
            <PluginHelpSection
              :name="$page.plugins.name"
              :variant="$page.plugins.variant"
              :repo="$page.plugins.repo"
              :plugin_type="$page.plugins.pluginType"
            />
            <PluginSidebar
              :name="$page.plugins.name"
              :domain_url="$page.plugins.domain_url"
              :repo="$page.plugins.repo"
              :maintenance_status="$page.plugins.maintenance_status"
              :keywords="$page.plugins.keywords"
              :variant="$page.plugins.variant"
              :is_default="$page.plugins.isDefault"
              :metrics="$page.plugins.metrics"
              :plugin_type="$page.plugins.pluginType"
            />
          </div>
        </div>
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
      title: this.$page.plugins.name,
    };
  },
  name: "PluginsTemplate",
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
query Plugins($path: String!, $name: String!) {
  plugins: plugins(path: $path) {
    id
    description
    label
    name
    path
    logo_url
    namespace
    next_steps
    next_steps_rendered
    variant
    isDefault
    pluginType
    pluginTypePlural
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
      description_rendered
      kind
      placeholder
    }
    prereq
    prereq_rendered
    usage
    usage_rendered
    metrics {
      ALL_PROJECTS
      ALL_EXECS
    }
  }
  variants: allPlugins(filter: { name: { eq: $name } }) {
    edges {
      node {
        name
        path
        variant
        isDefault
        keywords
      }
    }
  }
}
</page-query>

<style lang="scss"></style>
