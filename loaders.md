---
layout: page
title: Loaders
permalink: /loaders/
description: Use Meltano to easily load extracted data into arbitrary destinations (databases, SaaS APIs, and file formats) using Singer targets.
---

Meltano lets you easily load [extracted](/extractors/) data into arbitrary destinations (databases, SaaS APIs, and file formats) using [Singer targets](/singer/targets/), which take the role of [your project](https://docs.meltano.com/concepts/project)'s [loader plugins](https://docs.meltano.com/concepts/plugins#loaders).
To learn more about [extracting](/loaders/) and loading data using Meltano, refer to the [Data Integration (EL) guide](https://docs.meltano.com/guide/integration).

{% assign plugins = site.data.meltano.sorted_loaders %}

{% include plugin_grid.html plugins=plugins search="loaders" %}

## Don't see your destination listed here?

Any [Singer target](/singer/targets) can easily be [added to your Meltano project as a custom loader](https://docs.meltano.com/guide/plugin-management#custom-plugins).

If a target for your destination doesn't exist yet, you can learn how to [create your own from scratch](https://github.com/singer-io/getting-started/blob/master/docs/RUNNING_AND_DEVELOPING.md#developing-a-target). Once you've got the new loader working in your project, you can
[add it to the Hub](https://github.com/meltano/hub/tree/main/_data/meltano/loaders).
