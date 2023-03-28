<template>
  <Layout>
    <div class="plugins-overview">
      <p class="text-3xl md:text-5xl pb-4 pt-8 font-bold font-pjs text-purple">
        Welcome to MeltanoHub for Singer
      </p>
      <p>
        MeltanoHub for Singer is the leading destination for the Singer Community to discover taps,
        targets, and other valuable resources. Read the
        <a
          href="https://meltano.com/blog/2021/06/01/meltanohub-for-singer-launches-with-over-200-taps-and-targets/"
          >launch announcement</a
        >
        to learn more about our goals with MeltanoHub or read the
        <g-link to="/singer/docs"> docs</g-link> to understand more about our commitment to the
        Singer community and the architecture behind the Hub.
      </p>

      <ul class="list-disc list-inside plugins-list">
        <li class="page-single-plugin">sdk</li>
        <li class="page-single-plugin">spec</li>
      </ul>

      <p class="text-3xl md:text-5xl pb-4 pt-8 font-bold font-pjs text-purple">API Resources</p>
      <p>
        MeltanoHub for Singer is built for the entire Singer community. We have several resources
        available at a versioned endpoint that can be used by other organizations to build a catalog
        of taps and targets within their products. You can view the latest version of each resource
        below:
      </p>
      <ul class="list-disc list-inside plugins-list">
        <li class="page-single-plugin">tap json</li>
        <li class="page-single-plugin">target json</li>
        <li class="page-single-plugin">json schema</li>
      </ul>
    </div>
  </Layout>
</template>

<script>
export default {
  name: "SingerPage",
};
</script>

<style></style>
