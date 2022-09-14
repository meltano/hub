<template>
  <div>
    <p class="text-3xl" id="prereqs">Prerequisites</p>
    <p>
      If you haven't already, follow the initial steps of the
      <a href="https://docs.meltano.com/getting-started.html">Getting Started guide</a>:
    </p>
    <ol>
      <li>
        <a href="https://docs.meltano.com/getting-started.html#install-meltano">Install Meltano</a>
      </li>
      <li>
        <a href="https://docs.meltano.com/getting-started.html#create-your-meltano-project"
          >Create your Meltano project</a
        >
      </li>
    </ol>
    <div v-if="plugin.prereq" v-html="plugin.prereq_rendered"></div>
  </div>
</template>

<script>
export default {
  name: "PluginPrereqSection",
  props: ["plugin", "plugin_type"],
};
</script>

<style></style>
