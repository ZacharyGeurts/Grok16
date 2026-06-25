(function () {
  var STORAGE_THEME = "g16-theme";
  var STORAGE_SCALE = "g16-font-scale";
  var root = document.documentElement;

  function preferredTheme() {
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function applyTheme(theme) {
    root.setAttribute("data-theme", theme);
    localStorage.setItem(STORAGE_THEME, theme);
    var btn = document.getElementById("g16-theme-toggle");
    if (btn) {
      var dark = theme === "dark";
      btn.setAttribute("aria-pressed", dark ? "true" : "false");
      btn.setAttribute("aria-label", dark ? "Switch to light mode" : "Switch to dark mode");
      btn.title = dark ? "Light mode" : "Dark mode";
      btn.textContent = dark ? "☀ Light" : "☾ Dark";
    }
  }

  function applyScale(scale) {
    root.setAttribute("data-font-scale", scale);
    localStorage.setItem(STORAGE_SCALE, scale);
    var sel = document.getElementById("g16-font-scale");
    if (sel) sel.value = scale;
  }

  var theme = localStorage.getItem(STORAGE_THEME) || preferredTheme();
  var scale = localStorage.getItem(STORAGE_SCALE) || "1";
  applyTheme(theme);
  applyScale(scale);

  function mountControls() {
    var nav = document.querySelector("nav");
    if (!nav || document.getElementById("g16-theme-toggle")) return;

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
    scaleSelect.value = scale;

    var themeBtn = document.createElement("button");
    themeBtn.type = "button";
    themeBtn.id = "g16-theme-toggle";
    themeBtn.className = "control-btn theme-toggle";

    controls.appendChild(scaleLabel);
    controls.appendChild(scaleSelect);
    controls.appendChild(themeBtn);
    nav.appendChild(controls);

    applyTheme(theme);

    scaleSelect.addEventListener("change", function () {
      applyScale(scaleSelect.value);
    });

    themeBtn.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      applyTheme(next);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mountControls);
  } else {
    mountControls();
  }
})();