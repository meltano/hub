<template>
  <div class="single-plugin-aside">
    <h4>Install</h4>
    <pre><code>meltano add {{plugin_type}} {{ name }}  <span v-if="this.isVariantDefault()"></span></code></pre>
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

    <ul class="repo-shields">
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
    <h4>Meltano Stats</h4>

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
    "repo",
    "maintenance_status",
    "keywords",
    "variant",
    "plugin_type",
    "variants"
  ],
  // data() {
  //   return {
  //     variantIsDefault: null
  //   };
  // },
  computed: {
    isVariantDefault() {
      return this.$page.variants.edges.forEach((variant) => {
        if (this.$page.extractors.variant === variant.node.variant && variant.node.isDefault) {
          // this.variantIsDefault = true;
          console.log("true!");
          return true;
        }
        // this.variantIsDefault = false;
        console.log("false!");
        return false;
      });
    }
  },
  mounted() {
    console.log("mounted");
    this.isVariantDefault();
  },
  updated() {
    console.log("updated");
    this.isVariantDefault();
  }
};
</script>

<style lang="scss">
.repo-shields {
  list-style-type: none;
  padding: 0 0 0 30px;
}
</style>
