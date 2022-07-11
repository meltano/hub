<template>
  <Layout>
    <div class="home-details">
      <h1>Welcome to Meltano Hub</h1>
      <h2>MeltanoHub is a central place to find any Meltano plugin as well as Singer taps and targets. The Hub is
        lovingly curated by Meltano and the wider Singer community.</h2>
      <a href="https://docs.meltano.com/concepts/plugins">Learn More</a>
    </div>
  </Layout>
</template>

<script>
export default {
  metaInfo: {
    title: 'Home'
  }
}
</script>

<style lang="scss">
.home-details {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  text-align: center;

  h1 {
    font-size: 3rem;
    line-height: 1.25;
    margin: 25px auto;
  }

  h2 {
    margin: 25px auto;
  }

  a {
    margin: 25px auto;
    background: #d9042b;
    color: #fff;
    border-radius: 38px;
    display: flex;
    align-items: center;
    padding: 1rem;
    text-decoration: none;
    text-transform: uppercase;
  }
}

@media (min-width: 1000px) {
  .home-details {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    padding: 50px 20%;
    text-align: center;

    h1 {
      font-size: 4.7rem;
    }
  }
}
</style>
