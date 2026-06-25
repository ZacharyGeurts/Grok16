(function () {
  var STORAGE_THEME = "g16-theme";
  var STORAGE_SCALE = "g16-font-scale";
  var root = document.documentElement;
  var currentTheme = "light";

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
    } catch (e) {
      /* private mode / blocked storage */
    }
  }

  function preferredTheme() {
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function normalizeTheme(value) {
    return value === "dark" ? "dark" : "light";
  }

  function applyTheme(theme) {
    currentTheme = normalizeTheme(theme);
    root.setAttribute("data-theme", currentTheme);
    root.classList.toggle("theme-dark", currentTheme === "dark");
    storageSet(STORAGE_THEME, currentTheme);

    var btn = document.getElementById("g16-theme-toggle");
    if (btn) {
      var dark = currentTheme === "dark";
      btn.setAttribute("aria-pressed", dark ? "true" : "false");
      btn.setAttribute("aria-label", dark ? "Switch to light mode" : "Switch to dark mode");
      btn.title = dark ? "Light mode" : "Dark mode";
      btn.textContent = dark ? "☀ Light" : "☾ Dark";
    }
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

  applyTheme(readInitialTheme());
  applyScale(storageGet(STORAGE_SCALE) || "1");

  function navDirectChildren(nav, tag) {
    var out = [];
    var node = nav.firstChild;
    while (node) {
      if (node.nodeType === 1 && node.tagName === tag) out.push(node);
      node = node.nextSibling;
    }
    return out;
  }

  function structureNav(nav) {
    if (!nav || nav.dataset.structured) return;

    var links = navDirectChildren(nav, "A");
    if (!links.length) return;

    var top = document.createElement("div");
    top.className = "nav-top";

    var brand = document.createElement("div");
    brand.className = "nav-brand";
    var strong = nav.querySelector("strong");
    if (strong && strong.parentNode === nav) {
      brand.appendChild(strong);
      var ver = document.createElement("span");
      ver.className = "nav-version";
      ver.textContent = "v16.0.0";
      brand.appendChild(ver);
    }

    top.appendChild(brand);
    nav.insertBefore(top, nav.firstChild);

    var linksWrap = document.createElement("div");
    linksWrap.className = "nav-links";
    links.forEach(function (a) {
      linksWrap.appendChild(a);
    });
    nav.appendChild(linksWrap);

    Array.prototype.slice.call(nav.childNodes).forEach(function (node) {
      if (node.nodeType === 3 && node.textContent.trim()) {
        node.parentNode.removeChild(node);
      }
    });

    nav.dataset.structured = "1";
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

  function mountControls() {
    var nav = document.querySelector("nav");
    if (!nav) return;

    structureNav(nav);

    if (document.getElementById("g16-theme-toggle")) return;

    var top = nav.querySelector(".nav-top") || nav;
    var controls = document.createElement("div");
    controls.className = "nav-controls";
    controls.setAttribute("aria-label", "Display preferences");

    var scaleLabel = document.createElement("label");
    scaleLabel.className = "control-label";
    scaleLabel.setAttribute("for", "g16-font-scale");
    scaleLabel.textContent = "Size";

    var scaleSelect = document.createElement("select");
    scaleSelect.id = "g16-font-scale";
    scaleSelect.className = "control-select";
    scaleSelect.setAttribute("aria-label", "Font size");
    [
      ["0.875", "Small"],
      ["1", "Default"],
      ["1.125", "Large"],
      ["1.25", "XL"],
      ["1.5", "XXL"],
    ].forEach(function (opt) {
      var o = document.createElement("option");
      o.value = opt[0];
      o.textContent = opt[1];
      scaleSelect.appendChild(o);
    });
    scaleSelect.value = root.getAttribute("data-font-scale") || "1";

    var themeBtn = document.createElement("button");
    themeBtn.type = "button";
    themeBtn.id = "g16-theme-toggle";
    themeBtn.className = "control-btn theme-toggle";

    controls.appendChild(scaleLabel);
    controls.appendChild(scaleSelect);
    controls.appendChild(themeBtn);
    top.appendChild(controls);

    applyTheme(currentTheme);

    scaleSelect.addEventListener("change", function () {
      applyScale(scaleSelect.value);
    });

    themeBtn.addEventListener("click", function (event) {
      event.preventDefault();
      applyTheme(currentTheme === "dark" ? "light" : "dark");
    });
  }

  function init() {
    mountControls();
    wrapTables();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();