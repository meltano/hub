<template>
  <div class="help-module">
    <p class="text-3xl py-4" id="contribute">Something missing?</p>
    <p>This page is generated from a YAML file that you can contribute changes to.</p>
    <a
      v-if="name"
      :href="`https://github.com/meltano/hub/blob/main/_data/meltano/${plugin_type}/${name}/${variant}.yml`"
      >Edit it on GitHub!</a
    >
    <p class="text-3xl py-4" id="looking-for-help">Looking for help?</p>
    <div>
      If you're having trouble getting the
      {{ name }} extractor to work, look for an
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
  props: ["name", "plugin_type", "variant", "repo"],
};
</script>

<style lang="scss">
.help-module {
  margin-bottom: 40px;
}
</style>
