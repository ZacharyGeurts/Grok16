/**
 * Hostess7 Dewey library flyout — textbooks per language, best-guess ordering.
 */
(function (global) {
  "use strict";

  const state = {
    langs: [],
    extMap: {},
    books: [],
    bookByLang: new Map(),
    open: true,
    readerOpen: false,
    selectedLang: "plaintext",
    guesses: [],
    readerBook: null,
    readerText: "",
    readerLoading: false,
  };

  function $(id) { return document.getElementById(id); }

  function esc(s) {
    return String(s ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function langLabel(id) {
    const hit = state.langs.find((l) => l.id === id);
    return hit?.label || id;
  }

  function bookForLang(langId) {
    return state.bookByLang.get(langId) || null;
  }

  async function loadCatalog() {
    const [langs, books] = await Promise.all([
      fetch("data/languages-index.json").then((r) => r.json()),
      fetch("data/books-catalog.json").then((r) => r.json()),
    ]);
    state.langs = langs.languages || [];
    state.extMap = langs.extensions || {};
    state.books = books.books || [];
    state.bookByLang = new Map(state.books.map((b) => [b.lang_id, b]));
    if (global.AmmoCodeHighlight?.mergeExtensions) {
      global.AmmoCodeHighlight.mergeExtensions(state.extMap);
    }
    fillLangSelect();
    renderSidebar();
  }

  function fillLangSelect() {
    const sel = $("g16-lang-select");
    if (!sel) return;
    sel.innerHTML = state.langs
      .map((l) => `<option value="${esc(l.id)}">${esc(l.label)} (${esc(l.id)})</option>`)
      .join("");
    sel.value = state.selectedLang;
  }

  function orderedBooks() {
    const guessIds = state.guesses.map((g) => g.lang);
    const seen = new Set();
    const out = [];
    for (const gid of guessIds) {
      const b = bookForLang(gid);
      if (b && !seen.has(b.id)) {
        out.push({ ...b, guess: true });
        seen.add(b.id);
      }
    }
    const sel = bookForLang(state.selectedLang);
    if (sel && !seen.has(sel.id)) {
      out.push({ ...sel, guess: false, selected: true });
      seen.add(sel.id);
    }
    for (const b of state.books) {
      if (!seen.has(b.id)) out.push({ ...b, guess: false });
    }
    return out;
  }

  function renderGuesses() {
    const el = $("g16-guesses");
    const sec = $("g16-guess-section");
    if (!el || !sec) return;
    const top = state.guesses.filter((g) => bookForLang(g.lang)).slice(0, 3);
    if (!top.length) {
      sec.hidden = true;
      return;
    }
    sec.hidden = false;
    el.innerHTML = top
      .map((g) => {
        const b = bookForLang(g.lang);
        return `<button type="button" class="g16-guess-btn" data-lang="${esc(g.lang)}" title="Score ${g.score}">
          <span class="g16-guess-lang">${esc(langLabel(g.lang))}</span>
          <span class="g16-guess-book">${esc(b?.title || "")}</span>
        </button>`;
      })
      .join("");
    el.querySelectorAll(".g16-guess-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        const lang = btn.getAttribute("data-lang");
        setSelectedLang(lang);
        const b = bookForLang(lang);
        if (b) openReader(b);
      });
    });
  }

  function renderBookList() {
    const el = $("g16-book-list");
    if (!el) return;
    const books = orderedBooks();
    el.innerHTML = books
      .map((b) => {
        const tags = [];
        if (b.guess) tags.push("guess");
        if (b.selected) tags.push("selected");
        if (b.lang_id === state.selectedLang) tags.push("active");
        return `<button type="button" class="g16-book-spine ${tags.join(" ")}" data-lang="${esc(b.lang_id)}" data-id="${esc(b.id)}">
          <span class="g16-spine-title">${esc(b.title)}</span>
          <span class="g16-spine-lang">${esc(b.lang_id)}</span>
        </button>`;
      })
      .join("");
    el.querySelectorAll(".g16-book-spine").forEach((btn) => {
      btn.addEventListener("click", () => {
        const lang = btn.getAttribute("data-lang");
        const id = btn.getAttribute("data-id");
        setSelectedLang(lang);
        const b = state.books.find((x) => x.id === id);
        if (b) openReader(b);
      });
    });
  }

  function renderSidebar() {
    renderGuesses();
    renderBookList();
    const sel = $("g16-lang-select");
    if (sel) sel.value = state.selectedLang;
  }

  function setSelectedLang(langId, opts) {
    state.selectedLang = langId || "plaintext";
    renderSidebar();
    const sel = $("g16-lang-select");
    if (sel) sel.value = state.selectedLang;
    if (!opts?.fromEditor && global.Grok16EditorPages?.setLanguage) {
      global.Grok16EditorPages.setLanguage(state.selectedLang, { manual: true });
    }
  }

  function setGuesses(guesses) {
    state.guesses = guesses || [];
    renderSidebar();
  }

  function toggleSidebar() {
    state.open = !state.open;
    document.body.classList.toggle("g16-lib-collapsed", !state.open);
    const btn = $("g16-lib-toggle");
    if (btn) {
      btn.setAttribute("aria-expanded", String(state.open));
      btn.title = state.open ? "Collapse library" : "Expand library";
    }
    try {
      localStorage.setItem("g16-lib-open", state.open ? "1" : "0");
    } catch (_) { /* ignore */ }
  }

  function toggleReader() {
    state.readerOpen = !state.readerOpen;
    document.body.classList.toggle("g16-reader-open", state.readerOpen);
    const fly = $("g16-reader-flyout");
    if (fly) fly.hidden = !state.readerOpen;
  }

  function renderMarkdown(text) {
    let html = esc(text);
    html = html.replace(/^### (.+)$/gm, "<h3>$1</h3>");
    html = html.replace(/^## (.+)$/gm, "<h2>$1</h2>");
    html = html.replace(/^# (.+)$/gm, "<h1>$1</h1>");
    html = html.replace(/!\[([^\]]*)\]\(h7fig:[^)]+\)/g, "<em class=\"g16-fig\">[$1]</em>");
    html = html.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
    html = html.replace(/`([^`]+)`/g, "<code>$1</code>");
    return html;
  }

  async function openReader(book) {
    state.readerBook = book;
    state.readerOpen = true;
    state.readerLoading = true;
    document.body.classList.add("g16-reader-open");
    const fly = $("g16-reader-flyout");
    const body = $("g16-reader-body");
    const title = $("g16-reader-title");
    if (fly) fly.hidden = false;
    if (title) title.textContent = book.title || book.id;
    if (body) body.innerHTML = "<p class=\"g16-reader-loading\">Opening textbook…</p>";

    let text = "";
    try {
      const local = await fetch(`data/manuals/${book.lang_id}.md`);
      if (local.ok) text = await local.text();
    } catch (_) { /* fallback */ }

    if (!text.trim()) {
      try {
        const meta = await fetch(book.book_json).then((r) => r.json());
        const entries = meta.lies_index?.entries || [];
        text = entries.map((e) => e.excerpt).filter(Boolean).join("\n\n---\n\n");
        if (!text) text = `# ${book.title}\n\nTextbook on Hostess7 — open locally for full H7c reader.\n\n${book.github_tree}`;
      } catch (err) {
        text = `Could not load manual: ${err.message || err}`;
      }
    }

    state.readerText = text;
    state.readerLoading = false;
    if (body) body.innerHTML = `<article class="g16-reader-text">${renderMarkdown(text)}</article>`;
  }

  function closeReader() {
    state.readerOpen = false;
    state.readerBook = null;
    document.body.classList.remove("g16-reader-open");
    const fly = $("g16-reader-flyout");
    if (fly) fly.hidden = true;
  }

  function bind() {
    $("g16-lib-toggle")?.addEventListener("click", toggleSidebar);
    $("g16-reader-close")?.addEventListener("click", closeReader);
    $("g16-lang-select")?.addEventListener("change", (e) => {
      setSelectedLang(e.target.value, { manual: true });
    });
    $("g16-lang-filter")?.addEventListener("input", (e) => {
      const q = e.target.value.trim().toLowerCase();
      const sel = $("g16-lang-select");
      if (!sel) return;
      [...sel.options].forEach((opt) => {
        const show = !q || opt.text.toLowerCase().includes(q) || opt.value.includes(q);
        opt.hidden = !show;
      });
    });
    try {
      if (localStorage.getItem("g16-lib-open") === "0") {
        state.open = false;
        document.body.classList.add("g16-lib-collapsed");
      }
    } catch (_) { /* ignore */ }
  }

  async function init() {
    bind();
    await loadCatalog();
  }

  global.Grok16EditorLibrary = {
    init,
    setGuesses,
    setSelectedLang,
    bookForLang,
    openReader,
    toggleSidebar,
  };
})(typeof globalThis !== "undefined" ? globalThis : window);