<template>
  <Layout>
    <div class="single-plugin-overview">
      <div class="single-plugin-detail">
        <div class="single-plugin-top-bar">
          <h4>
            {{ $page.transformers.label }} -
            <span>{{ $page.transformers.description }}</span>
          </h4>
        </div>
        <div class="single-plugin-main">
          <g-image
            v-if="$page.transformers.logo_url"
            :src="
              require(`!!assets-loader?width=250!@logos/${$page.transformers.logo_url.replace(
                '/assets/logos/',
                ''
              )}`)
            "
          />
          <h1>
            {{ $page.transformers.name }} //
            <span>{{ $page.transformers.variant }}</span>
          </h1>
          <p>{{ $page.transformers.usage }}</p>
          <p>
            The {{ $page.transformers.name }}
            <a href="https://docs.meltano.com/concepts/plugins#transformer">transformer</a>
            uses SQL to transform data stored in your warehouse.
          </p>
          <p class="add-more-info">variant info here</p>
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
          <p>{{ $page.transformers.prereq }}</p>
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
          <!-- <h2>Capabilities</h2>
          <p>The current capabilities for <pre class="inline-code-block"><code>{{ $page.transformers.name }}</code></pre> may have been automatically set when originally added to the Hub. Please review the capabilities when using this extractor. If you find they are out of date, please consider updating them by making a pull request to the YAML file that defines the capabilities for this extractor.</p>
          <p>This plugin has the following capabilities:</p>
          <ul>
            <li v-for="(capability, index) in $page.transformers.capabilities" v-bind:key="index">{{capability}}</li>
          </ul> -->
          <h2>Settings</h2>
          <p>
            Settings for {{ $page.transformers.name }} itself can be configured through
            <a href="https://docs.getdbt.com/reference/dbt_project.yml">dbt_project.yml</a>
            as usual, which can be found at transform/dbt_project.yml in your Meltano project.
          </p>
          <p>
            The
            <a href="https://docs.meltano.com/contribute/plugins#setting-definitions">settings</a>
            for transformer {{ $page.transformers.name }} that are known to Meltano are documented
            below. To quickly find the setting you're looking for, use the Table of Contents at the
            top of the page.
          </p>
          <ul>
            <li v-for="(setting, index) in $page.transformers.settings" v-bind:key="index">
              {{ setting.name }}
            </li>
          </ul>
          <p>
            The settings for extractor tap-github that are known to Meltano are documented below. To
            quickly find the setting you're looking for, use the Table of Contents at the top of the
            page.
          </p>
          <h2>Commands</h2>
          <ol>
            <li v-for="(command, index) in $page.transformers.commands" v-bind:key="index">
              <h3>{{ command.args }}</h3>
              <span>{{ command.description }}</span>
            </li>
          </ol>
          <p class="add-more-info">Account ID</p>
          <p class="add-more-info">Personal Access Token</p>
          <p class="add-more-info">Start Date</p>
          <p class="add-more-info">End Date</p>
          <p class="add-more-info">Anything else</p>
          <h2>Looking for help?</h2>
          <div>
            If you're having trouble getting the
            {{ $page.transformers.name }} extractor to work, look for an
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
          :name="$page.transformers.name"
          :domain_url="$page.transformers.domain_url"
          :repo="$page.transformers.repo"
          :maintenance_status="$page.transformers.maintenance_status"
          :keywords="$page.transformers.keywords"
          :variant="$page.transformers.variant"
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
      title: this.$page.transformers.name,
    };
  },
  name: "TransformersTemplate",
  components: { PluginSidebar },
};
</script>

<page-query lang="graphql">
query Transformers($path: String!) {
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
      }
      compile {
        args
        description
      }
      deps {
        args
        description
      }
      run {
        args
        description
      }
      seed {
        args
        description
      }
      snapshot {
        args
        description
      }
      test {
        args
        description
      }
      freshness {
        args
        description
      }
      build {
        args
        description
      }
      docs_generate {
        args
        description
      }
      docs_serve {
        args
        description
      }
      debug {
        args
        description
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
