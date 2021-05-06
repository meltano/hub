---
layout: page
title: Meltano Extractors
permalink: /extractors/
description: Use Meltano to easily extract data out of arbitrary data sources (databases, SaaS APIs, and file formats) using Singer taps.
---

Meltano lets you easily extract data out of arbitrary data sources (databases, SaaS APIs, and file formats) using [Singer taps](https://www.singer.io/), which take the role of [your project](https://meltano.com/docs/project.html)'s [extractor plugins](https://meltano.com/docs/plugins.html#extractors).


Extractors for the following sources are currently [discoverable](https://meltano.com/docs/plugins.html#discoverable-plugins) and supported out of the box:

- [BigQuery](/extractors/bigquery.html)
- [Bing Ads](/extractors/bing-ads.html)
- [Chargebee](/extractors/chargebee.html)
- [Comma Separated Values (CSV)](/extractors/csv.html)
- [Facebook Ads](/extractors/facebook.html)
- [Fastly](/extractors/fastly.html)
- [GitLab](/extractors/gitlab.html)
- [Google Ads](/extractors/adwords.html)
- [Google Analytics](/extractors/google-analytics.html)
- [Marketo](/extractors/marketo.html)
- [MongoDB](/extractors/mongodb.html)
- [MySQL / MariaDB](/extractors/mysql.html)
- [PostgreSQL](/extractors/postgres.html)
- [Quickbooks](/extractors/quickbooks.html)
- [ReCharge](/extractors/recharge.html)
- [Sage Intacct](/extractors/intacct.html)
- [Salesforce](/extractors/salesforce.html)
- [Shopify](/extractors/shopify.html)
- [Slack](/extractors/slack.html)
- [Spreadsheets Anywhere](/extractors/spreadsheets-anywhere.html) (CSV files and Excel spreadsheets on cloud or local storage)
- [Stripe](/extractors/stripe.html)
- [Zendesk](/extractors/zendesk.html)
- [Zoom](/extractors/zoom.html)

To learn more about extracting and [loading](/loaders/) data using Meltano, refer to the [Data Integration (EL) guide](https://meltano.com/docs/integration.html).

::: tip Don't see your data source listed here?

If a [Singer tap](https://www.singer.io/#taps) for your source already exists,
it can easily be [added to your project as a custom extractor](https://meltano.com/docs/plugin-management.html#custom-plugins).
If not, you can learn how to [create your own from scratch](/tutorials/create-a-custom-extractor.html).

Once you've got the new extractor working in your project, please consider
[contributing its description](https://meltano.com/docs/contributor-guide.html#discoverable-plugins)
to the [index of discoverable plugins](https://meltano.com/docs/plugins.html#discoverable-plugins)
so that it can be added to this page!

:::
