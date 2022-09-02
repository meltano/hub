<template>
  <div v-if="requires">
    <h3>Requires</h3>
    <p>This {{ plugin_type }} requires the following plugins and variants to work:</p>
    <ul>
      <li v-for="(file, index) in requires.files" v-bind:key="index">
        {{ file.name }} - {{ file.variant }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "PluginRequiresSection",
  props: ["requires", "plugin_type"],
};
</script>

<style></style>
