<template>
  <div
    class="single-plugin-aside bg-gray-100 space-y-3 min-w-fit pl-4 order-first lg:pr-4 lg:order-last lg:border-l-2 border-black"
  >
    <div>
      <p class="text-lg py-2">Install</p>
      <code class="break-word bg-gray-300 p-2"
        >meltano add {{ plugin_type }} {{ name
        }}<span v-if="!is_default"> --variant {{ variant }}</span></code
      >
    </div>
    <div></div>

    <div v-if="domain_url">
      <p class="text-lg">Homepage</p>
      <div class="link-box">
        <img class="w-8 h-4 inline gap-x-11" src="../assets/images/link-solid.svg" /><a
          :href="domain_url"
          >{{ domain_url }}</a
        >
      </div>
    </div>

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
      </ul>
    </div>

    <div>
      <p class="text-lg">Repo</p>
      <div>
        <img class="w-8 h-4 inline gap-x-11" src="../assets/images/git-alt-brands.svg" /><a
          :href="repo"
          >{{ repo }}</a
        >
      </div>
    </div>

    <div>
      <ul class="list-disc list-inside shields space-y-1">
        <li>
          <img
            alt="Stars"
            :src="`https://img.shields.io/${repoType}/stars/${parsedRepo.user}/${parsedRepo.repo_name}?style=flat-square&label=Stars`"
          />
        </li>
        <li>
          <img
            alt="Forks"
            :src="`https://img.shields.io/${repoType}/forks/${parsedRepo.user}/${parsedRepo.repo_name}?style=flat-square&label=Forks`"
          />
        </li>
        <li>
          <img
            alt="Open Issues"
            :src="`https://img.shields.io/${
              repoType === 'github' ? 'github/issues-raw' : 'gitlab/issues/open-raw'
            }/${parsedRepo.user}/${parsedRepo.repo_name}?label=Open%20Issues`"
          />
        </li>
        <li>
          <img
            alt="Open PRs"
            :src="`https://img.shields.io/${
              repoType === 'github' ? 'github/issues-pr-raw' : 'gitlab/merge-requests/open'
            }/${parsedRepo.user}/${parsedRepo.repo_name}?label=Open%20Pull%20Requests`"
          />
        </li>
        <li>
          <img
            alt="Contributors"
            :src="`https://img.shields.io/${repoType}/contributors/${parsedRepo.user}/${parsedRepo.repo_name}?label=Contributors`"
          />
        </li>
        <li>
          <img
            alt="License"
            :src="`https://img.shields.io/${repoType}/license/${parsedRepo.user}/${parsedRepo.repo_name}?color=c0c0c4&label=License&style=flat-square`"
          />
        </li>
      </ul>
    </div>

    <div>
      <p class="text-lg">Maintainer</p>
      <ul class="list-disc list-inside shields">
        <li>
          <a :href="maintainer.url"
            ><img
              :alt="variant"
              :src="`https://img.shields.io/static/v1?label=&message=${maintainer.label}&color=grey`"
          /></a>
        </li>
      </ul>
    </div>

    <!-- <div v-if="metrics  (keywords ?? []).includes('meltano_sdk')"> -->
    <div v-if="metrics">
      <p class="text-lg">Meltano Stats</p>
      <ul class="list-disc list-inside shields space-y-1">
        <li v-if="metrics.ALL_EXECS">
          <img
            alt="Total Executions (Last 3 Months)"
            :src="`https://img.shields.io/badge/Total%20Executions%20(Last%203%20Months)-${metrics.ALL_EXECS}-c0c0c4`"
          />
        </li>
        <li v-if="metrics.ALL_PROJECTS">
          <img
            alt="Projects (Last 3 Months)"
            :src="`https://img.shields.io/badge/Projects%20(Last%203%20Months)-${metrics.ALL_PROJECTS}-c0c0c4`"
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
      </ul>
    </div>
    <div>
      <p class="text-lg">Keywords</p>
      <ul class="list-disc list-inside shields">
        <li>
          <img
            v-for="(keyword, index) in keywords"
            v-bind:key="index"
            class="inline m-1"
            :alt="keyword"
            :src="`https://img.shields.io/static/v1?label=&message=${keyword}&color=grey`"
          />
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "PluginSidebar",
  props: [
    "name",
    "domain_url",
    "is_default",
    "repo",
    "maintenance_status",
    "keywords",
    "variant",
    "plugin_type",
    "metrics",
    "maintainer",
  ],
  computed: {
    parsedRepo() {
      // For some plugin variants, either the `variant` or `name` doesn't match the GH repo
      // So we need to parse it from the repo URL to make badges
      // https://github.com/:user/:repoName
      const urlParts = this.repo.split("/");
      return { user: urlParts[3], repo_name: urlParts[4] };
    },
    repoType() {
      // Some plugins are hosted on github, some on gitlab
      return this.repo.includes("github.com") ? "github" : "gitlab";
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
