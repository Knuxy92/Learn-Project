/* จัดโครงหน้าบท (Design.md ส่วนประกอบ)
   - แบ่งเนื้อหาเป็น <section id> ที่ h2 แต่ละตัว + ใส่ data-reveal
   - h2 "ทบทวน" / "สรุป" → section.card
   - h2 "โจทย์ที่ต้องทำ" → section.card + แปลง list เป็นช่องติ๊ก ul.tasks
   - <table> → ห่อ .table-scroll สำหรับมือถือ
   ทำงานหลัง Astro ใส่ id ให้ heading แล้ว */

const CARD_TITLES = new Set(["ทบทวน", "สรุป"]);
const TASKS_TITLE = "โจทย์ที่ต้องทำ";

const headingText = (node) => {
  let text = "";
  const walk = (n) => {
    if (n.type === "text") text += n.value;
    if (Array.isArray(n.children)) n.children.forEach(walk);
  };
  walk(node);
  return text.trim();
};

const wrapTasks = (list) => {
  if (list.type !== "element" || (list.tagName !== "ul" && list.tagName !== "ol")) return list;
  const items = list.children.map((li) => {
    if (!Array.isArray(li.children) || li.children.length === 0) return li;
    return {
      type: "element",
      tagName: "li",
      properties: {},
      children: [
        {
          type: "element",
          tagName: "label",
          properties: {},
          children: [
            {
              type: "element",
              tagName: "input",
              properties: { type: "checkbox", "data-task": "" },
              children: [],
            },
            ...li.children,
          ],
        },
      ],
    };
  });
  return {
    type: "element",
    tagName: "ul",
    properties: { className: ["tasks"] },
    children: items,
  };
};

export default function rehypeSections() {
  return (tree) => {
    const src = tree.children ?? [];
    const out = [];
    let current = null; // { el, title, isCard, isTasks }

    const flush = () => {
      if (!current) return;
      out.push(current.el);
      current = null;
    };

    for (const node of src) {
      const isH2 = node.type === "element" && node.tagName === "h2";

      if (isH2) {
        flush();
        const title = headingText(node);
        const id = node.properties?.id ?? null;
        const isCard = CARD_TITLES.has(title);
        const isTasks = title === TASKS_TITLE;
        const classes = ["doc-section"];
        if (isCard || isTasks) classes.push("card");
        current = {
          title,
          isTasks,
          el: {
            type: "element",
            tagName: "section",
            properties: {
              className: classes,
              ...(id ? { id } : {}),
              "data-reveal": "",
            },
            children: [node],
          },
        };
        continue;
      }

      if (current) {
        if (current.isTasks && node.type === "element" && (node.tagName === "ul" || node.tagName === "ol")) {
          // ย่อหน้าอธิบายก่อน list เก็บตามปกติ — list แรกของ section โจทย์เท่านั้นที่กลายเป็นช่องติ๊ก
          if (!current.el.children.some((c) => c.properties?.className?.includes("tasks"))) {
            current.el.children.push(wrapTasks(node));
            continue;
          }
        }
        if (node.type === "element" && node.tagName === "table") {
          current.el.children.push({
            type: "element",
            tagName: "div",
            properties: { className: ["table-scroll"] },
            children: [node],
          });
          continue;
        }
        current.el.children.push(node);
        continue;
      }

      // เนื้อหาก่อน h2 แรก (เช่น ย่อหน้านำ) ปล่อยออกตรง ๆ
      out.push(node);
    }
    flush();

    tree.children = out;
  };
}
