<template>
  <Layout>
    <div class="w-full mx-auto plugins-overview max-w-7xl">
      <p class="pt-8 pb-4 text-3xl font-bold md:text-5xl font-pjs text-purple">Extractors</p>
      <div class="max-w-3xl mx-auto mb-4">
        <p class="mb-4">
          Meltano lets you easily extract data out of arbitrary sources (databases, SaaS APIs, and
          file formats) using Singer taps, which take the role of your project’s extractor plugins.
        </p>
        <p>
          To learn more about extracting and loading data using Meltano, refer to the
          <a href="https://docs.meltano.com/getting-started/part1" target="_blank" class="underline"
            >Getting Started guide</a
          >.
        </p>
      </div>

      <!-- Accordion -->
      <div class="w-full md:m-4" role="list">
        <div class="px-4 pt-2 mx-4 border rounded-lg bg-white-fade border-white-70">
          <div class="flex flex-col">
            <div class="flex items-center justify-center w-full px-4">
              <h2 class="text-xl font-bold text-center md:text-2xl font-pjs text-purple">
                Most Popular
              </h2>
              <button
                @click="toggleContent"
                class="relative focus:outline-none text-purple top-[5px]"
              >
                <svg
                  :class="chevronClass"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                  width="24"
                  height="24"
                >
                  <path
                    fill-rule="evenodd"
                    d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                    clip-rule="evenodd"
                  />
                </svg>
              </button>
            </div>
            <div class="grid grid-cols-2 gap-4 pb-6 mt-4 md:grid-cols-4" v-if="expanded">
              <div
                v-for="node in topWeightedNodes(8)"
                :key="node.id"
                class="p-2 overflow-hidden border rounded-md text-slate-800 hover:bg-white bg-white-07 md:p-4 border-purple/10"
              >
                <g-link
                  class="grid w-full grid-rows-2 gap-2 align-self-center place-items-center"
                  :to="node.path.split('--')[0]"
                >
                  <div class="block w-full row-span-4 text-center bg-white">
                    <g-image
                      v-if="node.logo_url"
                      :src="
                        require(`!!assets-loader?width=175&height=24&fit=inside!@logos/${node.logo_url.replace(
                          '/assets/logos/',
                          ''
                        )}`)
                      "
                      class="py-2 mx-auto"
                    />
                  </div>
                  <div class="grid content-end self-stretch">
                    <p class="text-xs font-bold text-center lg:text-sm text-clip">
                      {{ node.label }}
                    </p>
                  </div>
                </g-link>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /Accordion -->
      <div
        class="grid w-full grid-cols-2 gap-4 p-4 mt-4 rounded-lg md:grid-cols-4 md:m-4 place-items-stretch"
        role="list"
      >
        <div
          v-for="edge in $page.allPlugins.edges"
          :key="edge.node.id"
          class="h-48 p-2 overflow-hidden border rounded-md text-slate-800 hover:bg-white bg-white-07 md:p-4 border-purple/10"
        >
          <g-link
            class="grid w-full h-40 grid-rows-6 align-self-center place-items-center"
            :to="edge.node.path.split('--')[0]"
          >
            <div class="grid w-full h-24 row-span-4 bg-white place-self-center">
              <g-image
                v-if="edge.node.logo_url"
                :src="
                  require(`!!assets-loader?width=100&height=80&fit=inside!@logos/${edge.node.logo_url.replace(
                    '/assets/logos/',
                    ''
                  )}`)
                "
                class="object-contain place-self-center"
              />
            </div>
            <div class="grid content-end self-stretch row-span-5">
              <p class="text-xs font-bold underline lg:text-md justify-self-center text-clip">
                {{ edge.node.label }}
              </p>
            </div>
          </g-link>
        </div>
        <Pager
          :info="$page.allPlugins.pageInfo"
          class="col-span-2 m-4 mx-auto text-black pager-container md:col-span-4"
          linkClass="pager-container__link px-2.5 py-1 hover:text-sky-300"
          activeLinkClass="bg-blue text-white rounded-full"
        />
      </div>
    </div>
  </Layout>
</template>

<script>
import { Pager } from "gridsome";

export default {
  data() {
    return {
      expanded: true,
    };
  },
  renderTriggerd() {
    this.expanded = this.urlSegments.length === 1;
  },
  name: "ExtractorsPage",
  components: {
    Pager,
  },
  methods: {
    toggleContent() {
      this.expanded = !this.expanded;
    },
    processNodes({ edges }, maxValues, allExecsValues, allProjectsValues) {
      function percentile(x, arr) {
        arr.sort((a, b) => a - b);
        const index = arr.indexOf(x);
        const p = (100 * index) / (arr.length - 1);
        return Math.ceil(p);
      }
      const processedEdges = edges.map(({ node }) => {
        const projectWeightFactor = 2;
        const thisExecs = node.metrics.all_execs;
        const thisProjects = node.metrics.all_projects;
        const allExecsPercentile = percentile(thisExecs, allExecsValues);
        const allProjectsPercentile = percentile(thisProjects, allProjectsValues);
        const weight = allExecsPercentile + allProjectsPercentile * projectWeightFactor;

        return {
          ...node,
          metrics: {
            ...node.metrics,
            ALL_EXECS_PERCENTILE: allExecsPercentile,
            ALL_PROJECTS_PERCENTILE: allProjectsPercentile,
            WEIGHT: weight,
          },
        };
      });
      return processedEdges.sort((a, b) => b.metrics.WEIGHT - a.metrics.WEIGHT);
    },
    topWeightedNodes(num = 8) {
      return this.processedNodes.slice(0, num);
    },
  },
  computed: {
    chevronClass() {
      return this.expanded
        ? "relative bottom-1 transform rotate-180 transition-transform duration-300"
        : "relative bottom-1 transition-transform duration-300";
    },
    processedNodes() {
      return this.processNodes(
        this.$page.mostUsedPlugins,
        this.maxValues,
        this.allExecsValues,
        this.allProjectsValues
      );
    },
    allExecsValues() {
      return this.$page.mostUsedPlugins.edges.map((edge) => edge.node.metrics.all_execs);
    },
    allProjectsValues() {
      return this.$page.mostUsedPlugins.edges.map((edge) => edge.node.metrics.all_projects);
    },
    maxValues() {
      const allExecsValues = this.$page.mostUsedPlugins.edges.map(
        (edge) => edge.node.metrics.all_execs
      );
      const allProjectsValues = this.$page.mostUsedPlugins.edges.map(
        (edge) => edge.node.metrics.all_projects
      );

      const maxAllExecs = Math.max(...allExecsValues.filter((value) => value !== null));
      const maxAllProjects = Math.max(...allProjectsValues.filter((value) => value !== null));
      return { maxAllExecs, maxAllProjects };
    },
  },
};
</script>

<page-query lang="graphql">
query ($page: Int) {
  mostUsedPlugins: allPlugins(
    sortBy: "metrics.all_projects"
    order: DESC
    filter: {
      isDefault: { eq: true }
      pluginType: { eq: "extractor" }
      hidden: { ne: true }
      keywords: { contains: "meltano_sdk" }
      maintenance_status: { eq: "active" }
      metrics: { all_execs: { gt: 0 }, all_projects: { gt: 0 } }
    }
  ) {
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
        metrics {
          all_execs
          all_projects
        }
      }
    }
  }
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
