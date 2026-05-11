<template>
  <div class="px-2 w-full lg:w-4/12">
    <div>
      <div class="community-card">
        <div class="community-card__header">
          <svg
            class="community-card__icon"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            aria-hidden="true"
          >
            <circle cx="9" cy="7" r="3" stroke="#311772" stroke-width="1.75" />
            <circle cx="17" cy="8" r="2.25" stroke="#311772" stroke-width="1.5" />
            <path
              d="M2 19c0-3.314 3.134-6 7-6s7 2.686 7 6"
              stroke="#311772"
              stroke-width="1.75"
              stroke-linecap="round"
            />
            <path
              d="M17 13c2.209 0 4 1.567 4 3.5"
              stroke="#311772"
              stroke-width="1.5"
              stroke-linecap="round"
            />
          </svg>
          <span class="community-card__title">Meltano Community Connector</span>
        </div>
        <p class="community-card__body">
          {{ label }} is built and maintained by the Meltano community. For connectors that are
          built, tested, and supported by the Meltano team, explore Meltano Cloud.
        </p>
        <ul class="community-card__perks">
          <li>
            <svg viewBox="0 0 16 16" fill="none" aria-hidden="true">
              <path
                d="M3 8.5l3.5 3.5 6.5-7"
                stroke="#311772"
                stroke-width="1.75"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
            <span
              ><strong>Expert support</strong> — get support from experts who build and support
              connectors on Meltano Cloud</span
            >
          </li>
          <li>
            <svg viewBox="0 0 16 16" fill="none" aria-hidden="true">
              <path
                d="M3 8.5l3.5 3.5 6.5-7"
                stroke="#311772"
                stroke-width="1.75"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
            <span
              ><strong>Tested daily</strong> — daily monitoring catches issues before they hit your
              pipelines</span
            >
          </li>
          <li>
            <svg viewBox="0 0 16 16" fill="none" aria-hidden="true">
              <path
                d="M3 8.5l3.5 3.5 6.5-7"
                stroke="#311772"
                stroke-width="1.75"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
            <span
              ><strong>Low maintenance</strong> — API changes, schema drift and breaking changes
              handled for you</span
            >
          </li>
        </ul>
        <div class="community-card__actions">
          <a
            href="https://meltano.com/contact"
            rel="noopener noreferrer"
            class="community-card__btn community-card__btn--light"
          >
            Get in touch
          </a>
          <a
            href="https://meetings.hubspot.com/kyle-john"
            target="_blank"
            rel="noopener noreferrer"
            class="community-card__btn community-card__btn--primary"
          >
            Book a demo
          </a>
        </div>
      </div>
      <div class="single-plugin-aside order-first lg:order-last p-5">
        <div class="px-4 aside-inner space-y-4">
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
                  >meltano add {{ plugin_type }} {{ name
                  }}<span v-if="!is_default"> --variant {{ variant }}</span></code
                >
              </div>
              <div v-if="activeTab === 'modern'">
                <code class="break-word bg-white-07 rounded p-2 text-sm"
                  >meltano add
                  <span
                    v-if="
                      plugin_type === 'extractor' ||
                      plugin_type === 'loader' ||
                      plugin_type === 'utility'
                    "
                    >{{ name }}</span
                  ><span v-else>--plugin-type {{ plugin_type }} {{ name }}</span
                  ><span v-if="!is_default"> --variant {{ variant }}</span></code
                >
              </div>
            </div>
          </div>
          <div></div>
          <div>
            <p class="text-lg">Maintenance Status</p>
            <ul class="list-disc list-inside shields space-y-1">
              <li>
                <img
                  v-if="maintenance_status === 'active'"
                  alt="Maintenance Status"
                  src="https://img.shields.io/badge/Maintenance%20Status-Active%20(Stable)-brightgreen"
                />
                <img
                  v-else-if="maintenance_status === 'unknown'"
                  alt="Maintenance Status"
                  src="https://img.shields.io/badge/Maintenance%20Status-Unknown-lightgrey"
                />
                <img
                  v-else-if="maintenance_status === 'development'"
                  alt="Maintenance Status"
                  src="https://img.shields.io/badge/Maintenance%20Status-Development%20(Under%20Construction)-orange"
                />
                <img
                  v-else-if="maintenance_status === 'beta'"
                  alt="Maintenance Status"
                  src="https://img.shields.io/badge/Maintenance%20Status-Prerelease%20(Beta)-yellow"
                />
                <img
                  v-else-if="maintenance_status === 'inactive'"
                  alt="Maintenance Status"
                  src="https://img.shields.io/badge/Maintenance%20Status-Inactive%20or%20Stale-red"
                />
              </li>
              <li v-if="(keywords ?? []).includes('meltano_sdk')">
                <a href="https://sdk.meltano.com/en/latest/">
                  <img
                    alt="Built with the Meltano SDK"
                    src="https://img.shields.io/badge/Built%20with%20the%20Meltano%20SDK-✔-blueviolet"
                  />
                </a>
              </li>
              <li v-if="(keywords ?? []).includes('airbyte_protocol')">
                <a
                  :href="`https://docs.airbyte.com/integrations/${airbyte_name.replace('-', 's/')}`"
                >
                  <img
                    alt="Based on an Airbyte Connector"
                    src="https://img.shields.io/badge/Based%20on%20an%20Airbyte%20Connector-🔗-orange"
                  />
                </a>
              </li>
            </ul>
          </div>
          <div>
            <p class="text-lg">Repo</p>
            <div>
              <img
                v-if="repo.type === 'github'"
                class="w-8 h-4 inline gap-x-11"
                src="../assets/images/github-brands.svg"
              /><img
                v-else-if="repo.type === 'gitlab'"
                class="w-8 h-4 inline gap-x-11"
                src="../assets/images/gitlab-brands.svg"
              /><img
                v-else-if="repo.type === 'bitbucket'"
                class="w-8 h-4 inline gap-x-11"
                src="../assets/images/bitbucket-brands.svg"
              /><img
                v-else
                class="w-8 h-4 inline gap-x-11"
                src="../assets/images/git-alt-brands.svg"
              /><a :href="repo.url"
                ><img
                  class="inline gap-x-11"
                  :alt="repo.url"
                  :src="`https://img.shields.io/static/v1?label=${repo.user}&message=${repo.name}&color=blue`"
                />
              </a>
            </div>
          </div>
          <div
            v-if="!$page.plugins.keywords.includes('airbyte_protocol') && repo.type !== 'bitbucket'"
          >
            <ul class="list-disc list-inside shields space-y-1">
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
          <div
            v-if="
              $page.plugins.pluginType === 'extractor' &&
              $page.plugins.keywords.includes('airbyte_protocol')
            "
          >
            <ul class="list-disc list-inside shields space-y-1">
              <li>
                <img
                  alt="Last Commit Date"
                  :src="
                    (() => {
                      const url = `https://img.shields.io/${repo.type}/last-commit/${repo.user}/${repo.name}?label=Last%20Commit`;
                      const [path] = repo.url.match(/airbyte-integrations\S+/) ?? [];

                      return path ? `${url}&path=${path}` : url;
                    })()
                  "
                />
              </li>
              <li>
                <img alt="License" :src="`https://img.shields.io/badge/License-MIT-lightgrey`" />
              </li>
            </ul>
          </div>
          <div v-if="ext_repo">
            <p class="text-lg">EDK Extension Repo</p>
            <div>
              <img
                v-if="repo.type === 'github'"
                class="w-8 h-4 inline gap-x-11"
                src="../assets/images/github-brands.svg"
              /><img
                v-else-if="repo.type === 'gitlab'"
                class="w-8 h-4 inline gap-x-11"
                src="../assets/images/gitlab-brands.svg"
              /><img
                v-else
                class="w-8 h-4 inline gap-x-11"
                src="../assets/images/git-alt-brands.svg"
              /><a :href="ext_repo"
                ><img
                  class="inline gap-x-11"
                  :alt="ext_repo"
                  :src="`https://img.shields.io/static/v1?label=${parsedEDKRepo.user}&message=${parsedEDKRepo.repo_name}&color=blue`"
                />
              </a>
            </div>
          </div>
          <div>
            <p class="text-lg">Maintainer</p>
            <ul class="list-disc list-inside shields">
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
          <!-- <div v-if="metrics  (keywords ?? []).includes('meltano_sdk')"> -->
          <div v-if="metrics && (metrics.all_execs || metrics.all_projects)">
            <p class="text-lg">Meltano Stats</p>
            <ul class="list-disc list-inside shields space-y-1">
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
          <div v-if="hasPyPI">
            <p class="text-lg">PyPI Stats</p>
            <ul class="list-disc list-inside shields space-y-1">
              <li>
                <img
                  alt="PyPI Downloads"
                  :src="`https://img.shields.io/pypi/dm/${pip_url}?color=3438BF&label=PyPI%20Downloads&`"
                  :href="`https://pypi.org/project/${pip_url}/`"
                />
              </li>
              <li>
                <img
                  alt="PyPI Package Version"
                  :src="`https://img.shields.io/pypi/v/${pip_url}?color=3438BF&label=PyPI%20Package%20Version&`"
                  :href="`https://pypi.org/project/${pip_url}/`"
                />
              </li>
            </ul>
          </div>
          <div>
            <p class="text-lg">Keywords</p>
            <ul class="list-disc list-inside shields">
              <li>
                <img
                  v-for="(keyword, index) in keywords"
                  v-bind:key="index"
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
  </div>
