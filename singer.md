---
layout: page
header: singer
title: Singer Ecosystem
permalink: /singer/
description: The Leading Destination for the Singer Community
---

## Meltano's Commitment to the Singer Community

We aim to make the MeltanoHub a fantastic resource for members of the [Singer](https://singer.io) Community.
As we've detailed in the Meltano handbook, we're fully [embracing Singer](https://meltano.com/docs/#embracing-singer) and this section of the MeltanoHub is part of those efforts.

### Standardized Taps and Targets

We've started by converting all taps and targets compatible with Meltano to a clean YAML format that has no references to external tools.
Our expectation is that other tools, including Meltano, can utilize these definitions to build their own library of Singer-compatible taps and targets.

All taps and targets available through the MeltanoHub are listed here:

* [Singer Taps](/singer/taps/)
* [Singer Targets](/singer/targets/)

Each tap and target is defined in YAML and is validated against a JSON Schema available on [the Hub](/singer/api/v1/schema.json).
The JSON Schema will continue to evolve as we iterate towards a formal launch of the MeltanoHub, after which there will be strong versioning.

We've also compiled all taps and targets into their own JSON files for use by anyone.
The latest version of these files will always be available at these endpoints:

* [Tap JSON](/singer/taps.json)
* [Target JSON](/singer/targets.json)

These files will also be versioned when changes are made in a backwards-incompatible way. 
The versioned files will be available through the [API endpoint](/singer/api/v1/).
Individual YAML files are also available through the individual pages or on the [repository](https://gitlab.com/meltano/hub/) building the MeltanoHub.

### Tap and Target SDKs

We've also created an [SDK for Singer Taps](https://gitlab.com/meltano/singer-sdk) that is the best way to build and maintain Singer-compatible taps.
We're actively working on an [SDK for Singer Targets](https://gitlab.com/groups/meltano/-/epics/91) due to be launched in May 2021.

Read more about the [launch of the SDK on our blog](https://meltano.com/blog/2021/04/05/meltano-launches-v0-1-0-of-the-singer-tap-sdk/).

### Singer Spec

We've created a simplified version of the [Singer Specification](/singer/spec) with the goal of making it easier for people new to the Singer ecosystem to understand the spec.
