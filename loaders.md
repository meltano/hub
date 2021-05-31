---
layout: page
title: Loaders
permalink: /loaders/
description: Use Meltano to easily load extracted data into arbitrary destinations (databases, SaaS APIs, and file formats) using Singer targets.
---

Meltano lets you easily load [extracted](/extractors/) data into arbitrary destinations (databases, SaaS APIs, and file formats) using [Singer targets](/singer/targets/), which take the role of [your project](https://meltano.com/docs/project.html)'s [loader plugins](https://meltano.com/docs/plugins.html#loaders).
To learn more about [extracting](/loaders/) and loading data using Meltano, refer to the [Data Integration (EL) guide](https://meltano.com/docs/integration.html).

{% assign targets_count = site.data.targets.size %}
{% assign plugins = site.data.meltano.sorted_loaders %}
Meltano supports Singer targets for [{{targets_count}} different destinations](/singer/targets/) and
supports the following {{plugins.size}} [out of the box](https://meltano.com/docs/plugins.html#discoverable-plugins):

{% assign custom_targets_count = targets_count | minus: plugins.size %}
{% if custom_targets_count > 0 %}
{% capture more_title %} View {{custom_targets_count}} more targets {% endcapture %}
{% include plugin_grid.html plugins=plugins more_url="/singer/targets" more_title=more_title more_description="All are supported as custom loaders" %}
{% else %}
{% include plugin_grid.html plugins=plugins %}
{% endif %}

## Don't see your destination listed here?

Any [Singer target](/singer/targets) can easily be [added to your Meltano project as a custom loader](https://meltano.com/docs/plugin-management.html#custom-plugins).

If a target for your destination doesn't exist yet, you can learn how to [create your own from scratch](https://github.com/singer-io/getting-started/blob/master/docs/RUNNING_AND_DEVELOPING.md#developing-a-target). Once you've got the new loader working in your project, you can
[add it to the Hub](https://gitlab.com/meltano/hub/-/tree/main/_data/targets).
