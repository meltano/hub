<template>
  <Layout>
    <div class="plugins-overview mx-auto">
      <p class="text-3xl py-4">Files</p>
      <p>
        Meltano file plugins allow you to easily add new file resources to your data project. For
        example, Meltano utilities and other plugins can define file plugins that provide
        tool-specific scaffolding, templates, and applicable readme resources.
      </p>
      <div
        class="grid grid-cols-2 md:grid-cols-4 bg-slate-200 rounded-lg p-4 mt-4 md:m-4 gap-4 w-full place-items-stretch"
        role="list"
      >
        <div
          v-for="edge in $page.allPlugins.edges"
          :key="edge.node.id"
          class="grid rounded-md shadow-lg text-slate-800 h-36 hover:bg-slate-100 p-2 md:p-4 bg-white overflow-hidden place-items-center"
        >
          <g-link class="grid w-full h-full" :to="edge.node.path.split('--')[0]">
            <div class="grid align-self-center place-items-center">
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
  name: "FilesPage",
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
    filter: { isDefault: { eq: true }, pluginType: { eq: "file" } }
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
