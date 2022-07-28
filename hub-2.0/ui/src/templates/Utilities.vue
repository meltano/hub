<template>
  <Layout>
    <div class="single-plugin-overview">
      <div class="single-plugin-detail">
        <div class="single-plugin-top-bar">
          <h4>{{ $page.utilities.label }} - <span>{{ $page.utilities.description }}</span></h4>
        </div>
        <div class="single-plugin-main">
          <h1>
            {{ $page.utilities.name }} //
            <span>{{ $page.utilities.variant }}</span>
          </h1>
          <!-- <p>{{ $page.utilities.usage }}</p> -->
          <p>The {{ $page.utilities.name }} <a href="https://docs.meltano.com/concepts/plugins#utilities">utility</a> is
            {{ $page.utilities.definition }}</p>
          <p class="add-more-info">variant info here</p>
          <h2>Getting Started</h2>
          <h3>Prerequisites</h3>
          <p>If you haven't already, follow the initial steps of the <a
              href="https://docs.meltano.com/getting-started.html">Getting Started guide</a>:</p>
          <ol>
            <li><a href="https://docs.meltano.com/getting-started.html#install-meltano">Install Meltano</a></li>
            <li><a href="https://docs.meltano.com/getting-started.html#create-your-meltano-project">Create your Meltano
                project</a></li>
          </ol>
          <p>{{ $page.utilities.prereq }}</p>
          <p>{{ $page.utilities.next_steps }}</p>
          <h3>Installation and configuration</h3>
          <ol>
            <li>Add the {{ $page.utilities.name }} utility to your project using
              <pre class="inline-code-block"><code>meltano add</code></pre>:
            </li>
            <pre><code>meltano add utility {{ $page.utilities.name }}</code></pre>
          </ol>
          <h3>Next steps</h3>
          <p>Follow the remaining steps of the <a href="https://docs.meltano.com/getting-started.html">Getting Started
              guide</a>:</p>
          <ol>
            <li><a href="https://docs.meltano.com/getting-started.html#select-entities-and-attributes-to-extract">Select
                entities and attributes to extract</a></li>
            <li><a href="https://docs.meltano.com/getting-started.html#add-a-loader-to-send-data-to-a-destination">Add a
                loader to send data to a destination</a></li>
            <li><a href="https://docs.meltano.com/getting-started.html#run-a-data-integration-el-pipeline">Run a data
                integration (EL) pipeline</a></li>
          </ol>
          <p>If you run into any issues, learn how to get help.</p>
          <h2>Capabilities</h2>
          <p>The current capabilities for
          <pre class="inline-code-block"><code>{{ $page.utilities.name }}</code></pre> may have been automatically set
          when originally added to the Hub. Please review the capabilities when using this extractor. If you find they
          are out of date, please consider updating them by making a pull request to the YAML file that defines the
          capabilities for this extractor.</p>
          <p>This plugin has the following capabilities:</p>
          <ul>
            <li v-for="(capability, index) in $page.utilities.capabilities" v-bind:key="index">{{ capability }}</li>
          </ul>
          <h2>Settings</h2>
          <p>{{ $page.utilities.name }} requires the configuration of the following settings:</p>
          <ul>
            <li v-for="(setting, index) in $page.utilities.settings" v-bind:key="index">{{ setting.name }}</li>
          </ul>
          <p>The settings for extractor tap-github that are known to Meltano are documented below. To quickly find the
            setting you're looking for, use the Table of Contents at the top of the page.</p>
          <p class="add-more-info">Account ID</p>
          <p class="add-more-info">Personal Access Token</p>
          <p class="add-more-info">Start Date</p>
          <p class="add-more-info">End Date</p>
          <p class="add-more-info">Anything else</p>
          <h2>Looking for help?</h2>
          <p>If you're having trouble getting the {{ $page.utilities.name }} extractor to work, look for an <a
              href="https://github.com/singer-io/tap-github/issues">existing issue in its repository</a>, file a <a
              href="https://github.com/singer-io/tap-github/issues/new">new issue</a>, or <a
              href="https://meltano.com/slack">join the Meltano Slack community</a> and ask for help in the
          <pre class="inline-code-block"><code>#plugins-general channel</code></pre>.</p>
          <h3>Found an issue on this page?</h3>
          <p>This page is generated from a YAML file that you can contribute changes to. <a
              href="https://github.com/meltano/hub/blob/main/_data/meltano/extractors/tap-github/singer-io.yml">Edit it
              on GitHub!</a></p>
        </div>
        <div class="single-plugin-aside">
          <h4>Install</h4>
          <pre><code>meltano add {{ $page.utilities.name }}</code></pre>
          <h4>Homepage</h4>
          <div class="link-box">
            <img class="aside-icon" src="../assets/images/link-solid.svg" /><a :href="$page.utilities.domain_url">{{
                $page.utilities.domain_url
            }}</a>
          </div>
          <h4>Repo</h4>
          <div class="link-box">
            <img class="aside-icon" src="../assets/images/git-alt-brands.svg" /><a :href="$page.utilities.repo">{{
                $page.utilities.repo
            }}</a>
          </div>
          <h4>Maintenance Status</h4>
          <p>{{ $page.utilities.maintenance_status }}</p>
          <h4>Keywords</h4>
          <p v-for="(keyword, index) in $page.utilities.keywords" v-bind:key="index">{{ keyword }}</p>
        </div>
      </div>
    </div>
  </Layout>
</template>

<script>
export default {
  name: "UtilitiesTemplate",
};
</script>

<page-query lang="graphql">
query Utilities($path: String!) {
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
}
</page-query>

<style>
.add-more-info {
  color: red;
  border: 1px solid red;
}
</style>
