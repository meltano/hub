---
layout: page
title: Singer Taps
header: singer
permalink: /singer/taps/
description: Use Meltano to easily extract data out of arbitrary sources (databases, SaaS APIs, and file formats) using Singer taps.
---

[Singer](https://www.singer.io/) taps and targets can be used together to pull data from [any source](https://hub.meltano.com/singer/taps/) and send it to [any destination](https://hub.meltano.com/singer/targets/).
All taps listed here can be used standalone, or as [extractors](https://hub.meltano.com/extractors/) in [Meltano](https://meltano.com/).

{% assign plugins = site.data.meltano.sorted_extractors %}

{% include plugin_grid.html plugins=plugins search="taps" %}

## Don't see your source listed here?

We are working to add all taps in the ecosystem to MeltanoHub.

If a tap for your source doesn't exist yet, you can
create one yourself using the
[SDK](https://sdk.meltano.com) and then [click here](https://github.com/meltano/hub/issues/new) to submit
your tap to be listed on MeltanoHub. 

Any [Singer tap](/singer/targets) can easily be [added to your Meltano project as a custom extractor](https://docs.meltano.com/plugin-management.html#custom-plugins).
If a tap for your source doesn't exist yet, you can learn how to [create your own from scratch](https://github.com/singer-io/getting-started/blob/master/docs/RUNNING_AND_DEVELOPING.md#developing-a-tap). Once you've got the new extractor working in your project, you can
[add it to the Hub](https://github.com/meltano/hub/tree/main/_data/meltano/extractors).

Don’t want to build the tap yourself? These
[partners](https://meltano.com/partners/) can help.
