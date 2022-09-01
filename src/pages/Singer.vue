<template>
  <Layout>
    <div class="plugins-overview">
      <h1>Welcome to MeltanoHub for Singer</h1>
      <p>
        MeltanoHub for Singer is the leading destination for the Singer Community to discover taps,
        targets, and other valuable resources. Read the
        <a
          href="https://meltano.com/blog/2021/06/01/meltanohub-for-singer-launches-with-over-200-taps-and-targets/"
          >launch announcement</a
        >
        to learn more about our goals with MeltanoHub or read the
        <g-link to="/singer/docs">docs</g-link> to understand more about our commitment to the
        Singer community and the architecture behind the Hub.
      </p>

      <ul class="plugins-list">
        <li class="page-single-plugin"><g-link to="/singer/"> </g-link> singer taps</li>
        <li class="page-single-plugin"><g-link to="/singer/"> </g-link> singer targets</li>
        <li class="page-single-plugin"><g-link to="/singer/"> </g-link> sdk</li>
        <li class="page-single-plugin"><g-link to="/singer/"> </g-link> spec</li>
      </ul>

      <h1>API Resources</h1>
      <p>
        MeltanoHub for Singer is built for the entire Singer community. We have several resources
        available at a versioned endpoint that can be used by other organizations to build a catalog
        of taps and targets within their products. You can view the latest version of each resource
        below:
      </p>
      <ul class="plugins-list">
        <li class="page-single-plugin">
          <g-link to="/src/taps.json">tap json</g-link>
        </li>
        <li class="page-single-plugin">
          <g-link to="/src/targets.json">target json</g-link>
        </li>
        <li class="page-single-plugin">
          <g-link to="/src/schema.json">json schema</g-link>
        </li>
      </ul>
    </div>
  </Layout>
</template>

<script>
export default {
  name: "SingerPage"
};
</script>

<style lang="scss">
a {
  color: #fbbf52;
  text-decoration: none;
}
</style>
