(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  /* header e menu mobile */
  const hdr = $("[data-hdr]");
  const onScroll = () => hdr && hdr.classList.toggle("solid", scrollY > 40 || hdr.hasAttribute("data-solid"));
  addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  const drawer = $("[data-drawer]");
  const setDrawer = (open) => {
    if (!drawer) return;
    drawer.classList.toggle("open", open);
    drawer.setAttribute("aria-hidden", String(!open));
    document.body.style.overflow = open ? "hidden" : "";
  };
  $$("[data-open]").forEach((b) => b.addEventListener("click", () => setDrawer(true)));
  $$("[data-close], [data-drawer] a").forEach((b) => b.addEventListener("click", () => setDrawer(false)));
  addEventListener("keydown", (e) => e.key === "Escape" && setDrawer(false));

  /* comparsa allo scroll */
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver((es) => es.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
    }), { rootMargin: "0px 0px -8% 0px" });
    $$(".rv").forEach((el) => io.observe(el));
  } else $$(".rv").forEach((el) => el.classList.add("in"));

  /* filtri residenze */
  const grid = $("[data-grid]");
  if (grid) {
    const state = { borgo: "all", size: "all" };
    const cards = [...grid.children];
    const count = $("[data-count]"), countM = $("[data-count-m]"), empty = $("[data-empty]");
    const apply = () => {
      let n = 0;
      const filtered = state.borgo !== "all" || state.size !== "all";
      cards.forEach((c) => {
        const ok = (state.borgo === "all" || c.dataset.b === state.borgo) && (state.size === "all" || c.dataset.s === state.size);
        c.classList.toggle("out", !ok);
        if (c.classList.contains("feature")) { c.style.gridColumn = filtered ? "auto" : ""; c.style.flexDirection = filtered ? "column" : ""; }
        if (ok) n++;
      });
      const label = n + (n === 1 ? " residenza" : " residenze");
      if (count) count.textContent = label;
      if (countM) countM.textContent = label;
      if (empty) empty.style.display = n ? "none" : "block";
      grid.scrollLeft = 0;
    };
    $$(".chip").forEach((b) => b.addEventListener("click", () => {
      state[b.dataset.f] = b.dataset.v;
      $$(`.chip[data-f="${b.dataset.f}"]`).forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
      apply();
    }));
    apply();
  }

  /* carosello borghi */
  const rail = $("[data-railbox]");
  $$("[data-rail]").forEach((b) => b.addEventListener("click", () => {
    rail.scrollBy({ left: Number(b.dataset.rail) * rail.clientWidth * 0.8, behavior: "smooth" });
  }));

  /* galleria a schermo intero */
  const lb = $("[data-lb]");
  if (lb) {
    const lbImg = $("[data-lb-img]", lb), lbCount = $("[data-lb-count]", lb), lbThumbs = $("[data-lb-thumbs]", lb);
    let list = [], idx = 0;
    const show = (i) => {
      idx = (i + list.length) % list.length;
      lbImg.src = list[idx];
      lbCount.textContent = `${idx + 1} / ${list.length}`;
      [...lbThumbs.children].forEach((t, k) => t.setAttribute("aria-current", String(k === idx)));
      lbThumbs.children[idx]?.scrollIntoView({ block: "nearest", inline: "center" });
    };
    const open = (l, i) => {
      list = l;
      lbThumbs.innerHTML = l.length > 1 ? l.map((s, k) => `<button data-lb-go="${k}" aria-label="Foto ${k + 1}"><img loading="lazy" src="${s}" alt=""></button>`).join("") : "";
      $$(".lb-nav", lb).forEach((b) => (b.style.visibility = l.length > 1 ? "" : "hidden"));
      lb.showModal ? lb.showModal() : lb.setAttribute("open", "");
      show(i);
    };
    const close = () => (lb.close ? lb.close() : lb.removeAttribute("open"));
    document.addEventListener("click", (e) => {
      const o = e.target.closest("[data-open-lb]");
      if (o) { e.preventDefault(); return open(JSON.parse(o.closest("[data-gallery]").dataset.gallery), Number(o.dataset.openLb)); }
      const st = e.target.closest("[data-lb-step]"); if (st) return show(idx + Number(st.dataset.lbStep));
      const go = e.target.closest("[data-lb-go]"); if (go) return show(Number(go.dataset.lbGo));
      if (e.target.closest("[data-lb-close]")) close();
    });
    lb.addEventListener("keydown", (e) => { if (e.key === "ArrowRight") show(idx + 1); if (e.key === "ArrowLeft") show(idx - 1); });
    let tx = null;
    lb.addEventListener("touchstart", (e) => (tx = e.touches[0].clientX), { passive: true });
    lb.addEventListener("touchend", (e) => {
      if (tx === null) return;
      const dx = e.changedTouches[0].clientX - tx;
      if (Math.abs(dx) > 40) show(idx + (dx < 0 ? 1 : -1));
      tx = null;
    });
  }

  /* tour virtuale 360 (Pannellum caricato solo al primo clic) */
  const PNLM = "https://cdnjs.cloudflare.com/ajax/libs/pannellum/2.5.6/pannellum";
  let pnlmReady = null;
  const loadPnlm = () => pnlmReady || (pnlmReady = new Promise((ok, ko) => {
    const css = document.createElement("link"); css.rel = "stylesheet"; css.href = PNLM + ".css"; document.head.append(css);
    const js = document.createElement("script"); js.src = PNLM + ".js"; js.onload = ok; js.onerror = ko; document.head.append(js);
  }));
  $$("[data-tour]").forEach((tour) => {
    const panos = JSON.parse(tour.dataset.tour);
    const stage = $(".tour-stage", tour), start = $(".tour-start", tour);
    const thumbs = $$(".tour-thumbs button", tour);
    let viewer = null, current = 0;
    const mark = (i) => thumbs.forEach((t, k) => t.setAttribute("aria-pressed", String(k === i)));
    const boot = async (i) => {
      current = i; mark(i);
      if (viewer) return viewer.loadScene("p" + i);
      start.querySelector("span").textContent = "Caricamento del tour…";
      try { await loadPnlm(); } catch { start.querySelector("span").textContent = "Impossibile caricare il tour. Riprova."; return; }
      const box = document.createElement("div"); stage.append(box);
      const scenes = {};
      panos.forEach((p, k) => (scenes["p" + k] = { type: "equirectangular", panorama: p, hfov: 110, autoRotate: -2 }));
      viewer = window.pannellum.viewer(box, { default: { firstScene: "p" + i, autoLoad: true, sceneFadeDuration: 500, mouseZoom: false, showFullscreenCtrl: true, compass: false }, scenes });
      start.remove(); stage.querySelector("img")?.remove();
    };
    start.addEventListener("click", () => boot(current));
    thumbs.forEach((t, k) => t.addEventListener("click", () => boot(k)));
  });
  /* form contatti: AJAX senza reload, reset soltanto su risposta positiva */
  $$("[data-ajax-contact]").forEach((form) => {
    const status = $("[data-form-status]", form);
    const button = $("[data-form-submit]", form);
    if (!status || !button) return;
    const setStatus = (message, type) => {
      status.hidden = false;
      status.className = "contact-result " + (type === "success" ? "is-success" : type === "error" ? "is-error" : "");
      status.textContent = message;
      if (type !== "sending") status.focus({ preventScroll: true });
    };
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      if (!form.reportValidity() || button.disabled) return;
      button.disabled = true;
      form.setAttribute("aria-busy", "true");
      setStatus("Invio in corso…", "sending");
      try {
        const response = await fetch(form.action, {
          method: "POST",
          body: new FormData(form),
          headers: { Accept: "application/json" },
          credentials: "same-origin"
        });
        const data = await response.json().catch(() => ({}));
        if (!response.ok || data.success !== true) {
          throw new Error(typeof data.message === "string" ? data.message : "Invio non riuscito. Riprova più tardi.");
        }
        form.reset();
        setStatus(data.message || "Messaggio inviato correttamente.", "success");
      } catch (error) {
        setStatus(error instanceof Error ? error.message : "Errore di connessione. Riprova.", "error");
      } finally {
        button.disabled = false;
        form.removeAttribute("aria-busy");
      }
    });
  });
})();
