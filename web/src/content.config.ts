import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

// บทเรียนอ่านจาก curriculum/ โดยตรง — Markdown คือต้นฉบับเดียว (Design.md ข้อ 1)
// ไฟล์ไม่มี frontmatter เลย schema เปิดให้ว่างได้
const chapters = defineCollection({
  loader: glob({ pattern: "ch*.md", base: "../curriculum" }),
  schema: z.object({}).passthrough(),
});

export const collections = { chapters };
