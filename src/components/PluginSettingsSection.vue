<template>
  <div>
    <p class="text-3xl py-4" id="settings">Settings</p>
    <span class="space-y-3" v-if="settings">
      <div class="prose mt-3 p-2" v-if="preamble" v-html="preamble"></div>
      <p>
        The
        <code>{{ name }}</code> settings that are known to Meltano are documented below. To quickly
        find the setting you're looking for, click on any setting name from the list:
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
      <p class="text-3xl py-4" id="configuration">Configuration</p>
      <p>
        Settings for <code>{{ name }}</code> can be
        <a
          href="https://docs.meltano.com/reference/command-line-interface#config"
          >configured</a
        >
        by running:
      </p>
      <p><pre class="prose language-bash rounded-md"
        ><code>meltano config {{ name }} set --interactive</code
        ></pre></p>
      <p>
        Settings can also be configured using
        <a
          href="https://docs.meltano.com/guide/configuration#configuring-settings"
          >environment variables</a
        >.
      </p>
      <span v-for="(setting, index) in settings" v-bind:key="index">
        <p class="text-xl mt-3" :id="setting.name + '-setting'">
          <code>{{ setting.label }} ({{ setting.name }})</code>
        </p>
        <div
          class="prose bg-slate-100 p-2"
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
</template>

<script>
export default {
  name: "PluginSettingsSection",
  props: ["settings", "plugin_type_plural", "preamble", "name", "variant"],
};
</script>

<style></style>
