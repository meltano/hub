---
layout: page
title: Files
permalink: /files/
description: Use Meltano to add file resources to your data project.
---

Meltano file plugins allow you to easily add new file resources to your data project. For example, Meltano utilities and other plugins can define file plugins that provide tool-specific scaffolding, templates, and applicable readme resources. 

{% assign plugins = site.data.meltano.sorted_files %}



{% include plugin_grid.html plugins=plugins search="files" %}


