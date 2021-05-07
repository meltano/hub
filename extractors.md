---
layout: page
title: Extractors
permalink: /extractors/
description: Use Meltano to easily extract data out of arbitrary sources (databases, SaaS APIs, and file formats) using Singer taps.
---

Meltano lets you easily extract data out of arbitrary sources (databases, SaaS APIs, and file formats) using [Singer taps](/singer/taps/), which take the role of [your project](https://meltano.com/docs/project.html)'s [extractor plugins](https://meltano.com/docs/plugins.html#extractors).


Extractors for the following sources are currently [discoverable](https://meltano.com/docs/plugins.html#discoverable-plugins) and supported out of the box:

{% include plugin_grid.html plugins=site.data.meltano.extractors %}

To learn more about extracting and [loading](/loaders/) data using Meltano, refer to the [Data Integration (EL) guide](https://meltano.com/docs/integration.html).

## Don't see your source listed here?

If a [Singer tap](/singer/taps/) for your source already exists,
it can easily be [added to your Meltano project as a custom extractor](https://meltano.com/docs/plugin-management.html#custom-plugins).
If not, you can learn how to [create your own from scratch](https://meltano.com/tutorials/create-a-custom-extractor.html).

Once you've got the new extractor working in your project, you can
[add it to the Hub](https://gitlab.com/meltano/hub/-/tree/main/_data/taps).
