<script>
import Search from "../components/Search.vue";

export default {
  name: "HeaderLayout",
  components: {
    Search
  }
};
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
        <button class="hamburger"></button>
        <!-- <a
          class="github-button"
          href="https://github.com/meltano/meltano"
          data-size="large"
          data-show-count="true"
          aria-label="Star meltano/meltano on GitHub"
          >Star</a
        > -->
        <div class="dropdown">
          <a class="page-link" href="#">Plugins</a>
          <div class="dropdown-content">
            <g-link class="nav__link" to="/extractors">
              <h3>Extractors</h3>
              <span>
                View all SaaS API, database, and file sources from which Meltano can pull data
              </span>
            </g-link>
            <g-link class="nav__link" to="/loaders/">
              <h3>Loaders</h3>
              <span
                >View all database, file, and SaaS API destinations to which Meltano can send
                data</span
              >
            </g-link>
            <g-link class="nav__link" to="/transformers/">
              <h3>Transformers</h3>
              <span>Learn how to transform your loaded data using Meltano</span>
            </g-link>
            <g-link class="nav__link" to="/orchestrators">
              <h3>Orchestrators</h3>
              <span>Learn how to orchestrate scheduled pipelines in Meltano</span>
            </g-link>
            <g-link class="nav__link" to="/utilities/">
              <h3>Utilities</h3>
              <span>Add tools, commands, and other services to your project</span>
            </g-link>
            <g-link class="nav__link" to="/files/">
              <h3>Files</h3>
              <span>Add file resources to your Meltano project</span>
            </g-link>
          </div>
        </div>
        <div class="dropdown">
          <a class="page-link" href="#">Singer</a>
          <div class="dropdown-content">
            <g-link class="nav__link" to="/singer/taps">
              <h3>Taps</h3>
              <span>Find a Singer tap to pull data from a SaaS API, database, or file</span>
            </g-link>
            <g-link class="nav__link" to="/singer/targets">
              <h3>Targets</h3>
              <span>Find a Singer target to send data to a database, file, or SaaS API</span>
            </g-link>
            <a class="nav__link" href="https://sdk.meltano.com">
              <h3>SDK</h3>
              <span
                >Learn more about building Singer taps and targets for new sources and
                destinations</span
              >
            </a>
            <g-link class="nav__link" to="/singer/spec">
              <h3>Spec</h3>
              <span>Learn more about the Singer specification for open source data connectors</span>
            </g-link>
            <g-link class="nav__link" to="/singer/docs">
              <h3>Docs</h3>
              <span
                >Understand more about Singer taps and targets and how to use them with
                Meltano</span
              >
            </g-link>
            <g-link class="nav__link" to="/singer/api">
              <h3>API</h3>
              <span>Find the API resources for our Meltano + Singer taps and targets</span>
            </g-link>
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

    nav {
      display: flex;
      align-items: center;
    }
    nav span:first-of-type {
      height: 28px;
    }
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

.widget {
  border: 2px solid blue;
}

.dropdown {
  display: none;
  position: relative;
}

.dropdown-content {
  display: none;
  position: absolute;
  overflow: auto;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  text-align: center;
  width: 1000px;
  height: auto;
  right: 0;
  flex-wrap: wrap;
  border: 2px solid #3438bf;
}

.dropdown-content a {
  display: flex;
  color: #3438bf;
  text-decoration: none;
  flex-basis: 49%;
  padding: 10px 5px;
  text-align: left;
  flex-direction: column;
}

.dropdown-content a h3 {
  margin: 0 0 5px 0;
}

.dropdown-content a span {
  font-style: italic;
  color: #62626e;
}

.dropdown:hover .dropdown-content {
  display: flex;
  background: #fff;
}

.dropdown-content a:hover {
  color: #fff;
  background-color: #3438bf;

  span {
    color: #f1f1f2;
  }
}

@media (min-width: 391px) {
  .dropdown {
    display: inline-block;
  }
  .hamburger {
    display: none;
  }
}

@media (min-width: 1000px) {
  .header {
    .dropdown {
      .page-link {
        margin: 0 10px;
      }
    }
  }
}
</style>
