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
      navbarSearchLogic();
    });

    searchInput.disabled = false;
  });
}

navbarSearch();

function navbarSearchLogic() {
  const results = document.querySelector("ul.navbar-search-list");
  const pluginItems = results.querySelectorAll("li");
  const noneActive = Array.from(pluginItems).every((item) => {
    return item.classList.contains("not-active");
  });
  const someActive = Array.from(pluginItems).some((item) => {
    return item.classList.contains("active");
  });

  const parent = results.parentElement;

  if (noneActive) {
    parent.style.display = "none";
  } else if (someActive) {
    parent.style.display = "block";
  } else if (!noneActive && !someActive) {
    parent.style.display = "none";
  } else if (searchInput.activeElement) {
    parent.style.display = "block";
  }

  results.addEventListener("mouseleave", (e) => {
    parent.style.display = "none";
  });
  const searchInput = document.querySelector("input.homepage-search-input");
  searchInput.addEventListener("mouseenter", (e) => {
    parent.style.display = "block";
  });
}

function copyToClipBoard() {
  const pre = document.querySelectorAll("pre");

  pre.forEach((codeBlock) => {
    codeBlock.style.display = "flex";
    codeBlock.style.alignItems = "center";
    codeBlock.style.justifyContent = "space-between";
    codeBlock.style.cursor = "grab";
    const codeInner = codeBlock.querySelector("code");
    const copyButton = document.createElement("button");
    copyButton.type = "button";
    copyButton.ariaLabel = "Copy code to clipboard";
    codeBlock.append(copyButton);
    copyButton.addEventListener("click", function () {
      const code = codeInner.innerText.trim();
      window.navigator.clipboard.writeText(code);
    });
  });
}

copyToClipBoard();
