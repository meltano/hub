---
layout: page
title: Singer Targets
header: singer
permalink: /singer/targets/
description: Use Meltano to easily load extracted data into arbitrary destinations (databases, SaaS APIs, and file formats) using Singer targets.
---

[Singer](https://www.singer.io/) taps and targets can be used together to pull data from [any source](https://hub.meltano.com/singer/taps/) and send it to [any destination](https://hub.meltano.com/singer/targets/).
All targets listed here can be used standalone, or as [loaders](https://hub.meltano.com/loaders/) in [Meltano](https://meltano.com/).

{% assign plugins = site.data.meltano.sorted_loaders %}

{% include plugin_grid.html plugins=plugins search="targets" %}

## Don't see your target listed here?

We are working to add all targets in the ecosystem to MeltanoHub.

If a target for your destination doesn't exist yet, you can
create one yourself using the
[SDK](https://sdk.meltano.com) and then [click here](https://gitlab.com/meltano/hub/-/issues/new?issuable_template=Add%20New%20Singer%20Connector) to submit
your target to be listed on MeltanoHub. 

Any [Singer target](/singer/targets) can easily be [added to your Meltano project as a custom loader](https://docs.meltano.com/plugin-management.html#custom-plugins).
If a target for your destination doesn't exist yet, you can learn how to [create your own from scratch](https://github.com/singer-io/getting-started/blob/master/docs/RUNNING_AND_DEVELOPING.md#developing-a-target). Once you've got the new loader working in your project, you can
[add it to the Hub](https://gitlab.com/meltano/hub/-/tree/main/_data/meltano/loaders/).

Don’t want to build the target yourself? These
[partners](https://meltano.com/partners/) can help.
