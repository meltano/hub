<script setup lang="ts">
import { ref, computed } from 'vue';
import PluginSidebar from './PluginSidebar.vue';
import PluginSettingsSection from './PluginSettingsSection.vue';
import PluginCapabilitiesSection from './PluginCapabilitiesSection.vue';
import PluginCommandsSection from './PluginCommandsSection.vue';
import PluginHelpSection from './PluginHelpSection.vue';
import PluginPrereqSection from './PluginPrereqSection.vue';

interface PluginSetting {
  name: string;
  label?: string;
  description?: string;
  description_rendered?: string;
  kind?: string;
  placeholder?: string;
  value?: string;
}

interface PluginCommand {
  name: string;
  executable?: string;
  args?: string;
  description?: string;
}

interface Maintainer {
  name: string;
  label: string;
  url: string;
}

interface Plugin {
  name: string;
  variant: string;
  label?: string;
  description?: string;
  definition?: string;
  definition_rendered?: string;
  path: string;
  logo_url?: string;
  domain_url?: string;
  repo: string;
  ext_repo?: string;
  pip_url?: string;
  pluginType: string;
  pluginTypePlural: string;
  isDefault: boolean;
  hidden?: boolean;
  quality?: string;
  maintenance_status?: string;
  keywords?: string[];
  capabilities?: string[];
  settings?: PluginSetting[];
  settings_preamble_rendered?: string;
  commands?: PluginCommand[];
  usage?: string;
  usage_rendered?: string;
  prereq?: string;
  prereq_rendered?: string;
  next_steps?: string;
  next_steps_rendered?: string;
  metrics?: {
    all_projects?: number;
    all_execs?: number;
  };
  maintainer?: Maintainer;
  airbyte_name?: string;
}

interface ParsedRepo {
  url: string;
  type: string;
  user: string;
  name: string;
}

interface Props {
  plugin: Plugin;
  variants: Plugin[];
  parsedRepo: ParsedRepo;
}

const props = defineProps<Props>();
const activeTab = ref<'modern' | 'legacy'>('modern');

const filteredVariants = computed(() => {
  return props.variants.filter((v) => v.pluginType === props.plugin.pluginType);
});

const parsedVariantRepos = computed(() => {
  return filteredVariants.value.reduce(
    (acc, variant) => {
      acc[variant.variant] = parseRepoUrl(variant.repo);
      return acc;
    },
    {} as Record<string, ParsedRepo>
  );
});

function parseRepoUrl(repoUrl: string): ParsedRepo {
  const parts = repoUrl.split('/').slice(3);
  const [user, name] = parts;
  return {
    url: repoUrl,
    type: repoUrl.includes('github.com')
      ? 'github'
      : repoUrl.includes('gitlab.com')
        ? 'gitlab'
        : repoUrl.includes('bitbucket.org')
          ? 'bitbucket'
          : '',
    user: user || '',
    name: name || '',
  };
}

function getLogoPath(): string | null {
  if (!props.plugin.logo_url) return null;
  return props.plugin.logo_url;
}

function getVariantPath(variant: Plugin): string {
  return variant.path;
}

function getLastCommitBadgeUrl(variant: Plugin): string {
  const repo = parsedVariantRepos.value[variant.variant];
  const url = `https://img.shields.io/${repo.type}/last-commit/${repo.user}/${repo.name}?label=Last%20Commit`;

  if (!variant.keywords?.includes('airbyte_protocol')) {
    return url;
  }

  const pathMatch = repo.url.match(/airbyte-integrations\S+/);
  return pathMatch ? `${url}&path=${pathMatch[0]}` : url;
}
</script>

