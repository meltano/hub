<template>
  <div v-if="commands">
    <p class="text-3xl py-4" id="commands">Commands</p>
    <span
      >The {{ name }} {{ plugin_type }} supports the following commands that can be used with
      <pre><code>meltano invoke</code></pre>
      :</span
    >
    <div v-for="(value, key, index) in commands" v-bind:key="index">
      <span v-if="value">
        <h3>
          <pre><code>{{ value.name }}</code></pre>
        </h3>
        <span
          >Equivalent to:
          <pre><code>{{ value.args }}</code></pre>
        </span>
        <p>{{ value.description }}</p>
        <h3>How to use</h3>
        <span
          >Run this command using
          <pre><code>meltano invoke</code></pre>
        </span>
        <pre><code>meltano invoke {{ name }}:thing-to-do [additional arguments...]</code></pre>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: "PluginCommandsSection",
  props: ["commands", "name", "plugin_type"],
};
</script>

<style>
pre {
  display: inline-block;
}
</style>
