---
title: "Maintaining Taps & Targets"
description: "Find out how to maintain Singer taps and targets using the Meltano Singer SDK and Meltano Hub"
---

# Tap & Target Maintenance

Thanks for your interest in maintaining a tap or target! Here are some best practices and FAQs for contributing to and maintaining these projects.

The Singer community was started by Stitch in 2017 and since then many conventions and best practices have been adopted but are commonly unspoken or not explicitly documented which can be intimidating to newcomers.
This document is meant to memorialize some of the ways that the Singer community operates to make it easier to join, contribute, and benefit from.

## Best Practices

### Avoid Creating a New Variant When Possible

It's not uncommon in the Singer community (and the open source ecosystem in general) to see people fork a repo in order to add a single feature or bug fix but never get it merged to the upstream repo.
This approach may solve the short term problem but requires you to take on the burden of maintaining the repo moving forward.
By contributing back to the upstream you benefit the community and you can free yourself from maintaining your variant moving forward.
If everyone in our community puts their effort into maintaining the same connectors then we all benefit from less work and better quality.

### Favor Generically Useful vs Custom or Hardcoded Logic

Sometimes it's tempting to build a connector with only your exact needs baked in. For example only adding the streams you need or hard coding organization specific logic like account names, how credentials are sourced, etc. But with a little extra effort you can make it generically useful enough to attract other community members to use and help maintain your code.

- Add as much stream coverage as you can
- All configs should flow through the config.json input file
- No hardcoded values and logic, or at least not by default

### Document Settings Well

The most challenging part of using a community maintained connector is configuring it properly.
Always make sure to document your configurations well.

