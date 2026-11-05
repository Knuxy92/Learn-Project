// ล้าง content-layer cache ก่อน build — ใช้เมื่อแก้ plugins/render pipeline
// (cache อยู่ที่ .astro/ และ node_modules/.astro — md ไม่เปลี่ยน = render เก่าถูกใช้ซ้ำ)
import { rmSync } from "node:fs";

for (const dir of [".astro", "node_modules/.astro"]) {
  rmSync(dir, { recursive: true, force: true });
}
