<template>
  <Layout>
    <div class="plugins-overview">
      <h1>Extractors</h1>
      <p>
        Meltano lets you easily extract data out of arbitrary sources
        (databases, SaaS APIs, and file formats) using Singer taps, which take
        the role of your project’s extractor plugins. To learn more about
        extracting and loading data using Meltano, refer to the Data Integration
        (EL) guide.
      </p>
      <ul class="plugins-list">
        <li
          v-for="edge in $page.allExtractors.edges"
          :key="edge.node.id"
          class="page-single-plugin"
        >
          <g-link :to="edge.node.path">
            <h2>{{ edge.node.label }}</h2>
            <!-- <g-image :src="require(`!!assets-loader!@logos/${edge.node.logo_url}`)"/> -->
            <p>Variant: {{ edge.node.variant }}</p>
            <p>Mainenance Status: {{ edge.node.maintenance_status }}</p>
            <p>Description: {{ edge.node.description }}</p>
          </g-link>
        </li>
        <Pager
          :info="$page.allExtractors.pageInfo"
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
  name: "ExtractorsPage",
  components: {
    Pager,
  },
};
</script>

<page-query lang="graphql">
query ($page: Int) {
  allExtractors(perPage: 12, page: $page, sortBy: "label", order: DESC)
    @paginate {
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
