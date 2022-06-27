<template>
    <Layout>
        <div class="info">
            <h1>Orchestrators</h1>
            <p>Meltano orchestrator plugins provide advanced scheduling and workflow execution capabilities.</p>
            <div class="plugins-list"></div>
        </div>
    </Layout>
</template>

<script>
export default {
    name: "Orchestrators"
}
</script>

<style>
.info {
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>