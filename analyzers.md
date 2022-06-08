---
layout: page
title: Analyzers
permalink: /analyzers/
description: Learn how to analyze your data using Meltano
---

Meltano analyzers are utility plugins that enable you to analyze your data and build reports.

{% assign plugins = site.data.meltano.sorted_utilities %}


{% include plugin_grid.html plugins=plugins search="utilities" %}

## Don't see your analyzer listed here?

Any Python package that exposes an executable can easily be [added to your Meltano project as a custom utility](https://docs.meltano.com/concepts/plugins#utilities).

Once you've got your utility working in your project, you can
[add it to the Hub](https://github.com/meltano/hub/tree/main/_data/meltano/utility).
