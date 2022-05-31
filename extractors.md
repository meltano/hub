---
layout: page
title: Extractors
permalink: /extractors/
description: Use Meltano to easily extract data out of arbitrary sources (databases, SaaS APIs, and file formats) using Singer taps.
---

Meltano lets you easily extract data out of arbitrary sources (databases, SaaS APIs, and file formats) using [Singer taps](/singer/taps/), which take the role of [your project](https://docs.meltano.com/concepts/project)'s [extractor plugins](https://docs.meltano.com/concepts/plugins#extractors).
To learn more about extracting and [loading](/loaders/) data using Meltano, refer to the [Data Integration (EL) guide](https://docs.meltano.com/integration.html).

{% assign plugins = site.data.meltano.sorted_extractors %}

{% include plugin_grid.html plugins=plugins search="extractors" %}

## Don't see your source listed here?

Any [Singer tap](/singer/taps/) can easily be [added to your Meltano project as a custom extractor](https://docs.meltano.com/plugin-management.html#custom-plugins).

If a tap for your source doesn't exist yet, you can learn how to [create your own from scratch](https://meltano.com/tutorials/create-a-custom-extractor.html). Once you've got the new extractor working in your project, you can
[add it to the Hub](https://gitlab.com/meltano/hub/-/tree/main/_data/taps).
