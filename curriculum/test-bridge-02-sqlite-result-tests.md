# ช่วงเชื่อมทดสอบ 02: ทดสอบผลลัพธ์จาก SQLite

## ทำไมต้องมีช่วงเชื่อมนี้

ก่อน test storage function หรือ API ต้องแม่นก่อนว่า result ของ SQLite query ควรถูก assert ยังไง

บทนี้จะ test ตรงกับสิ่งที่เรียนมาแล้ว:

- `.all()`
- `.get()`
- `lastInsertRowid`
- `changes`

ยังไม่เปิด server และยังไม่ไปแตะ route

## เป้าหมาย

ฝึก 4 อย่าง:

1. test `.all()`
2. test `.get()`
3. test `lastInsertRowid`
4. test `changes`

## 1. Test `.all()`

`.all()` ใช้อ่านหลาย rows และคืน array

```ts
const rows = db
  .prepare("SELECT id, title, done FROM tasks ORDER BY id DESC")
  .all();
```

สิ่งที่ควร assert:

- เป็น array จริงไหม
- จำนวน rows ถูกไหม
- ลำดับตรงกับ `ORDER BY` ไหม

สรุป: `.all()` มัก test ด้วย `assert.ok(...)`, `assert.equal(...)`, `assert.deepEqual(...)`

## 2. Test `.get()`

`.get()` ใช้อ่าน row เดียว

```ts
const row = db
  .prepare("SELECT id, title, done FROM tasks WHERE id = ?")
  .get(id);
```

สิ่งที่ควร assert:

- ถ้าเจอ row ค่าควรถูก
- ถ้าไม่เจอควรได้ `undefined`

สรุป: `.get()` ต้อง test ทั้งกรณีเจอ และกรณีไม่เจอ

## 3. Test `lastInsertRowid`

หลัง `INSERT` ด้วย `.run()` จะได้ result object

```ts
const result = db
  .prepare("INSERT INTO tasks (title, done) VALUES (?, ?)")
  .run("Study SQL", 0);
```

สิ่งที่ควร assert:

- `lastInsertRowid` เป็นเลข
- เอา id นั้นไป query ต่อแล้วเจอ row จริง

สรุป: อย่าดูแค่ id ต้องเช็กต่อด้วยว่า row ถูกสร้างจริง

## 4. Test `changes`

หลัง `DELETE` หรือ `UPDATE` ต้องดูว่า query กระทบกี่ rows

```ts
const result = db
  .prepare("DELETE FROM tasks WHERE id = ?")
  .run(id);
```

สิ่งที่ควร assert:

- ลบสำเร็จควรได้ `changes === 1`
- ลบ id เดิมซ้ำอีกครั้งควรได้ `changes === 0`

สรุป: `changes` ช่วยแยก "แก้/ลบสำเร็จ" ออกจาก "รันได้แต่ไม่เจอ row"

## ตัวอย่าง

```ts
import { test } from "node:test";
import assert from "node:assert/strict";
import path from "node:path";
import { DatabaseSync } from "node:sqlite";

const dbPath = path.join(__dirname, "../test-bridge-02-storage/example.db");
const db = new DatabaseSync(dbPath);

db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL DEFAULT 0
  )
`);

test("insert should create a row and return lastInsertRowid", () => {
  db.prepare("DELETE FROM tasks").run();

  const result = db
    .prepare("INSERT INTO tasks (title, done) VALUES (?, ?)")
    .run("Study SQL", 0);

  const row = db
    .prepare("SELECT id, title, done FROM tasks WHERE id = ?")
    .get(Number(result.lastInsertRowid));

  assert.ok(typeof result.lastInsertRowid === "number" || typeof result.lastInsertRowid === "bigint");
  assert.deepEqual(row, {
    id: Number(result.lastInsertRowid),
    title: "Study SQL",
    done: 0,
  });
});
```

## งานที่ต้องทำ

แก้ไฟล์:

```txt
exercises/test-bridge-02-sqlite-result-tests.test.ts
```

ให้ทำตามนี้:

1. import:
   - `test` จาก `node:test`
   - `assert` จาก `node:assert/strict`
   - `path` จาก `node:path`
   - `DatabaseSync` จาก `node:sqlite`

2. สร้างไฟล์ database ที่:

```txt
exercises/test-bridge-02-storage/tasks.db
```

3. ใช้ `.exec()` สร้าง table `tasks`
   - `id INTEGER PRIMARY KEY AUTOINCREMENT`
   - `title TEXT NOT NULL`
   - `done INTEGER NOT NULL DEFAULT 0`

4. เขียน helper `resetTasksTable()`
   - ลบ rows เก่าออกก่อนแต่ละ test
   - reset ตัวนับ id ด้วย

5. เขียน test 4 ตัว:
   - `.all()` ควรคืน array 2 rows ตามลำดับ `ORDER BY id DESC`
   - `.get()` ควรคืน row เมื่อ id มีอยู่ และคืน `undefined` เมื่อไม่มี
   - `INSERT` ควรคืน `lastInsertRowid` และ query row นั้นเจอจริง
   - `DELETE` ควรคืน `changes === 1` รอบแรก และ `changes === 0` รอบที่สอง

6. ใช้ assert ให้ตรงสถานการณ์:
   - `assert.ok(...)` สำหรับเช็กชนิดหรือเงื่อนไข
   - `assert.equal(...)` สำหรับ number/undefined
   - `assert.deepEqual(...)` สำหรับ object/array

## วิธีรัน

ใช้คำสั่ง:

```bash
node --test -r ts-node/register exercises/test-bridge-02-sqlite-result-tests.test.ts
```

## ผลลัพธ์ที่คาดหวัง

เมื่อรัน test แล้วควรผ่าน 4 tests และอธิบายได้ว่า:

- `.all()` ใช้เช็กรายการยังไง
- `.get()` ต้องเช็กกรณีเจอ และกรณีไม่เจอ ยังไง
- `lastInsertRowid` ใช้ยืนยัน row ใหม่ยังไง
- `changes` ใช้ยืนยันการลบ/แก้ไขยังไง

เสร็จแล้วพิมพ์:

```txt
ตรวจ Test Bridge 02
```
