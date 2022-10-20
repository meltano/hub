<template>
  <div id="detail" class="prose p-5">
    <p>
      The {{ $page.plugins.name }}
      <a :href="'https://docs.meltano.com/concepts/plugins#' + $page.plugins.pluginTypePlural">{{
        $page.plugins.pluginType
      }}</a>
      <span v-if="$page.plugins.pluginType === 'extractor'">
        pulls data from
        <a :href="$page.plugins.domain_url">{{ $page.plugins.label }}</a> that can then be sent to a
        destination using a <g-link to="/loaders">loader</g-link>.</span
      >
      <span v-if="$page.plugins.pluginType === 'loader'">
        sends data into <a :href="$page.plugins.domain_url">{{ $page.plugins.label }}</a>
        after it was pulled from a source using an
        <g-link to="/extractors">extractor</g-link></span
      >
      <span v-if="$page.plugins.pluginType === 'transformer'">
        is a plugin for running SQL-based transformations on data stored in your warehouse.</span
      >
      <span v-if="$page.plugins.pluginType === 'orchestrator'">
        allows for workflows to be programmatically authored, scheduled, and monitored.</span
      >
      <span class="prose" v-if="$page.plugins.pluginType === 'utility'" v-html="$page.plugins.definition_rendered"></span>
      <span
        class="prose"
        v-if="$page.plugins.pluginType === 'file'"
        v-html="$page.plugins.definition_rendered"
      ></span>
    </p>
    <span v-if="$page.variants.edges && $page.variants.edges.length > 1">
      <h2>Available Variants</h2>
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
      <div v-if="requires">
        <h2>Requirements</h2>
        <p>This {{ plugin_type }} requires the following plugins and variants to work:</p>
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
        <div class="prose mt-3 p-2" v-if="plugin.prereq" v-html="plugin.prereq_rendered"></div>
      </div>
      <h3 id="installation">Installation and configuration</h3>
      <ol class="list-decimal list-inside pl-4">
        <li>
          Add the {{ $page.plugins.name }} {{ $page.plugins.pluginType }} to your project using
          <a href="https://docs.meltano.com/reference/command-line-interface#add">
            <pre class="inline-code-block"><code>meltano add</code></pre>
          </a>
          :
        </li>
        <pre
          class="prose language-bash rounded-md"
        ><code >meltano add {{ $page.plugins.pluginType }} {{ $page.plugins.name }}<span v-if="!$page.plugins.isDefault"> --variant {{ $page.plugins.variant }}</span></code></pre>
        <li>
          Configure the {{ $page.plugins.name }} <a href="#settings">settings</a> using
          <a href="https://docs.meltano.com/reference/command-line-interface#config">
            <pre class="inline-code-block"><code>meltano config</code></pre>
          </a>
          :
        </li>
        <pre
          class="prose language-bash rounded-md"
        ><code >meltano config {{ $page.plugins.name }} set --interactive</code></pre>
        <span v-if="$page.plugins.pluginType === 'extractor'">
          <li>
            Test that extractor settings are valid using
            <a href="https://docs.meltano.com/reference/command-line-interface#config">
              <pre class="inline-code-block"><code>meltano config</code></pre>
            </a>
            :
          </li>
          <pre
            class="prose language-bash rounded-md"
          ><code >meltano config {{ $page.plugins.name }} test</code></pre>
        </span>
      </ol>
      <h3>Next Steps</h3>
      <div
        v-if="$page.plugins.next_steps_rendered"
        v-html="$page.plugins.next_steps_rendered"
        class="prose"
      ></div>
      <!-- extractors default next steps -->
      <div v-else-if="$page.plugins.pluginType == 'extractor'">
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
      <div v-else-if="$page.plugins.pluginType == 'loader'">
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
      <div v-else-if="$page.plugins.pluginType == 'transformer'">
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
        <h2 id="capabilities">Capabilities</h2>
        <span class="space-y-3" v-if="capabilities && capabilities.length">
          <p>
            The current capabilities for
            <code>{{ name }}</code>
            may have been automatically set when originally added to the Hub. Please review the
            capabilities when using this {{ plugin_type }}. If you find they are out of date, please
            consider updating them by making a pull request to the YAML file that defines the
            capabilities for this {{ plugin_type }}.
          </p>
          <p>This plugin has the following capabilities:</p>
          <ul class="list-disc list-inside pl-4">
            <li v-for="(capability, index) in capabilities" v-bind:key="index">
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
        <span v-else
          >This plugin currently has no capabilities defined. If you know the capabilities required
          by this plugin, <a href="#contribute">please contribute!</a></span
        >
      </div>
      <div>
        <h2 id="settings">Settings</h2>
        <span class="space-y-3" v-if="settings && settings.length">
          <div class="prose mt-3 p-2" v-if="preamble" v-html="preamble"></div>
          <p>
            The
            <code>{{ name }}</code> settings that are known to Meltano are documented below. To
            quickly find the setting you're looking for, click on any setting name from the list:
          </p>
          <ul class="list-disc list-inside pl-4">
            <li v-for="(setting, index) in settings" v-bind:key="index">
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
              :href="`https://github.com/meltano/hub/blob/main/_data/meltano/${plugin_type_plural}/${name}/${variant}.yml`"
            >
              YAML file</a
            >
            that defines the settings for this plugin.
          </p>
          <span class="mt-6" v-for="(setting, index) in settings" v-bind:key="index">
            <p class="mt-3 text-xl" :id="setting.name + '-setting'">
              <code>{{ setting.label }} ({{ setting.name }})</code>
            </p>
            <ul class="list-inside list-disc pl-4 text-sm">
              <li>
                Environment variable:
                <code>{{
                  `${name.replaceAll("-", "_").toUpperCase()}_${setting.name
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
      <div v-if="$page.plugins.commands">
        <h2 id="commands">Commands</h2>
        <span
          >The {{ name }} {{ plugin_type }} supports the following commands that can be used with
          <pre class="inline-code-block">meltano invoke</pre>
          :</span
        >
        <div v-for="(value, key, index) in $page.plugins.commands" v-bind:key="index">
          <span v-if="value">
            <h3>
              <code>{{ $page.plugins.name }}:{{ value.name }}</code>
            </h3>
            <p>{{ value.description }}</p>
            <span
              >Run this command using <code class="inline-code-block">meltano invoke</code>:
            </span>
            <pre><code>meltano invoke {{ $page.plugins.name }}:{{ value.name }} [additional arguments...]</code></pre>
          </span>
        </div>
      </div>
      <div
        class="prose mt-4"
        v-if="$page.plugins.usage"
        v-html="$page.plugins.usage_rendered"
      ></div>
      <div class="help-module">
        <h2 id="contribute">Something missing?</h2>
        <p>This page is generated from a YAML file that you can contribute changes to.</p>
        <a
          v-if="name"
          :href="`https://github.com/meltano/hub/blob/main/_data/meltano/${plugin_type_plural}/${name}/${variant}.yml`"
          >Edit it on GitHub!</a
        >
        <h2 id="looking-for-help">Looking for help?</h2>
        <div>
          If you're having trouble getting the
          {{ name }} {{ plugin_type }} to work, look for an
          <a :href="`${repo}/issues`">existing issue in its repository</a>, file a
          <a :href="`${repo}/issues/new`">new issue</a>, or
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
  name: "PluginPrereqSection",
  props: ["plugin", "plugin_type"],
};
</script>

<style></style>
