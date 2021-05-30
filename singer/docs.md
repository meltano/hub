---
layout: page
header: singer
permalink: /singer/docs
description: The Leading Destination for the Singer Community
---

## Commitment to the Singer Community

The Meltano team aims to make MeltanoHub a fantastic resource for members of the [Singer](https://singer.io) Community.
We're fully [embracing Singer](https://meltano.com/docs/#embracing-singer) and MeltanoHub for Singer is a large part of those efforts.

## Development

MeltanoHub is under active development by Meltano. Check out the [main development epic](https://gitlab.com/groups/meltano/-/epics/83) for our roadmap or [view the issues](https://gitlab.com/meltano/hub/-/issues) to understand progress on a specific feature. 

## Standardized Connectors

All taps and targets are pulled from external sources, such as GitHub and GitLab, and are organized into a clean YAML format that has no references to external tools. Learn more about the [architecture of MeltanoHub for Singer here](/singer/docs/#architecture).

All taps and targets available through MeltanoHub are listed on the [Taps](/singer/taps/) and [Targets](/singer/targets/) pages.

Each tap and target is defined in YAML and is validated against a JSON Schema available via [the Hub API](/singer/api/v1/).

### Connector Metadata

Each connector page lists revelant information about the maintainer of the connector along with its maintenance status.

Additionally, metrics such as last update, stars, and open issues and PRs, are pulled from GitHub. These are useful proxy metrics for the quality of a given connector.

## API

* [API Directory](/singer/api/v1)

A listing of all taps and targets is available via the [API](/singer/api/v1) as JSON.
The latest version of these files will always be available at these endpoints:

* [Tap JSON](/singer/taps.json)
* [Target JSON](/singer/targets.json)

These files will also be versioned when changes are made in a backwards-incompatible way. 
The versioned files will be available through the [API](/singer/api/v1/).
Individual YAML files are also available through the individual connector pages or on the [repository](https://gitlab.com/meltano/hub/) building MeltanoHub.

Our expectation is that other tools, including Meltano, will utilize the data available via the API to build their own library of Singer taps and targets.

## Tap and Target SDKs

We've also created an [SDK for Taps](https://gitlab.com/meltano/singer-sdk) that is the best way to build and maintain Singer taps.
We're actively working on an [SDK for Targets](https://gitlab.com/groups/meltano/-/epics/91) due to be launched in June 2021.

Read more about the [launch of the SDK on the Meltano blog](https://meltano.com/blog/2021/04/05/meltano-launches-v0-1-0-of-the-singer-tap-sdk/).

## Singer Spec

We've created a simplified version of the [Singer Specification](/singer/spec) with the goal of making it easier for people new to the Singer ecosystem to understand the spec.

## Architecture

MeltanoHub is built with every part of the Singer ecosystem and Meltano product family. This is a completely open source, end-to-end, production example of Meltano using full-featured Singer connectors. 

We use Meltano itself to pull data from GitHub. View the Meltano project for this effort in the [Hub repository](https://gitlab.com/meltano/hub/-/tree/main/meltano).

Using the SDK, we built a [custom GitHub tap](https://github.com/dataops-tk/tap-github) and a [custom Athena target](https://github.com/aaronsteers/target-athena). Each of these are listed on the Hub as well.

We're using dbt to [manage transformations](https://gitlab.com/meltano/hub/-/tree/main/meltano/transform/transforms/marts/singer) with Athena to aid in curating the data.
