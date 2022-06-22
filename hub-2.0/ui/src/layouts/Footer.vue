<template>
  <footer class="footer">
      <div class="footer-item">
          <h3>Support</h3>
          <g-link class="nav__link" to="/extractors">Join Us On Slack</g-link>
          <g-link class="nav__link" to="/extractors">Documentation</g-link>
          <g-link class="nav__link" to="/extractors">Status</g-link>
          <g-link class="nav__link" to="/extractors">Contact</g-link>
      </div>
      <div class="footer-item">
          <h3>Company</h3>
          <g-link class="nav__link" to="/extractors">About</g-link>
          <g-link class="nav__link" to="/extractors">Blog</g-link>
          <g-link class="nav__link" to="/extractors">Press</g-link>
      </div>
      <div class="footer-item">
          <h3>Terms & Policies</h3>
          <g-link class="nav__link" to="/extractors">Policies</g-link>
          <g-link class="nav__link" to="/extractors">Terms of Use</g-link>
          <g-link class="nav__link" to="/extractors">Code of Conduct</g-link>
          <g-link class="nav__link" to="/extractors">Privacy</g-link>
      </div>
  </footer>
</template>

<script>
export default {
    name: 'Footer'
}
</script>

<style lang="scss">
    .footer {
        border-top: 2px solid #62626e;
        background: #f1f1f2;
        color: black;
        display: flex;
        .footer-item {
            display: flex;
            flex-direction: column;
            width: 33.333%;
            text-align: center;
        }
    }

</style>