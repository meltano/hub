<template>
  <div>
    <p class="text-xl py-3" id="prereqs">Prerequisites</p>
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
</template>

<script>
export default {
  name: "PluginPrereqSection",
  props: ["plugin", "plugin_type"],
};
</script>
