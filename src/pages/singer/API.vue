<template>
  <Layout>
    <div class="singer-overview">
      <h1>API</h1>
      <p>
        Meltano Hub for Singer is built for the entire Singer community. We have several resources
        available at a versioned endpoint that can be used by other organizations to build a catalog
        of taps and targets within their products. You can view the latest version of each resource
        below:
      </p>
      <ul class="api-list">
        <li class="api-link"><g-link>Tap JSON</g-link></li>
        <li class="api-link"><g-link>Target JSON</g-link></li>
        <li class="api-link"><g-link>JSON Schema</g-link></li>
      </ul>
    </div>
  </Layout>
</template>

<script>
export default {
  name: "SingerAPI"
};
</script>

<style lang="scss">
.singer-overview {
  min-width: 70%;
  text-align: center;
  justify-content: center;
}

.api-list {
  width: 100%;
  height: auto;
  background: #e8f0ff;
  display: flex;
  flex-wrap: wrap;
  padding-left: 0;
  text-align: center;
  margin: 40px auto 80px;
}

.api-link {
  color: #000;
  display: flex;
  flex-direction: column;
  list-style-type: none;
  padding: 0;
  margin: 0;
  flex-basis: 100%;
  a {
    color: #3438bf;
    text-decoration: none;
    padding: 30px;
  }

  a:hover {
    background: #b0e3c1;
  }
}

@media (min-width: 1000px) {
  .singer-overview {
    padding: 0 200px;
  }
}

@media (min-width: 768px) {
  .singer-overview {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0 70px;
    text-align: center;
  }
}

@media (min-width: 768px) {
  .api-link {
    flex-basis: 33.33333%;
  }
}
</style>
