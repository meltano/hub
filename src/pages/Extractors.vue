<template>
  <Layout>
    <div class="plugins-overview mx-auto">
      <p class="text-3xl py-4">Extractors</p>
      <p>
        Meltano lets you easily extract data out of arbitrary sources (databases, SaaS APIs, and
        file formats) using Singer taps, which take the role of your project’s extractor plugins. To
        learn more about extracting and loading data using Meltano, refer to the Data Integration
        (EL) guide.
      </p>
      <div
        class="grid grid-cols-2 md:grid-cols-4 bg-slate-200 rounded-lg p-4 mt-4 md:m-4 gap-4 w-full place-items-stretch"
        role="list"
      >
        <div
          v-for="edge in $page.allPlugins.edges"
          :key="edge.node.id"
          class="rounded-md shadow-lg text-slate-800 h-36 hover:bg-slate-100 p-2 md:p-4 bg-white overflow-hidden"
        >
          <g-link
            class="grid grid-rows-6 align-self-center place-items-center h-full w-full"
            :to="edge.node.path.split('--')[0]"
          >
            <div class="grid place-self-center row-span-4 h-full w-full">
              <g-image
                v-if="edge.node.logo_url"
                :src="
                  require(`!!assets-loader?width=175&height=80&fit=inside!@logos/${edge.node.logo_url.replace(
                    '/assets/logos/',
                    ''
                  )}`)
                "
                class="place-self-center"
              />
            </div>
            <div class="grid content-end row-span-5 self-stretch h-full">
              <p class="font-bold underline text-xs lg:text-md justify-self-center text-clip">
                {{ edge.node.label }}
              </p>
            </div>
          </g-link>
        </div>
        <Pager
          :info="$page.allPlugins.pageInfo"
          class="pager-container text-black m-4 col-span-2 md:col-span-4 mx-auto"
          linkClass="pager-container__link p-2 hover:text-sky-300"
          activeLinkClass="bg-sky-300 rounded-lg"
        />
      </div>
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
  allPlugins(
    perPage: 100
    page: $page
    sortBy: "label"
    order: ASC
    filter: { isDefault: { eq: true }, pluginType: { eq: "extractor" } }
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
