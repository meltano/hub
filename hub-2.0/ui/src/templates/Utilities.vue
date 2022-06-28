<template>
    <Layout>
        <!-- <p>{{$page.node.name}}</p> -->
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
    name: 'Utilities'
}
</script>

<page-query>
query {
    utilities: allUtilities {
        edges {
            node {
                id
                name
                label
                namespace
                maintenance_status
            }
        }
    }
}
</page-query>

<style>

</style>