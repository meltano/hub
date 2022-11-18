---
title: "Maintaining Taps & Targets"
description: "Find out how to maintain Singer taps and targets using the Meltano Singer SDK and Meltano Hub"
---

## Tap & Target Maintenance

Thanks for your interest in maintaining a tap or target! Here are some best practices and FAQs for contributing to and maintaining these projects.

### How are targets marked as "maintained" and "unmaintained"? What does a well-maintained tap or target look like?

There are no hard requirements for maintainership, but well-maintained taps typically follow these guidelines:

- Issues and PRs/MRs responded to within a week.
- TODO: Come up with a baseline list of capabilities?
- All settings documented, with additional documentation containing useage examples.

### How do I add my tap or target to the Meltano Hub?

Please follow the steps outlined in [this guide](/add-a-tap) and the PR request template.

### How can I become a maintainer in MeltanoLabs?

(TBD)

### How do I stop being a maintainer?

(TBD)

### Porting Singer Taps to the Meltano Singer SDK for Taps and Targets

If you'd like to port your tap or target to the Meltano Singer SDK, please see the [porting guide](https://sdk.meltano.com/en/latest/porting.html).

If you're taking over maintanership of a tap that hasn't yet been ported, it's best to get the existing tap working again before porting it over to the SDK. If you're not ready to port it just yet, please open an issue on your repo and tell us in `#contributing` on [Slack](https://meltano.com/slack). We may be able to find someone to help you.

#### How do I flag a tap that should be migrated to the SDK for community prioritization?

Please open an issue on the [Singer Most Wanted repo](https://github.com/MeltanoLabs/Singer-Most-Wanted/issues) to let the community know that a tap or target needs porting. We can try to find someone to port it.

## Unmaintained Taps and Targets

Taps will occasionally become dormant as maintainers change jobs or companies shift priorities.

### What is considered an unmaintained tap?

Here are some signs that a tap or target has been abandoned:

- Open PRs/MRs with no reviews
- Open issues with no response in the last 6 months
- Last commit over a year ago
- Many forks with minimal merges back into upstream

### How do I report an unmaintained tap?

Open an issue on the [Singer Most Wanted repository](https://github.com/MeltanoLabs/Singer-Working-Group). This lets the Meltano Team and the community know that this tap needs adopting.

### How do I take over maintenance of a tap or target?

- Create a fork of the project and make your changes
- Add to Meltano Hub

### What if I want to update a tap but don't want to maintain it long term?

Not a problem! Please open an issue on the [Singer Most Wanted repo](https://github.com/MeltanoLabs/Singer-Most-Wanted/issues) to let the Meltano Community know that a tap needs a maintainer. We can help find someone to maintain it.

## Where do I go if I want to pay someone to build a tap or add a feature?

Please reach out to one of our [Partners](https://meltano.com/partners/) to discuss custom taps and targets.

## How do I escalate an issue if it’s not being recognized by the maintainer?

Please join the #contributing channel on [Slack](https://meltano.com/slack) and tag `@Amanda Folson` along with a link to the issue.
