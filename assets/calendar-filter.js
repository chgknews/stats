(function () {
  const root = document.getElementById("calendar-filter");
  if (!root) return;

  const form = document.getElementById("calendar-filter-form");
  const toggle = document.getElementById("calendar-filter-toggle");
  const countEl = document.getElementById("calendar-filter-count");
  const emptyEl = document.getElementById("calendar-filter-empty");
  const rows = Array.from(root.querySelectorAll("tbody tr"));

  function checkedValues(name) {
    return Array.from(form.querySelectorAll('input[name="' + name + '"]:checked')).map(
      function (input) {
        return input.value;
      }
    );
  }

  function hasOverlap(haystack, needles) {
    if (!needles.length) return true;
    return needles.some(function (value) {
      return haystack.indexOf(value) !== -1;
    });
  }

  function applyFilters() {
    const geo = checkedValues("geo");
    const age = checkedValues("age");
    const game = checkedValues("game");
    const champInput = form.querySelector('input[name="champ"]');
    const champOnly = Boolean(champInput && champInput.checked);
    let visible = 0;

    rows.forEach(function (row) {
      const rowGeo = (row.getAttribute("data-geo") || "").split(/\s+/).filter(Boolean);
      const rowAge = (row.getAttribute("data-age") || "").split(/\s+/).filter(Boolean);
      const rowGame = (row.getAttribute("data-game") || "").split(/\s+/).filter(Boolean);
      const isChamp = row.getAttribute("data-champ") === "1";
      const match =
        hasOverlap(rowGeo, geo) &&
        hasOverlap(rowAge, age) &&
        hasOverlap(rowGame, game) &&
        (!champOnly || isChamp);

      row.hidden = !match;
      if (match) visible += 1;
    });

    emptyEl.hidden = visible !== 0;
    countEl.textContent = "Показано: " + visible + " из " + rows.length;
    syncUrl(geo, age, game, champOnly);
  }

  function syncUrl(geo, age, game, champOnly) {
    const params = new URLSearchParams();
    if (geo.length) params.set("geo", geo.join(","));
    if (age.length) params.set("age", age.join(","));
    if (game.length) params.set("game", game.join(","));
    if (champOnly) params.set("champ", "1");
    if (root.classList.contains("is-collapsed")) params.set("hide", "1");
    const query = params.toString();
    const next = query ? "?" + query : window.location.pathname;
    history.replaceState(null, "", next);
  }

  function applyUrl() {
    const params = new URLSearchParams(window.location.search);
    function restore(name, key) {
      const values = (params.get(key) || "").split(",").filter(Boolean);
      form.querySelectorAll('input[name="' + name + '"]').forEach(function (input) {
        input.checked = values.indexOf(input.value) !== -1;
      });
    }
    restore("geo", "geo");
    restore("age", "age");
    restore("game", "game");
    const champInput = form.querySelector('input[name="champ"]');
    if (champInput) champInput.checked = params.get("champ") === "1";
    setCollapsed(params.get("hide") === "1");
  }

  function setCollapsed(collapsed) {
    root.classList.toggle("is-collapsed", collapsed);
    toggle.setAttribute("aria-expanded", collapsed ? "false" : "true");
    toggle.textContent = collapsed ? "Показать фильтры" : "Скрыть фильтры";
  }

  toggle.addEventListener("click", function () {
    setCollapsed(!root.classList.contains("is-collapsed"));
    applyFilters();
  });

  form.addEventListener("change", applyFilters);
  form.addEventListener("reset", function () {
    window.setTimeout(applyFilters, 0);
  });

  applyUrl();
  applyFilters();
})();
