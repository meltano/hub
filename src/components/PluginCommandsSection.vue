<script setup lang="ts">
interface Command {
  name: string;
  args: string;
  description?: string;
}

interface Props {
  commands: Command[];
  name: string;
  pluginType: string;
}

defineProps<Props>();
</script>

<template>
  <div v-if="commands?.length">
    <p class="text-3xl pb-4 pt-8 font-bold" id="commands">Commands</p>
    <span
      >The {{ name }} {{ pluginType }} supports the following commands that can be used with
      <pre class="inline"><code>meltano invoke</code></pre>
      :</span
    >
    <div v-for="(command, index) in commands" :key="index">
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

<style scoped>
span > pre {
  display: inline-block;
}
</style>
