<script setup lang="ts">
interface Props {
  capabilities: string[];
  name: string;
  pluginType: string;
}

defineProps<Props>();
</script>

<template>
  <div>
    <p class="text-3xl pb-4 pt-8 font-bold font-hg" id="capabilities">Capabilities</p>
    <span class="space-y-3" v-if="capabilities && capabilities.length">
      <p>
        The current capabilities for
        <code>{{ name }}</code>
        may have been automatically set when originally added to the Hub. Please review the
        capabilities when using this {{ pluginType }}. If you find they are out of date, please
        consider updating them by making a pull request to the YAML file that defines the
        capabilities for this {{ pluginType }}.
      </p>
      <p>This plugin has the following capabilities:</p>
      <ul class="list-disc list-inside pl-4">
        <li v-for="(capability, index) in capabilities" :key="index">
          {{ capability }}
        </li>
      </ul>
      <p>
        You can
        <a
          href="https://docs.meltano.com/guide/configuration#overriding-discoverable-plugin-properties"
          >override these capabilities or specify additional ones</a
        >
        in your <code>meltano.yml</code> by adding the <code>capabilities</code> key.
      </p>
    </span>
    <span v-else
      >This plugin currently has no capabilities defined. If you know the capabilities required by
      this plugin, <a href="#contribute">please contribute!</a></span
    >
  </div>
</template>
