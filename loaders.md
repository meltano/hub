---
layout: page
title: Meltano Loaders
permalink: /loaders/
description: Use Meltano to easily load extracted data into arbitrary data destinations (databases, SaaS APIs, and file formats) using Singer targets.
---

Meltano lets you easily load [extracted](/extractors/) data into arbitrary data destinations (databases, SaaS APIs, and file formats) using [Singer targets](https://www.singer.io/), which take the role of [your project](https://meltano.com/docs/project.html)'s [loader plugins](https://meltano.com/docs/plugins.html#loaders).

Loaders for the following destinations are currently [discoverable](https://meltano.com/docs/plugins.html#discoverable-plugins) and supported out of the box:

- [BigQuery](/loaders/bigquery.html)
- [Comma Separated Values (CSV)](/loaders/csv.html)
- [JSON Lines (JSONL)](/loaders/jsonl.html)
- [PostgreSQL](/loaders/postgres.html)
- [Redshift](/loaders/redshift.html)
- [Snowflake](/loaders/snowflake.html)
- [SQLite](/loaders/sqlite.html)

To learn more about [extracting](/loaders/) and loading data using Meltano, refer to the [Data Integration (EL) guide](https://meltano.com/docs/integration.html).

::: tip Don't see your data destination listed here?

If a [Singer target](https://www.singer.io/#targets) for your destination already exists,
it can easily be [added to your project as a custom loader](https://meltano.com/docs/plugin-management.html#custom-plugins).
If not, you can learn how to [create your own from scratch](https://github.com/singer-io/getting-started/blob/master/docs/RUNNING_AND_DEVELOPING.md#developing-a-target).

Once you've got the new loader working in your project, please consider
[contributing its description](https://meltano.com/docs/contributor-guide.html#discoverable-plugins)
to the [index of discoverable plugins](https://meltano.com/docs/plugins.html#discoverable-plugins)
so that it can be added to this page!

:::
