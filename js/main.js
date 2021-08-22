function escapeRegex(string) {
  return string.replace(/[-\/\\^$*+?.()|[\]{}]/g, "\\$&");
}

window.addEventListener("DOMContentLoaded", () => {
  var field = document.querySelector("input.grid-search");
  if (!field) {
    return;
  }

  var grid = document.querySelector("ul.button-grid");
  var items = grid.querySelectorAll("li[data-search-terms]");

  field.addEventListener("input", (e) => {
    var query = e.target.value.trim().toLowerCase();

    items.forEach((item) => {
      var terms = item.getAttribute("data-search-terms");

      if (!query || terms.toLowerCase().indexOf(query) > -1) {
        item.style.display = "block";
      } else {
        item.style.display = "none";
      }
    });
  });

  field.disabled = false;
});
