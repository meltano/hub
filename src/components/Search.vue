<script setup>
import ExtractorIcon from "./icons-50/ExtractorIcon.vue";
import LoaderIcon from "./icons-50/LoaderIcon.vue";
import MapperV1Icon from "./icons-50/MapperV1Icon.vue";
import ToolIcon from "./icons-50/ToolIcon.vue";
</script>

<template>
  <div class="relative z-0">
    <div class="relative z-10">
      <input
        type="text"
        name="search"
        id="search"
        placeholder="Search 550+ connectors and tools"
        class="w-full h-10 py-3 pl-5 text-sm leading-none text-black bg-transparent search-bar placeholder:text-black placeholder:font-light font-ibm focus-visible:outline-0"
        ref="searchBar"
        :value="search"
        @input="search = $event.target.value"
        @focus="searchFocused = true"
        @blur="searchFocused = false"
        v-focus="searchFocused"
      />
      <div class="absolute mt-px right-3 top-1/4">
        <svg
          v-if="search === ''"
          class="hidden w-4 h-4 lg:block"
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
      <div v-if="search != ''" class="absolute right-3 top-1.5">
        <button @click="search = ''">
          <svg
            width="12"
            height="13"
            viewBox="0 0 12 13"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              clip-rule="evenodd"
              d="M11.7073 10.3762C12.0978 10.7667 12.0978 11.3999 11.7073 11.7904C11.3167 12.1809 10.6836 12.1809 10.2931 11.7904L6.41685 7.91419L2.5406 11.7904C2.15008 12.181 1.51691 12.181 1.12639 11.7904C0.735865 11.3999 0.735865 10.7668 1.12639 10.3762L5.00264 6.49998L1.12639 2.62373C0.735865 2.23321 0.735865 1.60004 1.12639 1.20952C1.51691 0.818995 2.15008 0.818995 2.5406 1.20952L6.41685 5.08577L10.2931 1.20956C10.6836 0.819035 11.3167 0.819035 11.7073 1.20956C12.0978 1.60008 12.0978 2.23325 11.7073 2.62377L7.83106 6.49998L11.7073 10.3762Z"
              fill="black"
            />
          </svg>
        </button>
      </div>
    </div>

    <div
      :class="[
        searchFocused || search ? 'bg-white border-blue-light' : 'border-blue ',
        search == '' ? '' : '',
        ,
        'absolute top-0 inset-x-0 pt-9 border duration-200 rounded-[20px] overflow-hidden',
      ]"
    >
      <!-- search results -->
      <div
        :class="[
          search == ''
            ? 'max-h-0 delay-0 overflow-hidden'
            : 'max-h-[560px] delay-0 overflow-scroll',
          ' transition-all  duration-200',
        ]"
      >
        <div v-for="(parent, index) in pluginResults" :key="index + 'item'" class="w-full">
          <div class="w-full px-5 py-4 bg-purple-lila/50">
            <div class="flex flex-row justify-between font-ibm">
              <div class="flex-1 w-auto">
                <div class="flex flex-row -mx-2">
                  <div class="px-2">
                    <component
                      v-if="parent.name === 'Extractor'"
                      class="w-6 h-6 duration-200 bg-white rounded-full group-hover:bg-blue group-hover:text-white"
                      :is="ExtractorIcon"
                    />
                    <component
                      v-if="parent.name === 'Loader'"
                      class="w-6 h-6 duration-200 bg-white rounded-full group-hover:bg-blue group-hover:text-white"
                      :is="LoaderIcon"
                    />
                    <component
                      v-if="parent.name === 'Mapper'"
                      class="w-6 h-6 duration-200 bg-white rounded-full group-hover:bg-blue group-hover:text-white"
                      :is="MapperV1Icon"
                    />
                    <component
                      v-if="parent.name === 'Tool'"
                      class="w-6 h-6 duration-200 bg-white rounded-full group-hover:bg-blue group-hover:text-white"
                      :is="ToolIcon"
                    />
                  </div>
                  <div class="px-2">{{ parent.pluginTypePlural }}</div>
                </div>
              </div>
              <div class="flex-none w-auto">
                <a href="" class="flex flex-row items-center group">
                  <span class="mr-2">See All </span>
                  <svg
                    class="duration-200 group-hover:translate-x-1"
                    width="7"
                    height="12"
                    viewBox="0 0 7 12"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M6 5.91663L1.5 10.5833"
                      stroke="black"
                      stroke-width="2"
                      stroke-linecap="round"
                    />
                    <path
                      d="M6 5.91663L1.5 1.41658"
                      stroke="black"
                      stroke-width="2"
                      stroke-linecap="round"
                    />
                  </svg>
                </a>
              </div>
            </div>
          </div>

          <div v-for="(plugin, index) in parent.nodes" :key="index + 'item'" class="w-full">
            <div
              :class="[
                index !== 0 ? 'border-purple-lila/50' : 'border-transparent',
                'w-full bg-white border-t px-5 py-4',
              ]"
            >
              <div class="flex flex-row items-center justify-start font-ibm">
                <div class="flex-none w-auto">
                  <div class="flex flex-row items-center -mx-2">
                    <div class="w-auto px-2">
                      <img
                        v-if="plugin.label === 'Microsoft Azure'"
                        :src="azure"
                        alt="azure"
                        class="w-6 h-6 mx-auto"
                      />

                      <img
                        v-if="plugin.label === 'Google Cloud Platform'"
                        :src="gc"
                        alt="azure"
                        class="w-6 h-6 mx-auto"
                      />
                    </div>
                    <div class="w-auto px-2">
                      <div
                        class="px-1 py-0.5 rounded flex flex-row group hover:text-purple text-black bg-purple-lila items-center group"
                      >
                        <div class="px-0.5">
                          <component
                            class="flex items-center justify-center w-5 h-5 rounded-full"
                            :is="VendorIcon"
                          />
                        </div>
                        <div class="px-0.5 text-sm">{{ plugin.name }}</div>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="flex-none w-auto px-2">
                  {{ plugin.label }}
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="w-full px-5 py-4 bg-white border-t border-purple-lila">
          <div class="flex flex-row items-center justify-start font-ibm">
            <div class="flex-none w-auto">
              <div class="flex flex-row items-center -mx-2">
                <div class="w-auto px-2">
                  <img :src="azure" alt="azure" class="w-6 h-6 mx-auto" />
                </div>
                <div class="w-auto px-2">
                  <div
                    class="px-1 py-0.5 rounded flex flex-row group hover:text-purple text-black bg-purple-lila items-center group"
                  >
                    <div class="px-0.5">
                      <component
                        class="flex items-center justify-center w-5 h-5 rounded-full"
                        :is="VendorIcon"
                      />
                    </div>
                    <div class="px-0.5 text-sm">Partner</div>
                  </div>
                </div>
              </div>
            </div>

            <div class="flex-none w-auto px-2">Microsoft Azure</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import gc from "../assets/images/extractors/gc.svg";
