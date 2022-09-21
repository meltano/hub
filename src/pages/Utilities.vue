<template>
  <Layout>
    <div class="plugins-overview">
      <p class="text-3xl py-4">Utilities</p>
      <p>
        Meltano utilities plugins allow virtually any open source data tool to be integrated with
        your data project.
      </p>
      <div
        class="grid grid-cols-2 md:grid-cols-4 place-items-center bg-slate-200 rounded-lg p-4 mt-4 md:m-4 gap-4 w-full"
        role="list"
      >
        <div
          v-for="edge in $page.allPlugins.edges"
          :key="edge.node.id"
          class="rounded-md shadow-lg text-slate-800 hover:bg-slate-100 self-center w-full h-full place-items-center p-2 md:p-4 bg-white overflow-hidden"
        >
          <g-link class="grid w-full h-full" :to="edge.node.path.split('--')[0]">
            <div class="place-self-center row-span-2 object-scale-down">
              <g-image
                v-if="edge.node.logo_url"
                :src="
                  require(`!!assets-loader?width=175&height=80&fit=inside!@logos/${edge.node.logo_url.replace(
                    '/assets/logos/',
                    ''
                  )}`)
                "
                class="place-self-center object-scale-down"
              />
            </div>
            <div class="row-span-1 self-end object-scale-down">
              <p
                class="font-bold underline text-xs md:text-lg justify-self-center place-self-end object-scale-down text-clip"
              >
                {{ edge.node.label }}
              </p>
            </div>
          </g-link>
        </div>
        <Pager
          :info="$page.allPlugins.pageInfo"
          class="pager-container"
          linkClass="pager-container__link"
        />
      </div>
    </div>
  </Layout>
</template>

<script>
import { Pager } from "gridsome";

export default {
  name: "UtilitiesPage",
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
    filter: { isDefault: { eq: true }, pluginType: { eq: "utility" } }
  ) @paginate {
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
