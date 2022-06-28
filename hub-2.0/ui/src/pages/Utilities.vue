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
        flex-basis: 33.333333%;
        a {
            color: #3438bf;
            text-decoration: none;
        }
        a:hover {
            background: #b0e3c1;
        }
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