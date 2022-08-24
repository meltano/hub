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
          <h2>Capabilities</h2>
          <div>
            The current capabilities for
            <pre class="inline-code-block"><code>{{ $page.utilities.name }}</code></pre>
            may have been automatically set when originally added to the Hub. Please review the
            capabilities when using this extractor. If you find they are out of date, please
            consider updating them by making a pull request to the YAML file that defines the
            capabilities for this extractor.
          </div>
          <p>This plugin has the following capabilities:</p>
          <ul>
            <li v-for="(capability, index) in $page.utilities.capabilities" v-bind:key="index">
              {{ capability }}
            </li>
          </ul>
          <h2>Settings</h2>
          <p>{{ $page.utilities.name }} requires the configuration of the following settings:</p>
          <ul>
            <li v-for="(setting, index) in $page.utilities.settings" v-bind:key="index">
              {{ setting.name }}
            </li>
          </ul>
          <p>
            The settings for {{ $page.utilities.name }} that are known to Meltano are documented
            below. To quickly find the setting you're looking for, use the Table of Contents at the
            top of the page.
          </p>
          <h2>Looking for help?</h2>
          <div>
            If you're having trouble getting the
            {{ $page.utilities.name }} extractor to work, look for an
            <a href="https://github.com/singer-io/tap-github/issues"
              >existing issue in its repository</a
            >, file a <a href="https://github.com/singer-io/tap-github/issues/new">new issue</a>, or
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

export default {
  metaInfo() {
    return {
      title: this.$page.utilities.name
    };
  },
  name: "UtilitiesTemplate",
  components: { PluginSidebar }
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
        args
        description
      }
      fix {
        args
        description
      }
      fix_force {
        args
        description
      }
      ingest_dbt {
        args
        description
      }
      ui {
        args
        description
      }
      create_admin {
        args
        description
      }
      load_examples {
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
    usage
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
