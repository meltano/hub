---
layout: page
title: Meltano Extractors
permalink: /extractors/
description: Use Meltano to easily extract data out of arbitrary data sources (databases, SaaS APIs, and file formats) using Singer taps.
---

Meltano lets you easily extract data out of arbitrary data sources (databases, SaaS APIs, and file formats) using [Singer taps](https://www.singer.io/), which take the role of [your project](https://meltano.com/docs/project.html)'s [extractor plugins](https://meltano.com/docs/plugins.html#extractors).


Extractors for the following sources are currently [discoverable](https://meltano.com/docs/plugins.html#discoverable-plugins) and supported out of the box:

{% include plugin_grid.html plugins=site.data.meltano.extractors %}

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
