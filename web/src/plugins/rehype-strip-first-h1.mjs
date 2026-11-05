/* ตัด h1 แรกออกจากเนื้อหา — หน้าเว็บเรนเดอร์หัวบทเองจากข้อมูลที่ parse แยก
   (h1 ต้นฉบับคือ "บทที่ N: ชื่อบท") */
export default function rehypeStripFirstH1() {
  return (tree) => {
    const children = tree.children ?? [];
    for (let i = 0; i < children.length; i += 1) {
      const node = children[i];
      if (node.type === "element" && node.tagName === "h1") {
        children.splice(i, 1);
        return;
      }
      // เจอ element อื่นก่อน h1 แปลว่าไม่มี h1 นำ — จบ
      if (node.type === "element") return;
    }
  };
}
