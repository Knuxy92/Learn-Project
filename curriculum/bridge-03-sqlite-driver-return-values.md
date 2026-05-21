# Bridge 03: SQLite Driver Return Values

## Why This Bridge Exists

หลัง `Bridge 02` ตอนนี้รู้แล้วว่า query แบบไหนใช้ "อ่าน", "สร้าง", "แก้", "ลบ"

แต่ยังมีอีกชั้นที่สำคัญมาก:

- query ถูกแล้ว แต่ควรเรียก `.all()`, `.get()`, `.run()`, หรือ `.exec()`
- ถ้า `SELECT` ไม่เจอ row จะได้อะไรกลับมา
- ถ้า `INSERT` สำเร็จ เราจะรู้ `id` ใหม่จากไหน
- ถ้า `DELETE` หรือ `UPDATE` ไม่กระทบ row เลย เราจะรู้ได้ยังไง

ถ้าไม่แยกชั้นนี้ให้ชัด ผู้เรียนจะเริ่มใช้ method ตามความจำแทนความเข้าใจ

## Entry Point

เราเข้า bridge นี้หลังจาก:

- จบ `Bridge 02 - SQL Query Basics`
- อ่าน SQL query ออกแล้ว
- พร้อมผูก query แต่ละแบบเข้ากับ SQLite driver method ที่ถูกต้อง

## Exit Point

ออกจาก bridge นี้ได้เมื่อทำได้ครบ:

1. อธิบายได้ว่า `.exec()` ใช้กับ setup SQL
2. อธิบายได้ว่า `.all()` ใช้อ่านหลาย rows และคืน `[]` ได้
3. อธิบายได้ว่า `.get()` ใช้อ่าน row เดียวและคืน `undefined` ได้
4. อธิบายได้ว่า `.run()` ใช้กับ `INSERT`, `UPDATE`, `DELETE`
5. ใช้ `lastInsertRowid` และ `changes` ได้ถูกสถานการณ์

## Return to Main Line

หลังจบ bridge นี้ เราจะไปต่อที่:

- `SQL Error vs Not Found`

เหตุผลคือพอแยก driver return values ได้แล้ว ค่อยต่อด้วยการแปลความหมายของผลลัพธ์ว่าอันไหนคือ "ไม่เจอข้อมูล" และอันไหนคือ "query/database พัง"

## Main Goal

bridge นี้เน้น 5 เรื่อง:

1. `.exec()`
2. `.all()`
3. `.get()`
4. `.run()`
5. `lastInsertRowid` และ `changes`

## 1. `.exec()`

ใช้กับ SQL setup ที่ไม่ได้ต้องการ row กลับมา

ตัวอย่าง:

```ts
db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL DEFAULT 0
  )
`);
```

ใช้ตอน:

- สร้าง table
- setup database ตอนเริ่ม app
- รัน SQL ที่ไม่ได้ต้องการอ่าน row กลับมา

ไม่ควรใช้ `.exec()` เพื่ออ่านข้อมูล task ออกมา

## 2. `.all()`

ใช้เมื่อคาดว่าจะได้หลาย rows

ตัวอย่าง:

```ts
const rows = db
  .prepare("SELECT id, title, done FROM tasks ORDER BY id DESC")
  .all();
```

จุดสำคัญ:

- คืน array
- ถ้า table ว่าง จะได้ `[]`
- ไม่ใช่ error ถ้าไม่มีข้อมูล

## 3. `.get()`

ใช้เมื่อคาดว่าจะได้ row เดียว

ตัวอย่าง:

```ts
const row = db
  .prepare("SELECT id, title, done FROM tasks WHERE id = ?")
  .get(id);
```

จุดสำคัญ:

- คืน row เดียว
- ถ้าไม่เจอ row จะได้ `undefined`
- ไม่ใช่ error ถ้า id นั้นไม่มีอยู่

## 4. `.run()`

ใช้กับ query ที่เปลี่ยนข้อมูล

ตัวอย่าง:

```ts
const result = db
  .prepare("INSERT INTO tasks (title, done) VALUES (?, ?)")
  .run(title, 0);
```

ใช้กับ:

- `INSERT`
- `UPDATE`
- `DELETE`

`.run()` ไม่ได้คืน row กลับมา แต่คืน result object

## 5. `lastInsertRowid`

ใช้หลัง `INSERT` เพื่อดูว่า row ที่เพิ่งสร้างได้ id อะไร

ตัวอย่าง:

```ts
const result = db
  .prepare("INSERT INTO tasks (title, done) VALUES (?, ?)")
  .run("Study SQLite", 0);

