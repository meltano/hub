---
layout: page
title: Loaders
permalink: /loaders/
description: Use Meltano to easily load extracted data into arbitrary destinations (databases, SaaS APIs, and file formats) using Singer targets.
---

Meltano lets you easily load [extracted](/extractors/) data into arbitrary destinations (databases, SaaS APIs, and file formats) using [Singer targets](/singer/targets/), which take the role of [your project](https://meltano.com/docs/project.html)'s [loader plugins](https://meltano.com/docs/plugins.html#loaders).

Loaders for the following destinations are currently [discoverable](https://meltano.com/docs/plugins.html#discoverable-plugins) and supported out of the box:

{% include plugin_grid.html plugins=site.data.meltano.sorted_loaders %}

To learn more about [extracting](/loaders/) and loading data using Meltano, refer to the [Data Integration (EL) guide](https://meltano.com/docs/integration.html).

## Don't see your destination listed here?

If a [Singer target](/singer/targets) for your destination already exists,
it can easily be [added to your project as a custom loader](https://meltano.com/docs/plugin-management.html#custom-plugins).
If not, you can learn how to [create your own from scratch](https://github.com/singer-io/getting-started/blob/master/docs/RUNNING_AND_DEVELOPING.md#developing-a-target).

Once you've got the new loader working in your project, you can
[add it to the Hub](https://gitlab.com/meltano/hub/-/tree/main/_data/targets).
