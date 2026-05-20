<template>
  <Layout>
    <div class="w-full px-4 mx-auto single-plugin-overview max-w-7xl">
      <div class="single-plugin-detail">
        <div class="single-plugin-top-bar">
          <div class="plugin-header">
            <a
              v-if="$page.plugins.domain_url"
              :href="$page.plugins.domain_url"
              target="_blank"
              rel="noopener noreferrer"
              class="plugin-header__logo-box"
            >
              <g-image
                v-if="$page.plugins.logo_url"
                :src="
                  require(`!!assets-loader?width=250&height=200&fit=inside!@logos/${$page.plugins.logo_url.replace(
                    '/assets/logos/',
                    ''
                  )}`)
                "
                class="plugin-header__logo-img"
              />
            </a>
            <div v-else class="plugin-header__logo-box">
              <g-image
                v-if="$page.plugins.logo_url"
                :src="
                  require(`!!assets-loader?width=250&height=200&fit=inside!@logos/${$page.plugins.logo_url.replace(
                    '/assets/logos/',
                    ''
                  )}`)
                "
                class="plugin-header__logo-img"
              />
            </div>
            <div class="plugin-header__content">
              <div class="plugin-header__title-row">
                <p class="plugin-label">{{ $page.plugins.label }}</p>
                <span class="community-pill">Meltano Community</span>
              </div>
              <p class="plugin-variant">
                {{ $page.plugins.name }} ({{ $page.plugins.variant }} variant)
                <span v-if="$page.plugins.quality == 'gold'"
                  ><a href="https://docs.meltano.com/contribute/connectors#connector-quality-matrix"
                    >🥇</a
                  ></span
                >
                <span v-if="$page.plugins.quality == 'silver'"
                  ><a href="https://docs.meltano.com/contribute/connectors#connector-quality-matrix"
                    >🥈</a
                  ></span
                >
                <span v-if="$page.plugins.quality == 'bronze'"
                  ><a href="https://docs.meltano.com/contribute/connectors#connector-quality-matrix"
                    >🥉</a
                  ></span
                >
              </p>
            </div>
          </div>
          <p class="plugin-community-desc">
            Open source connector supported by the Meltano Community, a growing community of over
            5500+ data engineers.
          </p>
          <div class="plugin-community-actions">
            <a
              href="https://github.com/meltano/meltano"
              target="_blank"
              rel="noopener noreferrer"
              class="plugin-action-btn"
            >
              <svg
                width="19"
                height="18"
                viewBox="0 0 19 18"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M8.61305 3.9375C8.2824 3.42006 7.82674 2.99423 7.28814 2.6993C6.74953 2.40438 6.14532 2.24986 5.53125 2.25C5.2581 2.72225 5.09427 3.24973 5.0518 3.79363C5.00934 4.33754 5.08932 4.88404 5.28586 5.39297C4.90107 5.95961 4.69285 6.62758 4.6875 7.3125V7.875C4.6875 8.77011 5.04308 9.62855 5.67601 10.2615C6.30895 10.8944 7.16739 11.25 8.0625 11.25H11.4375C12.3326 11.25 13.1911 10.8944 13.824 10.2615C14.4569 9.62855 14.8125 8.77011 14.8125 7.875V7.3125C14.8072 6.62758 14.5989 5.95961 14.2141 5.39297C14.4107 4.88404 14.4907 4.33754 14.4482 3.79363C14.4057 3.24973 14.2419 2.72225 13.9688 2.25C13.3547 2.24986 12.7505 2.40438 12.2119 2.6993C11.6733 2.99423 11.2176 3.42006 10.887 3.9375H8.61305Z"
                  stroke="#3A64FA"
                  stroke-width="1.5"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M7.5 16.3125V13.5C7.5 12.9033 7.73705 12.331 8.15901 11.909C8.58097 11.4871 9.15326 11.25 9.75 11.25C10.3467 11.25 10.919 11.4871 11.341 11.909C11.7629 12.331 12 12.9033 12 13.5V16.3125"
                  stroke="#3A64FA"
                  stroke-width="1.5"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M7.5 14.625H5.25C4.65326 14.625 4.08097 14.3879 3.65901 13.966C3.23705 13.544 3 12.9717 3 12.375C3 11.7783 2.76295 11.206 2.34099 10.784C1.91903 10.3621 1.34674 10.125 0.75 10.125"
                  stroke="#3A64FA"
                  stroke-width="1.5"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>

              Open source
            </a>
            <a
              href="https://meltano.com/slack"
              target="_blank"
              rel="noopener noreferrer"
              class="plugin-action-btn"
            >
              <svg
                width="18"
                height="18"
                viewBox="0 0 18 18"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M9 7.3125V9H3.9375C3.48995 9 3.06072 8.82221 2.74426 8.50574C2.42779 8.18928 2.25 7.76005 2.25 7.3125C2.25 6.86495 2.42779 6.43572 2.74426 6.11926C3.06072 5.80279 3.48995 5.625 3.9375 5.625H7.3125C7.76005 5.625 8.18928 5.80279 8.50574 6.11926C8.82221 6.43572 9 6.86495 9 7.3125Z"
                  stroke="#3A64FA"
                  stroke-width="1.5"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M9 5.625H7.3125C6.86495 5.625 6.43572 5.44721 6.11926 5.13074C5.80279 4.81428 5.625 4.38505 5.625 3.9375C5.625 3.48995 5.80279 3.06072 6.11926 2.74426C6.43572 2.42779 6.86495 2.25 7.3125 2.25C7.76005 2.25 8.18928 2.42779 8.50574 2.74426C8.82221 3.06072 9 3.48995 9 3.9375V5.625Z"
                  stroke="#3A64FA"
                  stroke-width="1.5"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M10.6875 9H9V3.9375C9 3.48995 9.17779 3.06072 9.49426 2.74426C9.81072 2.42779 10.2399 2.25 10.6875 2.25C11.1351 2.25 11.5643 2.42779 11.8807 2.74426C12.1972 3.06072 12.375 3.48995 12.375 3.9375V7.3125C12.375 7.76005 12.1972 8.18928 11.8807 8.50574C11.5643 8.82221 11.1351 9 10.6875 9Z"
                  stroke="#3A64FA"
                  stroke-width="1.5"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M12.375 9V7.3125C12.375 6.86495 12.5528 6.43572 12.8693 6.11926C13.1857 5.80279 13.6149 5.625 14.0625 5.625C14.5101 5.625 14.9393 5.80279 15.2557 6.11926C15.5722 6.43572 15.75 6.86495 15.75 7.3125C15.75 7.76005 15.5722 8.18928 15.2557 8.50574C14.9393 8.82221 14.5101 9 14.0625 9H12.375Z"
                  stroke="#3A64FA"
                  stroke-width="1.5"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M9 10.6875V9H14.0625C14.5101 9 14.9393 9.17779 15.2557 9.49426C15.5722 9.81072 15.75 10.2399 15.75 10.6875C15.75 11.1351 15.5722 11.5643 15.2557 11.8807C14.9393 12.1972 14.5101 12.375 14.0625 12.375H10.6875C10.2399 12.375 9.81072 12.1972 9.49426 11.8807C9.17779 11.5643 9 11.1351 9 10.6875Z"
                  stroke="#3A64FA"
                  stroke-width="1.5"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M9 12.375H10.6875C11.1351 12.375 11.5643 12.5528 11.8807 12.8693C12.1972 13.1857 12.375 13.6149 12.375 14.0625C12.375 14.5101 12.1972 14.9393 11.8807 15.2557C11.5643 15.5722 11.1351 15.75 10.6875 15.75C10.2399 15.75 9.81072 15.5722 9.49426 15.2557C9.17779 14.9393 9 14.5101 9 14.0625V12.375Z"
                  stroke="#3A64FA"
                  stroke-width="1.5"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M7.3125 9H9V14.0625C9 14.5101 8.82221 14.9393 8.50574 15.2557C8.18928 15.5722 7.76005 15.75 7.3125 15.75C6.86495 15.75 6.43572 15.5722 6.11926 15.2557C5.80279 14.9393 5.625 14.5101 5.625 14.0625V10.6875C5.625 10.2399 5.80279 9.81072 6.11926 9.49426C6.43572 9.17779 6.86495 9 7.3125 9Z"
                  stroke="#3A64FA"
                  stroke-width="1.5"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M5.625 9V10.6875C5.625 11.1351 5.44721 11.5643 5.13074 11.8807C4.81428 12.1972 4.38505 12.375 3.9375 12.375C3.48995 12.375 3.06072 12.1972 2.74426 11.8807C2.42779 11.5643 2.25 11.1351 2.25 10.6875C2.25 10.2399 2.42779 9.81072 2.74426 9.49426C3.06072 9.17779 3.48995 9 3.9375 9H5.625Z"
                  stroke="#3A64FA"
                  stroke-width="1.5"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
              Join Slack community
            </a>
          </div>
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
                            href="https://docs.meltano.com/contribute/connectors#connector-quality-matrix"
                            >🥇</a
                          ></span
                        >
                        <span v-if="variant.node.quality == 'silver'"
                          ><a
                            href="https://docs.meltano.com/contribute/connectors#connector-quality-matrix"
                            >🥈</a
                          ></span
                        >
                        <span v-if="variant.node.quality == 'bronze'"
                          ><a
                            href="https://docs.meltano.com/contribute/connectors#connector-quality-matrix"
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
                      <div class="space-y-2">
                        <div class="flex border-b border-gray-200">
                          <button
                            @click="activeTab = 'modern'"
                            :class="[
                              'px-4 py-2 text-sm font-medium border-b-2 transition-colors',
                              activeTab === 'modern'
                                ? 'border-blue-500 text-blue-600'
                                : 'border-transparent text-gray-500 hover:text-gray-700',
                            ]"
                          >
                            Meltano 3.8+
                          </button>
                          <button
                            @click="activeTab = 'legacy'"
                            :class="[
                              'px-4 py-2 text-sm font-medium border-b-2 transition-colors',
                              activeTab === 'legacy'
                                ? 'border-blue-500 text-blue-600'
                                : 'border-transparent text-gray-500 hover:text-gray-700',
                            ]"
                          >
                            Legacy (All versions)
                          </button>
                        </div>
                        <div v-if="activeTab === 'legacy'">
                          <pre
                            class="prose rounded-md language-bash"
                          ><code>meltano add {{ $page.plugins.pluginType }} {{ $page.plugins.name }}<span v-if="!$page.plugins.isDefault"> --variant {{ $page.plugins.variant }}</span></code></pre>
                        </div>
                        <div v-if="activeTab === 'modern'">
                          <pre
                            class="prose rounded-md language-bash"
                          ><code>meltano add <span v-if="$page.plugins.pluginType === 'extractor' || $page.plugins.pluginType === 'loader' || $page.plugins.pluginType === 'utility'">{{ $page.plugins.name }}</span><span v-else>--plugin-type {{ $page.plugins.pluginType }} {{ $page.plugins.name }}</span><span v-if="!$page.plugins.isDefault"> --variant {{ $page.plugins.variant }}</span></code></pre>
                        </div>
                      </div>
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
              :label="$page.plugins.label"
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
  data() {
    return {
      activeTab: "modern",
    };
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

<style lang="scss">
.single-plugin-top-bar {
  padding: 32px;
  background: #f4f1ff;
  border-radius: 8px;
  border: 1px solid rgba(49, 23, 114, 0.15);
  margin-bottom: 16px;
}

.plugin-header {
  display: flex;
  align-items: flex-start;
  gap: 20px;
  margin-bottom: 24px;

  &__logo-box {
    width: 72px;
    height: 72px;
    min-width: 72px;
    background: #ffffff;
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    padding: 8px;
  }

  &__logo-img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    object-position: center;
    display: block;
  }

  &__content {
    display: flex;
    flex-direction: column;
    gap: 8px;
    padding-top: 6px;
  }

  &__title-row {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
  }
}

