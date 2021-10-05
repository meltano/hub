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

The Singer Specification does a great job defining how taps and targets should communicate with each other at a high level but there's an additional layer of commonly used patterns and best practices that have emerged from the community which aren't documented in the spec that we're calling "capabilities". The following is our distilled list of the existing (and some future) capabilities that are commonly used by the Singer Community:

### Tap Specific

<a id="catalog"></a>
#### Catalog
The tap accepts a `--catalog` argument referencing a file that defines the structure of one or many data streams. For more details see the <a href="{{ "/singer/spec#catalogfiles" | prepend: site.baseurl | prepend: site.url }}">Catalog Files section</a> in our Singer Spec interpretation.

<a id="cap-catalog"></a>
#### Properties
The tap accepts the legacy `--properties` argument referencing a file that defines the structure of one or many data streams. For more details see the <a href="{{ "/singer/spec#catalogfiles" | prepend: site.baseurl | prepend: site.url }}">Catalog Files section</a> in our Singer Spec interpretation.

<a id="cap-discovery"></a>
#### Discovery Mode
The tap accepts a `--discovery` argument that is used to generate a catalog files. For more details see the <a href="{{ "/singer/spec#discoverymode" | prepend: site.baseurl | prepend: site.url }}">Discovery mode section</a> section in our Singer Spec interpretation.

<a id="cap-state"></a>
#### State
The tap accepts a `--state` argument and uses the input in order to run incremental syncs. For more details see the <a href="{{ "/singer/spec#statefiles" | prepend: site.baseurl | prepend: site.url }}">State Files section</a> section in our Singer Spec interpretation.

<a id="cap-logbased"></a>
#### Log Based Replication
This is a database source specific capability which supports reading the transaction logs of a database in order to identify incrementally changed data. The two common replication techniques are key-based or log-based replication. Key-based uses a timestamp or incrementing key to detect inserts and updates but not deletes. Whereas log-based replication uses the database’s binary log files to detect records that have been inserted, updated, or deleted. Supporting this capability, where applicable, means that targets have the information it needs to delete records in the destination.

<a id="cap-demomode"></a>
#### Demo Mode
This capability is still in development, but the goal is to make it easy for connector developers to test locally without having to make a connection to the source systems. This might be accomplished by implementing utilities that can generate and save test data or make saving and moving real HTTP requests for tests easier. Join the issue conversation [here](https://gitlab.com/meltano/sdk/-/issues/30)!

### Target Specific

<a id="cap-softdeletes"></a>
#### Soft Deletes
Targets that support this capability implement logic that soft deletes records from the destination, usually by populating a `deleted_at` timestamp field. The two common techniques for handling deletes in Singer are by using the ACTIVATE_VERSION message or using log-based replication on a database that supports it.

<a id="cap-harddeletes"></a>
#### Hard Deletes
Similar to the Soft Deletes capability, targets that support this capability implement logic that hard deletes records from the destination when they receive a notification (via ACTIVATE_VERSION or log-based replication) that the record was deleted from the source system.

<a id="cap-complextypes"></a>
#### Complex Data Type Support
This capability means that the target has a failsafe data type (e.g. string) to ensure safe handling of unparsable or unforseen types. It's common to find targets in the Singer ecosystem that have a set list of supported types and will throw an exception if they receive anything unexpected. With this capability supported you can feel comfortable that exceptions will not be raised for unsupported types.

### Either Tap or Target

<a id="cap-activateversion"></a>
#### Activate Version Message
Managing hard deletes in the source system is difficult but the Singer community has developed a technique using a message type which is not officially part of the Spec called ACTIVATE_VERSION.

Imagine the scenario where a key-based incremental sync has completed its initial load and a state bookmark is saved to be used as a filter in the next incremental run. Then in the source system a record is hard deleted. On the next incremental sync the tap will have no way of knowing that record was deleted, resulting in stale records that only exist in the destination table.

A simple solution could be to run a full sync everytime and have the target truncate any old records. But the other challenge is that targets have no way of knowing what sync mode the tap is running in: full table, incremental, or log based. If the target knew that the tap was running in full table sync mode then it would be able to effectively truncate the existing data and replace it with the newest full sync it receives.

This is where the ACTIVATE_VERSION message comes in! The ACTIVATE_VERSION message type is a mechanism that is used in full table sync mode which tells the target to disregard all previously received records and only consider the current version as “active”. By using this mechanism the sync between the tap and target can properly delete inactive versions of the data in the destination to clean up any stale records that were hard deleted.

Taps that support this capability will send along and ACTIVATE_VERSION message (usually generated from the current timestamp) prior to sending the RECORD messages on the first full sync and then at the end of each subsequent successful full table sync thereafter. Targets that support this capability implement logic that removes all non-active records from the destination.

<a id="cap-streammaps"></a>
#### Stream Maps
The ability to accept a mapping configuration can be used to do minor transformations to the data between the tap and target. The capability can be currently be implemented on the tap or target side but will soon be supported in Meltano itself. This includes things like:
- stream and property aliasing
- duplication and bifurcation of streams
- hashing or anonymizing PII/PHI
- row-level filtering
- suppression of streams or stream properties
- and more…

Taps and targets that support this capability have logic to accept the optional stream_maps config key and do the light transformations listed above.

<a id="cap-about"></a>
#### About
The tap or target accepts an `--about` argument which outputs details about the connector including its capabilities and settings which can be used in programmatically generate UI forms.

An example output in json format `--about --format=json` from [target-athena](https://github.com/MeltanoLabs/target-athena) built using the Meltano Singer SDK.

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

<a id="cap-batch"></a>
#### Batch
This capability is currently in development by the [Singer Working Group](https://github.com/MeltanoLabs/Singer-Spec-Working-Group) to align on a consistent approach for supporting batch sync messages in the Spec or as part of its officially supported patterns. The capability, which was inspired by [Wise’s Fast Sync feature](https://github.com/transferwise/pipelinewise/tree/e0a8ee15c05f019916f5400158b81de72cf33dc8/pipelinewise/fastsync), has the goal of bypassing some of the performance limitations inherent to the Singer Spec by using the optimized import/export features of modern data warehouses (Snowflake, Redshift, etc.). Taking this approach allows connectors to improve performance by both using the source and/or target’s most optimized technique for importing and exporting data while also avoiding the additional costs of serializing, deserializing, and piping each record. Join the issue conversation [here](https://gitlab.com/meltano/sdk/-/issues/9)!

## Architecture

MeltanoHub is built with every part of the Singer ecosystem and Meltano product family. This is a completely open source, end-to-end, production example of Meltano using full-featured Singer connectors.

We use Meltano itself to pull data from GitHub. View the Meltano project for this effort in the [Hub repository](https://gitlab.com/meltano/hub/-/tree/main/meltano).

Using the SDK, we built a [custom GitHub tap](/singer/taps/github-search) and a [custom Athena target](/singer/targets/target-athena).

We're using dbt to [manage transformations](https://gitlab.com/meltano/hub/-/tree/main/meltano/transform/transforms/marts/singer) with Athena to aid in curating the data.
