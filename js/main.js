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
        } else {
          item.style.display = "none";
        }
      });
    });

    searchInput.disabled = false;
  });
}

navbarSearch();
