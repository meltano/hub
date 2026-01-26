<script setup lang="ts">
import { ref, computed } from 'vue';

interface Repo {
  type: string;
  url: string;
  user: string;
  name: string;
}

interface Maintainer {
  label: string;
  url: string;
}

interface Metrics {
  all_execs?: number;
  all_projects?: number;
}

interface Props {
  name: string;
  airbyteName?: string;
  domainUrl?: string;
  isDefault: boolean;
  repo: Repo;
  maintenanceStatus: string;
  keywords: string[];
  variant: string;
  pluginType: string;
  metrics?: Metrics;
  maintainer?: Maintainer;
  pipUrl?: string;
  extRepo?: string;
}

const props = defineProps<Props>();
const activeTab = ref<'modern' | 'legacy'>('modern');

const parsedEDKRepo = computed(() => {
  if (!props.extRepo) return { user: '', repo_name: '' };
  const urlParts = props.extRepo.split('/');
  return { user: urlParts[3], repo_name: urlParts[4] };
});

const repoEDKType = computed(() => {
  return props.extRepo?.includes('github.com') ? 'github' : 'gitlab';
});

const hasPyPI = computed(() => {
  return (
    props.pipUrl &&
    !(
      props.pipUrl.includes('git+') ||
      props.pipUrl.includes('//') ||
      props.pipUrl.includes('=') ||
      props.pipUrl.includes(' ') ||
      props.pipUrl.includes('[')
    )
  );
});

const isAirbyteProtocol = computed(() => (props.keywords ?? []).includes('airbyte_protocol'));
const isMeltanoSdk = computed(() => (props.keywords ?? []).includes('meltano_sdk'));
const showRepoStats = computed(() => !isAirbyteProtocol.value && props.repo.type !== 'bitbucket');
const isExtractorAirbyte = computed(
  () => props.pluginType === 'extractor' && isAirbyteProtocol.value
);

function getAirbyteLastCommitUrl() {
  const baseUrl = `https://img.shields.io/${props.repo.type}/last-commit/${props.repo.user}/${props.repo.name}?label=Last%20Commit`;
  const match = props.repo.url.match(/airbyte-integrations\S+/);
  return match ? `${baseUrl}&path=${match[0]}` : baseUrl;
}
</script>

