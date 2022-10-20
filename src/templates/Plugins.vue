<template>
  <Layout>
    <div class="single-plugin-overview md:mx-36 sm:mx-0">
      <div class="single-plugin-detail">
        <div class="single-plugin-top-bar">
          <table>
            <tr>
              <td style="padding: 25px">
                <a
                  v-if="$page.plugins.domain_url"
                  :href="$page.plugins.domain_url"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <g-image
                    v-if="$page.plugins.logo_url"
                    :src="
                      require(`!!assets-loader?width=250&height=200&fit=inside!@logos/${$page.plugins.logo_url.replace(
                        '/assets/logos/',
                        ''
                      )}`)
                    "
                  />
                </a>
                <div v-else>
                  <g-image
                    v-if="$page.plugins.logo_url"
                    :src="
                      require(`!!assets-loader?width=250&height=200&fit=inside!@logos/${$page.plugins.logo_url.replace(
                        '/assets/logos/',
                        ''
                      )}`)
                    "
                  />
                </div>
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
        <div class="flex flex-col lg:flex-row w-screen sm:w-auto">
          <div>
            <PluginReadme
              :plugin="$page.plugins"
            />
          </div>
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
            :maintainer="$page.plugins.maintainer"
            :pip_url="$page.plugins.pip_url"
          />
        </div>
      </div>
    </div>
  </Layout>
</template>

<script>
import PluginSidebar from "../components/PluginSidebar.vue";
import PluginReadme from "../components/PluginReadme.vue";
// import PluginSettingsSection from "../components/PluginSettingsSection.vue";
// import PluginHelpSection from "../components/PluginHelpSection.vue";
// import PluginCapabilitiesSection from "../components/PluginCapabilitiesSection.vue";

export default {
  metaInfo() {
    return {
      title: this.$page.plugins.name,
    };
  },
  name: "PluginsTemplate",
  components: {
    PluginSidebar,
    PluginReadme,
  },
};
</script>

<page-query lang="graphql">
query Plugins($path: String!, $name: String!) {
  plugins: plugins(path: $path) {
    id
    description
    definition
    definition_rendered
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
      value
    }
    commands {
      name
      description
      args
    }
    prereq
    prereq_rendered
    settings_preamble
    settings_preamble_rendered
    usage
    usage_rendered
    metrics {
      ALL_PROJECTS
      ALL_EXECS
    }
    maintainer {
      name
      label
      url
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
