<template>
  <Layout>
    <div class="plugins-overview">
      <p class="text-3xl md:text-5xl pb-4 pt-8 font-bold font-pjs text-purple">
        Plugin Maintainers
      </p>
      <ul class="list-disc list-inside plugins-list">
        <li
          v-for="(edge, index) in $page.allMaintainers.edges"
          :key="index"
          class="page-single-plugin"
        >
          <p class="text-2xl">
            <a :href="`${edge.node.url}`">{{ edge.node.label }}</a>
          </p>
        </li>
        <Pager
          :info="$page.allMaintainers.pageInfo"
          class="pager-container"
          linkClass="pager-container__link"
        />
      </ul>
    </div>
  </Layout>
</template>

<script>
import { Pager } from "gridsome";

export default {
  name: "MaintainersPage",
  components: {
    Pager,
  },
};
</script>
<page-query lang="graphql">
query ($page: Int) {
  allMaintainers(perPage: 24, page: $page, sortBy: "label", order: ASC) @paginate {
    pageInfo {
      totalPages
      currentPage
    }
    edges {
      node {
        name
        label
        url
      }
    }
  }
}
</page-query>
<style></style>