</template>

<script>
export default {
  name: "PluginSidebar",
  props: [
    "name",
    "label",
    "airbyte_name",
    "domain_url",
    "is_default",
    "repo",
    "maintenance_status",
    "keywords",
    "variant",
    "plugin_type",
    "metrics",
    "maintainer",
    "pip_url",
    "ext_repo",
  ],
  data() {
    return {
      activeTab: "modern",
    };
  },
  computed: {
    parsedEDKRepo() {
      // For some plugin variants, either the `variant` or `name` doesn't match the GH repo
      // So we need to parse it from the repo URL to make badges
      // https://github.com/:user/:repoName
      const urlParts = this.ext_repo.split("/");
      return { user: urlParts[3], repo_name: urlParts[4] };
    },
    repoEDKType() {
      // Some plugins are hosted on github, some on gitlab
      return this.ext_repo.includes("github.com") ? "github" : "gitlab";
    },
    hasPyPI() {
      // Exclude more elaborate ways of specifying `pip_url`
      // TODO: figure out what we should do when
      //   - multiple packages are listed space-delimited
      //   - packages have version specifiers (==, ~=)
      //   - packages specify optional dependencies in []
      return (
        this.pip_url &&
        !(
          this.pip_url.includes("git+") ||
          this.pip_url.includes("//") ||
          this.pip_url.includes("=") ||
          this.pip_url.includes(" ") ||
          this.pip_url.includes("[")
        )
      );
    },
  },
};
</script>

