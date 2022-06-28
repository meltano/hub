<template>
    <Layout>
        <div class="info">
            <h1>Loaders</h1>
            <p>Meltano lets you easily load extracted data into arbitrary destinations (databases, SaaS APIs, and file
                formats) using Singer targets, which take the role of your project’s loader plugins. To learn more about
                extracting and loading data using Meltano, refer to the Data Integration (EL) guide.</p>
            <ul class="plugins-list">
                <li v-for="edge in $page.allLoaders.edges" :key="edge.node.id" class="page-single-plugin">
                    <h2>{{ edge.node.label }}</h2>
                    <!-- <g-image :src="require(`!!assets-loader!@/src${edge.node.logo_url}`)" /> -->
                    <p>{{ edge.node.variant }}</p>
                    <p>{{ edge.node.maintenance_status }}</p>
                    <p>{{ edge.node.description }}</p>
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
.info {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0 200px;

    h1 {
        font-size: 2.5em;
    }
}

.plugins-list {
    width: 100%;
    height: auto;
    background: #e8f0ff;
    display: flex;
    flex-wrap: wrap;
    margin-top: 40px;

    .page-single-plugin {
        color: #000;
        display: flex;
        flex-direction: column;
        list-style-type: none;
        padding: 0;
        margin: 0;
        flex-basis: 33.333333%
    }

    .pager-container {
        display: inline-block;
        text-align: center;
        width: 100%;
        margin: 20px auto;

        .active {
            background-color:#c0c0c4;
        }

        &__link {
            text-align: center;
            padding: 0.6rem 1.2rem;
            color: #3438bf;
            text-decoration: none;
        }
    }
}
</style>