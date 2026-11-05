/* Motion 3: ปุ่มคัดลอก — copy แล้วเปลี่ยนข้อความ + สลับไอคอน copy/check */

export function initCopy(): void {
  document.addEventListener("click", async (e) => {
    const target = e.target as HTMLElement | null;
    const btn = target?.closest<HTMLElement>(".copy-btn");
    if (!btn || btn.classList.contains("is-done")) return;
    const pre = btn.closest("figure")?.querySelector("pre");
    if (!pre) return;

    const text = pre.innerText;
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

    const label = btn.querySelector("span");
    const original = label?.textContent ?? "คัดลอก";
    btn.classList.add("is-done");
    btn.setAttribute("disabled", "");
    if (label) label.textContent = "คัดลอกแล้ว";
    setTimeout(() => {
      btn.classList.remove("is-done");
      btn.removeAttribute("disabled");
      if (label) label.textContent = original;
    }, 1600);
  });
}
