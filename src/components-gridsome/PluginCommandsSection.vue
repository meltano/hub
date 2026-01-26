<template>
  <div v-if="commands?.length">
    <p class="text-3xl pb-4 pt-8 font-bold" id="commands">Commands</p>
    <span
      >The {{ name }} {{ plugin_type }} supports the following commands that can be used with
      <pre><code>meltano invoke</code></pre>
      :</span
    >
    <div v-for="(command, key, index) in commands" v-bind:key="index">
      <p class="mt-3 text-xl" :id="command.name + '-command'">
        <code>{{ command.name }}</code>
      </p>
      <ul class="list-inside list-disc pl-4 text-sm">
        <li>
          Equivalent to:
          <code>{{ command.args }}</code>
        </li>
      </ul>
      <p>{{ command.description }}</p>
      <pre
        class="prose language-bash rounded-md"
      ><code>meltano invoke {{ name }}:{{ command.name }} [args...]</code></pre>
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
span > pre {
  display: inline-block;
}
</style>