<template>
  <div class="px-2 w-full lg:w-4/12">
    <div class="single-plugin-aside order-first lg:order-last p-5">
      <div class="px-4 aside-inner space-y-4">
        <!-- Install Section -->
        <div>
          <p class="text-lg py-2">Install</p>
          <div class="space-y-2">
            <div class="flex border-b border-gray-200">
              <button
                @click="activeTab = 'modern'"
                :class="[
                  'px-2 py-1 text-xs font-medium border-b-2 transition-colors',
                  activeTab === 'modern'
                    ? 'border-blue-500 text-blue-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700',
                ]"
              >
                v3.8+
              </button>
              <button
                @click="activeTab = 'legacy'"
                :class="[
                  'px-2 py-1 text-xs font-medium border-b-2 transition-colors',
                  activeTab === 'legacy'
                    ? 'border-blue-500 text-blue-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700',
                ]"
              >
                Legacy
              </button>
            </div>
            <div v-if="activeTab === 'legacy'">
              <code class="break-word bg-white-07 rounded p-2 text-sm"
                >meltano add {{ pluginType }} {{ name
                }}<span v-if="!isDefault"> --variant {{ variant }}</span></code
              >
            </div>
            <div v-if="activeTab === 'modern'">
              <code class="break-word bg-white-07 rounded p-2 text-sm"
                >meltano add
                <span
                  v-if="
                    pluginType === 'extractor' ||
                    pluginType === 'loader' ||
                    pluginType === 'utility'
                  "
                  >{{ name }}</span
                ><span v-else>--plugin-type {{ pluginType }} {{ name }}</span
                ><span v-if="!isDefault"> --variant {{ variant }}</span></code
              >
            </div>
          </div>
        </div>

        <div></div>

        <!-- Maintenance Status -->
        <div>
          <p class="text-lg">Maintenance Status</p>
          <ul class="list-none pl-7 space-y-1">
            <li>
              <img
                v-if="maintenanceStatus === 'active'"
                alt="Maintenance Status"
                src="https://img.shields.io/badge/Maintenance%20Status-Active%20(Stable)-brightgreen"
              />
              <img
                v-else-if="maintenanceStatus === 'unknown'"
                alt="Maintenance Status"
                src="https://img.shields.io/badge/Maintenance%20Status-Unknown-lightgrey"
              />
              <img
                v-else-if="maintenanceStatus === 'development'"
                alt="Maintenance Status"
                src="https://img.shields.io/badge/Maintenance%20Status-Development%20(Under%20Construction)-orange"
              />
              <img
                v-else-if="maintenanceStatus === 'beta'"
                alt="Maintenance Status"
                src="https://img.shields.io/badge/Maintenance%20Status-Prerelease%20(Beta)-yellow"
              />
              <img
                v-else-if="maintenanceStatus === 'inactive'"
                alt="Maintenance Status"
                src="https://img.shields.io/badge/Maintenance%20Status-Inactive%20or%20Stale-red"
              />
            </li>
            <li v-if="isMeltanoSdk">
              <a href="https://sdk.meltano.com/en/latest/">
                <img
                  alt="Built with the Meltano SDK"
                  src="https://img.shields.io/badge/Built%20with%20the%20Meltano%20SDK-✔-blueviolet"
                />
              </a>
            </li>
            <li v-if="isAirbyteProtocol && airbyteName">
              <a :href="`https://docs.airbyte.com/integrations/${airbyteName.replace('-', 's/')}`">
                <img
                  alt="Based on an Airbyte Connector"
                  src="https://img.shields.io/badge/Based%20on%20an%20Airbyte%20Connector-🔗-orange"
                />
              </a>
            </li>
          </ul>
        </div>

        <!-- Repo Section -->
        <div>
          <p class="text-lg">Repo</p>
          <div>
            <img
              v-if="repo.type === 'github'"
              class="w-8 h-4 inline gap-x-11"
              src="/images/github-brands.svg"
              alt="GitHub"
            /><img
              v-else-if="repo.type === 'gitlab'"
              class="w-8 h-4 inline gap-x-11"
              src="/images/gitlab-brands.svg"
              alt="GitLab"
            /><img
              v-else-if="repo.type === 'bitbucket'"
              class="w-8 h-4 inline gap-x-11"
              src="/images/bitbucket-brands.svg"
              alt="Bitbucket"
            /><img
              v-else
              class="w-8 h-4 inline gap-x-11"
              src="/images/git-alt-brands.svg"
              alt="Git"
            /><a :href="repo.url"
              ><img
                class="inline gap-x-11"
                :alt="repo.url"
                :src="`https://img.shields.io/static/v1?label=${repo.user}&message=${repo.name}&color=blue`"
              />
            </a>
          </div>
        </div>

        <!-- Repo Stats (non-Airbyte, non-Bitbucket) -->
        <div v-if="showRepoStats">
          <ul class="list-none pl-7 space-y-1">
            <li>
              <img
                alt="Stars"
                :src="`https://img.shields.io/${repo.type}/stars/${repo.user}/${repo.name}?label=Stars`"
              />
            </li>
            <li>
              <img
                alt="Forks"
                :src="`https://img.shields.io/${repo.type}/forks/${repo.user}/${repo.name}?label=Forks`"
              />
            </li>
            <li>
              <img
                alt="Last Commit Date"
                :src="`https://img.shields.io/${repo.type}/last-commit/${repo.user}/${repo.name}?label=Last%20Commit`"
              />
            </li>
            <li>
              <img
                alt="Open Issues"
                :src="`https://img.shields.io/${
                  repo.type === 'github' ? 'github/issues-raw' : 'gitlab/issues/open-raw'
                }/${repo.user}/${repo.name}?label=Open%20Issues`"
              />
            </li>
            <li>
              <img
                alt="Open PRs"
                :src="`https://img.shields.io/${
                  repo.type === 'github' ? 'github/issues-pr-raw' : 'gitlab/merge-requests/open'
                }/${repo.user}/${repo.name}?label=Open%20Pull%20Requests`"
              />
            </li>
            <li>
              <img
                alt="Contributors"
                :src="`https://img.shields.io/${repo.type}/contributors/${repo.user}/${repo.name}?label=Contributors`"
              />
            </li>
            <li>
              <img
                alt="License"
                :src="`https://img.shields.io/${repo.type}/license/${repo.user}/${repo.name}?color=c0c0c4&label=License`"
              />
            </li>
          </ul>
        </div>

        <!-- Airbyte Extractor Stats -->
        <div v-if="isExtractorAirbyte">
          <ul class="list-none pl-7 space-y-1">
            <li>
              <img alt="Last Commit Date" :src="getAirbyteLastCommitUrl()" />
            </li>
            <li>
              <img alt="License" src="https://img.shields.io/badge/License-MIT-lightgrey" />
            </li>
          </ul>
        </div>

        <!-- EDK Extension Repo -->
        <div v-if="extRepo">
          <p class="text-lg">EDK Extension Repo</p>
          <div>
            <img
              v-if="repoEDKType === 'github'"
              class="w-8 h-4 inline gap-x-11"
              src="/images/github-brands.svg"
              alt="GitHub"
            /><img
              v-else
              class="w-8 h-4 inline gap-x-11"
              src="/images/gitlab-brands.svg"
              alt="GitLab"
            /><a :href="extRepo"
              ><img
                class="inline gap-x-11"
                :alt="extRepo"
                :src="`https://img.shields.io/static/v1?label=${parsedEDKRepo.user}&message=${parsedEDKRepo.repo_name}&color=blue`"
              />
            </a>
          </div>
        </div>

        <!-- Maintainer -->
        <div>
          <p class="text-lg">Maintainer</p>
          <ul class="list-none pl-7">
            <li>
              <a v-if="maintainer" :href="maintainer.url"
                ><img
                  :alt="maintainer.label"
                  :src="`https://img.shields.io/static/v1?label=&message=${maintainer.label}&color=grey`"
                /> </a
              ><img
                v-else
                :alt="variant"
                :src="`https://img.shields.io/static/v1?label=&message=${variant}&color=grey`"
              />
            </li>
          </ul>
        </div>

        <!-- Meltano Stats -->
        <div v-if="metrics && (metrics.all_execs || metrics.all_projects)">
          <p class="text-lg">Meltano Stats</p>
          <ul class="list-none pl-7 space-y-1">
            <li v-if="metrics.all_execs">
              <img
                alt="Total Executions (Last 3 Months)"
                :src="`https://img.shields.io/badge/Total%20Executions%20(Last%203%20Months)-${metrics.all_execs.toLocaleString()}-c0c0c4`"
              />
            </li>
            <li v-if="metrics.all_projects">
              <img
                alt="Projects (Last 3 Months)"
                :src="`https://img.shields.io/badge/Projects%20(Last%203%20Months)-${metrics.all_projects.toLocaleString()}-c0c0c4`"
              />
            </li>
          </ul>
        </div>

        <!-- PyPI Stats -->
        <div v-if="hasPyPI">
          <p class="text-lg">PyPI Stats</p>
          <ul class="list-none pl-7 space-y-1">
            <li>
              <img
                alt="PyPI Downloads"
                :src="`https://img.shields.io/pypi/dm/${pipUrl}?color=3438BF&label=PyPI%20Downloads&`"
              />
            </li>
            <li>
              <img
                alt="PyPI Package Version"
                :src="`https://img.shields.io/pypi/v/${pipUrl}?color=3438BF&label=PyPI%20Package%20Version&`"
              />
            </li>
          </ul>
        </div>

        <!-- Keywords -->
        <div>
          <p class="text-lg">Keywords</p>
          <ul class="list-none pl-7">
            <li>
              <img
                v-for="(keyword, index) in keywords"
                :key="index"
                class="inline mr-1"
                :alt="keyword"
                :src="`https://img.shields.io/static/v1?label=&message=${keyword}&color=grey`"
              />
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
