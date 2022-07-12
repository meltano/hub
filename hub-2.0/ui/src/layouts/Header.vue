<script>
import Dropdown from "../components/Dropdown.vue";
import DropdownContent from "../components/DropdownContent.vue";
import DropdownItem from "../components/DropdownItem.vue";
export default {
  name: "Header",
  components: {
    Dropdown,
    DropdownContent,
    DropdownItem
  }
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
      <button class="hamburger">
        <div class="dropdown">
          <Dropdown>
            <template slot="toggler">
              <a class="nav__link">
                Plugins
              </a>
            </template>
            <DropdownContent>
              <DropdownItem>Action 1</DropdownItem>
              <DropdownItem>Action 2</DropdownItem>
              <DropdownItem>Action 3</DropdownItem>
            </DropdownContent>
          </Dropdown>
          <Dropdown>
            <template slot="toggler">
              <a class="nav__link">
                Singer
              </a>
            </template>
            <DropdownContent>
              <DropdownItem>Action 1</DropdownItem>
              <DropdownItem>Action 2</DropdownItem>
              <DropdownItem>Action 3</DropdownItem>
            </DropdownContent>
          </Dropdown>
        </div>
      </button>
      <div class="dropdown">
        <Dropdown>
          <template slot="toggler">
            <a class="nav__link">
              Plugins
            </a>
          </template>
          <DropdownContent>
            <DropdownItem>Action 1</DropdownItem>
            <DropdownItem>Action 2</DropdownItem>
            <DropdownItem>Action 3</DropdownItem>
          </DropdownContent>
        </Dropdown>
        <Dropdown>
          <template slot="toggler">
            <a class="nav__link">
              Singer
            </a>
          </template>
          <DropdownContent>
            <DropdownItem>Action 1</DropdownItem>
            <DropdownItem>Action 2</DropdownItem>
            <DropdownItem>Action 3</DropdownItem>
          </DropdownContent>
        </Dropdown>
      </div>

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
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 2px solid #f1f1f2;
  height: 80px;
  background: #fff;
  padding-left: 20px;
  padding-right: 20px;

  a {
    color: #3438bf;
    text-decoration: none;
  }

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
      display: flex;

      .nav__link {
        margin: 0 10px;
      }
    }

    .hamburger {
      display: none;
    }
  }
}
</style>