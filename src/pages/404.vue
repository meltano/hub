<template>
  <Layout>
    <div class="file-not-found">
      <p class="text-3xl md:text-5xl pb-4 pt-8 font-bold font-pjs text-purple">
        Whoops. Nothing to see here!
      </p>
    </div>
  </Layout>
</template>

<script>
export default {
  name: "404Page",
};
</script>

<style>
.file-not-found {
  display: flex;
  align-content: center;
  flex: 1 1 auto;
  justify-content: center;
}
</style>
