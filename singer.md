---
layout: page
header: singer
permalink: /singer/
description: The Leading Destination for the Singer Community
---

<h2 style="text-align:center"> Welcome to MeltanoHub for Singer </h2>

  <p>
  MeltanoHub for Singer is the leading destination for the Singer Community to discover
  taps, targets, and other valuable resources. Read the <a href="https://meltano.com/blog">launch announcement</a> to learn more about
  our goals with MeltanoHub or read the <a href="/singer/docs">docs</a> to understand more about our commitment to the Singer community and the architecture behind the Hub.
  </p>


  <ul class="button-grid two-columns">
    <li>
      <a href="/singer/taps">
        <strong>Singer Taps <small>{{site.data.taps.size}}</small></strong>

        <p>Find a Singer tap to pull data from a SaaS API, database, or file</p>
      </a>
    </li>
    <li>
      <a href="/singer/targets">
        <strong>Singer Targets <small>{{site.data.targets.size}}</small></strong>

        <p>
          Find a Singer target to load data into a database, file, or SaaS API
        </p>
      </a>
    </li>
    <li>
      <a href="https://gitlab.com/meltano/singer-sdk" target="_blank">
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
  </ul>

<h2 style="text-align:center" id="api-resources"> API Resources </h2>

  <p>
  MeltanoHub for Singer is built with the entire community in mind. We have several resources available
  at a <a href="/singer/api/v1">versioned endpoint</a> that can be used by other organizations to build a catalog of taps and targets within their products. You can view the latest version of each resource below:

  <ul class="button-grid three-columns">
    <li>
      <a href="/singer/api/v1/taps.json">
        <strong>Tap JSON</strong>
        <p>JSON file with all Singer taps on MeltanoHub</p>
      </a>
    </li>
    <li>
      <a href="/singer/api/v1/targets.json">
        <strong>Target JSON</strong>
        <p>JSON file with all Singer targets on MeltanoHub</p>
      </a>
    </li>
    <li>
      <a href="/singer/api/v1/schema.json">
        <strong>JSON Schema</strong>
        <p>JSON Schema used to validate connectors</p>
      </a>
    </li>
  </ul>
