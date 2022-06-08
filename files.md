---
layout: page
title: Files
permalink: /files/
description: Use Meltano to add file resources to your data project.
---

Meltano file plugins allow you to easily add new file resources to your data project. For example, Meltano utilities and other plugins can define file plugins that provide tool-specific scaffolding, templates, and applicable readme resources. 

{% assign plugins = site.data.meltano.sorted_files %}



{% include plugin_grid.html plugins=plugins search="files" %}

## Don't see your file bundle listed here?

Any [pip-installable package of files](https://docs.meltano.com/concepts/plugins#file-bundles) can easily be [added to your Meltano project as a custom extractor](https://docs.meltano.com/guide/plugin-management#custom-plugins).

Once you've got the new file bundle working in your project, you can
[add it to the Hub](https://github.com/meltano/hub/tree/main/_data/meltano/files).