const newId = Number(result.lastInsertRowid);
```

ใช้ตอน:

- create task
- ต้องการ return task ที่เพิ่งสร้าง
- ไม่ควรหา id เองจาก array หรือเดาเลขเอง

## 6. `changes`

ใช้หลัง `UPDATE` หรือ `DELETE` เพื่อดูว่ามีกี่ rows ที่ได้รับผล

ตัวอย่าง:

```ts
const result = db
  .prepare("DELETE FROM tasks WHERE id = ?")
  .run(id);

console.log(result.changes);
```

กรณีที่พบบ่อย:

- `changes > 0` แปลว่ามี row ถูกกระทบ
- `changes === 0` แปลว่า query รันได้ แต่ไม่เจอ row ที่ตรงเงื่อนไข

## Example

```ts
import path from "node:path";
import { DatabaseSync } from "node:sqlite";

const dbPath = path.join(__dirname, "../bridge-03-storage/example.db");
const db = new DatabaseSync(dbPath);

db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL DEFAULT 0
  )
`);

db.prepare("DELETE FROM tasks").run();

const insertResult = db
  .prepare("INSERT INTO tasks (title, done) VALUES (?, ?)")
  .run("Study Driver Methods", 0);

const newId = Number(insertResult.lastInsertRowid);

const oneTask = db
  .prepare("SELECT id, title, done FROM tasks WHERE id = ?")
  .get(newId);

const allTasks = db
  .prepare("SELECT id, title, done FROM tasks ORDER BY id DESC")
  .all();

const deleteResult = db
  .prepare("DELETE FROM tasks WHERE id = ?")
  .run(newId);

console.log("newId:", newId);
console.log("oneTask:", oneTask);
console.log("allTasks:", allTasks);
console.log("delete changes:", deleteResult.changes);
```

## งานที่ต้องทำ

แก้ไฟล์:

```txt
exercises/bridge-03-driver-return-values.ts
```

ให้ทำตามนี้:

1. import:
   - `path` จาก `node:path`
   - `DatabaseSync` จาก `node:sqlite`

2. สร้าง database file ที่:

```txt
exercises/bridge-03-storage/tasks.db
```

3. ใช้ `.exec()` สร้าง table `tasks`
   - `id INTEGER PRIMARY KEY AUTOINCREMENT`
   - `title TEXT NOT NULL`
   - `done INTEGER NOT NULL DEFAULT 0`

4. clear rows เก่าออกก่อนเริ่ม

5. ใช้ `.run()` insert task 2 ตัว

6. เก็บ `lastInsertRowid` ของ task ตัวที่ 2 ไว้ในตัวแปร `lastId`

7. ใช้ `.all()` อ่าน tasks ทั้งหมดแบบ `ORDER BY id DESC`

8. ใช้ `.get()` อ่าน task เดียวจาก `lastId`

9. ใช้ `.get()` อีกครั้งกับ id ที่ไม่มีจริง เช่น `9999`
   - เก็บผลไว้ในตัวแปร `missingTask`

10. ใช้ `.run()` delete task จาก `lastId`
    - เก็บ result ไว้ในตัวแปร `deleteResult`

11. ใช้ `.run()` delete id เดิมซ้ำอีกครั้ง
    - เก็บ result ไว้ในตัวแปร `deleteMissingResult`

12. พิมพ์ผลออกมา 6 อย่าง
    - `lastId`
    - all tasks
    - one task
    - missing task
    - `deleteResult.changes`
    - `deleteMissingResult.changes`

13. ตอบใน comment สั้นๆ ในไฟล์
    - `.all()` คืนอะไรเมื่อไม่มี rows
    - `.get()` คืนอะไรเมื่อไม่เจอ row
    - `lastInsertRowid` ใช้ทำอะไร
    - `changes === 0` แปลว่าอะไร

## Expected Outcome

หลังทำเสร็จ นายควรอธิบายได้ว่า:

- setup SQL ควรใช้ `.exec()`
- list query ควรใช้ `.all()`
- single-row query ควรใช้ `.get()`
- write query ควรใช้ `.run()`
- `lastInsertRowid` และ `changes` เอาไว้ตัดสินใจอะไร

เสร็จแล้วพิมพ์:

```txt
ตรวจ Bridge 03
```
