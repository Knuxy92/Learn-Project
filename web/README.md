# เว็บสมุดบทเรียน

เว็บอ่านบทเรียนที่เรนเดอร์ Markdown จากโฟลเดอร์ `curriculum/` โดยตรง ตามระบบดีไซน์ใน Design.md ทุกอย่างเป็น static ทั้งหมด ไม่มีเซิร์ฟเวอร์ ไม่มีฐานข้อมูล

## เครื่องมือ

- Astro 5 · pnpm (ล็อกเวอร์ชันใน package.json)
- Shiki ธีมสีเดียวตาม Design.md ทุกสีอ้าง token ผ่าน CSS vars
- ฟอนต์ self-host ผ่าน @fontsource ไม่พึ่ง CDN
- ไอคอน Lucide แบบ inline SVG จาก lucide-static

## คำสั่งหลัก

```
pnpm install        ติดตั้งครั้งแรก
pnpm dev            รัน dev server
pnpm build          build เป็น static ที่ dist/
pnpm run build:fresh  build แบบล้าง cache (ใช้เมื่อแก้ plugins)
pnpm preview        เสิร์ฟ dist ไว้ดูก่อนส่งขึ้นจริง
```

จำไว้ว่า pipeline ของ Markdown มี cache อยู่ที่ `.astro/` กับ `node_modules/.astro/` ถ้าแก้ไฟล์ใน `src/plugins/` แล้วผลลัพธ์ไม่เปลี่ยน ให้ใช้ `build:fresh` เสมอ

## Pipeline แปลง Markdown

ต้นฉบับคือไฟล์ `curriculum/chNN-*.md` ทั้ง 21 บท เว็บไม่แก้ไฟล์เหล่านี้เลย สิ่งที่ pipeline ทำเองตอน build มีสี่อย่าง

1. จับคู่บล็อกโค้ดกับบล็อกผลลัพธ์ จากย่อหน้าสั้นที่มีคำ ผลลัพธ์ ปิดท้าย (`src/plugins/remark-code-pairs.mjs`)
2. แบ่งเนื้อหาเป็น section ตาม h2 ทบทวนกับสรุปกลายเป็นการ์ด โจทย์ที่ต้องทำกลายเป็นช่องติ๊ก ตารางถูกห่อให้เลื่อนแนวนอนได้บนมือถือ (`src/plugins/rehype-sections.mjs`)
3. ตัด h1 แถวแรกทิ้ง เพราะหน้าเว็บเรนเดอร์หัวบทเอง (`src/plugins/rehype-strip-first-h1.mjs`)
4. ลำดับบทกับกลุ่มอยู่ที่ `src/data/chapters.ts` แก้กลุ่มที่ไฟล์เดียว

## เก็บความคืบหน้าผู้เรียน

ทั้งหมดอยู่ใน localStorage ของเครื่องผู้เรียน ไม่มีระบบบัญชี

- `lp:teaching` สถานะโหมดสอน ค่าเริ่มต้นคือเปิด
- `lp:last` บทที่เปิดล่าสุด ใช้โชว์ อ่านค้างไว้ที่ บนหน้าแรก
- `lp:done:chNN` ข้อโจทย์ที่ติ๊กแล้วของแต่ละบท

## Self-host ด้วย Docker

```
docker build -t learn-web .
docker run -p 8080:80 learn-web
```

เปิดที่ http://localhost:8080 ในไฟล์มี Caddyfile เสิร์ฟไฟล์ static พร้อม fallback ไปที่ index.html

## Vercel

ส่งโฟลเดอร์ `web/` ขึ้น repo แล้ว import ใน Vercel มันจับ Astro เอง ตั้ง Root Directory เป็น `web` จบ ไม่ต้องแก้ค่าอื่น

## เฟสถัดไปที่ยังไม่ทำ

- ค้นหาด้วย Pagefind ต้องทดสอบกับภาษาไทยก่อนเพราะไทยไม่เว้นวรรคระหว่างคำ
- รันโค้ดในเบราว์เซอร์ด้วย Pyodide ข้อมูลใน data/raw เล็กมาก ทำได้จริง แต่โจทย์ที่อ้าง exercises/ จะรันไม่ได้ทั้งหมด
