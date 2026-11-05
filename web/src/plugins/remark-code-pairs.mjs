/* จับคู่บล็อกโค้ดกับบล็อกผลลัพธ์ (Design.md ข้อ 3) — ทำงานระดับ remark (mdast)
   เพราะ lang ของ code มีอยู่เฉพาะที่นี่ (Astro ใส่ class language-x ให้ทีหลัง
   และ Shiki รันหลัง user plugins เสมอ)

   กติกา: ย่อหน้าป้าย = สั้น (≤60 ตัวอักษร) + จบด้วย ":" + มีคำ "ผลลัพธ์"
   (ครอบคลุม "ผลลัพธ์:" "ผลลัพธ์ที่ควรเห็น:" "ตัวอย่างผลลัพธ์:")
   code(lang อื่น) + ป้าย + code(txt) → ครอบ <div class="pair tight">
   code เดี่ยว → figure.code · txt ไม่มีคู่ → figure.result เดี่ยว

   โครง HTML แทรกเป็น mdast html node (raw) — Shiki ยัง highlight <pre><code>
   ที่ถูก remark-rehype สร้างตามปกติ */

const RESULT_LANGS = new Set(["txt", "text", "output", "console"]);

const esc = (s) =>
  s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

const html = (value) => ({ type: "html", value });

const ICONS = `
<svg class="ic-copy" aria-hidden="true" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></svg>
<svg class="ic-done" aria-hidden="true" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>`;

const codeHead = (lang) =>
  `<figure class="code"><figcaption class="code-head"><span class="lang">${esc(lang)}</span><button class="copy-btn" type="button" title="คัดลอกโค้ดไปรันใน CMD">${ICONS}<span>คัดลอก</span></button></figcaption>`;

const resultHead = () =>
  `<figure class="result"><figcaption class="result-head"><span class="lang">ผลลัพธ์</span></figcaption><span class="cover" aria-hidden="true">แตะเพื่อเฉลย</span>`;

const langOf = (codeNode) => (codeNode.lang ?? "").trim().toLowerCase();
const isResultCode = (node) => node.type === "code" && RESULT_LANGS.has(langOf(node));

const isMarker = (node) => {
  if (node.type !== "paragraph") return false;
  let text = "";
  const walk = (n) => {
    if (n.type === "text") text += n.value;
    if (Array.isArray(n.children)) n.children.forEach(walk);
  };
  walk(node);
  const t = text.trim();
  if (t.length === 0 || t.length > 60) return false;
  return (
    t === "ผลลัพธ์" ||
    (t.includes("ผลลัพธ์") && (t.endsWith(":") || /^(ตัวอย่าง)?ผลลัพธ์/.test(t)))
  );
};

export default function remarkCodePairs() {
  return (tree) => {
    const src = tree.children ?? [];
    const out = [];
    let i = 0;

    while (i < src.length) {
      const node = src[i];

      // ป้ายผลลัพธ์ที่ตามด้วย txt โดยตรง (ไม่ว่าจะมี code นำหน้าไหม)
      // ตัดป้ายทิ้ง — ถ้าไม่มีโค้ดคู่ txt จะกลายเป็น figure.result เดี่ยวที่ branch ถัดไป
      if (isMarker(node) && i + 1 < src.length && isResultCode(src[i + 1])) {
        i += 1;
        continue;
      }

      if (node.type === "code" && !isResultCode(node)) {
        const lang = langOf(node) || "text";
        let j = i + 1;
        let marker = null;
        if (j < src.length && isMarker(src[j])) {
          marker = src[j];
          j += 1;
        }
        if (j < src.length && isResultCode(src[j])) {
          // คู่โค้ด + ผลลัพธ์ — ป้ายตัดทิ้งเพราะ figure มีป้ายของตัวเอง
          out.push(html('<div class="pair tight">'));
          out.push(html(codeHead(lang)));
          out.push(node);
          out.push(html("</figure>"));
          out.push(html(resultHead()));
          out.push(src[j]);
          out.push(html("</figure></div>"));
          i = j + 1;
          continue;
        }
        // โค้ดเดี่ยว — ป้ายที่ไม่ได้คู่คงไว้เป็นย่อหน้า
        out.push(html(codeHead(lang)));
        out.push(node);
        out.push(html("</figure>"));
        if (marker) out.push(marker);
        i = j;
        continue;
      }

      if (isResultCode(node)) {
        // ผลลัพธ์ไม่มีโค้ดคู่ → figure เดี่ยว
        out.push(html(resultHead()));
        out.push(node);
        out.push(html("</figure>"));
        i += 1;
        continue;
      }

      out.push(node);
      i += 1;
    }

    tree.children = out;
  };
}