.plugin-label {
  font-size: 1.75rem;
  font-weight: 700;
  color: #1d2939;
  margin: 0;
  line-height: 1.2;
  font-family: "Plus Jakarta Sans", sans-serif;
}

.community-pill {
  display: inline-flex;
  align-items: center;
  padding: 4px 12px;
  border-radius: 13px;
  background: #e7ddff;
  color: #4923a9;
  font-size: 0.875rem;
  font-weight: 600;
  white-space: nowrap;
  font-family: "Plus Jakarta Sans", sans-serif;
  flex-shrink: 0;
}

.plugin-variant {
  font-size: 0.9375rem;
  color: #475467;
  margin: 0;
  line-height: 1.5;
}

.plugin-community-desc {
  font-size: 1rem;
  color: #1d2939;
  line-height: 1.6;
  margin: 20px 0 16px;
}

.plugin-community-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 8px;
}

.plugin-action-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 16px;
  border: 1px solid #d0d5dd;
  border-radius: 8px;
  background: #ffffff;
  color: #1d2939 !important;
  font-size: 0.9375rem;
  font-weight: 500;
  text-decoration: none !important;
  font-family: "Inter", sans-serif;
  transition: background-color 0.15s ease;

  &:hover {
    background-color: #f9fafb;
  }

  &__icon {
    width: 18px;
    height: 18px;
    flex-shrink: 0;
  }
}
</style>
