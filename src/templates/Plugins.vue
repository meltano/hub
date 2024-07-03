<template>
  <Layout>
    <div class="w-full px-4 mx-auto single-plugin-overview max-w-7xl">
      <div class="single-plugin-detail">
        <div class="single-plugin-top-bar">
          <table>
            <tr>
              <td class="p-5 lg:p-9">
                <a
                  v-if="$page.plugins.domain_url"
                  :href="$page.plugins.domain_url"
                  target="_blank"
                  class="flex justify-center w-24 h-24 bg-white lg:w-48 lg:h-48"
                  rel="noopener noreferrer"
                >
                  <g-image
                    v-if="$page.plugins.logo_url"
                    :src="
                      require(`!!assets-loader?width=250&height=200&fit=inside!@logos/${$page.plugins.logo_url.replace(
                        '/assets/logos/',
                        ''
                      )}`)
                    "
                    style="object-position: center; object-fit: contain"
                  />
                </a>
                <div v-else>
                  <g-image
                    v-if="$page.plugins.logo_url"
                    :src="
                      require(`!!assets-loader?width=250&height=200&fit=inside!@logos/${$page.plugins.logo_url.replace(
                        '/assets/logos/',
                        ''
                      )}`)
                    "
                  />
                </div>
              </td>
              <td>
                <p
                  class="pt-6 pb-4 text-3xl font-bold lg:text-5xl lg:pt-8 lg:pb-6 font-pjs text-purple"
                >
                  {{ $page.plugins.label }}
                </p>
                <p class="text-lg">
                  <code>{{ $page.plugins.name }} ({{ $page.plugins.variant }} variant)</code>
                  <span v-if="$page.plugins.quality == 'gold'"
                    ><a href="https://docs.meltano.com/cloud/connectors#connector-quality-matrix"
                      >🥇</a
                    ></span
                  >
                  <span v-if="$page.plugins.quality == 'silver'"
                    ><a href="https://docs.meltano.com/cloud/connectors#connector-quality-matrix"
                      >🥈</a
                    ></span
                  >
                  <span v-if="$page.plugins.quality == 'bronze'"
                    ><a href="https://docs.meltano.com/cloud/connectors#connector-quality-matrix"
                      >🥉</a
                    ></span
                  >
                </p>
                <p>
                  <b class="font-hg">{{ $page.plugins.description }}</b>
                </p>
              </td>
            </tr>
          </table>
        </div>
        <div class="w-full">
          <div class="flex flex-col-reverse -mx-2 lg:flex-row">
            <div class="w-full px-2 mt-4 lg:w-8/12 lg:mt-0">
              <div class="p-5 content-body">
                <div class="max-w-2xl p-4 rounded xl:max-w-3xl inner-body">
                  <p>
                    The {{ $page.plugins.name }}
                    <a
                      :href="
                        'https://docs.meltano.com/concepts/plugins#' +
                        $page.plugins.pluginTypePlural
                      "
                      >{{ $page.plugins.pluginType }}</a
                    >
                    <span v-if="$page.plugins.pluginType === 'extractor'">
                      pulls data from
                      <a :href="$page.plugins.domain_url">{{ $page.plugins.label }}</a> that can
                      then be sent to a destination using a
                      <g-link to="/loaders">loader</g-link>.</span
                    >
                    <span v-if="$page.plugins.hidden === true">
                      <p class="pt-8 pb-4 text-3xl font-bold" id="hidden-warning">
                        This plugin is deprecated and not recommended for use. Please use another
                        variant.
                      </p>
                    </span>
                    <span
                      v-if="
                        $page.plugins.pluginType === 'extractor' &&
                        $page.plugins.keywords.includes('airbyte_protocol')
                      "
                    >
                      <p class="pt-8 pb-4 text-3xl font-bold" id="airbyte-preview">
                        Airbyte Usage Notice
                      </p>
                      This connector uses
                      <g-link to="https://github.com/meltanolabs/tap-airbyte-wrapper"
                        >tap-airbyte-wrapper</g-link
                      >
                      to call the underlying Airbyte source Docker container. This means
                      <i>you must</i> have <a :href="'https://www.docker.com/'">Docker</a> installed
                      and running prior to usage. We also recommend using Meltano version 2.13.0 or
                      later. <br /><br />
                      Container-based connectors
                      <i>can introduce deployment challenges</i> including the potential need to run
                      Docker-in-Docker (not currently supported by services like AWS ECS, Meltano
                      Cloud, etc. see
                      <a
                        :href="'https://docs.meltano.com/guide/advanced-topics#am-i-able-to-put-my-meltano-project-with-airbyte-connectors-in-production'"
                        >FAQ</a
                      >
                      and
                      <g-link to="https://docs.airbyte.com/deploying-airbyte/on-aws-ecs/"
                        >Airbyte's ECS deployment docs</g-link
                      >
                      for more details). Before using this variant we recommend considering if/how
                      you will be able to deploy container-based connectors to production.
                      <br /><br />
                      For more context on how this Airbyte integration works please checkout out the
                      <a
                        :href="'https://docs.meltano.com/guide/advanced-topics#airbyte-connector-integration-faq'"
                        >FAQ in the Meltano Docs</a
                      >.
                      <br />
                      <!-- For more detailed information on this connector, checkout the link to the documentation on the <a :href="`https://docs.airbyte.com/integrations/sources/${name.replace('tap-','')}`">source connector page</a>. -->
                    </span>
                    <span
                      class="prose"
                      v-if="$page.plugins.pluginType === 'extractor'"
                      v-html="$page.plugins.definition_rendered"
                    ></span>
                    <span v-if="$page.plugins.pluginType === 'loader'">
                      sends data into
                      <a :href="$page.plugins.domain_url">{{ $page.plugins.label }}</a>
                      after it was pulled from a source using an
                      <g-link to="/extractors">extractor</g-link></span
                    >
                    <span v-if="$page.plugins.pluginType === 'transformer'">
                      is a plugin for running SQL-based transformations on data stored in your
                      warehouse.</span
                    >
                    <span v-if="$page.plugins.pluginType === 'orchestrator'">
                      allows for workflows to be programmatically authored, scheduled, and
                      monitored.</span
                    >
                    <span
                      class="prose"
                      v-if="$page.plugins.pluginType === 'utility'"
                      v-html="$page.plugins.definition_rendered"
                    ></span>
                    <span
                      class="prose"
                      v-if="$page.plugins.pluginType === 'file'"
                      v-html="$page.plugins.definition_rendered"
                    ></span>
                    <span v-if="$page.plugins.pluginType === 'mapper'">
                      is a plugin for transforming data between an extractor and a loader. Commonly
                      used for obfuscating, filtering, or removing sensitive data from streams.
                    </span>
                    <span v-if="$page.plugins.pluginType === 'utility' && $page.plugins.ext_repo">
                      <p class="pt-8 pb-4 text-3xl font-bold md:text-5xl font-pjs text-purple">
                        EDK Based Plugin
                      </p>
                      This utility is based on the Meltano Extension Developer Kit (EDK) which is
                      the preferred way to build and add non-Singer plugins to Meltano Hub. For more
                      information about the EDK, please read
                      <a
                        href="https://docs.meltano.com/guide/advanced-topics#extension-developer-kit-edk"
                        >this section of the Meltano docs</a
                      >. If you have any feedback or suggestions, add them to the
                      <g-link to="https://github.com/meltano/edk/">EDK repo</g-link>.
                    </span>
                  </p>
                  <span class="space-y-3" v-if="filteredVariants && filteredVariants.length > 1">
                    <p class="text-2xl">Alternate Implementations</p>
                    <ul class="pl-4 list-disc list-inside">
                      <li v-for="(variant, index) in filteredVariants" v-bind:key="index">
                        <g-link
                          class="tooltip"
                          :to="variant.node.path"
                          v-if="variant.node.path !== $page.plugins.path"
                        >
                          {{ variant.node.maintainer.label }}
                          <div class="tooltip-content">
                            <img
                              alt="Last Commit Date"
                              :src="
                                ((repo) => {
                                  const url = `https://img.shields.io/${repo.type}/last-commit/${repo.user}/${repo.name}?label=Last%20Commit`;

                                  if (!variant.node.keywords.includes('airbyte_protocol')) {
                                    return url;
                                  }

                                  const [path] = repo.url.match(/airbyte-integrations\S+/) ?? [];
                                  return path ? `${url}&path=${path}` : url;
                                })(parsedVariantRepos[variant.node.variant])
                              "
                            />
                          </div>
                        </g-link>
                        <span v-else>{{ variant.node.maintainer.label }}</span>
                        <span v-if="variant.node.isDefault"> (default)</span>
                        <span v-if="variant.node.keywords.includes('meltano_sdk')">
                          <img
                            class="inline pl-2"
                            alt="Built with the Meltano SDK"
                            src="https://img.shields.io/badge/-Meltano%20SDK-blueviolet"
                          />
                        </span>
                        <span v-if="variant.node.quality == 'gold'"
                          ><a
                            href="https://docs.meltano.com/cloud/connectors#connector-quality-matrix"
                            >🥇</a
                          ></span
                        >
                        <span v-if="variant.node.quality == 'silver'"
                          ><a
                            href="https://docs.meltano.com/cloud/connectors#connector-quality-matrix"
                            >🥈</a
                          ></span
                        >
                        <span v-if="variant.node.quality == 'bronze'"
                          ><a
                            href="https://docs.meltano.com/cloud/connectors#connector-quality-matrix"
                            >🥉</a
                          ></span
                        >
                      </li>
                    </ul>
                  </span>
                  <div>
                    <p class="pt-8 pb-4 text-3xl font-bold font-hg" id="getting-started">
                      Getting Started
                    </p>
                    <PluginPrereqSection
                      :plugin="$page.plugins"
                      :plugin_type="$page.plugins.pluginType"
                    />
                    <p class="py-3 text-xl" id="installation">Installation and configuration</p>
                    <ol class="pl-4 list-decimal list-inside">
                      <li>
                        Add the {{ $page.plugins.name }} {{ $page.plugins.pluginType }} to your
                        project using
                        <a href="https://docs.meltano.com/reference/command-line-interface#add">
                          <pre class="inline-code-block"><code>meltano add</code></pre>
                        </a>
                        :
                      </li>
                      <pre
                        class="prose rounded-md language-bash"
                      ><code >meltano add {{ $page.plugins.pluginType }} {{ $page.plugins.name }}<span v-if="!$page.plugins.isDefault"> --variant {{ $page.plugins.variant }}</span></code></pre>
                      <span>
                        <li>
                          Configure the {{ $page.plugins.name }}
                          <a href="#settings">settings</a> using
                          <a
                            href="https://docs.meltano.com/reference/command-line-interface#config"
                          >
                            <pre class="inline-code-block"><code>meltano config</code></pre>
                          </a>
                          :
                        </li>
                        <pre
                          class="prose rounded-md language-bash"
                        ><code >meltano config {{ $page.plugins.name }} set --interactive</code></pre>
                      </span>
                      <span v-if="$page.plugins.pluginType === 'extractor'">
                        <li>
                          Test that extractor settings are valid using
                          <a
                            href="https://docs.meltano.com/reference/command-line-interface#config"
                          >
                            <pre class="inline-code-block"><code>meltano config</code></pre>
                          </a>
                          :
                        </li>
                        <pre
                          class="prose rounded-md language-bash"
                        ><code >meltano config {{ $page.plugins.name }} test</code></pre>
                      </span>
                    </ol>
                    <p class="py-3 text-xl">Next steps</p>
                    <div
                      v-if="$page.plugins.next_steps_rendered"
                      v-html="$page.plugins.next_steps_rendered"
                      class="prose"
                    ></div>
                    <!-- extractors default next steps -->
                    <div v-else-if="$page.plugins.pluginType == 'extractor'">
                      <p>
                        Follow the remaining steps of the
                        <a href="https://docs.meltano.com/getting-started/part1"
                          >Getting Started guide</a
                        >:
                      </p>
                      <ol class="pl-4 list-decimal list-inside">
                        <li>
                          <a
                            href="https://docs.meltano.com/getting-started/part1#select-entities-and-attributes-to-extract"
                            >Select entities and attributes to extract</a
                          >
                        </li>
                        <li>
                          <a href="https://docs.meltano.com/getting-started/part2"
                            >Add a loader to send data to a destination</a
                          >
                        </li>
                        <li>
                          <a
                            href="https://docs.meltano.com/getting-started/part2#run-your-data-integration-el-pipeline"
                            >Run a data integration (EL) pipeline</a
                          >
                        </li>
                      </ol>
                    </div>
                    <!-- loaders default next steps -->
                    <div v-else-if="$page.plugins.pluginType == 'loader'">
                      <p>
                        Follow the remaining steps of the
                        <a href="https://docs.meltano.com/getting-started/part1"
                          >Getting Started guide</a
                        >:
                      </p>
                      <ol class="pl-4 list-decimal list-inside">
                        <li>
                          <a
                            href="https://docs.meltano.com/getting-started/part2#run-your-data-integration-el-pipeline"
                            >Run a data integration (EL) pipeline</a
                          >
                        </li>
                      </ol>
                    </div>
                    <!-- Default transformers next steps -->
                    <div v-else-if="$page.plugins.pluginType == 'transformer'">
                      <p>
                        Follow the remaining steps of the
                        <a href="https://docs.meltano.com/getting-started/part3"
                          >Getting Started guide</a
                        >:
                      </p>
                      <ol class="pl-4 list-decimal list-inside">
                        <li>
                          <a href="https://docs.meltano.com/getting-started/part3">
                            Transform loaded data for analysis
                          </a>
                        </li>
                      </ol>
                    </div>
                    <!-- Default mapper next steps -->
                    <div v-else-if="$page.plugins.pluginType == 'mapper'">
                      <p>
                        Follow the remaining steps of the
                        <a href="https://docs.meltano.com/getting-started/part4"
                          >Getting Started guide</a
                        >:
                      </p>
                      <ol class="pl-4 list-decimal list-inside">
                        <li>
                          <a href="https://docs.meltano.com/getting-started/part4">
                            Inline Data Mapping
                          </a>
                        </li>
                        <li>
                          See the
                          <a href="https://docs.meltano.com/guide/mappers">
                            mappers documentation
                          </a>
                          or the plugin repo's README.md for more details on configuration.
                        </li>
                      </ol>
                    </div>
                    <!-- No next steps defined for this plugin. -->
                    <div v-else></div>
                    <!-- Help section -->
                    <p>
                      If you run into any issues,
                      <a href="#looking-for-help">learn how to get help</a>.
                    </p>
                  </div>
                  <div>
                    <PluginCapabilitiesSection
                      :capabilities="$page.plugins.capabilities"
                      :name="$page.plugins.name"
                      :plugin_type="$page.plugins.pluginType"
                    />
                    <PluginSettingsSection
                      :settings="$page.plugins.settings"
                      :name="$page.plugins.name"
                      :plugin_type_plural="$page.plugins.pluginTypePlural"
                      :variant="$page.plugins.variant"
                      :preamble="$page.plugins.settings_preamble_rendered"
                    />
                    <PluginCommandsSection
                      :commands="$page.plugins.commands"
                      :name="$page.plugins.name"
                      :plugin_type="$page.plugins.pluginType"
                    />
                    <div
                      class="p-2 mt-3 prose"
                      v-if="$page.plugins.usage"
                      v-html="$page.plugins.usage_rendered"
                    ></div>
                    <PluginHelpSection
                      :name="$page.plugins.name"
                      :variant="$page.plugins.variant"
                      :repo="$page.plugins.repo"
                      :plugin_type="$page.plugins.pluginType"
                      :plugin_type_plural="$page.plugins.pluginTypePlural"
                    />
                  </div>
                </div>
              </div>
            </div>
            <PluginSidebar
              :name="$page.plugins.name"
              :domain_url="$page.plugins.domain_url"
              :repo="parsedRepo"
              :maintenance_status="$page.plugins.maintenance_status"
              :keywords="$page.plugins.keywords"
              :variant="$page.plugins.variant"
              :is_default="$page.plugins.isDefault"
              :metrics="$page.plugins.metrics"
              :plugin_type="$page.plugins.pluginType"
              :maintainer="$page.plugins.maintainer"
              :pip_url="$page.plugins.pip_url"
              :airbyte_name="$page.plugins.airbyte_name"
              :ext_repo="$page.plugins.ext_repo"
            />
          </div>
        </div>
      </div>
    </div>
  </Layout>
