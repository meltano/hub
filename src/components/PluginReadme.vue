<template>
  <div id="detail" class="prose p-5">
    <p>
      The {{ plugin.name }}
      <a :href="'https://docs.meltano.com/concepts/plugins#' + plugin.pluginTypePlural">{{
        plugin.pluginType
      }}</a>
      <span v-if="plugin.pluginType === 'extractor'">
        pulls data from
        <a :href="plugin.domain_url">{{ plugin.label }}</a> that can then be sent to a
        destination using a <g-link to="/loaders">loader</g-link>.</span
      >
      <span v-if="plugin.pluginType === 'loader'">
        sends data into <a :href="plugin.domain_url">{{ plugin.label }}</a>
        after it was pulled from a source using an
        <g-link to="/extractors">extractor</g-link></span
      >
      <span v-if="plugin.pluginType === 'transformer'">
        is a plugin for running SQL-based transformations on data stored in your warehouse.</span
      >
      <span v-if="plugin.pluginType === 'orchestrator'">
        allows for workflows to be programmatically authored, scheduled, and monitored.</span
      >
      <span class="prose" v-if="plugin.pluginType === 'utility'" v-html="plugin.definition_rendered"></span>
      <span
        class="prose"
        v-if="plugin.pluginType === 'file'"
        v-html="plugin.definition_rendered"
      ></span>
    </p>
    <span v-if="$page.variants.edges && $page.variants.edges.length > 1">
      <h2>Available Variants</h2>
      <ul class="list-disc list-inside pl-4">
        <li v-for="(variant, index) in variants.edges" v-bind:key="index">
          <g-link :to="variant.node.path" v-if="variant.node.path !== plugin.path">{{
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
      <div v-if="requires">
        <h2>Requirements</h2>
        <p>This {{ plugin.pluginType }} requires the following plugins and variants to work:</p>
        <ul class="list-disc list-inside">
          <li v-for="(file, index) in requires.files" v-bind:key="index">
            {{ file.name }} - {{ file.variant }}
          </li>
        </ul>
      </div>
    </span>
    <div>
      <h2 id="getting-started">Getting Started</h2>
      <div>
        <h3>Prerequisites</h3>
        <p>
          If you haven't already, follow the initial steps of the
          <a href="https://docs.meltano.com/getting-started/installation">Getting Started guide</a>:
        </p>
        <ol class="list-decimal list-inside pl-4">
          <li>
            <a href="https://docs.meltano.com/getting-started/installation">Install Meltano</a>
          </li>
          <li>
            <a href="https://docs.meltano.com/getting-started/part1">Create your Meltano project</a>
          </li>
        </ol>
        <div class="prose mt-3" v-if="plugin.prereq" v-html="plugin.prereq_rendered"></div>
      </div>
      <h3 id="installation">Installation and configuration</h3>
      <ol class="list-decimal list-inside pl-4">
        <li>
          Add the {{ plugin.name }} {{ plugin.pluginType }} to your project using
          <a href="https://docs.meltano.com/reference/command-line-interface#add">
            <pre class="inline-code-block"><code>meltano add</code></pre>
          </a>
          :
        </li>
        <pre
          class="prose language-bash rounded-md"
        ><code >meltano add {{ plugin.pluginType }} {{ plugin.name }}<span v-if="!plugin.isDefault"> --variant {{ plugin.variant }}</span></code></pre>
        <li>
          Configure the {{ plugin.name }} <a href="#settings">settings</a> using
          <a href="https://docs.meltano.com/reference/command-line-interface#config">
            <pre class="inline-code-block"><code>meltano config</code></pre>
          </a>
          :
        </li>
        <pre
          class="prose language-bash rounded-md"
        ><code >meltano config {{ plugin.name }} set --interactive</code></pre>
        <span v-if="plugin.pluginType === 'extractor'">
          <li>
            Test that extractor settings are valid using
            <a href="https://docs.meltano.com/reference/command-line-interface#config">
              <pre class="inline-code-block"><code>meltano config</code></pre>
            </a>
            :
          </li>
          <pre
            class="prose language-bash rounded-md"
          ><code >meltano config {{ plugin.name }} test</code></pre>
        </span>
      </ol>
      <h3>Next Steps</h3>
      <div
        v-if="plugin.next_steps_rendered"
        v-html="plugin.next_steps_rendered"
        class="prose"
      ></div>
      <div v-else-if="plugin.pluginType == 'extractor'">
        <p>
          Follow the remaining steps of the
          <a href="https://docs.meltano.com/getting-started/part1">Getting Started guide</a>:
        </p>
        <ol class="list-decimal list-inside pl-4">
          <li>
            <a
              href="https://docs.meltano.com/getting-started/part1#select-entities-and-attributes-to-extract"
              >Select entities and attributes to extract</a
            >
          </li>
          <li>
            <a href="https://docs.meltano.com/getting-started/part2"
              >Add a loader to send data to a destination</a
            >
          </li>
          <li>
            <a
              href="https://docs.meltano.com/getting-started/part2#run-your-data-integration-el-pipeline"
              >Run a data integration (EL) pipeline</a
            >
          </li>
        </ol>
      </div>

      <!-- loaders default next steps -->
      <div v-else-if="plugin.pluginType == 'loader'">
        <p>
          Follow the remaining steps of the
          <a href="https://docs.meltano.com/getting-started/part1">Getting Started guide</a>:
        </p>
        <ol class="list-decimal list-inside pl-4">
          <li>
            <a
              href="https://docs.meltano.com/getting-started/part2#run-your-data-integration-el-pipeline"
              >Run a data integration (EL) pipeline</a
            >
          </li>
        </ol>
      </div>

      <!-- Default transformers next steps -->
      <div v-else-if="plugin.pluginType == 'transformer'">
        <p>
          Follow the remaining steps of the
          <a href="https://docs.meltano.com/getting-started/part3">Getting Started guide</a>:
        </p>
        <ol class="list-decimal list-inside pl-4">
          <li>
            <a href="https://docs.meltano.com/getting-started/part3">
              Transform loaded data for analysis
            </a>
          </li>
        </ol>
      </div>
      <!-- No next steps defined for this plugin. -->
      <div v-else></div>

      <!-- Help section -->
      <p>If you run into any issues, learn how to get help.</p>
    </div>
    <div>
      <div>
        <span class="space-y-3" v-if="plugin.capabilities && plugin.capabilities.length">
          <h2 id="capabilities">Capabilities</h2>
          <p>
            The current capabilities for
            <code>{{ plugin.name }}</code>
            may have been automatically set when originally added to the Hub. Please review the
            capabilities when using this {{ plugin.pluginType }}. If you find they are out of date, please
            consider updating them by making a pull request to the YAML file that defines the
            capabilities for this {{ plugin.pluginType }}.
          </p>
          <p>This plugin has the following capabilities:</p>
          <ul class="list-disc list-inside pl-4">
            <li v-for="(capability, index) in plugin.capabilities" v-bind:key="index">
              {{ capability }}
            </li>
          </ul>
          <p>
            You can
            <a
              href="https://docs.meltano.com/guide/configuration#overriding-discoverable-plugin-properties"
              >override these capabilities or specify additional ones</a
            >
            in your <code>meltano.yml</code> by adding the <code>capabilities</code> key.
          </p>
        </span>
        <span v-else-if="plugin.type === 'extractor'">
          <h2 id="capabilities">Capabilities</h2>
          <p>
            This plugin currently has no capabilities defined. If you know the capabilities required
            by this plugin, <a href="#contribute">please contribute!</a>
          </p>
        </span>
      </div>
      <div>
        <h2 id="settings">Settings</h2>
        <span class="space-y-3" v-if="plugin.settings && plugin.settings.length">
          <div class="prose mt-3 p-2" v-if="plugin.preamble" v-html="plugin.preamble"></div>
          <p>
            The
            <code>{{ plugin.name }}</code> settings that are known to Meltano are documented below. To
            quickly find the setting you're looking for, click on any setting name from the list:
          </p>
          <ul class="list-disc list-inside pl-4">
            <li v-for="(setting, index) in plugin.settings" v-bind:key="index">
              <a :href="'#' + setting.name + '-setting'"
                ><code>{{ setting.name }}</code></a
              >
            </li>
          </ul>
          <p>
            You can
            <a
              href="https://docs.meltano.com/guide/configuration#overriding-discoverable-plugin-properties"
              >override these settings or specify additional ones</a
            >
            in your <code>meltano.yml</code> by adding the <code>settings</code> key.
          </p>
          <p>
            Please consider adding any settings you have defined locally to this definition on
            MeltanoHub by making a pull request to the
            <a
              :href="`https://github.com/meltano/hub/blob/main/_data/meltano/${plugin.pluginTypePlural}/${plugin.name}/${plugin.variant}.yml`"
            >
              YAML file</a
            >
            that defines the settings for this plugin.
          </p>
          <span class="mt-6" v-for="(setting, index) in plugin.settings" v-bind:key="index">
            <p class="mt-3 text-xl" :id="setting.name + '-setting'">
              {{ setting.label }} (<code>{{ setting.name }}</code>)
            </p>
            <ul class="list-inside list-disc pl-4 text-sm">
              <li>
                Environment variable:
                <code>{{
                  `${setting.name.replaceAll("-", "_").toUpperCase()}_${setting.name
                    .replaceAll(".", "_")
                    .toUpperCase()}`
                }}</code>
              </li>
              <li v-if="setting.value">
                Default Value: <code>{{ setting.value }}</code>
              </li>
            </ul>
            <div
              class="prose mt-3 bg-slate-100 p-2"
              v-if="setting.description"
              v-html="setting.description_rendered"
            ></div>
            <span v-else>[No description provided.]</span>
          </span>
        </span>
        <span v-else
          >This plugin currently has no settings defined. If you know the settings required by this
          plugin, <a href="#contribute">please contribute!</a></span
        >
      </div>
      <div v-if="plugin.commands && plugin.commands.length">
        <h2 id="commands">Commands</h2>
        <span
          >The {{ plugin.name }} {{ plugin.pluginType }} supports the following commands that can be used with
          <pre class="inline-code-block">meltano invoke</pre>
          :</span
        >
        <div v-for="(value, key, index) in plugin.commands" v-bind:key="index">
          <span v-if="value">
            <h3>
              <code>{{ plugin.name }}:{{ value.name }}</code>
            </h3>
            <p>{{ value.description }}</p>
            <span
              >Run this command using <code class="inline-code-block">meltano invoke</code>:
            </span>
            <pre><code>meltano invoke {{ plugin.name }}:{{ value.name }} [additional arguments...]</code></pre>
          </span>
        </div>
      </div>
      <div
        class="prose mt-4"
        v-if="plugin.usage"
        v-html="plugin.usage_rendered"
      ></div>
      <div class="help-module">
        <h2 id="contribute">Something missing?</h2>
        <p>This page is generated from a YAML file that you can contribute changes to.</p>
        <a
          v-if="plugin.name"
          :href="`https://github.com/meltano/hub/blob/main/_data/meltano/${plugin.pluginTypePlural}/${plugin.name}/${plugin.variant}.yml`"
          >Edit it on GitHub!</a
        >
        <h2 id="looking-for-help">Looking for help?</h2>
        <div>
          If you're having trouble getting the
          {{ plugin.name }} {{ plugin.pluginType }} to work, look for an
          <a :href="`${plugin.repo}/issues`">existing issue in its repository</a>, file a
          <a :href="`${plugin.repo}/issues/new`">new issue</a>, or
          <a href="https://meltano.com/slack">join the Meltano Slack community</a>
          and ask for help in the
          <pre class="inline-code-block"><code>#plugins-general</code></pre>
          channel.
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PluginReadme",
  props: ["plugin", "variants"],
};
</script>

<style></style>
