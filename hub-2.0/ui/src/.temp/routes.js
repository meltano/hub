const c1 = () => import(/* webpackChunkName: "page--src--templates--utilities-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/templates/Utilities.vue")
const c2 = () => import(/* webpackChunkName: "page--src--templates--extractors-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/templates/Extractors.vue")
const c3 = () => import(/* webpackChunkName: "page--src--templates--loaders-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/templates/Loaders.vue")
const c4 = () => import(/* webpackChunkName: "page--src--templates--files-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/templates/Files.vue")
const c5 = () => import(/* webpackChunkName: "page--src--templates--transformers-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/templates/Transformers.vue")
const c6 = () => import(/* webpackChunkName: "page--src--templates--orchestrators-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/templates/Orchestrators.vue")
const c7 = () => import(/* webpackChunkName: "page--src--pages--utilities-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/Utilities.vue")
const c8 = () => import(/* webpackChunkName: "page--src--pages--transformers-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/Transformers.vue")
const c9 = () => import(/* webpackChunkName: "page--src--pages--orchestrators-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/Orchestrators.vue")
const c10 = () => import(/* webpackChunkName: "page--src--pages--loaders-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/Loaders.vue")
const c11 = () => import(/* webpackChunkName: "page--src--pages--files-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/Files.vue")
const c12 = () => import(/* webpackChunkName: "page--src--pages--extractors-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/Extractors.vue")
const c13 = () => import(/* webpackChunkName: "page--src--pages--404-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/404.vue")
const c14 = () => import(/* webpackChunkName: "page--src--pages--index-vue" */ "/Users/alexmarple/Sites/Meltano/hub/hub-2.0/ui/src/pages/Index.vue")

