# โปรเจกต์เรียน JavaScript สู่ฝั่งเซิร์ฟเวอร์ (backend)

โปรเจกต์นี้เป็นพื้นที่เรียน JavaScript ตั้งแต่พื้นฐานไปจนทำ API ฝั่งเซิร์ฟเวอร์ด้วย Express ได้จริง

## เส้นทางการเรียน

1. JavaScript พื้นฐาน (Ch1-Ch12)
2. JavaScript ขั้นกลางสำหรับงานฝั่งเซิร์ฟเวอร์ (Ch13-Ch16)
3. ฝั่งเซิร์ฟเวอร์ด้วย Express (Ch17-Ch22)
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
- pnpm สำหรับติดตั้งแพ็กเกจที่ต้องใช้

```bash
pnpm install
```

## คำสั่งที่ใช้บ่อย

รันการทดสอบ (test) ทั้งหมด:

```bash
pnpm test
```

รันการทดสอบเฉพาะไฟล์:

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
และต้องใส่นามสกุล `.js` ในเส้นทางไฟล์ (path) ทุกครั้งที่นำเข้า (import) ไฟล์เอง

โฟลเดอร์ `storage/` ใช้เก็บไฟล์ JSON ที่สร้างตอนรัน และไม่ถูกติดตามใน git
