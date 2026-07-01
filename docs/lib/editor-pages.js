/**
 * Grok16 GitHub Pages — static AmmoCode syntax editor shell.
 */
(function (global) {
  "use strict";

  const STORAGE_KEY = "grok16-editor-draft";

  const state = {
    language: "plaintext",
    path: "untitled",
    dirty: false,
    autoDiscern: true,
    lastDiscern: "",
  };

  function $(id) { return document.getElementById(id); }

  function editorText() {
    return $("g16-editor")?.value || "";
  }

  function paint(opts) {
    const text = editorText();
    const hi = $("g16-highlight");
    const gut = $("g16-gutter");
    if (hi && global.AmmoCodeHighlight) {
      hi.innerHTML = global.AmmoCodeHighlight.highlight(text, state.language);
    }
    if (gut && global.AmmoCodeHighlight) {
      gut.textContent = global.AmmoCodeHighlight.gutterLines(text);
    }
    syncScroll();
    if (!opts?.skipDiscern) runDiscern();
  }

  function syncScroll() {
    const ed = $("g16-editor");
    const hi = $("g16-highlight");
    const gut = $("g16-gutter");
    if (!ed) return;
    if (hi) {
      hi.scrollTop = ed.scrollTop;
      hi.scrollLeft = ed.scrollLeft;
    }
    if (gut) gut.scrollTop = ed.scrollTop;
  }

  function setLanguage(lang, opts) {
    state.language = lang || "plaintext";
    if (opts?.manual) state.autoDiscern = false;
    const el = $("g16-lang-label");
    if (el) el.textContent = state.language;
    if (!opts?.skipPaint) paint({ skipDiscern: true });
  }

  function runDiscern() {
    if (!global.Grok16EditorDiscern) return;
    const text = editorText();
    const { lang, guesses } = global.Grok16EditorDiscern.discern(
      state.path,
      text,
      global.AmmoCodeHighlight?.EXT_MAP
    );
    const guessEl = $("g16-discern-pill");
    if (guessEl) {
      guessEl.textContent = guesses.length
        ? `guess: ${guesses.map((g) => g.lang).join(", ")}`
        : "discern: —";
    }
    global.Grok16EditorLibrary?.setGuesses(guesses);
    if (text.trim().length > 8 && state.autoDiscern && text !== state.lastDiscern) {
      state.lastDiscern = text;
      state.language = lang;
      $("g16-lang-label").textContent = lang;
      global.Grok16EditorLibrary?.setSelectedLang(lang, { fromEditor: true });
      const hi = $("g16-highlight");
      if (hi && global.AmmoCodeHighlight) {
        hi.innerHTML = global.AmmoCodeHighlight.highlight(text, state.language);
      }
    }
  }

  function saveDraft() {
    try {
      localStorage.setItem(
        STORAGE_KEY,
        JSON.stringify({
          content: editorText(),
          language: state.language,
          path: state.path,
        })
      );
    } catch (_) { /* ignore */ }
  }

  function loadDraft() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return;
      const doc = JSON.parse(raw);
      if (doc.content && $("g16-editor")) $("g16-editor").value = doc.content;
      if (doc.language) state.language = doc.language;
      if (doc.path) state.path = doc.path;
      $("g16-path-label").textContent = state.path;
    } catch (_) { /* ignore */ }
  }

  function bindEditor() {
    const ed = $("g16-editor");
    if (!ed) return;
    ed.addEventListener("input", () => {
      state.dirty = true;
      paint();
      saveDraft();
    });
    ed.addEventListener("scroll", syncScroll);
    ed.addEventListener("keydown", (e) => {
      if (e.key === "Tab") {
        e.preventDefault();
        const start = ed.selectionStart;
        const end = ed.selectionEnd;
        const val = ed.value;
        ed.value = val.slice(0, start) + "    " + val.slice(end);
        ed.selectionStart = ed.selectionEnd = start + 4;
        paint();
      }
    });
    $("g16-file-input")?.addEventListener("change", async (e) => {
      const file = e.target.files?.[0];
      if (!file) return;
      const text = await file.text();
      ed.value = text;
      state.path = file.name;
      state.dirty = false;
      $("g16-path-label").textContent = state.path;
      paint();
      saveDraft();
      e.target.value = "";
    });
    $("g16-open-btn")?.addEventListener("click", () => $("g16-file-input")?.click());
    $("g16-export-btn")?.addEventListener("click", () => {
      const blob = new Blob([editorText()], { type: "text/plain" });
      const a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = state.path === "untitled" ? "snippet.txt" : state.path;
      a.click();
      URL.revokeObjectURL(a.href);
      state.dirty = false;
      $("g16-status").textContent = "exported (non-destructive)";
    });
    $("g16-clear-btn")?.addEventListener("click", () => {
      ed.value = "";
      state.path = "untitled";
      state.language = "plaintext";
      $("g16-path-label").textContent = state.path;
      paint();
      saveDraft();
    });
  }

  async function init() {
    loadDraft();
    bindEditor();
    setLanguage(state.language);
    await global.Grok16EditorLibrary?.init();
    paint();
    $("g16-status").textContent = "Programmerland · static editor · compile via local AmmoCode";
  }

  global.Grok16EditorPages = { init, setLanguage, paint };
  document.addEventListener("DOMContentLoaded", init);
})(typeof globalThis !== "undefined" ? globalThis : window);