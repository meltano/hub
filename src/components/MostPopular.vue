<script setup lang="ts">
import { ref, computed } from 'vue';

interface PluginMetrics {
  all_projects?: number;
  all_execs?: number;
  ALL_EXECS_PERCENTILE?: number;
  ALL_PROJECTS_PERCENTILE?: number;
  WEIGHT?: number;
}

interface Plugin {
  id?: string;
  name: string;
  label: string;
  path: string;
  logo_url?: string;
  metrics?: PluginMetrics;
}

interface Props {
  plugins: Plugin[];
  title?: string;
  count?: number;
}

const props = withDefaults(defineProps<Props>(), {
  title: 'Most Popular',
  count: 8,
});

const expanded = ref(true);

function toggleContent() {
  expanded.value = !expanded.value;
}

const chevronClass = computed(() => {
  return expanded.value
    ? 'relative bottom-1 transform rotate-180 transition-transform duration-300'
    : 'relative bottom-1 transition-transform duration-300';
});

function percentile(x: number, arr: number[]): number {
  const sorted = [...arr].sort((a, b) => a - b);
  const index = sorted.indexOf(x);
  const p = (100 * index) / (sorted.length - 1);
  return Math.ceil(p);
}

const processedPlugins = computed(() => {
  const allExecsValues = props.plugins.map((p) => p.metrics?.all_execs ?? 0);
  const allProjectsValues = props.plugins.map((p) => p.metrics?.all_projects ?? 0);
  const projectWeightFactor = 2;

  return props.plugins
    .map((plugin) => {
      const thisExecs = plugin.metrics?.all_execs ?? 0;
      const thisProjects = plugin.metrics?.all_projects ?? 0;
      const allExecsPercentile = percentile(thisExecs, allExecsValues);
      const allProjectsPercentile = percentile(thisProjects, allProjectsValues);
      const weight = allExecsPercentile + allProjectsPercentile * projectWeightFactor;

      return {
        ...plugin,
        metrics: {
          ...plugin.metrics,
          ALL_EXECS_PERCENTILE: allExecsPercentile,
          ALL_PROJECTS_PERCENTILE: allProjectsPercentile,
          WEIGHT: weight,
        },
      };
    })
    .sort((a, b) => (b.metrics?.WEIGHT ?? 0) - (a.metrics?.WEIGHT ?? 0))
    .slice(0, props.count);
});

function getPluginPath(plugin: Plugin): string {
  return plugin.path.split('--')[0];
}

function getLogoUrl(plugin: Plugin): string | null {
  if (!plugin.logo_url) return null;
  return plugin.logo_url;
}
</script>

<template>
  <div class="w-full md:m-4" role="list">
    <div class="px-4 pt-2 mx-4 border rounded-lg bg-white-fade border-white-70">
      <div class="flex flex-col">
        <div class="flex items-center justify-center w-full px-4">
          <h2 class="text-xl font-bold text-center md:text-2xl font-pjs text-purple">
            {{ title }}
          </h2>
          <button
            @click="toggleContent"
            class="relative focus:outline-none text-purple top-[5px]"
            :aria-expanded="expanded"
          >
            <svg
              :class="chevronClass"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20"
              fill="currentColor"
              width="24"
              height="24"
            >
              <path
                fill-rule="evenodd"
                d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                clip-rule="evenodd"
              />
            </svg>
          </button>
        </div>
        <div class="grid grid-cols-2 gap-4 pb-6 mt-4 md:grid-cols-4" v-if="expanded">
          <div
            v-for="plugin in processedPlugins"
            :key="plugin.name"
            class="p-2 overflow-hidden border rounded-md text-slate-800 hover:bg-white bg-white-07 md:p-4 border-purple/10"
          >
            <a
              class="grid w-full grid-rows-2 gap-2 align-self-center place-items-center"
              :href="getPluginPath(plugin)"
            >
              <div class="block w-full row-span-4 text-center bg-white">
                <img
                  v-if="getLogoUrl(plugin)"
                  :src="getLogoUrl(plugin)!"
                  :alt="plugin.label"
                  class="py-2 mx-auto max-w-[175px] max-h-[24px] object-contain"
                />
              </div>
              <div class="grid content-end self-stretch">
                <p class="text-xs font-bold text-center lg:text-sm text-clip">
                  {{ plugin.label }}
                </p>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
