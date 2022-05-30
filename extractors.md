---
layout: page
title: Extractors
permalink: /extractors/
description: Use Meltano to easily extract data out of arbitrary sources (databases, SaaS APIs, and file formats) using Singer taps.
---

Meltano lets you easily extract data out of arbitrary sources (databases, SaaS APIs, and file formats) using [Singer taps](/singer/taps/), which take the role of [your project](https://docs.meltano.com/concepts/project)'s [extractor plugins](https://docs.meltano.com/concepts/plugins#extractors).
To learn more about extracting and [loading](/loaders/) data using Meltano, refer to the [Data Integration (EL) guide](https://docs.meltano.com/integration.html).


<h1>
  <a href="/singer">Singer Ecosystem</a>
</h1>
<p>
  If you're here to learn more about the
  <a href="/singer">Singer ecosystem</a>, check out one of these resources:
</p>

<ul class="button-grid two-columns">
  <li>
    <a href="https://sdk.meltano.com" target="_blank">
      <strong>SDK for Taps &amp; Targets</strong>

      <p>
        Learn more about building Singer taps and targets for new sources and
        destinations
      </p>
    </a>
  </li>
  <li>
    <a href="/singer/spec">
      <strong>Singer Spec</strong>

      <p>
        Learn more about the Singer specification for open source data
        connectors
      </p>
    </a>
  </li>
  <li>
    <a href="/singer#api-resources">
      <strong>API Directory</strong>
      <p>
        Learn more about the API resources available for the entire Singer
        community
      </p>
    </a>
  </li>
  <li>
    <a href="/singer/docs">
      <strong>Documentation</strong>
      <p>
        Learn more about the details and architecture of MeltanoHub for Singer
      </p>
    </a>
  </li>
</ul>

{% assign plugins = site.data.meltano.sorted_extractors %}

{% include plugin_grid.html plugins=plugins search="extractors" %}

## Don't see your source listed here?

Any [Singer tap](/singer/taps/) can easily be [added to your Meltano project as a custom extractor](https://docs.meltano.com/plugin-management.html#custom-plugins).

If a tap for your source doesn't exist yet, you can learn how to [create your own from scratch](https://meltano.com/tutorials/create-a-custom-extractor.html). Once you've got the new extractor working in your project, you can
[add it to the Hub](https://gitlab.com/meltano/hub/-/tree/main/_data/taps).
