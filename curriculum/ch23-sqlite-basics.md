# Chapter 23: SQLite Basics

## Recap

ตอนนี้นายมี:

- API ที่แยกโครงสร้างได้
- persistence ผ่าน JSON file
- automated tests
- ความเข้าใจ Promise/await ที่พอใช้กับ async flow ได้แล้ว

ก้าวถัดไปคือเข้า database จริง

แต่ยังไม่ควรกระโดดเข้า ORM หรือ logic API ทันที

บทนี้จะโฟกัสแค่พื้นฐานของ SQLite ก่อน:

- เปิด database
- สร้าง table
- insert row
- select row

## 1. Why SQLite First

SQLite เหมาะกับช่วงนี้เพราะ:

- ไม่ต้องติดตั้ง database server แยก
- ใช้ไฟล์เดียว
- เห็น schema และ query ชัด
- เหมาะกับการเรียนพื้นฐาน SQL

## 2. `node:sqlite`

Node ในเครื่องนี้มี `node:sqlite` ใช้ได้

ข้อดีคือ:

- ไม่ต้องลง package เพิ่ม
- ใช้กับบทเรียนได้ทันที

ข้อสังเกต:

- ตอนนี้ยังมี experimental warning
- แต่พอสำหรับการเรียนพื้นฐานและทำแบบฝึกหัด

## 3. Database File

SQLite เก็บข้อมูลลงไฟล์ เช่น:

```txt
storage/tasks.db
```

ถ้าไฟล์ไม่มี มันจะสร้างให้

## 4. Table

table คือโครงสร้างเก็บ row หลายตัว

เช่น table `tasks`

```sql
CREATE TABLE IF NOT EXISTS tasks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  done INTEGER NOT NULL
);
```

ความหมาย:

- `id` เป็นเลขหลัก
- `AUTOINCREMENT` ให้ database ช่วยสร้าง id
- `title` เป็นข้อความ
- `done` เก็บ 0/1 แทน boolean

## 5. Insert

ตัวอย่าง insert:

```sql
INSERT INTO tasks (title, done) VALUES (?, ?);
```

`?` คือ placeholder สำหรับค่าที่จะส่งเข้าไป

## 6. Select

ตัวอย่าง select:

```sql
SELECT id, title, done FROM tasks;
```

เรามักต้องแปลง `done`

จาก:

- `0`
- `1`

ให้เป็น:

- `false`
- `true`

## 7. Row Mapping

database row ไม่จำเป็นต้องตรงกับ type ของแอป 100%

เช่นใน SQLite:

- `done` อาจเป็น `0 | 1`

แต่ในแอปเราอยากได้:

- `done: boolean`

ดังนั้นต้องมี mapping

```ts
const mappedTask = {
  id: row.id,
  title: row.title,
  done: row.done === 1,
};
```

## 8. Example

```ts
import path from "node:path";
import { DatabaseSync } from "node:sqlite";

const dbPath = path.join(__dirname, "storage/tasks.db");
const db = new DatabaseSync(dbPath);

db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL
  )
`);

db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run(
  "Learn SQLite",
  0,
);

const rows = db.prepare("SELECT id, title, done FROM tasks").all();
console.log(rows);
```

## Guided Exercise

ให้แก้ไฟล์:

```txt
exercises/ch23-sqlite-basics.ts
```

ให้ทำตามนี้:

1. import:
   - `path` จาก `node:path`
   - `DatabaseSync` จาก `node:sqlite`

2. สร้าง `type DbTaskRow`
   - `id: number`
   - `title: string`
   - `done: number`

3. สร้าง `type Task`
   - `id: number`
   - `title: string`
   - `done: boolean`

4. สร้าง database file ที่:

```txt
exercises/ch23-storage/tasks.db
```

5. สร้าง table `tasks` ถ้ายังไม่มี

6. insert task อย่างน้อย 2 ตัว

7. query tasks ทั้งหมดออกมา

8. map rows จาก `DbTaskRow[]` เป็น `Task[]`

9. พิมพ์:
   - raw rows
   - mapped tasks

## Important Note

บทนี้ยังไม่ทำ API

เรากำลังเรียน:

- database file
- table
- row
- query
- row mapping

หลังจากบทนี้ค่อยย้าย task API ไปใช้ SQLite ใน `Ch24`

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch23
```