SDK based connectors have a [--about command option](https://sdk.meltano.com/en/latest/implementation/cli.html#about) that prints out the documented settings and descriptions from `tap.py`. MeltanoHub scrapes these settings and descriptions for building documentation so you should make sure to keep them up to date.

For non-SDK based connectors you will commonly find an example config.json in the repo.
The Meltano community has also invested in documenting these on MeltanoHub for your convenience.

### Advertise It On Meltano Hub

Once your connector is functioning and ready to go, make sure you get it listed on MeltanoHub (see [docs](/add-a-tap)) so others can find it.
More users means more contributors and maintainers for your code base!

### Use Meltano SDK

We might be a little biased on this one but using an SDK allows you to reduce code, increase reliability, comply with the Singer Spec, gain features with an SDK version upgrade, and work well within the Meltano community.

## Common Patterns

Since Singer is only a spec (see Meltano's [Singer Spec docs](http://localhost:8080/singer/docs#singer-spec)) for how data should be formatted and passed between connectors there have become many common patterns, tools, and SDKs to help speed the process up.

#### [singer-io](https://github.com/singer-io)

- Mostly from scratch implementations, using the [singer-python](https://github.com/singer-io/singer-python) library for some shared methods
- Commonly have most of the code in the module's `__init__.py` file with a `main` method
- Logic for parsing cli inputs uses argparse and is required by every connector
- A `REQUIRED_CONFIG_KEYS` list to validate required config values
- Dependencies are usually in the setup.py vs in requirements.txt
- Very few target examples because they we're originally built to always send data to the [Stitch](https://www.stitchdata.com/) service with [target-stitch](https://github.com/singer-io/target-stitch)
- Usually unit tests are limited
- The developer needs to know internal rules like when its safe to write state messages or how to handle ACTIVATE_VERSION messages
- The `catalog` input file was originally called `properties` so some will accept either
- [Getting started guide](https://github.com/singer-io/getting-started)
- [tap template](https://github.com/singer-io/singer-tap-template)

#### [Meltano SDK](https://sdk.meltano.com/en/latest/) Based Connectors

A software development kit that abstracts many of the challenges of building Singer connectors so the developer doesn't need to know about them and also provides accelerators to speed up the process of writing a new connector. See the [Meltano SDK](https://sdk.meltano.com/en/latest/) docs for more details. Example of some features:

- cookiecutter templates to seed a connector repo
- manages translating records into Singer spec compliant messages
- methods for common API functionality (i.e. parent child relationships, pagination, retry, post processing, etc.)
- methods for common SQL functionality
- default unit tests
- additional features for testing, printing config metadata,

#### [Pipelinewise](https://github.com/transferwise/pipelinewise)

- An open source tool created in 2019 that helps configure and run Singer connectors, similar to Meltano
- Maintains its own list of connectors that it supports. You can also run all of these with Meltano!
- Well documented patterns around [metadata columns](https://transferwise.github.io/pipelinewise/user_guide/metadata_columns.html), [replication methods](https://transferwise.github.io/pipelinewise/concept/replication_methods.html), and [schema changes](https://transferwise.github.io/pipelinewise/user_guide/schema_changes).

## Evaluating a tap or target

These are things you can look for when evaluating a tap or target.
Many of these recommendations can be used for evaluating open source projects in general.

You should start by looking on MeltanoHub to find and evaluate connectors.
Although a connector can still be listed if its not well maintained so click through to the repo to inspect it closer if you're unsure.
None of these attributes alone will tell you what the best connectors are, so look at many of them to make a holistic evaluation.

- <u>Organization backed connectors</u>: If its in the namespace of `meltano`/`meltanolabs`/`transferwise`/`singer-io`/ etc. its usually a good bet that the connector is maintained because one of the organizations is invested in it's success. Although this isn't always the case, especially with some of the older singer-io variants.
- <u>MeltanoHub default</u>: The Meltano community does it's best to label the most active variant as the default on MeltanoHub. Although it's still possible that the best option is unmaintained.
- <u>Meltano SDK</u>: If it uses the Meltano SDK then its a good sign that its relatively recent and has good support for common features. If there are many TODOs still in the repo that came with the cookiecutter it might indicate that the connector was never finished or is a hobby project.
- <u>Stream coverage</u>: You can evaluate 2 variants against each other based on stream coverage. Sometimes a new variant is written that has more features but is only supporting a small number of streams.
- <u>Latest commit timestamp</u>: If there are commits in the last couple months then its probably decently maintained.
- <u>Total amount of commits</u>: If it only has a few commits it could still be in development, but if the latest timestamp is also a while ago it might indicate that it was a hobby project or never completed.
- <u>Open Pull Requests</u>: Are there pending PRs that aren't being addressed?
- <u>Open Issues</u>: Are there many open issues that aren't being addressed? Lots of issues could also mean that it has high traffic and many feature requests so look closely at what the issues are for.
- <u>Forks</u>: How many forks are there? It could indicate that people need to fork it to fix bugs or update dependencies before they got it working.
- <u>Network Insights</u>: GitHub has a [network insights](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/understanding-connections-between-repositories) feature that allows you to see forks of the repo and recent commits. Sometimes this reveals a fork that is more active than the main repo, potentially indicating that the fork is the new best variant.

## FAQs

### How are targets marked as "maintained" and "unmaintained"? What does a well-maintained tap or target look like?

There are no hard requirements for maintainership, but well-maintained taps typically follow these guidelines:

- Issues and PRs/MRs responded to within a week.
- All settings documented, with additional documentation containing usage examples.
- Dependencies regularly updated
- Support for the recent Python versions

The Meltano community does it's best to mark the best connectors as the default variant on Meltano Hub.
If you think the default should be different, open an issue!

### How do I add my tap or target to the Meltano Hub?

Please follow the steps outlined in [this guide](/add-a-tap) and the PR request template.

### Porting Singer Taps to the Meltano Singer SDK for Taps and Targets

If you'd like to port your tap or target to the Meltano Singer SDK, please see the [porting guide](https://sdk.meltano.com/en/latest/porting.html).

If you're taking over maintanership of a tap that hasn't yet been ported, it's best to get the existing tap working again before porting it over to the SDK. If you're not ready to port it just yet, please open an issue on your repo and tell us in `#contributing` on [Slack](https://meltano.com/slack). We may be able to find someone to help you.

### How do I flag a tap that should be migrated to the SDK for community prioritization?

Please open an issue on the [Singer Most Wanted repo](https://github.com/MeltanoLabs/Singer-Most-Wanted/issues) to let the community know that a tap or target needs porting. We can try to find someone to port it.

### How can I become a maintainer in MeltanoLabs? How do I stop being a maintainer?

Please see the [MeltanoLabs Meta repo](https://github.com/MeltanoLabs/Meta) for more information on how we manage this organization.

# Unmaintained Taps and Targets

Taps will occasionally become dormant as maintainers change jobs, companies shift priorities, or individual maintainers don't have enough time.

## FAQs

### What is considered an unmaintained tap?

Here are some signs that a tap or target has been abandoned:

- Open PRs/MRs with no reviews
- Open issues with no response in the last 6 months
- Last commit over a year ago
- Many forks with minimal merges back into upstream

### How do I report an unmaintained tap?

Open an issue on the [Singer Most Wanted repository](https://github.com/MeltanoLabs/Singer-Working-Group). This lets the Meltano Team and the community know that this tap needs adopting.

### How do I take over maintenance of a tap or target?

Usually the Meltano community can help determine the best path forward but the options are usually:

1. Fork it to your personal or organization's GitHub namespace:

- Create a fork of the project
- Make your changes
- Add your fork to Meltano Hub and make it the new default

2. Communicate with the current owner:

- If the maintainer prefers you can become a maintainer on their repo

3. Migrate it to MeltanoLabs:

- See [MeltanoLabs README](https://github.com/MeltanoLabs/Meta#adding-a-new-connector) for details on transferring the repo
- Make your changes
- Update Meltano Hub and make it the new default

### What if I want to update a tap but don't want to maintain it long term?

Not a problem! Please open an issue on the [Singer Most Wanted repo](https://github.com/MeltanoLabs/Singer-Most-Wanted/issues) to let the Meltano Community know that a tap needs a maintainer. We can help find someone to maintain it.

### Where do I go if I want to pay someone to build a tap or add a feature?

Please reach out to one of our [Partners](https://meltano.com/partners/) to discuss custom taps and targets.

### How do I escalate an issue if it’s not being recognized by the maintainer?

Please join the #contributing channel on [Slack](https://meltano.com/slack) and tag `@Amanda Folson` along with a link to the issue.