import azure from "../assets/images/extractors/azure.svg";

import VendorIcon from "./icons-50/VendorIcon.vue";

const searchResults = [
  {
    node: {
      id: 1,
      path: "/path--1",
      logo_url: gc,
      label: "Google Cloud Platform",
      pluginType: "Extractor",
      pluginTypePlural: "Extractors",
      name: "Partner",
      description: "This is the description for Plugin 1",
    },
  },
  {
    node: {
      id: 2,
      path: "/path--2",
      logo_url: azure,
      label: "Microsoft Azure",
      pluginType: "Extractor",
      pluginTypePlural: "Extractors",
      name: "Vendor",
      description: "This is the description for Plugin 2",
    },
  },
  {
    node: {
      id: 3,
      path: "/path--3",
      logo_url: gc,
      label: "Google Cloud Platform",
      pluginType: "Loader",
      pluginTypePlural: "Loaders",
      name: "Vendor",
      description: "This is the description for Plugin 3",
    },
  },
  {
    node: {
      id: 4,
      path: "/path--4",
      logo_url: azure,
      label: "Microsoft Azure",
      pluginType: "Loader",
      pluginTypePlural: "Loaders",
      name: "Partner",
      description: "This is the description for Plugin 4",
    },
  },
  {
    node: {
      id: 5,
      path: "/path--5",
      logo_url: gc,
      label: "Google Cloud Platform",
      pluginType: "Mapper",
      pluginTypePlural: "Mappers",
      name: "Vendor",
      description: "This is the description for Plugin 5",
    },
  },
  {
    node: {
      id: 6,
      path: "/path--6",
      logo_url: azure,
      label: "Microsoft Azure",
      pluginType: "Mapper",
      pluginTypePlural: "Mappers",
      name: "Partner",
      description: "This is the description for Plugin 6",
    },
  },
  {
    node: {
      id: 7,
      path: "/path--7",
      logo_url: gc,
      label: "Google Cloud Platform",
      pluginType: "Tool",
      pluginTypePlural: "Tools",
      name: "Partner",
      description: "This is the description for Plugin 7",
    },
  },
  {
    node: {
      id: 8,
      path: "/path--8",
      logo_url: azure,
      label: "Microsoft Azure",
      pluginType: "Extractor",
      pluginTypePlural: "Extractors",
      name: "Vendor",
      description: "This is the description for Plugin 8",
    },
  },
  {
    node: {
      id: 9,
      path: "/path--9",
      logo_url: gc,
      label: "Google Cloud Platform",
      pluginType: "Mapper",
      pluginTypePlural: "Mappers",
      name: "Partner",
      description: "This is the description for Plugin 9",
    },
  },
  {
    node: {
      id: 10,
      path: "/path--10",
      logo_url: azure,
      label: "Microsoft Azure",
      pluginType: "Loader",
      pluginTypePlural: "Loaders",
      name: "Vendor",
      description: "This is the description for Plugin 10",
    },
  },
];