</template>

<script>
import PluginSidebar from "../components/PluginSidebar.vue";
import PluginSettingsSection from "../components/PluginSettingsSection.vue";
import PluginCommandsSection from "../components/PluginCommandsSection.vue";
import PluginHelpSection from "../components/PluginHelpSection.vue";
import PluginCapabilitiesSection from "../components/PluginCapabilitiesSection.vue";
import PluginPrereqSection from "../components/PluginPrereqSection.vue";

export default {
  metaInfo() {
    return {
      title: this.$page.plugins.name,
      meta: [
        {
          name: "robots",
          content: this.$page.plugins.hidden ? "noindex" : "all",
        },
      ],
    };
  },
  name: "PluginsTemplate",
  components: {
    PluginSidebar,
    PluginSettingsSection,
    PluginCommandsSection,
    PluginHelpSection,
    PluginCapabilitiesSection,
    PluginPrereqSection,
  },
  computed: {
    filteredVariants() {
      return this.$page.variants.edges.filter(
        (variant) => variant.node.pluginType === this.$page.plugins.pluginType
      );
    },
    parsedVariantRepos() {
      return this.filteredVariants.reduce(
        (parsed, variant) => ({
          ...parsed,
          [variant.node.variant]: this.$parseRepo(variant.node.repo),
        }),
        {}
      );
    },
    parsedRepo() {
      return this.$parseRepo(this.$page.plugins.repo);
    },
  },
  methods: {
    $parseRepo(repoUrl) {
      const [user, name] = repoUrl.split("/").slice(3);
      return {
        url: repoUrl,
        type: (() => {
          if (repoUrl.includes("github.com")) return "github";
          if (repoUrl.includes("gitlab.com")) return "gitlab";
          if (repoUrl.includes("bitbucket.org")) return "bitbucket";
          return "";
        })(),
        user,
        name,
      };
    },
  },
};
</script>

<page-query lang="graphql">
query Plugins($path: String!, $name: String!) {
  plugins: plugins(path: $path) {
    id
    description
    definition
    definition_rendered
    label
    name
    airbyte_name
    path
    logo_url
    namespace
    hidden
    next_steps
    next_steps_rendered
    variant
    isDefault
    pluginType
    pluginTypePlural
    pip_url
    repo
    ext_repo
    maintenance_status
    keywords
    domain_url
    capabilities
    settings {
      name
      label
      description
      description_rendered
      kind
      placeholder
      value
    }
    commands {
      name
      executable
      args
      description
    }
    prereq
    prereq_rendered
    quality
    settings_preamble
    settings_preamble_rendered
    usage
    usage_rendered
    metrics {
      all_projects
      all_execs
    }
    maintainer {
      name
      label
      url
    }
  }
  variants: allPlugins(filter: { name: { eq: $name }, hidden: { ne: true } }) {
    edges {
      node {
        name
        path
        variant
        isDefault
        keywords
        pluginType
        quality
        repo
        maintainer {
          name
          label
        }
      }
    }
  }
}
</page-query>

<style lang="scss"></style>
