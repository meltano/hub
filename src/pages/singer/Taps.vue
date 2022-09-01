<template>
  <Layout>
    <div class="plugins-overview">
      <h1>Taps</h1>
      <p>
        <a href="https://www.singer.io/">Singer</a> taps and targets can be used together to pull data from <g-link to="/singer/taps">any source</g-link> and send it to any <g-link to="/singer/targets">destination</g-link>. All taps listed here can be used standalone, or as <g-link to="/extractors">extractors</g-link> in <a href="https://www.meltano.com">Meltano</a>.
      </p>
      <ul class="plugins-list">
        <li
          v-for="edge in $page.allExtractors.edges"
          :key="edge.node.id"
          class="page-single-plugin"
        >
          <g-link :to="edge.node.path">
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
  name: "SingerTapsPage",
  components: {
    Pager,
  },
};
</script>

<page-query lang="graphql">
query ($page: Int) {
  allExtractors(perPage: 100, page: $page, sortBy: "label", order: ASC) @paginate {
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