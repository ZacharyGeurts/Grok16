(function () {
  var STORAGE_THEME = "g16-theme";
  var STORAGE_SCALE = "g16-font-scale";
  var root = document.documentElement;

  function storageGet(key) {
    try {
      return localStorage.getItem(key);
    } catch (e) {
      return null;
    }
  }

  function storageSet(key, value) {
    try {
      localStorage.setItem(key, value);
    } catch (e) {}
  }

  function preferredTheme() {
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function normalizeTheme(value) {
    return value === "dark" ? "dark" : "light";
  }

  function clearInlineBodyPaint() {
    var body = document.body;
    if (!body) return;
    body.style.removeProperty("background-color");
    body.style.removeProperty("color");
  }

  function updateThemeButtons(theme) {
    var lightBtn = document.getElementById("g16-theme-light");
    var darkBtn = document.getElementById("g16-theme-dark");
    if (lightBtn) lightBtn.setAttribute("aria-pressed", theme === "light" ? "true" : "false");
    if (darkBtn) darkBtn.setAttribute("aria-pressed", theme === "dark" ? "true" : "false");
  }

  function applyTheme(theme) {
    theme = normalizeTheme(theme);
    root.setAttribute("data-theme", theme);
    clearInlineBodyPaint();
    updateThemeButtons(theme);
    storageSet(STORAGE_THEME, theme);
  }

  function applyScale(scale) {
    var allowed = { "0.875": 1, "1": 1, "1.125": 1, "1.25": 1, "1.5": 1 };
    if (!allowed[scale]) scale = "1";
    root.setAttribute("data-font-scale", scale);
    storageSet(STORAGE_SCALE, scale);
    var sel = document.getElementById("g16-font-scale");
    if (sel) sel.value = scale;
  }

  function readInitialTheme() {
    var stored = storageGet(STORAGE_THEME);
    if (stored === "dark" || stored === "light") return stored;
    var attr = root.getAttribute("data-theme");
    if (attr === "dark" || attr === "light") return attr;
    return preferredTheme();
  }

  function bindControls() {
    var scaleSelect = document.getElementById("g16-font-scale");
    if (scaleSelect) {
      scaleSelect.addEventListener("change", function () {
        applyScale(scaleSelect.value);
      });
    }

    var lightBtn = document.getElementById("g16-theme-light");
    var darkBtn = document.getElementById("g16-theme-dark");

    if (lightBtn) {
      lightBtn.addEventListener("click", function (e) {
        e.preventDefault();
        applyTheme("light");
      });
    }

    if (darkBtn) {
      darkBtn.addEventListener("click", function (e) {
        e.preventDefault();
        applyTheme("dark");
      });
    }
  }

  function wrapTables() {
    Array.prototype.forEach.call(document.querySelectorAll("table"), function (table) {
      var parent = table.parentElement;
      if (parent && parent.classList.contains("table-scroll")) return;
      var wrap = document.createElement("div");
      wrap.className = "table-scroll";
      wrap.setAttribute("tabindex", "0");
      wrap.setAttribute("role", "region");
      wrap.setAttribute("aria-label", "Scrollable table");
      table.parentNode.insertBefore(wrap, table);
      wrap.appendChild(table);
    });
  }

  function init() {
    applyTheme(readInitialTheme());
    applyScale(storageGet(STORAGE_SCALE) || "1");
    bindControls();
    wrapTables();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();