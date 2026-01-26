<script setup lang="ts">
import { ref, computed } from 'vue';

interface PluginNode {
  id: string;
  name: string;
  label: string;
  description?: string;
  path: string;
  logo_url?: string;
  pluginType: string;
  pluginTypePlural: string;
  keywords?: string[];
}

interface Props {
  plugins: PluginNode[];
}

const props = defineProps<Props>();

const search = ref('');
const searchFocused = ref(false);
const hoveringOnSearchOptions = ref(false);
const searchBarRef = ref<HTMLInputElement | null>(null);

const searchResults = computed(() => {
  if (!search.value.trim()) return [];

  const searchTerms = search.value.toLowerCase().trim().split(' ');

  return props.plugins
    .filter((plugin) => {
      const pluginTextFields = [
        plugin.name,
        plugin.name.replace(/-/g, ' '),
        plugin.description || '',
        plugin.label,
        plugin.keywords?.join(' ') || '',
      ];
      const searchIn = pluginTextFields.join(' ').toLowerCase();
      return searchTerms.every((term) => searchIn.includes(term));
    })
    .sort((a, b) => {
      const typeCompare = a.pluginType.localeCompare(b.pluginType);
      if (typeCompare !== 0) return typeCompare;
      return a.name.localeCompare(b.name);
    });
});

function handleResultClick() {
  hoveringOnSearchOptions.value = false;
  searchFocused.value = false;
  search.value = '';
}

function getLogoPath(plugin: PluginNode): string {
  if (plugin.logo_url) {
    return plugin.logo_url;
  }
  return `/assets/logos/${plugin.pluginTypePlural}/${plugin.name}.png`;
}

function getPluginPath(plugin: PluginNode): string {
  return plugin.path.split('--')[0];
}
</script>

<template>
  <div class="relative">
    <input
      type="text"
      name="search"
      id="search"
      placeholder="Search 600+ connectors and tools"
      class="search-bar text-black text-sm bg-transparent pl-4 border-solid border-blue border rounded-[9999px] py-1.5 w-full placeholder:text-par placeholder:font-light font-ibm focus-visible:outline-0"
      ref="searchBarRef"
      v-model="search"
      @focus="searchFocused = true"
      @blur="searchFocused = false"
    />
    <div class="absolute right-2 top-1/4">
      <svg
        class="w-6 block mt-0.5"
        width="12"
        height="15"
        viewBox="0 0 12 15"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          fill-rule="evenodd"
          clip-rule="evenodd"
          d="M10 6.59998C10 8.80911 8.20914 10.6 6 10.6C3.79086 10.6 2 8.80911 2 6.59998C2 4.39084 3.79086 2.59998 6 2.59998C8.20914 2.59998 10 4.39084 10 6.59998ZM8.38157 12.1087C7.65149 12.4248 6.8462 12.6 6 12.6C2.68629 12.6 0 9.91368 0 6.59998C0 3.28627 2.68629 0.599976 6 0.599976C9.31371 0.599976 12 3.28627 12 6.59998C12 8.34688 11.2534 9.91942 10.062 11.0159L11.4 12.8C11.7314 13.2418 11.6418 13.8686 11.2 14.2C10.7582 14.5313 10.1314 14.4418 9.8 14L8.38157 12.1087Z"
          fill="#080216"
        />
      </svg>
    </div>
    <Transition
      enter-active-class="transition duration-200 transform ease-custom"
      enter-from-class="scale-y-0 -translate-y-1/2 opacity-0"
      enter-to-class="scale-y-100 translate-y-0 opacity-100"
      leave-active-class="transition duration-300 transform ease-custom"
      leave-from-class="scale-y-100 translate-y-0 opacity-100"
      leave-to-class="scale-y-0 -translate-y-1/2 opacity-0"
    >
      <div
        class="absolute z-40 grid w-full grid-cols-1 py-2 mx-auto mt-12 overflow-y-auto shadow-lg max-h-96 justify-self-center grid-span-1 bg-slate-100"
        v-if="search !== '' && (searchFocused || hoveringOnSearchOptions)"
      >
        <div
          v-if="searchResults.length > 0"
          class="grid w-full grid-cols-1 gap-2 px-3 rounded grid-span-1 justify-self-center"
        >
          <div
            v-for="plugin in searchResults.slice(0, 10)"
            :key="plugin.id || plugin.name"
            class="grid w-full grid-cols-1 grid-span-1 place-self-start"
            @mouseover="hoveringOnSearchOptions = true"
            @mouseleave="hoveringOnSearchOptions = false"
            @click="handleResultClick"
          >
            <a
              :href="getPluginPath(plugin)"
              class="grid w-full h-full grid-cols-12 bg-white rounded align-self-center hover:bg-slate-200"
            >
              <div class="grid h-full col-span-3 p-4 place-items-center">
                <img
                  v-if="plugin.logo_url"
                  :src="getLogoPath(plugin)"
                  :alt="plugin.label"
                  class="max-w-[75px] max-h-[50px] object-contain"
                />
              </div>
              <div class="grid col-span-9 grid-rows-3 p-3 align-items-center">
                <div class="flex pt-1 space-x-3">
                  <p class="text-lg font-bold text-black underline place-self-center">
                    {{ plugin.label }}
                  </p>
                  <div class="place-self-center">
                    <span
                      class="px-2 py-1 text-sm text-center rounded-lg bg-sky-100 place-self-center"
                    >
                      {{ plugin.pluginType }}
                    </span>
                  </div>
                </div>
                <span class="text-black">{{ plugin.description || 'No description' }}</span>
              </div>
            </a>
          </div>
        </div>

        <div v-else class="block px-2">
          <a
            href="https://github.com/MeltanoLabs/Singer-Most-Wanted"
            class="flex items-center w-full bg-white rounded-md"
            target="_blank"
            rel="noopener noreferrer"
          >
            <svg class="h-4 ml-4" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <polyline points="15,3 21,3 21,9" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <line x1="10" y1="14" x2="21" y2="3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <p class="p-4 text-amber-800 hover:text-amber-700">
              Don't see the connector you're looking for? Open an issue to let us know.
            </p>
          </a>
        </div>
      </div>
    </Transition>
  </div>
</template>

<style scoped>
.search-bar {
  position: relative;
}
</style>
