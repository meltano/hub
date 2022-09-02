<template>
  <div>
    <h2 id="settings">Settings</h2>
    <span v-if="settings">
      <p>
        The
        <code>{{ name }}</code> settings that are known to Meltano are documented below. To quickly
        find the setting you're looking for, click on any setting name from the list:
      </p>
      <ul>
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
        MeltanoHub by making a
        <a href="#contributing">pull request to the YAML file</a>.
      </p>
      <span v-for="(setting, index) in settings" v-bind:key="index">
        <h3 :id="setting.name + '-setting'">
          <code>{{ setting.label }} ({{ setting.name }})</code>
        </h3>
        <p>
          <span v-if="setting.description">{{ setting.description }}</span>
          <span v-else><a href="#contribute">[No description provided.]</a></span>
        </p>
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
  props: ["settings", "name"],
};
</script>

<style></style>
