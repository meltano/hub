<template>
  <Layout>
    <div class="plugins-overview">
      <h1>Loaders</h1>
      <p>
        Meltano lets you easily load extracted data into arbitrary destinations (databases, SaaS
        APIs, and file formats) using Singer targets, which take the role of your project’s loader
        plugins. To learn more about extracting and loading data using Meltano, refer to the Data
        Integration (EL) guide.
      </p>
      <ul class="plugins-list">
        <li v-for="edge in $page.allPlugins.edges" :key="edge.node.id" class="page-single-plugin">
          <g-link :to="edge.node.path.split('--')[0]">
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
            <p>{{ edge.node.pluginType }}</p>
          </g-link>
        </li>
        <Pager
          :info="$page.allPlugins.pageInfo"
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
  name: "LoadersPage",
  components: {
    Pager,
  },
};
</script>

<page-query lang="graphql">
query ($page: Int) {
  allPlugins(
    perPage: 100
    page: $page
    sortBy: "label"
    order: ASC
    filter: { isDefault: { eq: true }, pluginType: { eq: "loader" } }
  ) @paginate {
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
        pluginType
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
