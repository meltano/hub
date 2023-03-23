<template>
  <Layout>
    <div class="home-details mx-auto">
      <p class="text-5xl tracking-wide mb-3">Welcome to Meltano Hub</p>
      <p class="text-xl mb-2 max-w-3xl mx-auto">
        <a class="underline hover:no-underline hover:text-blue" href="https://meltano.com" target="_blank">Meltano</a> is your CLI for ELT+. Open source,
        flexible, scales to your needs &mdash; with a data engineering workflow you'll love.
      </p>
      <p class="text-xl mx-auto max-w-2xl">
        Meltano Hub is a central place to find any
        <a class="underline hover:no-underline hover:text-blue" href="https://docs.meltano.com/concepts/plugins" target="_blank">Meltano plugin</a> as
        well as <a class="underline hover:no-underline hover:text-blue" href="https://hub.meltano.com/singer/docs" target="_blank">Singer</a> taps and
        targets. The Hub is lovingly curated by Meltano and the wider Singer community.
      </p>
    </div>
  </Layout>
</template>

<script>
export default {
  metaInfo: {
    title: "Home",
  },
  name: "HomePage",
};
</script>

<style lang="scss">
.home-details {
  font-family: "Hanken Grotesk";
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  text-align: center;
}

@media (min-width: 1000px) {
  .home-details {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    padding: 72px 20% 72px;
    text-align: center;
  }
}
</style>
