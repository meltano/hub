<template>
  <Layout>
    <div class="plugins-overview">
      <h1>Plugin Maintainers</h1>
      <ul class="plugins-list">
        <li
          v-for="(edge, index) in $page.allMaintainers.edges"
          :key="index"
          class="page-single-plugin"
        >
          <h2>
            <a :href="`${edge.node.url}`">{{ edge.node.label }}</a>
          </h2>
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
    Pager
  }
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
