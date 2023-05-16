<template>
  <div class="help-module">
    <p class="text-3xl pb-4 pt-8 font-bold font-hg" id="contribute">Something missing?</p>
    <p>This page is generated from a YAML file that you can contribute changes to.</p>
    <a
      v-if="name"
      :href="`https://github.com/meltano/hub/blob/main/_data/meltano/${plugin_type_plural}/${name}/${variant}.yml`"
      >Edit it on GitHub!</a
    >
    <p class="text-3xl pb-4 pt-8 font-bold font-hg" id="looking-for-help">Looking for help?</p>
    <div v-if="$page.plugins.keywords.includes('airbyte_protocol')">
      If you're having trouble getting the
      {{ name }} {{ plugin_type }} to work, read the
      <a :href="`https://docs.meltano.com/guide/advanced-topics#airbyte-connector-integration-faq`"
        >Airbyte connector FAQ</a
      >, look for an
      <a :href="`https://github.com/airbytehq/airbyte/issues`"
        >existing issue in the Airbyte repository</a
      >, file a <a :href="`https://github.com/airbytehq/airbyte/issues/new`">new issue</a>, or
      <a href="https://meltano.com/slack">join the Meltano Slack community</a>
      and ask for help in the
      <pre class="inline-code-block"><code>#plugins-general</code></pre>
      channel.
    </div>
    <div v-if="!$page.plugins.keywords.includes('airbyte_protocol')">
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
</template>

<script>
export default {
  name: "PluginHelpSection",
  props: ["name", "plugin_type", "plugin_type_plural", "variant", "repo"],
};
</script>

<style lang="scss">
.help-module {
  margin-bottom: 40px;
}
</style>
