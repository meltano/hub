<template>
    <Layout>
        <div class="plugins-overview">
            <h1>Files</h1>
            <p>Meltano file plugins allow you to easily add new file resources to your data project. For example,
                Meltano utilities and other plugins can define file plugins that provide tool-specific scaffolding,
                templates, and applicable readme resources.</p>
            <ul class="plugins-list">
                <li v-for="edge in $page.allFiles.edges" :key="edge.node.id" class="page-single-plugin">
                    <g-link :to="edge.node.path">
                        <h2>{{ edge.node.label }}</h2>
                        <!-- <g-image :src="require(`!!assets-loader!@/src${edge.node.logo_url}`)" /> -->
                        <p>{{ edge.node.variant }}</p>
                        <p>{{ edge.node.maintenance_status }}</p>
                        <p>{{ edge.node.description }}</p>
                    </g-link>
                </li>
                <Pager :info="$page.allFiles.pageInfo" class="pager-container" linkClass="pager-container__link" />
            </ul>
        </div>
    </Layout>
</template>

<script>
import { Pager } from 'gridsome';
export default {
    name: "Files",
    components: {
        Pager
    }
}
</script>

<page-query>
query ($page: Int) {
	allFiles(perPage: 12, page: $page, sortBy: "label", order: DESC) @paginate {
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

<style lang="scss">

</style>