<template>
  <div class="w-full px-4 mx-auto single-plugin-overview max-w-7xl">
    <div class="single-plugin-detail">
      <div class="single-plugin-top-bar">
        <table>
          <tr>
            <td class="p-5 lg:p-9">
              <a
                v-if="plugin.domain_url"
                :href="plugin.domain_url"
                target="_blank"
                class="flex justify-center w-24 h-24 bg-white lg:w-48 lg:h-48"
                rel="noopener noreferrer"
              >
                <img
                  v-if="getLogoPath()"
                  :src="getLogoPath()!"
                  :alt="plugin.label || plugin.name"
                  class="object-contain max-w-[250px] max-h-[200px]"
                />
              </a>
              <div v-else>
                <img
                  v-if="getLogoPath()"
                  :src="getLogoPath()!"
                  :alt="plugin.label || plugin.name"
                  class="object-contain max-w-[250px] max-h-[200px]"
                />
              </div>
            </td>
            <td>
              <p class="pt-6 pb-4 text-3xl font-bold lg:text-5xl lg:pt-8 lg:pb-6 font-pjs text-purple">
                {{ plugin.label }}
              </p>
              <p class="text-lg">
                <code>{{ plugin.name }} ({{ plugin.variant }} variant)</code>
                <span v-if="plugin.quality === 'gold'">
                  <a href="https://docs.meltano.com/contribute/connectors#connector-quality-matrix">🥇</a>
                </span>
                <span v-if="plugin.quality === 'silver'">
                  <a href="https://docs.meltano.com/contribute/connectors#connector-quality-matrix">🥈</a>
                </span>
                <span v-if="plugin.quality === 'bronze'">
                  <a href="https://docs.meltano.com/contribute/connectors#connector-quality-matrix">🥉</a>
                </span>
              </p>
              <p>
                <b class="font-hg">{{ plugin.description }}</b>
              </p>
            </td>
          </tr>
        </table>
      </div>

      <div class="w-full">
        <div class="flex flex-col-reverse -mx-2 lg:flex-row">
          <div class="w-full px-2 mt-4 lg:w-8/12 lg:mt-0">
            <div class="p-5 content-body">
              <div class="max-w-2xl p-4 rounded xl:max-w-3xl inner-body">
                <p>
                  The {{ plugin.name }}
                  <a
                    :href="'https://docs.meltano.com/concepts/plugins#' + plugin.pluginTypePlural"
                  >{{ plugin.pluginType }}</a>

                  <span v-if="plugin.pluginType === 'extractor'">
                    pulls data from
                    <a :href="plugin.domain_url">{{ plugin.label }}</a> that can
                    then be sent to a destination using a
                    <a href="/loaders">loader</a>.
                  </span>

                  <span v-if="plugin.hidden === true">
                    <p class="pt-8 pb-4 text-3xl font-bold" id="hidden-warning">
                      This plugin is deprecated and not recommended for use. Please use another
                      variant.
                    </p>
                  </span>

                  <span
                    v-if="plugin.pluginType === 'extractor' && plugin.keywords?.includes('airbyte_protocol')"
                  >
                    <p class="pt-8 pb-4 text-3xl font-bold" id="airbyte-preview">
                      Airbyte Usage Notice
                    </p>
                    This connector uses
                    <a href="https://github.com/meltanolabs/tap-airbyte-wrapper">tap-airbyte-wrapper</a>
                    to call the underlying Airbyte source Docker container. This means
                    <i>you must</i> have <a href="https://www.docker.com/">Docker</a> installed
                    and running prior to usage.
                  </span>

                  <span
                    class="prose"
                    v-if="plugin.pluginType === 'extractor'"
                    v-html="plugin.definition_rendered"
                  ></span>

                  <span v-if="plugin.pluginType === 'loader'">
                    sends data into
                    <a :href="plugin.domain_url">{{ plugin.label }}</a>
                    after it was pulled from a source using an
                    <a href="/extractors">extractor</a>
                  </span>

                  <span v-if="plugin.pluginType === 'transformer'">
                    is a plugin for running SQL-based transformations on data stored in your
                    warehouse.
                  </span>

                  <span v-if="plugin.pluginType === 'orchestrator'">
                    allows for workflows to be programmatically authored, scheduled, and
                    monitored.
                  </span>

                  <span
                    class="prose"
                    v-if="plugin.pluginType === 'utility'"
                    v-html="plugin.definition_rendered"
                  ></span>

                  <span
                    class="prose"
                    v-if="plugin.pluginType === 'file'"
                    v-html="plugin.definition_rendered"
                  ></span>

                  <span v-if="plugin.pluginType === 'mapper'">
                    is a plugin for transforming data between an extractor and a loader. Commonly
                    used for obfuscating, filtering, or removing sensitive data from streams.
                  </span>
                </p>

                <!-- Alternate Implementations -->
                <span class="space-y-3" v-if="filteredVariants && filteredVariants.length > 1">
                  <p class="text-2xl">Alternate Implementations</p>
                  <ul class="pl-4 list-disc list-inside">
                    <li v-for="variant in filteredVariants" :key="variant.variant">
                      <a
                        class="tooltip"
                        :href="getVariantPath(variant)"
                        v-if="variant.path !== plugin.path"
                      >
                        {{ variant.maintainer?.label || variant.variant }}
                        <div class="tooltip-content">
                          <img
                            alt="Last Commit Date"
                            :src="getLastCommitBadgeUrl(variant)"
                          />
                        </div>
                      </a>
                      <span v-else>{{ variant.maintainer?.label || variant.variant }}</span>
                      <span v-if="variant.isDefault"> (default)</span>
                      <span v-if="variant.keywords?.includes('meltano_sdk')">
                        <img
                          class="inline pl-2"
                          alt="Built with the Meltano SDK"
                          src="https://img.shields.io/badge/-Meltano%20SDK-blueviolet"
                        />
                      </span>
                      <span v-if="variant.quality === 'gold'">
                        <a href="https://docs.meltano.com/contribute/connectors#connector-quality-matrix">🥇</a>
                      </span>
                      <span v-if="variant.quality === 'silver'">
                        <a href="https://docs.meltano.com/contribute/connectors#connector-quality-matrix">🥈</a>
                      </span>
                      <span v-if="variant.quality === 'bronze'">
                        <a href="https://docs.meltano.com/contribute/connectors#connector-quality-matrix">🥉</a>
                      </span>
                    </li>
                  </ul>
                </span>

                <!-- Getting Started -->
                <div>
                  <p class="pt-8 pb-4 text-3xl font-bold font-hg" id="getting-started">
                    Getting Started
                  </p>
                  <PluginPrereqSection
                    :prereq="plugin.prereq"
                    :prereq-rendered="plugin.prereq_rendered"
                    :plugin-type="plugin.pluginType"
                  />
                  <p class="py-3 text-xl" id="installation">Installation and configuration</p>
                  <ol class="pl-4 list-decimal list-inside">
                    <li>
                      Add the {{ plugin.name }} {{ plugin.pluginType }} to your
                      project using
                      <a href="https://docs.meltano.com/reference/command-line-interface#add">
                        <pre class="inline-code-block"><code>meltano add</code></pre>
                      </a>
                      :
                    </li>
                    <div class="space-y-2">
                      <div class="flex border-b border-gray-200">
                        <button
                          @click="activeTab = 'modern'"
                          :class="[
                            'px-4 py-2 text-sm font-medium border-b-2 transition-colors',
                            activeTab === 'modern'
                              ? 'border-blue-500 text-blue-600'
                              : 'border-transparent text-gray-500 hover:text-gray-700',
                          ]"
                        >
                          Meltano 3.8+
                        </button>
                        <button
                          @click="activeTab = 'legacy'"
                          :class="[
                            'px-4 py-2 text-sm font-medium border-b-2 transition-colors',
                            activeTab === 'legacy'
                              ? 'border-blue-500 text-blue-600'
                              : 'border-transparent text-gray-500 hover:text-gray-700',
                          ]"
                        >
                          Legacy (All versions)
                        </button>
                      </div>
                      <div v-if="activeTab === 'legacy'">
                        <pre class="prose rounded-md language-bash"><code>meltano add {{ plugin.pluginType }} {{ plugin.name }}<span v-if="!plugin.isDefault"> --variant {{ plugin.variant }}</span></code></pre>
                      </div>
                      <div v-if="activeTab === 'modern'">
                        <pre class="prose rounded-md language-bash"><code>meltano add <span v-if="['extractor', 'loader', 'utility'].includes(plugin.pluginType)">{{ plugin.name }}</span><span v-else>--plugin-type {{ plugin.pluginType }} {{ plugin.name }}</span><span v-if="!plugin.isDefault"> --variant {{ plugin.variant }}</span></code></pre>
                      </div>
                    </div>
                    <span>
                      <li>
                        Configure the {{ plugin.name }}
                        <a href="#settings">settings</a> using
                        <a href="https://docs.meltano.com/reference/command-line-interface#config">
                          <pre class="inline-code-block"><code>meltano config</code></pre>
                        </a>
                        :
                      </li>
                      <pre class="prose rounded-md language-bash"><code>meltano config {{ plugin.name }} set --interactive</code></pre>
                    </span>
                    <span v-if="plugin.pluginType === 'extractor'">
                      <li>
                        Test that extractor settings are valid using
                        <a href="https://docs.meltano.com/reference/command-line-interface#config">
                          <pre class="inline-code-block"><code>meltano config</code></pre>
                        </a>
                        :
                      </li>
                      <pre class="prose rounded-md language-bash"><code>meltano config {{ plugin.name }} test</code></pre>
                    </span>
                  </ol>
                  <p class="py-3 text-xl">Next steps</p>
                  <div
                    v-if="plugin.next_steps_rendered"
                    v-html="plugin.next_steps_rendered"
                    class="prose"
                  ></div>
                  <!-- Default next steps for extractors -->
                  <div v-else-if="plugin.pluginType === 'extractor'">
                    <p>
                      Follow the remaining steps of the
                      <a href="https://docs.meltano.com/getting-started/part1">Getting Started guide</a>:
                    </p>
                    <ol class="pl-4 list-decimal list-inside">
                      <li>
                        <a href="https://docs.meltano.com/getting-started/part1#select-entities-and-attributes-to-extract">
                          Select entities and attributes to extract
                        </a>
                      </li>
                      <li>
                        <a href="https://docs.meltano.com/getting-started/part2">
                          Add a loader to send data to a destination
                        </a>
                      </li>
                      <li>
                        <a href="https://docs.meltano.com/getting-started/part2#run-your-data-integration-el-pipeline">
                          Run a data integration (EL) pipeline
                        </a>
                      </li>
                    </ol>
                  </div>
                  <!-- Default next steps for loaders -->
                  <div v-else-if="plugin.pluginType === 'loader'">
                    <p>
                      Follow the remaining steps of the
                      <a href="https://docs.meltano.com/getting-started/part1">Getting Started guide</a>:
                    </p>
                    <ol class="pl-4 list-decimal list-inside">
                      <li>
                        <a href="https://docs.meltano.com/getting-started/part2#run-your-data-integration-el-pipeline">
                          Run a data integration (EL) pipeline
                        </a>
                      </li>
                    </ol>
                  </div>
                  <!-- Default next steps for transformers -->
                  <div v-else-if="plugin.pluginType === 'transformer'">
                    <p>
                      Follow the remaining steps of the
                      <a href="https://docs.meltano.com/getting-started/part3">Getting Started guide</a>:
                    </p>
                    <ol class="pl-4 list-decimal list-inside">
                      <li>
                        <a href="https://docs.meltano.com/getting-started/part3">
                          Transform loaded data for analysis
                        </a>
                      </li>
                    </ol>
                  </div>
                  <!-- Default next steps for mappers -->
                  <div v-else-if="plugin.pluginType === 'mapper'">
                    <p>
                      Follow the remaining steps of the
                      <a href="https://docs.meltano.com/getting-started/part4">Getting Started guide</a>:
                    </p>
                    <ol class="pl-4 list-decimal list-inside">
                      <li>
                        <a href="https://docs.meltano.com/getting-started/part4">Inline Data Mapping</a>
                      </li>
                      <li>
                        See the
                        <a href="https://docs.meltano.com/guide/mappers">mappers documentation</a>
                        or the plugin repo's README.md for more details on configuration.
                      </li>
                    </ol>
                  </div>
                  <p>
                    If you run into any issues,
                    <a href="#looking-for-help">learn how to get help</a>.
                  </p>
                </div>

                <!-- Plugin sections -->
                <div>
                  <PluginCapabilitiesSection
                    :capabilities="plugin.capabilities || []"
                    :name="plugin.name"
                    :plugin-type="plugin.pluginType"
                  />
                  <PluginSettingsSection
                    :settings="plugin.settings || []"
                    :name="plugin.name"
                    :plugin-type-plural="plugin.pluginTypePlural"
                    :variant="plugin.variant"
                    :preamble="plugin.settings_preamble_rendered"
                    :is-sdk-plugin="(plugin.keywords || []).includes('meltano_sdk')"
                  />
                  <PluginCommandsSection
                    :commands="plugin.commands || []"
                    :name="plugin.name"
                    :plugin-type="plugin.pluginType"
                  />
                  <div
                    class="p-2 mt-3 prose"
                    v-if="plugin.usage"
                    v-html="plugin.usage_rendered"
                  ></div>
                  <PluginHelpSection
                    :name="plugin.name"
                    :variant="plugin.variant"
                    :repo="plugin.repo"
                    :plugin-type="plugin.pluginType"
                    :plugin-type-plural="plugin.pluginTypePlural"
                    :is-airbyte-protocol="(plugin.keywords || []).includes('airbyte_protocol')"
                  />
                </div>
              </div>
            </div>
          </div>
          <PluginSidebar
            :name="plugin.name"
            :domain-url="plugin.domain_url"
            :repo="parsedRepo"
            :maintenance-status="plugin.maintenance_status || 'unknown'"
            :keywords="plugin.keywords || []"
            :variant="plugin.variant"
            :is-default="plugin.isDefault"
            :metrics="plugin.metrics"
            :plugin-type="plugin.pluginType"
            :maintainer="plugin.maintainer"
            :pip-url="plugin.pip_url"
            :airbyte-name="plugin.airbyte_name"
            :ext-repo="plugin.ext_repo"
          />
        </div>
      </div>
    </div>
  </div>
</template>
