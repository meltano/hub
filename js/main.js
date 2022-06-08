function escapeRegex(string) {
  return string.replace(/[-\/\\^$*+?.()|[\]{}]/g, "\\$&");
}

function searchGrid() {
  window.addEventListener("DOMContentLoaded", () => {
    const field = document.querySelector("input.grid-search");
    if (!field) {
      return;
    }

    const grid = document.querySelector("ul.button-grid");
    const items = grid.querySelectorAll("li[data-search-terms]");

    field.addEventListener("input", (e) => {
      let query = e.target.value.trim().toLowerCase();

      items.forEach((item) => {
        let terms = item.getAttribute("data-search-terms");

        if (!query || terms.toLowerCase().indexOf(query) > -1) {
          item.style.display = "block";
        } else {
          item.style.display = "none";
        }
      });
    });

    field.disabled = false;
  });
}

searchGrid();

function navbarSearch() {
  window.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.querySelector("input.homepage-search-input");
    if (!searchInput) {
      return;
    }

    const searchResults = document.querySelector("ul.navbar-search-list");
    const searchResultsItems = searchResults.querySelectorAll(
      "li[data-search-terms]"
    );

    searchInput.addEventListener("input", (e) => {
      let searchQuery = e.target.value.trim().toLowerCase();

      searchResultsItems.forEach((item) => {
        let searchTerms = item.getAttribute("data-search-terms");

        if (
          !searchQuery ||
          searchTerms.toLowerCase().indexOf(searchQuery) > -1
        ) {
          item.style.display = "block";
          item.classList.add("active");
          item.classList.remove("not-active");
        } else {
          item.style.display = "none";
          item.classList.add("not-active");
          item.classList.remove("active");
        }
      });
      hideSearchListHeaders();
    });

    searchInput.disabled = false;
  });
}

navbarSearch();

function hideSearchListHeaders() {
  const results = document.querySelector("ul.navbar-search-list");
  const pluginItems = results.querySelectorAll("li");
  const noneActive = Array.from(pluginItems).every((item) => {
    return item.classList.contains("not-active");
  });
  const someActive = Array.from(pluginItems).some((item) => {
    return item.classList.contains("active");
  });

  const parent = results.parentElement;
  const searchInput = document.querySelector("input.homepage-search-input");

  // if none are active display none
  // if some are active display block
  // if all are not active or not active display none
  // if input is focused display block
  // if (noneActive) {
  //   parent.style.display = "none";
  // } else if (someActive) {
  //   parent.style.display = "block";
  // } else if (!noneActive && !someActive) {
  //   parent.style.display = "none";
  // } else if (searchInput.activeElement) {
  //   parent.style.display = "block";
  // }

  if(noneActive) {
    parent.style.display = "none"
  } else {
    parent.style.display = "block"
  }

  searchInput.addEventListener('mouseleave', {
    parent.style.display = "none"
  })



  // if (noneActive) {
  //   parent.style.display = "none";
  // } else if (someActive) {
  //   parent.style.display = "block";
  // } else {
  //   parent.style.display = "inherit";
  // }

  // if (noneActive) {
  //   parent.style.display = "none";
  // } else if (someActive) {
  //   parent.style.display = "block";
  // } else if (searchInput.value === 0) {
  //   parent.style.display = "none";
  // }

  // if (someActive) {
  //   parent.display.style = "block";
  // } else {
  //   parent.style.display = "none";
  // }
}
