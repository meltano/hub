<template>
    <Layout>
        <!-- <p v-html="$page.extractor.node.description" />
        <p v-html="$page.extractor.node.label" />
        <p v-html="$page.extractor.node.name" />
        <p v-html="$page.extractor.node.logo_url" />
        <p v-html="$page.extractor.node.namespace" />
        <p v-html="$page.extractor.node.variant" />
        <p v-html="$page.extractor.node.pip_url" />
        <p v-html="$page.extractor.node.repo" />
        <p v-html="$page.extractor.node.capabilities" />
        <p v-html="$page.extractor.node.domain_url" />
        <p v-html="$page.extractor.node.maintenance_status" />
        <p v-html="$page.extractor.node.keywords" /> -->
    </Layout>
</template>

<script>
export default {
    name: 'Extractors'
}
</script>

<page-query>

</page-query>

<style>
</style>

<!-- query ($id: ID!) {
  allExtractors(id: $id) {
    edges {
        node {
description
label
name
logo_url
namespace
variant
pip_url
repo
capabilities
domain_url
maintenance_status
keywords
        }
    }

  }
} -->