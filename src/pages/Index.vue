<template>
  <Layout>
    <div class="home-details">
      <p class="mb-3 text-5xl tracking-wide">Welcome to Meltano Hub</p>
      <p class="text-xl">
        Meltano Hub is a central place to find any Meltano plugin as well as Singer taps and
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
    padding: 50px 20%;
    text-align: center;
  }
}
</style>
