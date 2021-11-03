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

We've also created an [SDK for Taps](https://sdk.meltano.com) that is the best way to build and maintain Singer taps.
We're actively working on an [SDK for Targets](https://gitlab.com/groups/meltano/-/epics/91) due to be launched in June 2021.

Read more about the [launch of the SDK on the Meltano blog](https://meltano.com/blog/2021/04/05/meltano-launches-v0-1-0-of-the-singer-tap-sdk/).

## Singer Spec

We've created a simplified version of the [Singer Specification](/singer/spec) with the goal of making it easier for people new to the Singer ecosystem to understand the spec.


## Singer Connector Capabilities

The Singer Specification does a great job defining how taps and targets should communicate with each other at a high level but there's an additional layer of commonly used patterns and best practices that have emerged from the community which aren't documented in the spec that we're calling "capabilities".
The following is our distilled list of the existing (and some future) capabilities that are commonly used by the Singer Community:

### Tap Specific

#### Catalog

The tap accepts a `--catalog` argument referencing a file that defines the structure of one or many data streams.
For more details see the <a href="{{ "/singer/spec#catalog-files" | prepend: site.baseurl | prepend: site.url }}">Catalog Files section</a> in our Singer Spec interpretation.

#### Properties

The tap accepts the legacy `--properties` argument referencing a file that defines the structure of one or many data streams.
For more details see the <a href="{{ "/singer/spec#catalog-files" | prepend: site.baseurl | prepend: site.url }}">Catalog Files section</a> in our Singer Spec interpretation.

#### Discovery

The tap accepts a `--discovery` argument that is used to generate a catalog files.
For more details see the <a href="{{ "/singer/spec#discovery-mode" | prepend: site.baseurl | prepend: site.url }}">Discovery mode section</a> section in our Singer Spec interpretation.

#### State

The tap accepts a `--state` argument and uses the input in order to run incremental syncs.
For more details see the <a href="{{ "/singer/spec#state-files" | prepend: site.baseurl | prepend: site.url }}">State Files section</a> section in our Singer Spec interpretation.

#### Log Based

This is a database source specific capability which supports reading the transaction logs of a database in order to identify incrementally changed data.
The two common replication techniques are key-based or log-based replication.
Key-based uses a timestamp or incrementing key to detect inserts and updates but not deletes.
Whereas log-based replication uses the database’s binary log files to detect records that have been inserted, updated, or deleted.
Supporting this capability, where applicable, means that targets have the information it needs to delete records in the destination.

#### Test

This capability is still in development, but the goal is to make it easy for connector developers to test locally without having to make a connection to the source systems.
This might be accomplished by implementing utilities that can generate and save test data or make saving and moving real HTTP requests for tests easier.
Join the issue conversation [here](https://gitlab.com/meltano/sdk/-/issues/30)!

### Target Specific

#### Soft Delete

Targets that support this capability implement logic that soft deletes records in the destination, usually by populating a `deleted_at` timestamp field.
The two common techniques for handling deletes in Singer are by using the `ACTIVATE_VERSION` message or using log-based replication on a database that supports it.
Targets commonly implement both soft and hard deletes, in which case the behavior is configurable in the target's config settings.

#### Hard Delete

Similar to the Soft Deletes capability, targets that support the hard delete capability implement logic that removes records from the destination when they receive a notification (via `ACTIVATE_VERSION` or log-based replication) that a record was deleted from the source system.
Targets commonly implement both soft and hard deletes, in which case the behavior is configurable in the target's config settings.

#### Datatype Failsafe

This capability means that the target has a failsafe data type (e.g. string) to ensure safe handling of unparsable or unforseen types.
It's common to find targets in the Singer ecosystem that have a set list of supported types and will throw an exception if they receive anything unexpected.
With this capability supported you can feel comfortable that exceptions will not be raised for unsupported types.

#### Record Flattening

It's common for taps to output nested json data which needs to be flattened by the target in order to be loaded into a columnar format destinations.
For example, the following is a nested json record:

```json
{
  "col_a": {
    "subcol_1": 1,
    "subcol_2": 2
  }
}
```

After flattening it would look like the like this:

```json
{
  "col_a__subcol_1": 1,
  "col_a__subcol_2": 2
}
```

Targets that support this capability also usually accept a configurable `max_level` of flattening to limit iterations of very heavily nested records.

### Either Tap or Target

#### Activate Version

Managing hard deletes in the source system is difficult but the Singer community has developed a technique using a message type called `ACTIVATE_VERSION`.
This isnt a standardized message type in the Singer Spec yet but its currently under review by the [Singer Working Group](https://github.com/MeltanoLabs/Singer-Spec-Working-Group) to be officially added.
Join the issue conversation [here](https://github.com/MeltanoLabs/Singer-Spec-Working-Group/issues/9)!

Imagine the scenario where a key-based incremental sync has completed its initial load and a state bookmark is saved to be used as a filter in the next incremental run.
Then in the source system a record is hard deleted.
On the next incremental sync the tap will have no way of knowing that record was deleted, resulting in stale records that only exist in the destination table.

A simple solution could be to run a full sync everytime and have the target truncate any old records.
But the other challenge is that targets have no way of knowing what sync mode the tap is running in: full table, incremental, or log based.
If the target knew that the tap was running in full table sync mode then it would be able to effectively truncate the existing data and replace it with the newest full sync it receives.

This is where the `ACTIVATE_VERSION` message comes in!
The `ACTIVATE_VERSION` message type is a mechanism that is used in full table sync mode which tells the target to disregard all previously received records and only consider the current version as “active”.
By using this mechanism the sync between the tap and target can properly delete inactive versions of the data in the destination to clean up any stale records that were hard deleted.

Taps that support this capability will send along and `ACTIVATE_VERSION` message (usually generated from the current timestamp) prior to sending the `RECORD` messages on the first full sync and then at the end of each subsequent successful full table sync thereafter.
Targets that support this capability implement logic that removes all non-active records from the destination.

#### Stream Maps

The ability to accept a mapping configuration can be used to do minor transformations to the data between the tap and target.
The capability can be currently be implemented on the tap or target side but will soon be supported in Meltano itself.
This includes things like:
- stream and property aliasing
- duplication and bifurcation of streams
- hashing or anonymizing PII/PHI
- row-level filtering
- suppression of streams or stream properties
- and more…

Taps and targets that support this capability have logic to accept the optional stream_maps config key and do light transformations like those listed above.
This is a built-in capability for SDK-based (>=0.3.0) taps and targets.
See the SDK documentation [here](https://sdk.meltano.com/en/latest/stream_maps.html) for more details and use cases.

#### About

The tap or target accepts an `--about` argument which outputs details about the connector including its capabilities and settings which can be used in programmatically generate UI forms. This information can be output in JSON or Markdown format. 

An example output in json format `--about --format=json` from [target-athena](https://github.com/MeltanoLabs/target-athena) built using the Meltano SDK for Singer:

```json
{
  "name": "target-athena",
  "version": "0.0.1",
  "sdk_version": "0.3.9",
  "capabilities": [
    "target"
  ],
  "settings": {
    "type": "object",
    "properties": {
      "s3_bucket": {
        "type": [
          "string"
        ]
      },
      ...
  }
}
```

#### Batch

This capability is currently in development by the [Singer Working Group](https://github.com/MeltanoLabs/Singer-Spec-Working-Group) to align on a consistent approach for supporting batch sync messages in the Spec or as part of its officially supported patterns.
The capability, which was inspired by [Wise’s Fast Sync feature](https://github.com/transferwise/pipelinewise/tree/e0a8ee15c05f019916f5400158b81de72cf33dc8/pipelinewise/fastsync), has the goal of bypassing some of the performance limitations inherent to the Singer Spec by using the optimized import/export features of modern data warehouses (Snowflake, Redshift, etc.).
For example if a tap and target both had batch support the tap could theoretically know to directly write records to csv files somewhere (i.e. S3) in an ideal format for the target to import, ultimately skipping most of the piping step.
Taking this approach allows connectors to improve performance by both using the source and/or target’s most optimized technique for importing and exporting data while also avoiding the additional costs of serializing, deserializing, and piping each record.
Join the issue conversation [here](https://gitlab.com/meltano/sdk/-/issues/9)!

## Architecture

MeltanoHub is built with every part of the Singer ecosystem and Meltano product family. This is a completely open source, end-to-end, production example of Meltano using full-featured Singer connectors.

We use Meltano itself to pull data from GitHub. View the Meltano project for this effort in the [Hub repository](https://gitlab.com/meltano/hub/-/tree/main/meltano).

Using the SDK, we built a [custom GitHub tap](/singer/taps/github-search) and a [custom Athena target](/singer/targets/target-athena).

We're using dbt to [manage transformations](https://gitlab.com/meltano/hub/-/tree/main/meltano/transform/transforms/marts/singer) with Athena to aid in curating the data.

## Meltano Usage Metrics

Meltano collects [anonymous usage stats](https://meltano.com/docs/settings.html#send-anonymous-usage-stats) using Google Analytics. 
We use this data to learn about the size of our user base and overal feature usage.
This helps us determine the highest impact improvements we can make to Meltano and the Singer ecosystem.

To better support the Meltano and Singer communities, we have started aggregating metrics about the usage of taps and targets within Meltano. 
In line with our value of [Transparency](https://meltano.com/docs/#transparency), we are sharing this data with the communithy to help everyone better understand the overall quality of Singer connectors.

<u>Current Metrics:</u>

- Executions (Last 3 Months): The sum of executions via [`meltano elt`](https://meltano.com/docs/command-line-interface.html#elt) or [`meltano invoke`](https://meltano.com/docs/command-line-interface.html#invoke)) that used the plugin.

- Projects (Last 3 Months): The distinct count of [project IDs](https://meltano.com/docs/settings.html#project-id) that have executed the plugin at least once in the last 3 months.

Note that metrics will only show up on a plugin page if they're non-zero. 

Currently these metrics do not take into account the specific variant of the plugin but rather an aggregation of all variants used under that plugin's namespace. 
This is a limitation of the event data that's being collected. 
For example, [tap-gitlab](/taps/gitlab) has multiple variants ([MeltanoLabs](https://github.com/MeltanoLabs/tap-gitlab), [singer-io](https://github.com/singer-io/tap-gitlab), etc.) which are all rolled up into the parent tap-gitlab namespace.

Since Meltano makes it easy for users to [opt out](https://meltano.com/docs/settings.html#send-anonymous-usage-stats) of sending usage stats we assume that metrics are undercounted.

Checkout the [Meltano Squared](https://gitlab.com/meltano/squared) repository to see how we're using Meltano to extract and aggregate these metrics.
