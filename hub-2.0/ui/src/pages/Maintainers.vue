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
          <h2>{{ edge.node.label }}</h2>
          <p>{{ edge.node.name }}</p>
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
  allMaintainers(perPage: 24, page: $page, sortBy: "label", order: ASC)
    @paginate {
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
