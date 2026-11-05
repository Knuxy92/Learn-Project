/* Motion ตาม Design.md — มีแค่ 3 อย่าง
   1) เนื้อหาค่อยเลื่อนขึ้นและจางเข้า  2) แถบอ่านด้านบน  3) ปุ่มคัดลอกเปลี่ยนข้อความ
   animate เฉพาะ transform กับ opacity เท่านั้น */

import { initCopy } from "./copy";
import {
  getTeaching,
  setTeaching,
  initTasks,
  initResume,
  setLastChapter,
} from "./progress";

const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)").matches;

/* 1) เนื้อหาค่อยเลื่อนขึ้นและจางเข้า (ไล่จังหวะเป็นชุด) */
function initReveal(): void {
  const revealEls = document.querySelectorAll<HTMLElement>("[data-reveal]");
  if (!("IntersectionObserver" in window) || reduceMotion) {
    revealEls.forEach((el) => el.classList.add("is-in"));
    return;
  }
  const io = new IntersectionObserver(
    (entries) => {
      let i = 0;
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        const el = entry.target as HTMLElement;
        el.style.transitionDelay = `${Math.min(i * 55, 320)}ms`;
        el.classList.add("is-in");
        el.addEventListener(
          "transitionend",
          () => {
            el.style.transitionDelay = "";
          },
          { once: true }
        );
        io.unobserve(el);
        i += 1;
      }
    },
    { threshold: 0.08, rootMargin: "0px 0px -6% 0px" }
  );
  revealEls.forEach((el) => io.observe(el));
}

/* 2) แถบอ่าน: อ่านไปแล้วกี่เปอร์เซ็นต์ (CSS ปิดเองบนมือถือ) */
function initReadbar(): void {
  const bar = document.querySelector<HTMLElement>("#readbar span");
  if (!bar) return;
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

/* ไฮไลต์หัวข้อที่กำลังอ่านในสารบัญซ้าย */
function initSpy(): void {
  const tocLinks = [...document.querySelectorAll<HTMLAnchorElement>('.toc a[href^="#"]')];
  if (!tocLinks.length || !("IntersectionObserver" in window)) return;
  const map = new Map<Element, HTMLAnchorElement>();
  tocLinks.forEach((a) => {
    const sec = document.getElementById(a.getAttribute("href")!.slice(1));
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

/* โหมดสอน: ซ่อนผลลัพธ์ไว้ก่อนให้เดา แล้วแตะเพื่อเฉลย (default เปิด, จำสถานะ) */
function initTeaching(): void {
  const btn = document.getElementById("teach");
  if (!btn) return;
  const apply = (on: boolean) => {
    document.body.classList.toggle("teaching", on);
    btn.setAttribute("aria-pressed", String(on));
  };
  apply(getTeaching());
  btn.addEventListener("click", () => {
    const on = !document.body.classList.contains("teaching");
    setTeaching(on);
    apply(on);
  });
  document.querySelectorAll<HTMLElement>("figure.result").forEach((fig) => {
    fig.addEventListener("click", () => {
      if (document.body.classList.contains("teaching")) fig.classList.add("is-revealed");
    });
  });
}

/* เก็บบทล่าสุดไว้โชว์หน้าแรก */
function initLastChapter(): void {
  const ch = document.documentElement.dataset.ch;
  if (ch) setLastChapter(ch);
}

initReveal();
initReadbar();
initSpy();
initTeaching();
initCopy();
initTasks();
initResume();
initLastChapter();
