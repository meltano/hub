<script>
import Dropdown from "../components/Dropdown.vue";
import DropdownContent from "../components/DropdownContent.vue";
import DropdownItem from "../components/DropdownItem.vue";
import Search from "../components/Search.vue";
export default {
  name: "Header",
  components: {
    Dropdown,
    DropdownContent,
    DropdownItem,
    Search
  }
}
</script>
<template>
  <header class="header">
    <div class="top-nav">
      <strong>
        <g-link to="/">
          <g-image src="../assets/images/meltano-logo-stacked-padded.svg" width="80" />
        </g-link>
      </strong>
      <nav class="nav">
        <button class="hamburger">
        </button>
        <div class="dropdown">
          <a class="page-link" href="#">Plugins</a>
          <div class="dropdown-content">
            <g-link class="nav__link" to="/extractors">Extractors</g-link>
            <g-link class="nav__link" to="/loaders/">Loaders</g-link>
            <g-link class="nav__link" to="/transformers/">Transformers</g-link>
            <g-link class="nav__link" to="/orchestrators">Orchestrators</g-link>
            <g-link class="nav__link" to="/utilities/">Utilities</g-link>
            <g-link class="nav__link" to="/files/">Files</g-link>
          </div>
        </div>
        <div class="dropdown">
          <a class="page-link" href="#">Singer</a>
          <div class="dropdown-content">
            <g-link class="nav__link" to="/extractors">Extractors</g-link>
            <g-link class="nav__link" to="/loaders/">Loaders</g-link>
            <g-link class="nav__link" to="/transformers/">Transformers</g-link>
            <g-link class="nav__link" to="/orchestrators">Orchestrators</g-link>
            <g-link class="nav__link" to="/utilities/">Utilities</g-link>
            <g-link class="nav__link" to="/files/">Files</g-link>
          </div>
        </div>
      </nav>
    </div>
    <div class="bottom-search">
      <Search />
    </div>
  </header>
</template>

<style lang="scss">
.header {
  display: flex;
  background: #fff;
  flex-wrap: wrap;

  .top-nav {
    width: 100%;
    display: flex;
    justify-content: space-between;
    padding: 0 20px;
    align-items: center;
    border-bottom: 2px solid #f1f1f2;
  }

  .bottom-search {
    width: 100%;
  }

  a {
    color: #3438bf;
    text-decoration: none;
  }

  .hamburger {
    background: url("../assets/images/bars-solid.svg") no-repeat;
    width: 40px;
    height: 40px;
    color: #3438bf;
    border: none;
  }
}


.dropdown {
  display: inline-block;
  position: relative;
}

.dropdown-content {
  display: none;
  position: absolute;
  right: -60px;
  width: 300%;
  overflow: auto;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  text-align: center;
}

.dropdown-content a {
  display: block;
  color: #3438bf;
  padding: 5px;
  text-decoration: none;
}

.dropdown:hover .dropdown-content {
  display: block;
  background: #fff;
}

.dropdown-content a:hover {
  color: #fff;
  background-color: #3438bf;
}

@media (min-width: 1000px) {
  .header {
    .dropdown {

      .page-link {
        margin: 0 10px;
      }
    }

    .hamburger {
      display: none;
    }
  }
}
</style>