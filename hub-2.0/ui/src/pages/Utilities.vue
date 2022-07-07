<template>
    <Layout>
        <div class="info">
            <h1>Utilities</h1>
            <p>Meltano utilities plugins allow virtually any open source data tool to be integrated with your data
                project.</p>
            <ul class="plugins-list">
                <li v-for="edge in $page.allUtilities.edges" :key="edge.node.id" class="page-single-plugin">
                    <g-link :to="edge.node.path">
                        <h2>{{ edge.node.label }}</h2>
                        <!-- <g-image :src="require(`!!assets-loader!@/src${edge.node.logo_url}`)" /> -->
                        <p>{{ edge.node.variant }}</p>
                        <p>{{ edge.node.maintenance_status }}</p>
                        <p>{{ edge.node.description }}</p>
                    </g-link>
                </li>
                <Pager :info="$page.allUtilities.pageInfo" class="pager-container" linkClass="pager-container__link" />
            </ul>
        </div>
    </Layout>
</template>

<script>
import { Pager } from 'gridsome';
export default {
    name: "Utilities",
    components: {
        Pager
    }
}
</script>

<page-query>
query ($page: Int) {
	allUtilities(perPage: 12, page: $page, sortBy: "label", order: DESC) @paginate {
    pageInfo {
      totalPages
      currentPage
    }
		edges {
      node {
        id
				description
                path
				label
				name
				logo_url
				namespace
				variant
				pip_url
				repo
				maintenance_status
				keywords
      }
    }
  }
}
</page-query>

<style lang="scss">

</style>