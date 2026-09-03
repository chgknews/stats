(function () {
  if (window.__chronicleExpandBound) return;
  window.__chronicleExpandBound = true;

  function wrapperOf(el) {
    return el.closest(".text-wrapper");
  }

  function setOpen(wrapper, open) {
    if (!wrapper) return;
    var details = wrapper.querySelector(".extra-details");
    var button = wrapper.querySelector(".toggle-btn");
    var arrow = wrapper.querySelector(".arrow-icon");
    var summary = wrapper.querySelector(".summary-text");
    if (details) {
      if (open) details.classList.add("visible");
      else details.classList.remove("visible");
    }
    if (button) {
      button.setAttribute("aria-expanded", open ? "true" : "false");
      button.setAttribute("aria-label", open ? "Скрыть" : "Показать");
    }
    if (arrow) {
      arrow.textContent = open ? "▼" : "▶";
    }
    if (summary) {
      if (open) summary.classList.add("expanded");
      else summary.classList.remove("expanded");
    }
  }

  function setAll(root, open) {
    var wrappers = root.querySelectorAll(".text-wrapper");
    for (var i = 0; i < wrappers.length; i++) {
      setOpen(wrappers[i], open);
    }
  }

  document.addEventListener("click", function (event) {
    var root = event.target.closest(".table-container");
    if (!root) return;

    var expandAll = event.target.closest("[data-expand-all]");
    if (expandAll && root.contains(expandAll)) {
      event.preventDefault();
      setAll(root, true);
      return;
    }

    var collapseAll = event.target.closest("[data-collapse-all]");
    if (collapseAll && root.contains(collapseAll)) {
      event.preventDefault();
      setAll(root, false);
      return;
    }

    var toggle = event.target.closest(".toggle-btn");
    if (toggle && root.contains(toggle)) {
      event.preventDefault();
      var wrapper = wrapperOf(toggle);
      var details = wrapper && wrapper.querySelector(".extra-details");
      var isOpen = !!(details && details.classList.contains("visible"));
      setOpen(wrapper, !isOpen);
    }
  });
})();