export default [
  {
    path: "/utilities/sqlfluff/sqlfluff/",
    component: c1
  },
  {
    path: "/extractors/tap-dynamics/zafar-toshpulatov/",
    component: c2
  },
  {
    path: "/extractors/tap-google-analytics/zenkay/",
    component: c2
  },
  {
    path: "/extractors/tap-wordpress-plugin-stats/yoast/",
    component: c2
  },
  {
    path: "/loaders/target-azureblobstorage/shrutikaponde-vc/",
    component: c3
  },
  {
    path: "/loaders/target-bigquery/transferwise/",
    component: c3
  },
  {
    path: "/loaders/target-csv/singer-io/",
    component: c3
  },
  {
    path: "/loaders/target-gsheet/singer-io/",
    component: c3
  },
  {
    path: "/loaders/target-gsheet/tmonks/",
    component: c3
  },
  {
    path: "/loaders/target-magentobi/singer-io/",
    component: c3
  },
  {
    path: "/loaders/target-postgres/transferwise/",
    component: c3
  },
  {
    path: "/loaders/target-redshift/transferwise/",
    component: c3
  },
  {
    path: "/loaders/target-snowflake/transferwise/",
    component: c3
  },
  {
    path: "/loaders/target-stitch/singer-io/",
    component: c3
  },
  {
    path: "/extractors/tap-brightpearl/zookal/",
    component: c2
  },
  {
    path: "/extractors/tap-starshipit/zookal/",
    component: c2
  },
  {
    path: "/extractors/tap-wordpress-reviews/yoast/",
    component: c2
  },
  {
    path: "/extractors/tap-wordpress-stats/yoast/",
    component: c2
  },
  {
    path: "/extractors/tap-adyen/yoast/",
    component: c2
  },
  {
    path: "/extractors/tap-basecone/yoast/",
    component: c2
  },
  {
    path: "/extractors/tap-coosto/yoast/",
    component: c2
  },
  {
    path: "/extractors/tap-megaphone/yujoy/",
    component: c2
  },
  {
    path: "/extractors/tap-paypal/yoast/",
    component: c2
  },
  {
    path: "/extractors/tap-postmark/yoast/",
    component: c2
  },
  {
    path: "/extractors/tap-rest-api-msdk/widen/",
    component: c2
  },
  {
    path: "/extractors/tap-twinfield/yoast/",
    component: c2
  },
  {
    path: "/loaders/target-magentobi/robertjmoore/",
    component: c3
  },
  {
    path: "/extractors/tap-spreadsheets-anywhere/williamqliu/",
    component: c2
  },
  {
    path: "/extractors/tap-autopilot/wcjohnson11/",
    component: c2
  },
  {
    path: "/extractors/tap-hubspot/wcjohnson11/",
    component: c2
  },
  {
    path: "/extractors/tap-mssql/wintersrd/",
    component: c2
  },
  {
    path: "/extractors/tap-s3-csv/valulucchesi/",
    component: c2
  },
  {
    path: "/loaders/target-kinesis/prontopro/",
    component: c3
  },
  {
    path: "/extractors/tap-amazon-ads-dsp/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-autodesk-bim-360/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-google-search-console/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-oracle/visch/",
    component: c2
  },
  {
    path: "/extractors/tap-search-ads/uptilab2/",
    component: c2
  },
  {
    path: "/extractors/tap-sentry/valulucchesi/",
    component: c2
  },
  {
    path: "/loaders/target-azureblobstorage/olehegi/",
    component: c3
  },
  {
    path: "/loaders/target-azureblobstorage/opencolleges/",
    component: c3
  },
  {
    path: "/extractors/tap-amazon-ads-dsp/schonfeld/",
    component: c2
  },
  {
    path: "/extractors/tap-bing-ads/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-campaign-monitor/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-criteo/uptilab2/",
    component: c2
  },
  {
    path: "/extractors/tap-exacttarget/uptilab2/",
    component: c2
  },
  {
    path: "/extractors/tap-forecast/uptilab2/",
    component: c2
  },
  {
    path: "/extractors/tap-google-analytics/transferwise/",
    component: c2
  },
  {
    path: "/extractors/tap-google-sheets/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-harvest-forecast/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-hubspot/uniquelyhonest/",
    component: c2
  },
  {
    path: "/extractors/tap-kwanko/uptilab2/",
    component: c2
  },
  {
    path: "/extractors/tap-linkedin-ads/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-ms-teams/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-referral-saasquatch/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-s3-csv/transferwise/",
    component: c2
  },
  {
    path: "/extractors/tap-sevenrooms/uptilab2/",
    component: c2
  },
  {
    path: "/extractors/tap-snapchat-ads/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-tiktok/uptilab2/",
    component: c2
  },
  {
    path: "/extractors/tap-twitter-ads/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-typo/typo-ai/",
    component: c2
  },
  {
    path: "/extractors/tap-urban-airship/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-workday-raas/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-youtube-analytics/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-zendesk-chat/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-zendesk/twilio-labs/",
    component: c2
  },
  {
    path: "/loaders/target-kinesis/marouane-tradelab/",
    component: c3
  },
  {
    path: "/extractors/tap-3plcentral/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-activecampaign/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-adroll/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-adwords/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-appsflyer/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-asana/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-autopilot/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-bigcommerce/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-braintree/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-campaign-monitor/sbwheeler/",
    component: c2
  },
  {
    path: "/extractors/tap-chargify/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-circle-ci/sisudata/",
    component: c2
  },
  {
    path: "/extractors/tap-closeio/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-codat/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-crossbeam/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-db2/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-deputy/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-dynamodb/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-eloqua/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-eloqua/timvisher/",
    component: c2
  },
  {
    path: "/extractors/tap-emarsys/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-exacttarget/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-exchangeratesapi/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-facebook/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-fixerio/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-freshdesk/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-frontapp/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-fullstory/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-github-org-projects/rossmcdonald/",
    component: c2
  },
  {
    path: "/extractors/tap-github/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-gitlab/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-google-analytics/saidtezel/",
    component: c2
  },
  {
    path: "/extractors/tap-harvest/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-helpscout/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-hubspot/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-hubspot/thoughtchad/",
    component: c2
  },
  {
    path: "/extractors/tap-ilevel/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-impact/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-intercom/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-invoiced/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-jira/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-kafka/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-kafka/transferwise/",
    component: c2
  },
  {
    path: "/extractors/tap-kustomer/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-listrak/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-liveperson/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-liveperson/tomekzbrozek/",
    component: c2
  },
  {
    path: "/extractors/tap-looker/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-lookml/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-mailchimp/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-mailshake/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-mambu/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-marketo/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-mixpanel/transferwise/",
    component: c2
  },
  {
    path: "/extractors/tap-mongodb/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-mongodb/transferwise/",
    component: c2
  },
  {
    path: "/extractors/tap-mssql/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-mysql/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-mysql/transferwise/",
    component: c2
  },
  {
    path: "/extractors/tap-oracle/transferwise/",
    component: c2
  },
  {
    path: "/extractors/tap-ordway/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-pardot/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-pendo/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-pepperjam/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-pipedrive/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-platformpurple/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-postgres/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-postgres/transferwise/",
    component: c2
  },
  {
    path: "/extractors/tap-purecloud/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-quickbase/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-recharge/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-recruitee/tahasadiki/",
    component: c2
  },
  {
    path: "/extractors/tap-responsys/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-revinate/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-saasoptics/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-sailthru/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-salesforce/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-salesforce/transferwise/",
    component: c2
  },
  {
    path: "/extractors/tap-selligent/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-sendgrid/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-sftp/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-shiphero/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-shopify/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-signonsite/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-skubana/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-slack/transferwise/",
    component: c2
  },
  {
    path: "/extractors/tap-sling/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-snowflake/transferwise/",
    component: c2
  },
  {
    path: "/extractors/tap-stripe/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-surveymonkey/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-taboola/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-timebutler/taikonauten/",
    component: c2
  },
  {
    path: "/extractors/tap-toggl/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-trello/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-twilio/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-twilio/transferwise/",
    component: c2
  },
  {
    path: "/extractors/tap-typeform/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-ujet/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-uservoice/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-woocommerce/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-wootric/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-xero/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-yotpo/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-zendesk/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-zendesk/transferwise/",
    component: c2
  },
  {
    path: "/extractors/tap-zoom/singer-io/",
    component: c2
  },
  {
    path: "/extractors/tap-zuora/transferwise/",
    component: c2
  },
  {
    path: "/loaders/target-athena/meltanolabs/",
    component: c3
  },
  {
    path: "/loaders/target-parquet/mirelagrigoras/",
    component: c3
  },
  {
    path: "/loaders/target-parquet/mrtns/",
    component: c3
  },
  {
    path: "/loaders/target-postgres/meltano/",
    component: c3
  },
  {
    path: "/loaders/target-snowflake/meltano/",
    component: c3
  },
  {
    path: "/loaders/target-sqlite/meltano/",
    component: c3
  },
  {
    path: "/loaders/target-sqlite/meltanolabs/",
    component: c3
  },
  {
    path: "/loaders/target-yaml/meltanolabs/",
    component: c3
  },
  {
    path: "/extractors/tap-bling-erp/r4ir4/",
    component: c2
  },
  {
    path: "/extractors/tap-campaign-monitor/radico/",
    component: c2
  },
  {
    path: "/extractors/tap-currencyfreaks/spacecowboy/",
    component: c2
  },
  {
    path: "/extractors/tap-dynamodb/srjonemed/",
    component: c2
  },
  {
    path: "/extractors/tap-facebook-posts/rowanv/",
    component: c2
  },
  {
    path: "/extractors/tap-fastly/splitio/",
    component: c2
  },
  {
    path: "/extractors/tap-hubspot/spacecowboy/",
    component: c2
  },
  {
    path: "/extractors/tap-kafka/stvhanna/",
    component: c2
  },
  {
    path: "/extractors/tap-linkedin-ads/radico/",
    component: c2
  },
  {
    path: "/extractors/tap-liveperson/stvhanna/",
    component: c2
  },
  {
    path: "/extractors/tap-mailgun/streetteam/",
    component: c2
  },
  {
    path: "/extractors/tap-mongodb/stvhanna/",
    component: c2
  },
  {
    path: "/extractors/tap-officernd/saltboxteam/",
    component: c2
  },
  {
    path: "/extractors/tap-okta/rshah-amplify/",
    component: c2
  },
  {
    path: "/extractors/tap-richpanel/richpanel-company/",
    component: c2
  },
  {
    path: "/extractors/tap-slack/richard-clark/",
    component: c2
  },
  {
    path: "/extractors/tap-spreadsheets-anywhere/rfainc/",
    component: c2
  },
  {
    path: "/extractors/tap-sumologic/splitio/",
    component: c2
  },
  {
    path: "/extractors/tap-vnda-ecommerce/r4ir4/",
    component: c2
  },
  {
    path: "/extractors/tap-yotpo/stvhanna/",
    component: c2
  },
  {
    path: "/extractors/tap-bynder/radico/",
    component: c2
  },
  {
    path: "/extractors/tap-csv/robertjmoore/",
    component: c2
  },
  {
    path: "/extractors/tap-customerx/rafaeljusi/",
    component: c2
  },
  {
    path: "/extractors/tap-dynamodb/rpaterson/",
    component: c2
  },
  {
    path: "/extractors/tap-eloqua/radico/",
    component: c2
  },
  {
    path: "/extractors/tap-estoca/r4ir4/",
    component: c2
  },
  {
    path: "/extractors/tap-exactsales/rafaeljusi/",
    component: c2
  },
  {
    path: "/extractors/tap-facebook/reachlocal/",
    component: c2
  },
  {
    path: "/extractors/tap-gleantap/radico/",
    component: c2
  },
  {
    path: "/extractors/tap-grader/reachlocal/",
    component: c2
  },
  {
    path: "/extractors/tap-hubplanner/rangle/",
    component: c2
  },
  {
    path: "/extractors/tap-hubspot/ragbadaskar/",
    component: c2
  },
  {
    path: "/extractors/tap-kustomer/rossbrg/",
    component: c2
  },
  {
    path: "/extractors/tap-listen360/radico/",
    component: c2
  },
  {
    path: "/extractors/tap-mongodb/rudybear/",
    component: c2
  },
  {
    path: "/extractors/tap-process-street/process-street/",
    component: c2
  },
  {
    path: "/extractors/tap-purecloud/rumeau/",
    component: c2
  },
  {
    path: "/extractors/tap-simplifi/reachlocal/",
    component: c2
  },
  {
    path: "/extractors/tap-sling/rfdearborn/",
    component: c2
  },
  {
    path: "/extractors/tap-spreadsheets-anywhere/quickbi/",
    component: c2
  },
  {
    path: "/extractors/tap-surveymonkey/rahimnathwani/",
    component: c2
  },
  {
    path: "/extractors/tap-telemetrics/reachlocal/",
    component: c2
  },
  {
    path: "/extractors/tap-walkscore/radico/",
    component: c2
  },
  {
    path: "/extractors/tap-zendesk/radico/",
    component: c2
  },
  {
    path: "/loaders/target-magentobi/kirill533/",
    component: c3
  },
  {
    path: "/extractors/tap-amazon-mws/pys933/",
    component: c2
  },
  {
    path: "/extractors/tap-auth0/process-street/",
    component: c2
  },
  {
    path: "/extractors/tap-dbt-artifacts/prratek/",
    component: c2
  },
  {
    path: "/extractors/tap-facebook-reviews/packlane/",
    component: c2
  },
  {
    path: "/extractors/tap-facebook/primedata-ai/",
    component: c2
  },
  {
    path: "/extractors/tap-sklik/polar-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-square/pk-sakthivel/",
    component: c2
  },
  {
    path: "/extractors/tap-twitter-streams/pbegle/",
    component: c2
  },
  {
    path: "/extractors/tap-clarabridge/pathlight/",
    component: c2
  },
  {
    path: "/extractors/tap-eventbrite/phillymedia/",
    component: c2
  },
  {
    path: "/extractors/tap-five9/pathlight/",
    component: c2
  },
  {
    path: "/extractors/tap-gorgias/pathlight/",
    component: c2
  },
  {
    path: "/extractors/tap-helpshift/pathlight/",
    component: c2
  },
  {
    path: "/extractors/tap-hubspot/potloc/",
    component: c2
  },
  {
    path: "/extractors/tap-instagram/prratek/",
    component: c2
  },
  {
    path: "/extractors/tap-kafka/pbegle/",
    component: c2
  },
  {
    path: "/extractors/tap-kustomer/pathlight/",
    component: c2
  },
  {
    path: "/extractors/tap-livechat/pathlight/",
    component: c2
  },
  {
    path: "/extractors/tap-maestroqa/pathlight/",
    component: c2
  },
  {
    path: "/extractors/tap-nikabot/phdesign/",
    component: c2
  },
  {
    path: "/extractors/tap-snapengage/pathlight/",
    component: c2
  },
  {
    path: "/extractors/tap-stella/pathlight/",
    component: c2
  },
  {
    path: "/extractors/tap-stripe/prratek/",
    component: c2
  },
  {
    path: "/extractors/tap-workramp/pathlight/",
    component: c2
  },
  {
    path: "/extractors/tap-zuora/ota-insight/",
    component: c2
  },
  {
    path: "/loaders/target-magentobi/isabella232/",
    component: c3
  },
  {
    path: "/extractors/tap-bold/oriskincare/",
    component: c2
  },
  {
    path: "/extractors/tap-dynamodb/onemedical/",
    component: c2
  },
  {
    path: "/extractors/tap-eloqua/onemedical/",
    component: c2
  },
  {
    path: "/loaders/target-airtable/hotgluexyz/",
    component: c3
  },
  {
    path: "/loaders/target-csv/hotgluexyz/",
    component: c3
  },
  {
    path: "/utilities/superset/apache/",
    component: c1
  },
  {
    path: "/extractors/tap-amazon-mws/mmichie/",
    component: c2
  },
  {
    path: "/extractors/tap-anaplan/matthew-skinner/",
    component: c2
  },
  {
    path: "/extractors/tap-ask-nicely/mashey/",
    component: c2
  },
  {
    path: "/extractors/tap-auth0/nickhould/",
    component: c2
  },
  {
    path: "/extractors/tap-bling-erp/muriloo/",
    component: c2
  },
  {
    path: "/extractors/tap-carbon-intensity/meltano/",
    component: c2
  },
  {
    path: "/extractors/tap-chargify/manatees-first/",
    component: c2
  },
  {
    path: "/extractors/tap-google-analytics/meltano/",
    component: c2
  },
  {
    path: "/extractors/tap-google-analytics/meltanolabs/",
    component: c2
  },
  {
    path: "/extractors/tap-google-sheets/matatika/",
    component: c2
  },
  {
    path: "/extractors/tap-kanbanize/n8sty/",
    component: c2
  },
  {
    path: "/extractors/tap-ms-teams/mauricio87/",
    component: c2
  },
  {
    path: "/extractors/tap-paypal/milk-bar/",
    component: c2
  },
  {
    path: "/extractors/tap-persistiq/nickleomartin/",
    component: c2
  },
  {
    path: "/extractors/tap-quaderno/nickleomartin/",
    component: c2
  },
  {
    path: "/extractors/tap-spreadsheets-anywhere/mashey/",
    component: c2
  },
  {
    path: "/extractors/tap-spreadsheets-anywhere/mmeyer/",
    component: c2
  },
  {
    path: "/extractors/tap-vnda-ecommerce/muriloo/",
    component: c2
  },
  {
    path: "/extractors/tap-adwords/meltano/",
    component: c2
  },
  {
    path: "/extractors/tap-appfigures/meowwolf/",
    component: c2
  },
  {
    path: "/extractors/tap-appstore/miroapp/",
    component: c2
  },
  {
    path: "/extractors/tap-athena/meltanolabs/",
    component: c2
  },
  {
    path: "/extractors/tap-auth0/matatika/",
    component: c2
  },
  {
    path: "/extractors/tap-call-cap/llazarovgannett/",
    component: c2
  },
  {
    path: "/extractors/tap-csv/meltano/",
    component: c2
  },
  {
    path: "/extractors/tap-csv/meltanolabs/",
    component: c2
  },
  {
    path: "/extractors/tap-dbt/meltanolabs/",
    component: c2
  },
  {
    path: "/extractors/tap-domo/mashey/",
    component: c2
  },
  {
    path: "/extractors/tap-estoca/muriloo/",
    component: c2
  },
  {
    path: "/extractors/tap-facebook/meltano/",
    component: c2
  },
  {
    path: "/extractors/tap-fastly/meltano/",
    component: c2
  },
  {
    path: "/extractors/tap-github/meltanolabs/",
    component: c2
  },
  {
    path: "/extractors/tap-gitlab/meltano/",
    component: c2
  },
  {
    path: "/extractors/tap-gitlab/meltanolabs/",
    component: c2
  },
  {
    path: "/extractors/tap-gmail/mashey/",
    component: c2
  },
  {
    path: "/extractors/tap-googleads/matatika/",
    component: c2
  },
  {
    path: "/extractors/tap-hubspot/mvaerle/",
    component: c2
  },
  {
    path: "/extractors/tap-insightly/mrtns/",
    component: c2
  },
  {
    path: "/extractors/tap-ireckonu/mashey/",
    component: c2
  },
  {
    path: "/extractors/tap-lotr/mattarderne/",
    component: c2
  },
  {
    path: "/extractors/tap-marketman/mashey/",
    component: c2
  },
  {
    path: "/extractors/tap-marketo/meltano/",
    component: c2
  },
  {
    path: "/extractors/tap-meltano/matatika/",
    component: c2
  },
  {
    path: "/extractors/tap-mongodb/madlittlemods/",
    component: c2
  },
  {
    path: "/extractors/tap-open-library/loeakaodas/",
    component: c2
  },
  {
    path: "/extractors/tap-openweathermap/matatika/",
    component: c2
  },
  {
    path: "/extractors/tap-oracle/mpcarter/",
    component: c2
  },
  {
    path: "/extractors/tap-ordway/mozartdata/",
    component: c2
  },
  {
    path: "/extractors/tap-ordway/mubarakrocky/",
    component: c2
  },
  {
    path: "/extractors/tap-peloton/meltanolabs/",
    component: c2
  },
  {
    path: "/extractors/tap-prometheus/miroapp/",
    component: c2
  },
  {
    path: "/extractors/tap-purecloud/mynarskip/",
    component: c2
  },
  {
    path: "/extractors/tap-salesforce/meltano/",
    component: c2
  },
  {
    path: "/extractors/tap-shipstation/mashey/",
    component: c2
  },
  {
    path: "/extractors/tap-shopify/matatika/",
    component: c2
  },
  {
    path: "/extractors/tap-slack/mashey/",
    component: c2
  },
  {
    path: "/extractors/tap-slack/meltanolabs/",
    component: c2
  },
  {
    path: "/extractors/tap-solarvista/matatika/",
    component: c2
  },
  {
    path: "/extractors/tap-spotify/matatika/",
    component: c2
  },
  {
    path: "/extractors/tap-spreadsheets-anywhere/laurents/",
    component: c2
  },
  {
    path: "/extractors/tap-stackexchange/meltanolabs/",
    component: c2
  },
  {
    path: "/extractors/tap-stripe/meltano/",
    component: c2
  },
  {
    path: "/extractors/tap-surveymonkey/mikedillion/",
    component: c2
  },
  {
    path: "/extractors/tap-thunderboard/matatika/",
    component: c2
  },
  {
    path: "/extractors/tap-treez/mashey/",
    component: c2
  },
  {
    path: "/extractors/tap-trello/matatika/",
    component: c2
  },
  {
    path: "/extractors/tap-zendesk-sell/leag/",
    component: c2
  },
  {
    path: "/extractors/tap-zenefits/mashey/",
    component: c2
  },
  {
    path: "/extractors/tap-zoom/mashey/",
    component: c2
  },
  {
    path: "/files/files-datahub/z3z1ma/",
    component: c4
  },
  {
    path: "/extractors/tap-asana/lambtron/",
    component: c2
  },
  {
    path: "/extractors/tap-chargify/lambtron/",
    component: c2
  },
  {
    path: "/extractors/tap-clover/kalai-wavicle/",
    component: c2
  },
  {
    path: "/extractors/tap-clubspeed/lambtron/",
    component: c2
  },
  {
    path: "/extractors/tap-fixerio/lpillmann/",
    component: c2
  },
  {
    path: "/extractors/tap-iterable/lambtron/",
    component: c2
  },
  {
    path: "/extractors/tap-loopreturns/loopreturns/",
    component: c2
  },
  {
    path: "/extractors/tap-mailchimp/lovepopcards/",
    component: c2
  },
  {
    path: "/extractors/tap-mongodb/luandy64/",
    component: c2
  },
  {
    path: "/extractors/tap-onfleet/lambtron/",
    component: c2
  },
  {
    path: "/extractors/tap-recurly/lambtron/",
    component: c2
  },
  {
    path: "/extractors/tap-square/kalai-wavicle/",
    component: c2
  },
  {
    path: "/extractors/tap-stringee/lamlephamngoc/",
    component: c2
  },
  {
    path: "/extractors/tap-toast/lambtron/",
    component: c2
  },
  {
    path: "/extractors/tap-toggl/lambtron/",
    component: c2
  },
  {
    path: "/loaders/target-parquet/estrategiahq/",
    component: c3
  },
  {
    path: "/loaders/target-postgres/datamill-co/",
    component: c3
  },
  {
    path: "/loaders/target-snowflake/datamill-co/",
    component: c3
  },
  {
    path: "/extractors/tap-amazon-ads-dsp/isabella232/",
    component: c2
  },
  {
    path: "/extractors/tap-anaplan/kdamodaran1/",
    component: c2
  },
  {
    path: "/extractors/tap-apparel-magic/jamespotz/",
    component: c2
  },
  {
    path: "/extractors/tap-dynamodb/krillw/",
    component: c2
  },
  {
    path: "/extractors/tap-idealo-click-report/horze-international/",
    component: c2
  },
  {
    path: "/extractors/tap-insided/karbonhq/",
    component: c2
  },
  {
    path: "/extractors/tap-kafka/koszti/",
    component: c2
  },
  {
    path: "/extractors/tap-kustomer/jeffhuth-bytecode/",
    component: c2
  },
  {
    path: "/extractors/tap-pendo/jeffhuth-bytecode/",
    component: c2
  },
  {
    path: "/extractors/tap-spreadsheets-anywhere/juleshuisman/",
    component: c2
  },
  {
    path: "/extractors/tap-udemy-for-business/immuta/",
    component: c2
  },
  {
    path: "/extractors/tap-zoom/karbonhq/",
    component: c2
  },
  {
    path: "/loaders/target-datadotworld/datadotworld/",
    component: c3
  },
  {
    path: "/loaders/target-gcs/datateer/",
    component: c3
  },
  {
    path: "/loaders/target-gsheet/dmnpignaud/",
    component: c3
  },
  {
    path: "/utilities/great-expectations/great-expectations/",
    component: c1
  },
  {
    path: "/extractors/tap-amazon-ads-dsp/goes-funky/",
    component: c2
  },
  {
    path: "/extractors/tap-amazon-mws/imcallister/",
    component: c2
  },
  {
    path: "/extractors/tap-criteo/jude188/",
    component: c2
  },
  {
    path: "/extractors/tap-deputy/jordanrburger/",
    component: c2
  },
  {
    path: "/extractors/tap-dynamics/integress-inc/",
    component: c2
  },
  {
    path: "/extractors/tap-dynamics/jarobe42/",
    component: c2
  },
  {
    path: "/extractors/tap-dynamodb/jannikweichert/",
    component: c2
  },
  {
    path: "/extractors/tap-eloqua/jjbarberio2/",
    component: c2
  },
  {
    path: "/extractors/tap-feed/jawats/",
    component: c2
  },
  {
    path: "/extractors/tap-ms-teams/isabella232/",
    component: c2
  },
  {
    path: "/extractors/tap-pagerduty/jacksonh/",
    component: c2
  },
  {
    path: "/extractors/tap-pendo/jwalterclark/",
    component: c2
  },
  {
    path: "/extractors/tap-sms/jboltron3000/",
    component: c2
  },
  {
    path: "/extractors/tap-workday-raas/isabella232/",
    component: c2
  },
  {
    path: "/loaders/target-cassandra/coeff/",
    component: c3
  },
  {
    path: "/extractors/tap-awin/horze-international/",
    component: c2
  },
  {
    path: "/extractors/tap-awin/ideavateltd/",
    component: c2
  },
  {
    path: "/extractors/tap-centra/icebug/",
    component: c2
  },
  {
    path: "/extractors/tap-clockify/immuta/",
    component: c2
  },
  {
    path: "/extractors/tap-daisycon/horze-international/",
    component: c2
  },
  {
    path: "/extractors/tap-deputy/isabella232/",
    component: c2
  },
  {
    path: "/extractors/tap-eloqua/isabella232/",
    component: c2
  },
  {
    path: "/extractors/tap-facebook-pages/goes-funky/",
    component: c2
  },
  {
    path: "/extractors/tap-fixerio/isabella232/",
    component: c2
  },
  {
    path: "/extractors/tap-immuta/immuta/",
    component: c2
  },
  {
    path: "/extractors/tap-invoiced/invoiced/",
    component: c2
  },
  {
    path: "/extractors/tap-kafka/isabella232/",
    component: c2
  },
  {
    path: "/extractors/tap-kustomer/isabella232/",
    component: c2
  },
  {
    path: "/extractors/tap-liveperson/isabella232/",
    component: c2
  },
  {
    path: "/extractors/tap-logmeinrescue/isabella232/",
    component: c2
  },
  {
    path: "/extractors/tap-okta/isabella232/",
    component: c2
  },
  {
    path: "/extractors/tap-pendo/isabella232/",
    component: c2
  },
  {
    path: "/extractors/tap-platformpurple/isabella232/",
    component: c2
  },
  {
    path: "/extractors/tap-purecloud/isabella232/",
    component: c2
  },
  {
    path: "/extractors/tap-reviewscouk/ideavateltd/",
    component: c2
  },
  {
    path: "/extractors/tap-sendgrid/isabella232/",
    component: c2
  },
  {
    path: "/extractors/tap-sling/isabella232/",
    component: c2
  },
  {
    path: "/extractors/tap-surveymonkey/horze-international/",
    component: c2
  },
  {
    path: "/extractors/tap-surveymonkey/ichensvmk/",
    component: c2
  },
  {
    path: "/extractors/tap-surveymonkey/isabella232/",
    component: c2
  },
  {
    path: "/extractors/tap-teamwork/immuta/",
    component: c2
  },
  {
    path: "/extractors/tap-yotpo/isabella232/",
    component: c2
  },
  {
    path: "/extractors/tap-zuora/isabella232/",
    component: c2
  },
  {
    path: "/loaders/target-apprise/auto-idm/",
    component: c3
  },
  {
    path: "/extractors/tap-airtable/goes-funky/",
    component: c2
  },
  {
    path: "/extractors/tap-amazon-advertising/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-amazon-mws/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-campaign-monitor/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-chargebee/hotgluexyz/",
    component: c2
  },
  {
    path: "/extractors/tap-csv/hotgluexyz/",
    component: c2
  },
  {
    path: "/extractors/tap-dynamodb/henriblancke/",
    component: c2
  },
  {
    path: "/extractors/tap-eloqua/gdm-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-facebook/hbellala/",
    component: c2
  },
  {
    path: "/extractors/tap-fixerio/haaspt/",
    component: c2
  },
  {
    path: "/extractors/tap-gmail-csv/food-spotter/",
    component: c2
  },
  {
    path: "/extractors/tap-intacct/hotgluexyz/",
    component: c2
  },
  {
    path: "/extractors/tap-kafka/gadget-inc/",
    component: c2
  },
  {
    path: "/extractors/tap-klaviyo/hotgluexyz/",
    component: c2
  },
  {
    path: "/extractors/tap-mixpanel/hotgluexyz/",
    component: c2
  },
  {
    path: "/extractors/tap-netsuite/hotgluexyz/",
    component: c2
  },
  {
    path: "/extractors/tap-pinterest-ads/gthesheep/",
    component: c2
  },
  {
    path: "/extractors/tap-pivotal-tracker/goodeggs/",
    component: c2
  },
  {
    path: "/extractors/tap-procore/hotgluexyz/",
    component: c2
  },
  {
    path: "/extractors/tap-quickbooks/hotgluexyz/",
    component: c2
  },
  {
    path: "/extractors/tap-s3-csv/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-sendinblue/hotgluexyz/",
    component: c2
  },
  {
    path: "/extractors/tap-sevenrooms/hugo4400/",
    component: c2
  },
  {
    path: "/extractors/tap-woocommerce/hotgluexyz/",
    component: c2
  },
  {
    path: "/loaders/target-azureblobstorage/allanw/",
    component: c3
  },
  {
    path: "/loaders/target-bigquery/adswerve/",
    component: c3
  },
  {
    path: "/loaders/target-jsonl/andyh1203/",
    component: c3
  },
  {
    path: "/loaders/target-kinesis/aaimtt/",
    component: c3
  },
  {
    path: "/loaders/target-pardot/anelendata/",
    component: c3
  },
  {
    path: "/extractors/tap-adwords/georgiyolovski/",
    component: c2
  },
  {
    path: "/extractors/tap-autodesk-bim-360/datamill-co/",
    component: c2
  },
  {
    path: "/extractors/tap-awin/gthesheep/",
    component: c2
  },
  {
    path: "/extractors/tap-bazaarvoice/gthesheep/",
    component: c2
  },
  {
    path: "/extractors/tap-bronto/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-dayforce/goodeggs/",
    component: c2
  },
  {
    path: "/extractors/tap-ebay/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-facebook/georgiyolovski/",
    component: c2
  },
  {
    path: "/extractors/tap-holidays/goodeggs/",
    component: c2
  },
  {
    path: "/extractors/tap-lever/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-listrak/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-liveperson/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-mavenlink/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-monday/gthesheep/",
    component: c2
  },
  {
    path: "/extractors/tap-orbit/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-outbrain/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-pagerduty/goodeggs/",
    component: c2
  },
  {
    path: "/extractors/tap-platformpurple/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-purecloud/falek-marcin/",
    component: c2
  },
  {
    path: "/extractors/tap-purecloud/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-ringcentral/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-selligent/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-simplifi/georgiyolovski/",
    component: c2
  },
  {
    path: "/extractors/tap-tableau/gthesheep/",
    component: c2
  },
  {
    path: "/extractors/tap-taboola/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-talkable/gthesheep/",
    component: c2
  },
  {
    path: "/extractors/tap-tickettailor/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-trustpilot/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-uservoice/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-wonolo/goodeggs/",
    component: c2
  },
  {
    path: "/extractors/tap-yotpo/fishtown-analytics/",
    component: c2
  },
  {
    path: "/extractors/tap-aconex/fostersdata/",
    component: c2
  },
  {
    path: "/extractors/tap-acuite/fostersdata/",
    component: c2
  },
  {
    path: "/extractors/tap-bigquery/fixdauto/",
    component: c2
  },
  {
    path: "/extractors/tap-bls/frasermarlow/",
    component: c2
  },
  {
    path: "/extractors/tap-dynamodb/fixdauto/",
    component: c2
  },
  {
    path: "/extractors/tap-eloqua/fauxpasonics/",
    component: c2
  },
  {
    path: "/extractors/tap-eloqua/flopotok/",
    component: c2
  },
  {
    path: "/extractors/tap-fulfil/fulfilio/",
    component: c2
  },
  {
    path: "/extractors/tap-insightly/fostersdata/",
    component: c2
  },
  {
    path: "/extractors/tap-mode/franloza/",
    component: c2
  },
  {
    path: "/extractors/tap-netlify/franloza/",
    component: c2
  },
  {
    path: "/extractors/tap-newrelic/fixdauto/",
    component: c2
  },
  {
    path: "/extractors/tap-powerbi-metadata/dataops-tk/",
    component: c2
  },
  {
    path: "/extractors/tap-quickbase/flash716/",
    component: c2
  },
  {
    path: "/extractors/tap-servicem8/fostersdata/",
    component: c2
  },
  {
    path: "/extractors/tap-signonsite/fostersdata/",
    component: c2
  },
  {
    path: "/extractors/tap-spreadsheets-anywhere/ets/",
    component: c2
  },
  {
    path: "/extractors/tap-twitter-ads/dreamdata-io/",
    component: c2
  },
  {
    path: "/extractors/tap-yotpo/flopotok/",
    component: c2
  },
  {
    path: "/extractors/tap-agilecrm/dreamdata-io/",
    component: c2
  },
  {
    path: "/extractors/tap-chargebee/envoy/",
    component: c2
  },
  {
    path: "/extractors/tap-clubhouse/envoy/",
    component: c2
  },
  {
    path: "/extractors/tap-confluence/edgarrmondragon/",
    component: c2
  },
  {
    path: "/extractors/tap-density/envoy/",
    component: c2
  },
  {
    path: "/extractors/tap-dynamics/datamill-co/",
    component: c2
  },
  {
    path: "/extractors/tap-dynamics/dreamdata-io/",
    component: c2
  },
  {
    path: "/extractors/tap-eloqua/datamill-co/",
    component: c2
  },
  {
    path: "/extractors/tap-eloqua/erikogan/",
    component: c2
  },
  {
    path: "/extractors/tap-exacttarget/estrategiahq/",
    component: c2
  },
  {
    path: "/extractors/tap-fixerio/ebunt/",
    component: c2
  },
  {
    path: "/extractors/tap-fixerio/einartg/",
    component: c2
  },
  {
    path: "/extractors/tap-google-sheets/dcaribou/",
    component: c2
  },
  {
    path: "/extractors/tap-kustomer/emrom1008/",
    component: c2
  },
  {
    path: "/extractors/tap-linkedin-ads/dedicatedtodata/",
    component: c2
  },
  {
    path: "/extractors/tap-parquet/dataops-tk/",
    component: c2
  },
  {
    path: "/extractors/tap-purecloud/eltonarodrigues/",
    component: c2
  },
  {
    path: "/extractors/tap-readthedocs/edgarrmondragon/",
    component: c2
  },
  {
    path: "/extractors/tap-slack/envoy/",
    component: c2
  },
  {
    path: "/extractors/tap-webcrm/dreamdata-io/",
    component: c2
  },
  {
    path: "/extractors/tap-abcfinancial/dmzobel/",
    component: c2
  },
  {
    path: "/extractors/tap-aws-cost-explorer/albert-marrero/",
    component: c2
  },
  {
    path: "/extractors/tap-clickcast/datateer/",
    component: c2
  },
  {
    path: "/extractors/tap-contentful/dmzobel/",
    component: c2
  },
  {
    path: "/extractors/tap-fabdb/dwallace0723/",
    component: c2
  },
  {
    path: "/extractors/tap-google-search-console/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-hellobaton/dluftspring/",
    component: c2
  },
  {
    path: "/extractors/tap-kustomer/cdolan-summersalt/",
    component: c2
  },
  {
    path: "/extractors/tap-kustomer/drueffect/",
    component: c2
  },
  {
    path: "/extractors/tap-pendo/diegobatt/",
    component: c2
  },
  {
    path: "/extractors/tap-purecloud/drewbanin/",
    component: c2
  },
  {
    path: "/extractors/tap-redash/domb16/",
    component: c2
  },
  {
    path: "/extractors/tap-redshift/datadotworld/",
    component: c2
  },
  {
    path: "/extractors/tap-surveymonkey/danladd/",
    component: c2
  },
  {
    path: "/transformers/dbt-bigquery/dbt-labs/",
    component: c5
  },
  {
    path: "/transformers/dbt-postgres/dbt-labs/",
    component: c5
  },
  {
    path: "/transformers/dbt-redshift/dbt-labs/",
    component: c5
  },
  {
    path: "/transformers/dbt-snowflake/dbt-labs/",
    component: c5
  },
  {
    path: "/utilities/datahub/datahub-project/",
    component: c1
  },
  {
    path: "/extractors/singer-tap-zenhub/chillu/",
    component: c2
  },
  {
    path: "/extractors/tap-billwerk/bi-media/",
    component: c2
  },
  {
    path: "/extractors/tap-chargify/chrishumphries/",
    component: c2
  },
  {
    path: "/extractors/tap-chatitive/codyss/",
    component: c2
  },
  {
    path: "/extractors/tap-crossbeam/b-ryan/",
    component: c2
  },
  {
    path: "/extractors/tap-dynamodb/cosimon/",
    component: c2
  },
  {
    path: "/extractors/tap-forecast/cguimont/",
    component: c2
  },
  {
    path: "/extractors/tap-google-sheets/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-gorgias/brooklyn-data/",
    component: c2
  },
  {
    path: "/extractors/tap-greenhouse/codyss/",
    component: c2
  },
  {
    path: "/extractors/tap-hubspot/cdchan/",
    component: c2
  },
  {
    path: "/extractors/tap-klaviyo/codyss/",
    component: c2
  },
  {
    path: "/extractors/tap-linkedin-ads/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-mongodb/checkr/",
    component: c2
  },
  {
    path: "/extractors/tap-ms-teams/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-mssql/cmoresid/",
    component: c2
  },
  {
    path: "/extractors/tap-officernd/cschouten/",
    component: c2
  },
  {
    path: "/extractors/tap-outreach/cmbramwell/",
    component: c2
  },
  {
    path: "/extractors/tap-pendo/alisa-aylward-toast/",
    component: c2
  },
  {
    path: "/extractors/tap-rakuten/chrisgoddard/",
    component: c2
  },
  {
    path: "/extractors/tap-rickandmorty/clrcrl/",
    component: c2
  },
  {
    path: "/extractors/tap-rockgympro/cinchio/",
    component: c2
  },
  {
    path: "/extractors/tap-sendgrid/codyss/",
    component: c2
  },
  {
    path: "/extractors/tap-sleeper/collinprather/",
    component: c2
  },
  {
    path: "/extractors/tap-smartsheet/brooklyn-data/",
    component: c2
  },
  {
    path: "/extractors/tap-snapchat-ads/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-twitter-ads/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-youtube-analytics/bytecodeio/",
    component: c2
  },
  {
    path: "/transformers/dbt/dbt-labs/",
    component: c5
  },
  {
    path: "/extractors/tap-3plcentral/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-activecampaign/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-amazon-mws/adswerve/",
    component: c2
  },
  {
    path: "/extractors/tap-chargify/andylu-test/",
    component: c2
  },
  {
    path: "/extractors/tap-dynamics/bellyfat/",
    component: c2
  },
  {
    path: "/extractors/tap-dynamics/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-frontapp/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-harvest-forecast/assembleinc/",
    component: c2
  },
  {
    path: "/extractors/tap-helpscout/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-ilevel/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-impact/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-intercom/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-kustomer/beamtech/",
    component: c2
  },
  {
    path: "/extractors/tap-kustomer/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-looker/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-lookml/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-mailshake/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-mambu/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-mercadopago/a-rusi/",
    component: c2
  },
  {
    path: "/extractors/tap-mixpanel/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-pendo/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-pepperjam/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-recharge/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-revinate/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-saasoptics/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-sailthru/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-sftp/bonobos/",
    component: c2
  },
  {
    path: "/extractors/tap-skubana/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-spreadsheets-anywhere/andrewcstewart/",
    component: c2
  },
  {
    path: "/extractors/tap-strava/briansloane/",
    component: c2
  },
  {
    path: "/extractors/tap-thinkific/birdiecare/",
    component: c2
  },
  {
    path: "/extractors/tap-twilio/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-twitter/bernietai/",
    component: c2
  },
  {
    path: "/extractors/tap-typeform/albert-marrero/",
    component: c2
  },
  {
    path: "/extractors/tap-typeform/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-ujet/bytecodeio/",
    component: c2
  },
  {
    path: "/extractors/tap-yotpo/bombas/",
    component: c2
  },
  {
    path: "/extractors/tap-bigquery/anelendata/",
    component: c2
  },
  {
    path: "/extractors/tap-chargify/angaza/",
    component: c2
  },
  {
    path: "/extractors/tap-clickup/autoidm/",
    component: c2
  },
  {
    path: "/extractors/tap-dynamodb/ahuynh3/",
    component: c2
  },
  {
    path: "/extractors/tap-exchangeratehost/anelendata/",
    component: c2
  },
  {
    path: "/extractors/tap-fixerio/angaza/",
    component: c2
  },
  {
    path: "/extractors/tap-hubspot/anthonyp/",
    component: c2
  },
  {
    path: "/extractors/tap-indeed/aroder/",
    component: c2
  },
  {
    path: "/extractors/tap-kanbanize/ashalan/",
    component: c2
  },
  {
    path: "/extractors/tap-pubg/autoidm/",
    component: c2
  },
  {
    path: "/extractors/tap-saasoptics/anelendata/",
    component: c2
  },
  {
    path: "/extractors/tap-surveymonkey/abij/",
    component: c2
  },
  {
    path: "/extractors/tap-webcrawl/anelendata/",
    component: c2
  },
  {
    path: "/files/files-dbt-bigquery/meltano/",
    component: c4
  },
  {
    path: "/files/files-dbt-postgres/meltano/",
    component: c4
  },
  {
    path: "/files/files-dbt-redshift/meltano/",
    component: c4
  },
  {
    path: "/files/files-dbt-snowflake/meltano/",
    component: c4
  },
  {
    path: "/files/files-docker-compose/meltano/",
    component: c4
  },
  {
    path: "/files/files-gitlab-ci/meltano/",
    component: c4
  },
  {
    path: "/files/files-great-expectations/meltano/",
    component: c4
  },
  {
    path: "/files/files-airflow/meltano/",
    component: c4
  },
  {
    path: "/files/files-dbt/meltano/",
    component: c4
  },
  {
    path: "/files/files-docker/meltano/",
    component: c4
  },
  {
    path: "/orchestrators/airflow/apache/",
    component: c6
  },
  {
    path: "/utilities/:page(\\d+)?/",
    component: c7
  },
  {
    path: "/transformers/:page(\\d+)?/",
    component: c8
  },
  {
    path: "/orchestrators/:page(\\d+)?/",
    component: c9
  },
  {
    path: "/loaders/:page(\\d+)?/",
    component: c10
  },
  {
    path: "/files/:page(\\d+)?/",
    component: c11
  },
  {
    path: "/extractors/:page(\\d+)?/",
    component: c12
  },
  {
    name: "404",
    path: "/404/",
    component: c13
  },
  {
    name: "home",
    path: "/",
    component: c14
  },
  {
    name: "*",
    path: "*",
    component: c13
  }
]
