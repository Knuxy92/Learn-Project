# โปรเจกต์เรียน JavaScript / TypeScript

โปรเจกต์นี้เป็นพื้นที่เรียน JavaScript -> TypeScript -> Backend API แบบเรียง prerequisite ให้ชัด

## เส้นทางการเรียนปัจจุบัน

เริ่มตาม curriculum:

1. พื้นฐาน JavaScript
2. JavaScript ระดับกลาง
3. TypeScript
4. การสร้าง API

ไฟล์หลัก:

- `CURRICULUM_TRACK.md` - เส้นทางและสถานะบททั้งหมด
- `CHAPTER_STATUS.md` - เช็กลิสต์และสรุปรายบท
- `curriculum/ch01-setup-first-code.md` - บทเรียนบทแรก
- `exercises/ch01-first-code.js` - โจทย์บทแรก

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

- Node.js 22 ขึ้นไป (โปรเจกต์ใช้ `node:sqlite` ซึ่งมากับ Node เอง)
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
node --test -r ts-node/register exercises/test-bridge-01-assert-basics.test.ts
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

โฟลเดอร์ `*-storage/` ใช้เก็บไฟล์ SQLite ที่สร้างตอนรัน ไม่ได้ track ใน git
