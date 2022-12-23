<template>
  <div>
    <p class="text-3xl py-4" id="settings">Settings</p>
    <span class="space-y-3" v-if="settings && settings.length">
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
        <p>Configure this setting directly using the following Meltano command:</p>
        <pre class="prose language-bash rounded-md"><code >meltano config {{ name }} set {{ setting.name.replace(".", " ") }} [value]</code></pre>
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
