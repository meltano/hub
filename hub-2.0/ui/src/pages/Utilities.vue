<template>
  <Layout>
    <div class="plugins-overview">
      <h1>Utilities</h1>
      <p>
        Meltano utilities plugins allow virtually any open source data tool to be integrated with
        your data project.
      </p>
      <ul class="plugins-list">
        <li v-for="edge in $page.allUtilities.edges" :key="edge.node.id" class="page-single-plugin">
          <g-link :to="edge.node.path">
            <h2>{{ edge.node.label }}</h2>
            <g-image
              v-if="edge.node.logo_url"
              :src="
                require(`!!assets-loader?width=175&height=80&fit=inside!@logos/${edge.node.logo_url.replace(
                  '/assets/logos/',
                  ''
                )}`)
              "
            />
            <h2>{{ edge.node.label }}</h2>
            <h2>
              <code>{{ edge.node.name }}</code
              ><br /><code>from {{ edge.node.variant }}</code>
            </h2>
            <p>
              <i>{{ edge.node.maintenance_status }} status</i>
            </p>
          </g-link>
        </li>
        <Pager
          :info="$page.allUtilities.pageInfo"
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
  name: "UtilitiesPage",
  components: {
    Pager
  }
};
</script>

<page-query lang="graphql">
query ($page: Int) {
  allUtilities(perPage: 100, page: $page, sortBy: "label", order: ASC) @paginate {
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

<style lang="scss"></style>
