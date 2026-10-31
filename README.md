# โปรเจกต์เรียน JavaScript สู่ Backend

โปรเจกต์นี้เป็นพื้นที่เรียน JavaScript ตั้งแต่พื้นฐานไปจนทำ Backend API ด้วย Express ได้จริง

## เส้นทางการเรียน

1. JavaScript พื้นฐาน (Ch1-Ch12)
2. JavaScript ขั้นกลางสำหรับงาน backend (Ch13-Ch16)
3. Backend ด้วย Express (Ch17-Ch22)
4. งานท้าย: Task API ที่ใช้งานได้จริง (Ch23)

ไฟล์หลัก:

- `CURRICULUM_TRACK.md` - เส้นทางและสถานะบททั้งหมด
- `CHAPTER_STATUS.md` - เช็กลิสต์และสรุปรายบท
- `NEXT_BACKEND_PLAN.md` - แผนหลังจบหลักสูตรนี้

## เริ่มตรงนี้

อ่านบทแรก:

```bash
cat curriculum/ch01-setup-first-code.md
```

รันตัวอย่าง:

```bash
node curriculum/ch01/hello-world.js
```

เปิดโจทย์:

```bash
cat exercises/ch01-first-code.js
```

รันโจทย์:

```bash
node exercises/ch01-first-code.js
```

เสร็จแล้วพิมพ์:

```txt
ตรวจ Ch1
```

## สิ่งที่ต้องมี

- Node.js 20 ขึ้นไป
- pnpm สำหรับติดตั้ง dependency

```bash
pnpm install
```

## คำสั่งที่ใช้บ่อย

รัน test ทั้งหมด:

```bash
pnpm test
```

รัน test เฉพาะไฟล์:

```bash
node --test exercises/test-bridge-01-assert-basics.test.js
```

ตรวจ lint:

```bash
pnpm lint
```

## โครงสร้างโฟลเดอร์

```txt
curriculum/   บทเรียนและตัวอย่างโค้ด
exercises/    โจทย์และ mini project
```

โปรเจกต์นี้เป็น ESM ทั้งหมด (`"type": "module"`) จึงใช้ `import` / `export`
และต้องใส่นามสกุล `.js` ใน path ทุกครั้งที่ import ไฟล์เอง

โฟลเดอร์ `storage/` ใช้เก็บไฟล์ JSON ที่สร้างตอนรัน ไม่ได้ track ใน git
