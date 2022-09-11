<template>
  <Layout>
    <div class="single-plugin-overview">
      <div class="single-plugin-detail">
        <div class="single-plugin-top-bar">
          <table>
            <tr>
              <td style="padding: 25px">
                <g-image
                  v-if="$page.utilities.logo_url"
                  :src="
                    require(`!!assets-loader?width=250&height=200&fit=inside!@logos/${$page.utilities.logo_url.replace(
                      '/assets/logos/',
                      ''
                    )}`)
                  "
                />
              </td>
              <td>
                <h1>
                  {{ $page.utilities.label }}
                </h1>
                <h2>
                  <code>{{ $page.utilities.name }} from {{ $page.utilities.variant }}</code>
                </h2>
                <p>
                  <b>{{ $page.utilities.description }}</b>
                </p>
              </td>
            </tr>
          </table>
        </div>
        <div class="single-plugin-main">
          <p>
            The {{ $page.utilities.name }}
            <a href="https://docs.meltano.com/concepts/plugins#utilities">utility</a>
            is {{ $page.utilities.definition }}
          </p>
          <h3>Other Available Variants</h3>
          <ul>
            <li v-for="(variant, index) in $page.variants.edges" v-bind:key="index">
              <g-link :to="variant.node.path" v-if="variant.node.path !== $page.utilities.path">{{
                variant.node.variant
              }}</g-link>
              <span v-else>{{ variant.node.variant }}</span>
              <span v-if="variant.node.isDefault"> (default)</span>
            </li>
          </ul>
          <h2>Getting Started</h2>
          <PluginPrereqSection :plugin="$page.utilities" plugin_type="utility" />
          <h3>Installation and configuration</h3>
          <ol>
            <li>
              Add the {{ $page.utilities.name }} utility to your project using
              <pre class="inline-code-block"><code>meltano add</code></pre>
              :
            </li>
            <pre><code>meltano add utility {{ $page.utilities.name }}</code></pre>
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
          <span v-if="$page.utilities.usage" v-html="$page.utilities.usageRendered"></span>
          <PluginCapabilitiesSection
            :capabilities="$page.utilities.capabilities"
            :name="$page.utilities.name"
            plugin_type="utility"
          />
          <PluginSettingsSection
            :settings="$page.utilities.settings"
            :preamble="$page.utilities.settings_preambleRendered"
            :name="$page.utilities.name"
          />
          <PluginCommandsSection
            :commands="$page.utilities.commands"
            :name="$page.utilities.name"
            plugin_type="utilities"
          />
          <PluginHelpSection
            :name="$page.utilities.name"
            :variant="$page.utilities.variant"
            :repo="$page.utilities.repo"
            plugin_type="utility"
          />
        </div>
        <PluginSidebar
          :name="$page.utilities.name"
          :domain_url="$page.utilities.domain_url"
          :repo="$page.utilities.repo"
          :maintenance_status="$page.utilities.maintenance_status"
          :keywords="$page.utilities.keywords"
          :variant="$page.utilities.variant"
          plugin_type="utility"
        />
      </div>
    </div>
  </Layout>
</template>

<script>
import PluginSidebar from "../components/PluginSidebar.vue";
import PluginSettingsSection from "../components/PluginSettingsSection.vue";
import PluginCommandsSection from "../components/PluginCommandsSection.vue";
import PluginCapabilitiesSection from "../components/PluginCapabilitiesSection.vue";
import PluginHelpSection from "../components/PluginHelpSection.vue";
import PluginPrereqSection from "../components/PluginPrereqSection.vue";

export default {
  metaInfo() {
    return {
      title: this.$page.utilities.name,
    };
  },
  name: "UtilitiesTemplate",
  components: {
    PluginSidebar,
    PluginSettingsSection,
    PluginCommandsSection,
    PluginCapabilitiesSection,
    PluginHelpSection,
    PluginPrereqSection,
  },
};
</script>

<page-query lang="graphql">
query Utilities($path: String!, $name: String!) {
  utilities: utilities(path: $path) {
    id
    name
    description
    path
    label
    logo_url
    namespace
    definition
    variant
    pip_url
    repo
    maintenance_status
    keywords
    next_steps
    commands {
      lint {
        name
        args
        description
      }
      fix {
        name
        args
        description
      }
      fix_force {
        name
        args
        description
      }
      ingest_dbt {
        name
        args
        description
      }
      ui {
        name
        args
        description
      }
      create_admin {
        name
        args
        description
      }
      load_examples {
        name
        args
        description
      }
    }
    requires {
      files {
        name
        variant
      }
    }
    settings {
      name
      label
      description
      env
    }
    prereq
    prereqRendered
    usage
    usageRendered
    settings_preamble
    settings_preambleRendered
  }
  variants: allUtilities(filter: { name: { eq: $name } }) {
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

<style>
.add-more-info {
  color: red;
  border: 1px solid red;
}
</style>
