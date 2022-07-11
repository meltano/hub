<script>
export default {
  name: "Header"
}
</script>
<template>
  <header class="header">
    <strong>
      <g-link to="/">
        <g-image src="../assets/images/meltano-logo-stacked-padded.svg" width="80" />
      </g-link>
    </strong>
    <nav class="nav">
      <button class="hamburger"></button>
      <button class="dropdown">Plugins</button>
      <button class="dropdown">Singer</button>
      <!-- <g-link class="nav__link" to="/extractors">Extractors</g-link>
      <g-link class="nav__link" to="/loaders/">Loaders</g-link>
      <g-link class="nav__link" to="/transformers/">Transformers</g-link>
      <g-link class="nav__link" to="/orchestrators">Orchestrators</g-link>
      <g-link class="nav__link" to="/utilities/">Utilities</g-link>
      <g-link class="nav__link" to="/files/">Files</g-link> -->
    </nav>
  </header>
</template>

<style lang="scss">
.header {
  // .nav__link {
  //   display: none;
  // }
  .dropdown {
    display: none;
  }

  .hamburger {
    background: url("../assets/images/bars-solid.svg") no-repeat;
    width: 40px;
    height: 40px;
    color: #3438bf;
    border: none;
  }
}

@media (min-width: 1000px) {
  .header {
    .dropdown {
      display: block;
    }
    .hamburger {
      display: none;
    }
  }
}
</style>