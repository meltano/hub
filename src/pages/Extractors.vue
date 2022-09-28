<template>
  <Layout>
    <div class="plugins-overview mx-auto">
      <p class="py-4 text-3xl">Extractors</p>
      <p>
        Meltano lets you easily extract data out of arbitrary sources (databases, SaaS APIs, and
        file formats) using Singer taps, which take the role of your project’s extractor plugins. To
        learn more about extracting and loading data using Meltano, refer to the Data Integration
        (EL) guide.
      </p>
      <div
        class="mt-4 grid w-full grid-cols-2 place-items-stretch gap-4 rounded-lg bg-slate-200 p-4 md:m-4 md:grid-cols-4"
        role="list"
      >
        <div
          v-for="edge in $page.allPlugins.edges"
          :key="edge.node.id"
          class="h-48 overflow-hidden rounded-md bg-white p-2 text-slate-800 shadow-lg hover:bg-slate-100 md:p-4"
        >
          <g-link
            class="align-self-center grid h-40 w-full grid-rows-6 place-items-center"
            :to="edge.node.path.split('--')[0]"
          >
            <div class="row-span-4 grid h-24 w-full place-self-center">
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
            <div class="row-span-5 grid content-end self-stretch">
              <p class="justify-self-center text-clip text-xs font-bold underline lg:text-md">
                {{ edge.node.label }}
              </p>
            </div>
          </g-link>
        </div>
        <Pager
          :info="$page.allPlugins.pageInfo"
          class="pager-container col-span-2 m-4 mx-auto text-black md:col-span-4"
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
    sortBy: "label_lowercase"
    order: ASC
    filter: { isDefault: { eq: true }, pluginType: { eq: "extractor" }, hidden: { ne: true } }
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
