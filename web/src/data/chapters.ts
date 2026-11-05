/* Manifest บทเรียน — กลุ่มเป็นข้อเสนอตาม Design.md ข้อ 2
   ลำดับและชื่อบทมาจากไฟล์จริงใน curriculum/ */

export interface ChapterGroup {
  name: string;
  from: number;
  to: number;
}

export const GROUPS: ChapterGroup[] = [
  { name: "พื้นฐาน Python", from: 1, to: 5 },
  { name: "โครงสร้างข้อมูลและไฟล์", from: 6, to: 8 },
  { name: "NumPy", from: 9, to: 11 },
  { name: "pandas", from: 12, to: 20 },
  { name: "โปรเจกต์", from: 21, to: 21 },
];

export const groupOf = (no: number): ChapterGroup | undefined =>
  GROUPS.find((g) => no >= g.from && no <= g.to);

export const chNo = (id: string): number => {
  const m = id.match(/ch(\d+)/);
  return m ? Number(m[1]) : 0;
};

export const shortId = (id: string): string => id.match(/^ch\d+/)?.[0] ?? id;

/* นับชุดโค้ดจากไฟล์ต้นฉบับ — จำนวนรั้ว ``` หรือ ~~~ หารสอง */
export const countFences = (body: string): number =>
  (body.match(/^[ \t]{0,3}(?:```|~~~)/gm)?.length ?? 0) / 2;

const TITLE_RE = /^#\s*บทที่\s*(\d+)\s*[:：]\s*(.+)$/m;

export const parseTitle = (body: string): { no: number; title: string } => {
  const m = body.match(TITLE_RE);
  if (!m) return { no: 0, title: "" };
  return { no: Number(m[1]), title: m[2].trim() };
};

export const pad2 = (n: number): string => String(n).padStart(2, "0");
