<template>
  <div>
    <p class="text-3xl pb-4 pt-8 font-bold" id="settings">Settings</p>
    <span class="space-y-3" v-if="settings && settings.length">
      <div class="prose mt-3 p-2" v-if="preamble" v-html="preamble"></div>
      <p>
        The
        <code>{{ name }}</code> settings that are known to Meltano are documented below. To quickly
        find the setting you're looking for, click on any setting name from the list:
      </p>
      <ul class="list-disc list-inside pl-4">
        <li v-for="(setting, index) in definedSettings" v-bind:key="index">
          <a :href="setting.href"
            ><code>{{ setting.name }}</code></a
          >
        </li>
      </ul>
      <div v-if="sdkSettings.length > 0">
        <details>
          <summary class="text-xl pb-4 pt-4 font-bold font-hg">Expand To Show SDK Settings</summary>
          <ul class="list-disc list-inside pl-4">
            <li v-for="(setting, index) in sdkSettings" v-bind:key="index">
              <a :href="setting.href"
                ><code>{{ setting.name }}</code></a
              >
            </li>
          </ul>
        </details>
      </div>
      <p>
        You can also list these settings using
        <a href="https://docs.meltano.com/reference/command-line-interface#config">
          <pre class="inline-code-block"><code>meltano config</code></pre>
        </a>
        with the <code>list</code>
        subcommand:
      </p>
      <pre class="prose language-bash rounded-md"><code >meltano config {{ name }} list</code></pre>
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
      <span class="mt-6" v-for="(setting, index) in definedSettings" v-bind:key="index">
        <p class="mt-3 text-xl" :id="setting.name.replace(/\./g, '-') + '-setting'">
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
        <br />
        <p>Configure this setting directly using the following Meltano command:</p>
        <pre
          class="prose language-bash rounded-md"
        ><code >meltano config {{ name }} set {{ setting.name.replace(".", " ") }} [value]</code></pre>
      </span>

      <div v-if="sdkSettings.length > 0">
        <details :open="sdkSettings.some((setting) => setting.href === this.$route.hash)">
          <summary class="text-2xl pb-4 pt-4 font-bold font-hg">
            Expand To Show SDK Settings
          </summary>
          <span class="mt-6" v-for="(setting, index) in sdkSettings" v-bind:key="index">
            <p class="mt-3 text-xl" :id="setting.name.replace(/\./g, '-') + '-setting'">
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
            <br />
            <p>Configure this setting directly using the following Meltano command:</p>
            <pre
              class="prose language-bash rounded-md"
            ><code >meltano config {{ name }} set {{ setting.name.replace(".", " ") }} [value]</code></pre>
          </span>
        </details>
      </div>
    </span>
    <span v-else
      >This plugin currently has no settings defined. If you know the settings required by this
      plugin, <a href="#contribute">please contribute!</a></span
    >
  </div>
</template>

<script>
export default {
  name: "PluginSettingsSection",
  props: ["settings", "plugin_type_plural", "preamble", "name", "variant"],
  data() {
    return {
      hardcodedValues: [
        "stream_maps",
        "stream_map_config",
        "faker_config.locale",
        "faker_config.seed",
        "batch_config.encoding.compression",
        "batch_config.encoding.format",
        "batch_config.storage.prefix",
        "batch_config.storage.root",
        "flattening_enabled",
        "flattening_max_depth",
        "default_target_schema",
        "add_record_metadata",
        "hard_delete",
        "validate_records",
        "load_method",
      ],
    };
  },
  computed: {
    $settingsWithHref() {
      return this.settings.map((setting) => ({
        ...setting,
        href: `#${setting.name.replace(/\./g, "-")}-setting`,
      }));
    },
    $isSdkPlugin() {
      return this.$page.plugins.keywords.includes("meltano_sdk");
    },
    definedSettings() {
      return this.$isSdkPlugin
        ? this.$settingsWithHref.filter((setting) => !this.hardcodedValues.includes(setting.name))
        : this.$settingsWithHref;
    },
    sdkSettings() {
      return this.$isSdkPlugin
        ? this.$settingsWithHref.filter((setting) => this.hardcodedValues.includes(setting.name))
        : [];
    },
  },
};
</script>

<style></style>