export default {
  name: "SearchBar",
  data() {
    return {
      search: "",
      searchFocused: false,
      hoveringOnSearchOptions: false,
      searchResults,
    };
  },
  computed: {
    pluginResults() {
      const plugins = searchResults;
      const results = {};
      plugins.forEach((plugin) => {
        const { node } = plugin;
        const { pluginType, pluginTypePlural } = node;
        if (!results[pluginType]) {
          results[pluginType] = {
            name: pluginType,
            pluginTypePlural,
            nodes: [node],
          };
        } else {
          results[pluginType].nodes.push(node);
        }
      });
      return Object.values(results);
    },
  },
};
</script>
<!--
<static-query lang="graphql">
query {
  allPlugins(
    filter: {
      isDefault: { eq: true }
      hidden: { ne: true }
      pluginType: { nin: ["transform", "orchestrator", "transformer"] }
      name: {
        nin: [
          "files-airflow"
          "files-dbt-snowflake"
          "files-dbt-redshift"
          "files-dbt-postgres"
          "files-dbt-duckdb"
          "files-dbt-bigquery"
          "files-dbt"
        ]
      }
    }
  ) {
    edges {
      node {
        id
        description
        path
        label
        name
        logo_url
        pluginType
        pluginTypePlural
        keywords
      }
    }
  }
}
</static-query> -->

<style lang="scss">
.search-bar {
  position: relative;
  &::before {
    content: "";
    display: block;
    top: 10px;
    right: 10px;
    width: 14px;
    height: 14px;
    position: absolute;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
  }
}
.search {
  .results {
    box-shadow: 1px 2px 4px rgba(0, 0, 0, 0.3);
    position: absolute;
    width: 75%;
    align-content: left;
    margin-top: 80px;
    background: white;
    line-height: 1rem;

    .result-item {
      color: black;
      padding: 0.5rem;
      border-bottom: 2px solid black;

      a {
        text-decoration: none;
        display: flex;
        justify-content: space-between;
      }
    }
  }
}
</style>
