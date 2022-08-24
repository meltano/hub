<template>
  <Layout>
    <div class="plugins-overview">
      <h1>Files</h1>
      <p>
        Meltano file plugins allow you to easily add new file resources to your data project. For
        example, Meltano utilities and other plugins can define file plugins that provide
        tool-specific scaffolding, templates, and applicable readme resources.
      </p>
      <ul class="plugins-list">
        <li v-for="edge in $page.allFiles.edges" :key="edge.node.id" class="page-single-plugin">
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
              <pre><code>{{ edge.node.name }}</code></pre>
            </h2>
          </g-link>
        </li>
        <Pager
          :info="$page.allFiles.pageInfo"
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
  name: "FilesPage",
  components: {
    Pager,
  },
};
</script>

<page-query lang="graphql">
query ($page: Int) {
  allFiles(perPage: 100, page: $page, sortBy: "label", order: ASC) @paginate {
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
