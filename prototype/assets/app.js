/* สมุดบทเรียน — หน้าตัวอย่าง
   Motion ยึด Design.md: มีแค่ 3 อย่าง
   1) เนื้อหาค่อยเลื่อนขึ้นและจางเข้า  2) แถบอ่านด้านบน  3) ปุ่มคัดลอกเปลี่ยนข้อความ
   animate เฉพาะ transform กับ opacity เท่านั้น */
(() => {
  "use strict";

  const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ไอคอน Lucide (ซ่อนจาก screen reader เพราะตกแต่งล้วน) */
  if (window.lucide) lucide.createIcons({ attrs: { "aria-hidden": "true" } });

  /* 1) เนื้อหาค่อยเลื่อนขึ้นและจางเข้า (ไล่จังหวะเป็นชุด) */
  const revealEls = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window && !reduceMotion) {
    const io = new IntersectionObserver(
      (entries) => {
        let i = 0;
        for (const entry of entries) {
          if (!entry.isIntersecting) continue;
          const el = entry.target;
          const delay = Math.min(i * 55, 320);
          el.style.transitionDelay = `${delay}ms`;
          el.classList.add("is-in");
          el.addEventListener(
            "transitionend",
            () => { el.style.transitionDelay = ""; },
            { once: true }
          );
          io.unobserve(el);
          i += 1;
        }
      },
      { threshold: 0.08, rootMargin: "0px 0px -6% 0px" }
    );
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add("is-in"));
  }

  /* 2) แถบอ่าน: อ่านไปแล้วกี่เปอร์เซ็นต์ (CSS ปิดเองบนมือถือ) */
  const bar = document.querySelector("#readbar span");
  if (bar) {
    let ticking = false;
    const update = () => {
      ticking = false;
      const doc = document.documentElement;
      const max = doc.scrollHeight - window.innerHeight;
      const p = max > 0 ? Math.min(1, Math.max(0, doc.scrollTop / max)) : 0;
      bar.style.transform = `scaleX(${p})`;
    };
    window.addEventListener(
      "scroll",
      () => {
        if (!ticking) {
          ticking = true;
          requestAnimationFrame(update);
        }
      },
      { passive: true }
    );
    update();
  }

  /* 3) ปุ่มคัดลอก: เปลี่ยนข้อความชั่วคราว (ไอคอน copy/check สลับด้วย CSS) */
  document.querySelectorAll("[data-copy]").forEach((btn) => {
    const target = document.getElementById(btn.dataset.copy);
    if (!target) return;
    const label = btn.querySelector("span");
    btn.addEventListener("click", async () => {
      const text = target.innerText;
      try {
        await navigator.clipboard.writeText(text);
      } catch {
        const ta = document.createElement("textarea");
        ta.value = text;
        ta.setAttribute("readonly", "");
        ta.style.position = "fixed";
        ta.style.opacity = "0";
        document.body.appendChild(ta);
        ta.select();
        document.execCommand("copy");
        ta.remove();
      }
      const original = label.textContent;
      label.textContent = "คัดลอกแล้ว";
      btn.classList.add("is-done");
      btn.disabled = true;
      setTimeout(() => {
        label.textContent = original;
        btn.classList.remove("is-done");
        btn.disabled = false;
      }, 1600);
    });
  });

  /* ไฮไลต์หัวข้อที่กำลังอ่านในสารบัญซ้าย */
  const tocLinks = [...document.querySelectorAll('.toc a[href^="#"]')];
  if (tocLinks.length && "IntersectionObserver" in window) {
    const map = new Map();
    tocLinks.forEach((a) => {
      const sec = document.getElementById(a.getAttribute("href").slice(1));
      if (sec) map.set(sec, a);
    });
    const spy = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (!entry.isIntersecting) continue;
          const link = map.get(entry.target);
          if (!link) continue;
          tocLinks.forEach((x) => x.classList.remove("is-active"));
          link.classList.add("is-active");
        }
      },
      { rootMargin: "-20% 0px -70% 0px" }
    );
    map.forEach((_, sec) => spy.observe(sec));
  }

  /* โหมดสอน: ซ่อนผลลัพธ์ไว้ก่อนให้เดา แล้วแตะเพื่อเฉลย (default เปิด) */
  const teachBtn = document.getElementById("teach");
  if (teachBtn) {
    const setTeach = (on) => {
      document.body.classList.toggle("teaching", on);
      teachBtn.setAttribute("aria-pressed", String(on));
    };
    setTeach(true);
    teachBtn.addEventListener("click", () => {
      setTeach(!document.body.classList.contains("teaching"));
    });
    document.querySelectorAll("figure.result").forEach((fig) => {
      fig.addEventListener("click", () => {
        if (document.body.classList.contains("teaching")) {
          fig.classList.add("is-revealed");
        }
      });
    });
  }
})();
