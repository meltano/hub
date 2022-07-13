<template>
    <Layout>
        <div class="singer">
            <h1>Welcome to MeltanoHub for Singer</h1>
            <p>MeltanoHub for Singer is the leading destination for the Singer Community to discover taps, targets, and
                other valuable resources. Read the launch announcement to learn more about our goals with MeltanoHub or
                read the docs to understand more about our commitment to the Singer community and the architecture
                behind the Hub.</p>

            Singer Taps 305
            Find a Singer tap to pull data from a SaaS API, database, or file

            Singer Targets 22
            Find a Singer target to send data to a database, file, or SaaS API

            SDK for Taps & Targets
            Learn more about building Singer taps and targets for new sources and destinations

            Singer Spec
            Learn more about the Singer specification for open source data connectors

            <h1>API Resources</h1>
            <p>MeltanoHub for Singer is built for the entire Singer community. We have several resources available at a
                versioned endpoint that can be used by other organizations to build a catalog of taps and targets within
                their products. You can view the latest version of each resource below:</p>


            Tap JSON
            JSON file with all Singer taps on MeltanoHub

            Target JSON
            JSON file with all Singer targets on MeltanoHub

            JSON Schema
            JSON Schema used to validate connectors
        </div>
    </Layout>
</template>

<script>
export default {
    name: "Singer"
}
</script>

<style lang="scss">
.singer {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    text-align: center;
}
</style>