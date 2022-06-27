<template>
    <Layout>
        <div class="info">
            <h1>Loaders</h1>
            <p>Meltano lets you easily load extracted data into arbitrary destinations (databases, SaaS APIs, and file
                formats) using Singer targets, which take the role of your project’s loader plugins. To learn more about
                extracting and loading data using Meltano, refer to the Data Integration (EL) guide.</p>
            <div class="plugins-list"></div>
        </div>
    </Layout>
</template>

<script>
export default {
    name: "Loaders"
}
</script>

<style lang="scss">
.info {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0 200px;
    h1 {
        font-size: 2.5em;
    }
}

.plugins-list {
    width: 100%;
    height: 200px;
    background: #e8f0ff;
    margin-top: 40px;
}
</style>