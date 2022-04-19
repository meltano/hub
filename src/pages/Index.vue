<template>
  <Layout>
    <div class="home-details">
      <h1>Welcome to Meltano Hub</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur excepturi labore tempore expedita, et iste tenetur suscipit explicabo! Dolores, aperiam non officia eos quod asperiores</p>
      <h2>Tempore expedita, et iste tenetur suscipit explicabo! Dolores, aperiam non officia eos quod asperiores</h2>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur excepturi labore tempore expedita, et iste tenetur</p>
      <a href="/">Learn more about DataOps</a>
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
    width: 200px;
    height: 50px;
    background: #d9042b;
    color: #fff;
    border-radius: 38px;
    display: flex;
    align-items: center;
    padding: 5px;
    text-decoration: none;
    text-transform: uppercase;
  }
}
</style>
