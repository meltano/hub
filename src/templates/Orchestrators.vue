<template>
  <Layout>
    <div class="single-plugin-overview">
      <div class="single-plugin-detail">
        <div class="single-plugin-top-bar">
          <table>
            <tr>
              <td style="padding: 25px">
                <g-image
                  v-if="$page.orchestrators.logo_url"
                  :src="
                    require(`!!assets-loader?width=250&height=200&fit=inside!@logos/${$page.orchestrators.logo_url.replace(
                      '/assets/logos/',
                      ''
                    )}`)
                  "
                />
              </td>
              <td>
                <h1>
                  {{ $page.orchestrators.label }}
                </h1>
                <h2>
                  <code>{{ $page.orchestrators.name }} from {{ $page.orchestrators.variant }}</code>
                </h2>
                <p>
                  <b>{{ $page.orchestrators.description }}</b>
                </p>
              </td>
            </tr>
          </table>
        </div>
        <div class="single-plugin-main">
          <p>
            The {{ $page.orchestrators.name }}
            <a href="https://docs.meltano.com/concepts/plugins#orchestrators"
              >Meltano orchestrator</a
            >
            allows for workflows to be programmatically authored, scheduled, and monitored.
          </p>
          <h3>Other Available Variants</h3>
          <ul>
            <li v-for="(variant, index) in $page.variants.edges" v-bind:key="index">
              <g-link
                :to="variant.node.path"
                v-if="variant.node.path !== $page.orchestrators.path"
                >{{ variant.node.variant }}</g-link
              >
              <span v-else>{{ variant.node.variant }}</span>
              <span v-if="variant.node.isDefault"> (default)</span>
            </li>
          </ul>
          <h2>Getting Started</h2>
          <PluginPrereqSection :plugin="$page.orchestrators" plugin_type="orchestrator" />
          <PluginRequiresSection
            :requires="$page.orchestrators.requires"
            plugin_type="orchestrator"
            :name="$page.orchestrators.name"
          />
          <h3>Installation and configuration</h3>

          <p>Add the airflow orchestrator to your project using meltano add :</p>
          <ol>
            <li>
              <pre class=""><code>meltano add orchestrator airflow</code></pre>
            </li>
            <li>
              Configure the settings below using
              <pre class="inline-code-block"><code>meltano config</code></pre>
              .
            </li>
          </ol>

          <h3>Next steps</h3>
          <span
            v-if="$page.orchestrators.next_steps"
            v-html="$page.orchestrators.next_stepsRendered"
          ></span>
          <p>If you run into any issues, learn how to get help.</p>
          <PluginSettingsSection
            :settings="$page.orchestrators.settings"
            :preamble="$page.orchestrators.settings_preambleRendered"
            :name="$page.orchestrators.name"
          />
          <PluginCommandsSection
            :commands="$page.orchestrators.commands"
            :name="$page.orchestrators.name"
            plugin_type="orchestrator"
          />
          <PluginHelpSection
            :name="$page.orchestrators.name"
            :variant="$page.orchestrators.variant"
            :repo="$page.orchestrators.repo"
            plugin_type="orchestrators"
          />
        </div>
        <PluginSidebar
          :name="$page.orchestrators.name"
          :domain_url="$page.orchestrators.domain_url"
          :repo="$page.orchestrators.repo"
          :maintenance_status="$page.orchestrators.maintenance_status"
          :keywords="$page.orchestrators.keywords"
          :variant="$page.orchestrators.variant"
          plugin_type="orchestrator"
        />
      </div>
    </div>
  </Layout>
</template>

<script>
import PluginSidebar from "../components/PluginSidebar.vue";
import PluginSettingsSection from "../components/PluginSettingsSection.vue";
import PluginCommandsSection from "../components/PluginCommandsSection.vue";
import PluginRequiresSection from "../components/PluginRequiresSection.vue";
import PluginHelpSection from "../components/PluginHelpSection.vue";
import PluginPrereqSection from "../components/PluginPrereqSection.vue";

export default {
  metaInfo() {
    return {
      title: this.$page.orchestrators.name,
    };
  },
  name: "OrchestratorsTemplate",
  components: {
    PluginSidebar,
    PluginSettingsSection,
    PluginCommandsSection,
    PluginRequiresSection,
    PluginHelpSection,
    PluginPrereqSection,
  },
};
</script>

<page-query lang="graphql">
query Orchestrators($path: String!, $name: String!) {
  orchestrators: orchestrators(path: $path) {
    id
    path
    label
    name
    logo_url
    namespace
    variant
    pip_url
    repo
    next_steps
    next_stepsRendered
    requires {
      files {
        name
        variant
      }
    }
    maintenance_status
    commands {
      create_admin {
        name
        args
        description
      }
      ui {
        name
        args
        description
      }
    }
    settings {
      name
    }
    logo_url
    settings_preamble
    settings_preambleRendered
  }
  variants: allOrchestrators(filter: { name: { eq: $name } }) {
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

<style></style>
