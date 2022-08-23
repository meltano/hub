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
          <h1>
            {{ $page.orchestrators.name }} //
            <span>{{ $page.orchestrators.variant }}</span>
          </h1>
          <p>{{ $page.orchestrators.usage }}</p>
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
          <p>{{ $page.orchestrators.prereq }}</p>
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
          <p>{{ $page.orchestrators.next_steps }}</p>
          <p>If you run into any issues, learn how to get help.</p>
          <!-- <h2>Capabilities</h2>
          <p>The current capabilities for
          <pre class="inline-code-block"><code>{{ $page.orchestrators.name }}</code></pre> may have been automatically
          set when originally added to the Hub. Please review the capabilities when using this extractor. If you find
          they are out of date, please consider updating them by making a pull request to the YAML file that defines the
          capabilities for this extractor.</p>
          <p>This plugin has the following capabilities:</p>
          <ul>
            <li v-for="(capability, index) in $page.orchestrators.capabilities" v-bind:key="index">{{ capability }}</li>
          </ul> -->
          <h2>Settings</h2>
          <p>
            {{ $page.orchestrators.name }} requires the configuration of the following settings:
          </p>
          <ul>
            <li v-for="(setting, index) in $page.orchestrators.settings" v-bind:key="index">
              {{ setting.name }}
            </li>
          </ul>
          <p>
            The settings for extractor tap-github that are known to Meltano are documented below. To
            quickly find the setting you're looking for, use the Table of Contents at the top of the
            page.
          </p>
          <!-- <h3>Personal Access Tokens (access_token)</h3>
          <ul><li>Environment variable: TAP_GITHUB_ACCESS_TOKEN</li></ul> -->
          <p class="add-more-info">Account ID</p>
          <p class="add-more-info">Personal Access Token</p>
          <p class="add-more-info">Start Date</p>
          <p class="add-more-info">End Date</p>
          <p class="add-more-info">Anything else</p>
          <h2>Looking for help?</h2>
          <div>
            If you're having trouble getting the
            {{ $page.orchestrators.name }} orchestrator to work, look for an
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
          :name="$page.orchestrators.name"
          :domain_url="$page.orchestrators.domain_url"
          :repo="$page.orchestrators.repo"
          :maintenance_status="$page.orchestrators.maintenance_status"
          :keywords="$page.orchestrators.keywords"
          :variant="$page.orchestrators.variant"
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
      title: this.$page.orchestrators.name
    };
  },
  name: "OrchestratorsTemplate",
  components: { PluginSidebar }
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
    requires {
      files {
        name
        variant
      }
    }
    maintenance_status
    commands {
      create_admin {
        args
        description
      }
      ui {
        args
        description
      }
    }
    settings {
      name
    }
    logo_url
    settings_preamble
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

<style>
.add-more-info {
  color: red;
  border: 1px solid red;
}
</style>
