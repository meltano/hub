<template>
  <footer class="footer">
      <div class="footer-item">
          <h3>Support</h3>
          <a class="nav__link" href="https://www.meltano.com/slack">Join Us On Slack</a>
          <a class="nav__link" href="https://docs.meltano.com/">Documentation</a>
          <a class="nav__link" href="https://www.meltano.com/contact">Contact</a>
      </div>
      <div class="footer-item">
          <h3>Company</h3>
          <a class="nav__link" href="https://www.meltano.com/about">About</a>
          <a class="nav__link" href="https://www.meltano.com/blog">Blog</a>
          <a class="nav__link" href="https://www.meltano.com/press">Press</a>
      </div>
      <div class="footer-item">
          <h3>Terms & Policies</h3>
          <a class="nav__link" href="https://www.meltano.com/privacy-policy">Privacy Policy</a>
          <a class="nav__link" href="https://www.meltano.com/terms-of-service">Terms of Service</a>
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
        padding: 25px 0;
        .footer-item {
            display: flex;
            flex-direction: column;
            width: 33.333%;
            text-align: center;
        }
    }

</style>