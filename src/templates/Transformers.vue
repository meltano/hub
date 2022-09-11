<template>
  <Layout>
    <div class="single-plugin-overview">
      <div class="single-plugin-detail">
        <div class="single-plugin-top-bar">
          <table>
            <tr>
              <td style="padding: 25px">
                <g-image
                  v-if="$page.transformers.logo_url"
                  :src="
                    require(`!!assets-loader?width=250&height=200&fit=inside!@logos/${$page.transformers.logo_url.replace(
                      '/assets/logos/',
                      ''
                    )}`)
                  "
                />
              </td>
              <td>
                <h1>
                  {{ $page.transformers.label }}
                </h1>
                <h2>
                  <code>{{ $page.transformers.name }} from {{ $page.transformers.variant }}</code>
                </h2>
                <p>
                  <b>{{ $page.transformers.description }}</b>
                </p>
              </td>
            </tr>
          </table>
        </div>
        <div class="single-plugin-main">
          <p>
            The {{ $page.transformers.name }}
            <a href="https://docs.meltano.com/concepts/plugins#transformer">transformer</a>
            uses SQL to transform data stored in your warehouse.
          </p>
          <h3>Other Available Variants</h3>
          <ul>
            <li v-for="(variant, index) in $page.variants.edges" v-bind:key="index">
              <g-link
                :to="variant.node.path"
                v-if="variant.node.path !== $page.transformers.path"
                >{{ variant.node.variant }}</g-link
              >
              <span v-else>{{ variant.node.variant }}</span>
              <span v-if="variant.node.isDefault"> (default)</span>
            </li>
          </ul>
          <h2>Getting Started</h2>
          <PluginPrereqSection :plugin="$page.transformers" plugin_type="transformer" />
          <PluginRequiresSection
            :requires="$page.transformers.requires"
            :name="$page.transformers.name"
            plugin_type="transformer"
          />
          <h3>Installation and configuration</h3>
          <ol>
            <li>
              Add the {{ $page.transformers.name }} transformer to your project using
              <pre class="inline-code-block"><code>meltano add</code></pre>
              :
            </li>
            <pre><code>meltano add transformer {{ $page.transformers.name }}</code></pre>
            <li>
              Configure the
              <a href="https://hub.meltano.com/transformers/dbt#settings">settings</a>
              below using
              <pre class="inline-code-block"><code>meltano config</code></pre>
              .
            </li>
          </ol>
          <h3>Next steps</h3>
          <p>
            Follow the remaining steps of the
            <a href="https://docs.meltano.com/getting-started.html">Getting Started guide</a>:
          </p>
          <ol>
            <li>
              <a
                href="https://docs.meltano.com/getting-started.html#transform-loaded-data-for-analysis"
                >Transform loaded data for analysis</a
              >
            </li>
          </ol>
          <p>If you run into any issues, learn how to get help.</p>
          <PluginSettingsSection
            :settings="$page.transformers.settings"
            :name="$page.transformers.name"
          />
          <PluginCommandsSection
            :commands="$page.transformers.commands"
            :name="$page.transformers.name"
            plugin_type="transformer"
          />
          <PluginHelpSection
            :name="$page.transformers.name"
            :variant="$page.transformers.variant"
            :repo="$page.transformers.repo"
            plugin_type="transformers"
          />
        </div>
        <PluginSidebar
          :name="$page.transformers.name"
          :domain_url="$page.transformers.domain_url"
          :repo="$page.transformers.repo"
          :maintenance_status="$page.transformers.maintenance_status"
          :keywords="$page.transformers.keywords"
          :variant="$page.transformers.variant"
          plugin_type="transformer"
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
      title: this.$page.transformers.name,
    };
  },
  name: "TransformersTemplate",
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
query Transformers($path: String!, $name: String!) {
  transformers: transformers(path: $path) {
    id
    path
    label
    name
    logo_url
    namespace
    variant
    pip_url
    repo
    requires {
      files {
        name
        variant
      }
    }
    maintenance_status
    settings {
      name
      label
      value
    }
    commands {
      clean {
        args
        description
        name
      }
      compile {
        args
        description
        name
      }
      deps {
        args
        description
        name
      }
      run {
        args
        description
        name
      }
      seed {
        args
        description
        name
      }
      snapshot {
        args
        description
        name
      }
      test {
        args
        description
        name
      }
      freshness {
        args
        description
        name
      }
      build {
        args
        description
        name
      }
      docs_generate {
        args
        description
        name
      }
      docs_serve {
        args
        description
        name
      }
      debug {
        args
        description
        name
      }
    }
  }
  variants: allTransformers(filter: { name: { eq: $name } }) {
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
