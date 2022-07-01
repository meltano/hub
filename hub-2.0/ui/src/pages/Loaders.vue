<template>
    <Layout>
        <div class="info">
            <h1>Loaders</h1>
            <p>Meltano lets you easily load extracted data into arbitrary destinations (databases, SaaS APIs, and file
                formats) using Singer targets, which take the role of your project’s loader plugins. To learn more about
                extracting and loading data using Meltano, refer to the Data Integration (EL) guide.</p>
            <ul class="plugins-list">
                <li v-for="edge in $page.allLoaders.edges" :key="edge.node.id" class="page-single-plugin">
                    <g-link :to="edge.node.path">
                        <h2>{{ edge.node.label }}</h2>
                        <!-- <g-image :src="require(`!!assets-loader!@/src${edge.node.logo_url}`)" /> -->
                        <p>{{ edge.node.variant }}</p>
                        <p>{{ edge.node.maintenance_status }}</p>
                        <p>{{ edge.node.description }}</p>
                    </g-link>
                </li>
                <Pager :info="$page.allLoaders.pageInfo" class="pager-container" linkClass="pager-container__link" />
            </ul>
        </div>
    </Layout>
</template>

<script>
import { Pager } from 'gridsome';
export default {
    name: "Loaders",
    components: {
        Pager
    }
}
</script>

<page-query>
query ($page: Int) {
	allLoaders(perPage: 12, page: $page, sortBy: "label", order: DESC) @paginate {
    pageInfo {
      totalPages
      currentPage
    }
		edges {
      node {
                id
                path
				description
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