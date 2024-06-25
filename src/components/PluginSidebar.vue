<template>
  <div class="px-2 w-full lg:w-4/12">
    <div class="single-plugin-aside order-first lg:order-last p-5">
      <div class="px-4 aside-inner space-y-4">
        <div>
          <p class="text-lg py-2">Install</p>
          <code class="break-word bg-white-07 rounded p-2 text-sm"
            >meltano add {{ plugin_type }} {{ name
            }}<span v-if="!is_default"> --variant {{ variant }}</span></code
          >
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
              <a :href="`https://docs.airbyte.com/integrations/${airbyte_name.replace('-', 's/')}`">
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
</template>

<script>
export default {
  name: "PluginSidebar",
  props: [
    "name",
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
</style>
