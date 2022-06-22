<template>
  <Layout>
    <div class="home-details">
      <h1>Welcome to Meltano Hub</h1>
      <h2>Meltano Hub is where you can find Meltano-supported, Singer-specific, and community-built extractors, loaders, utilities, and everything else.</h2>
      <p>Tempore expedita, et iste tenetur suscipit explicabo! Dolores, aperiam non officia eos quod asperiores</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur excepturi labore tempore expedita, et iste tenetur</p>
      <a href="/">Learn More</a>
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
  padding: 50px 20%;
  text-align: center;
  h1 {
    font-size: 4.7rem;
    line-height: 1.25;
  }
  a {
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
</style>
