<template>
  <Layout>
    <div class="plugins-overview">
      <h1>Orchestrators</h1>
      <p>
        Meltano orchestrator plugins provide advanced scheduling and workflow
        execution capabilities.
      </p>
      <ul class="plugins-list">
        <li
          v-for="edge in $page.allOrchestrators.edges"
          :key="edge.node.id"
          class="page-single-plugin"
        >
          <g-link :to="edge.node.path">
            <h2>{{ edge.node.label }}</h2>
            <!-- <g-image :src="require(`!!assets-loader!@/src${edge.node.logo_url}`)" /> -->
            <p>{{ edge.node.variant }}</p>
            <p>{{ edge.node.maintenance_status }}</p>
            <p>{{ edge.node.description }}</p>
          </g-link>
        </li>
        <Pager
          :info="$page.allOrchestrators.pageInfo"
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
  name: "OrchestratorsPage",
  components: {
    Pager,
  },
};
</script>

<page-query>
query ($page: Int) {
	allOrchestrators(perPage: 12, page: $page, sortBy: "label", order: DESC) @paginate {
    pageInfo {
      totalPages
      currentPage
    }
		edges {
      node {
                id
                path
				label
				name
				logo_url
				namespace
				variant
				pip_url
				repo
				maintenance_status
      }
    }
  }
}
</page-query>

<style lang="scss"></style>
