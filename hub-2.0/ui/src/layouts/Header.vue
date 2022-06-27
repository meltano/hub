<template>
    <header class="header">
      <strong>
        <g-link to="/"><g-image src="../images/meltano-logo-stacked-padded.svg" width="80" /></g-link>
      </strong>
      <nav class="nav">
        <g-link class="nav__link" to="/extractors">Extractors</g-link>
        <g-link class="nav__link" to="/loaders/">Loaders</g-link>
        <g-link class="nav__link" to="/transformers/">Transformers</g-link>
        <g-link class="nav__link" to="/orchestrators">Orchestrators</g-link>
        <!-- <g-link class="nav__link" to="/validators/">Validators</g-link>
        <g-link class="nav__link" to="/analyzers/">Analzyers</g-link> -->
        <g-link class="nav__link" to="/utilities/">Utilities</g-link>
        <g-link class="nav__link" to="/files/">Files</g-link>
      </nav>
    </header>
</template>

<script>
export default {
    name: "Header"
}
</script>

<style>

</style>