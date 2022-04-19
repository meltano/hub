<template>
  <footer class="footer">
      <div class="footer-item">
          <h3>Footer Heading Title</h3>
          <p>Item Link</p>
          <p>Item Link</p>
          <p>Item Link</p>
          <p>Item Link</p>
      </div>
      <div class="footer-item">
          <h3>Footer Heading Title</h3>
          <p>Item Link</p>
          <p>Item Link</p>
          <p>Item Link</p>
      </div>
      <div class="footer-item">
          <h3>Footer Heading Title</h3>
          <p>Item Link</p>
          <p>Item Link</p>
          <p>Item Link</p>
          <p>Item Link</p>
          <p>Item Link</p>
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