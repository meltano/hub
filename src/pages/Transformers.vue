<template>
  <Layout>
    <div class="plugins-overview">
      <p class="text-3xl py-4">Transformers</p>
      <p>
        Meltano transformer plugins allow you to create new derived transformations from raw data
        sources.
      </p>
      <ul class="list-disc list-inside plugins-list">
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
            <p class="text-2xl">{{ edge.node.label }}</p>
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
  name: "TransformersPage",
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
    filter: { isDefault: { eq: true }, pluginType: { eq: "transformer" } }
  ) @paginate {
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
        pluginType
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
