<template>
  <div class="single-plugin-aside">
    <h4>Install</h4>
    <pre><code>meltano add {{plugin_type}} {{ name }}<span v-if="!is_default"> --variant {{ variant }}</span></code></pre>
    <h4>Homepage</h4>
    <div class="link-box">
      <img class="aside-icon" src="../assets/images/link-solid.svg" /><a :href="domain_url">{{
        domain_url
      }}</a>
    </div>
    <h4>Maintenance Status</h4>
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
    <h4>Repo</h4>
    <div class="link-box">
      <img class="aside-icon" src="../assets/images/git-alt-brands.svg" /><a :href="repo">{{
        repo
      }}</a>
    </div>

    <ul class="shields">
      <li>
        <img
          alt="GitHub - Stars"
          :src="`https://img.shields.io/github/stars/${variant}/${name}?style=flat-square&label=Stars`"
        />
      </li>
      <li>
        <img
          alt="GitHub - Forks"
          :src="`https://img.shields.io/github/forks/${variant}/${name}?style=flat-square&label=Forks`"
        />
      </li>
      <li>
        <img
          alt="GitHub - Open Issues"
          :src="`https://img.shields.io/github/issues-raw/${variant}/${name}?label=Open%20Issues`"
        />
      </li>
      <li>
        <img
          alt="GitHub - Open PRs"
          :src="`https://img.shields.io/github/issues-pr-raw/${variant}/${name}?label=Open%20Pull%20Requests`"
        />
      </li>
      <li>
        <img
          alt="GitHub - Contributors"
          :src="`https://img.shields.io/github/contributors/${variant}/${name}?label=Contributors`"
        />
      </li>
      <li>
        <img
          alt="GitHub - License"
          :src="`https://img.shields.io/github/license/${variant}/${name}?color=c0c0c4&label=License&style=flat-square`"
        />
      </li>
    </ul>
    <h4>Maintainer</h4>
    <div v-if="metrics">
      <h4>Meltano Stats</h4>
      <ul class="shields">
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
      </ul>
    </div>
    <h4>Keywords</h4>
    <p>{{ (keywords ?? []).join(", ") }}</p>
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
  ],
};
</script>

<style lang="scss">
.shields {
  list-style-type: none;
  padding: 0 0 0 30px;
}
</style>