<style lang="scss">
.shields {
  list-style-type: none;
  padding: 0 0 0 30px;
}

.community-card {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 16px;
  margin-bottom: 16px;
  border-radius: 8px;
  background: rgba(49, 23, 114, 0.06);
  border: 1px solid rgba(49, 23, 114, 0.2);

  &__header {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  &__icon {
    width: 22px;
    height: 22px;
    flex-shrink: 0;
  }

  &__title {
    font-size: 1rem;
    font-weight: 600;
    color: #311772;
    font-family: "Plus Jakarta Sans", sans-serif;
    line-height: 1.3;
  }

  &__body {
    font-size: 0.875rem;
    color: #62626e;
    line-height: 1.6;
    margin: 0;
    font-family: "Hanken Grotesk", sans-serif;
  }

  &__perks {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 8px;

    li {
      display: flex;
      align-items: flex-start;
      gap: 8px;
      font-size: 0.8125rem;
      color: #62626e;
      font-family: "Hanken Grotesk", sans-serif;
      line-height: 1.5;

      svg {
        width: 16px;
        height: 16px;
        flex-shrink: 0;
        margin-top: 2px;
      }

      strong {
        color: #311772;
      }
    }
  }

  &__actions {
    display: flex;
    gap: 8px;
  }

  &__btn {
    display: flex;
    align-items: center;
    justify-content: center;
    flex: 1;
    padding: 10px 14px;
    border-radius: 6px;
    font-size: 0.875rem;
    font-weight: 600;
    text-decoration: none;
    font-family: "Plus Jakarta Sans", sans-serif;
    transition: opacity 0.15s ease;

    &:hover {
      opacity: 0.85;
      text-decoration: none;
    }

    &--light {
      background: #ffffff;
      color: #311772;
      border: 1px solid rgba(49, 23, 114, 0.25);
    }

    &--primary {
      background: #3a64fa;
      color: #ffffff !important;
      border: 1px solid transparent;
    }
  }
}
</style>
