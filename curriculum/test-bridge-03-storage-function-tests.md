# Test Bridge 03: Storage Function Tests

## Why This Bridge Exists

ก่อนจะไป test route หรือ HTTP status เราต้องแน่ใจก่อนว่า storage layer ทำงานถูกจริง

บทนี้จะยังไม่เปิด server และยังไม่แตะ `Express`

เราจะ test ตรงกับ function พวกนี้ใน `task-store.ts`:

- `readTasks()`
- `findTaskById()`
- `createTask()`
- `deleteTask()`

## Goal

ฝึก 4 อย่าง:

1. reset database ให้สะอาดก่อนแต่ละ test
2. test function ที่อ่านข้อมูล
3. test function ที่สร้างข้อมูล
4. test function ที่ลบข้อมูล

## 1. ทำไมต้อง test storage function ก่อน

ถ้า route พัง เราจะยังไม่รู้ทันทีว่าพังเพราะ:

- route logic
- validation
- storage function

ถ้าเราแยก test storage function ก่อน เราจะรู้ชัดขึ้นว่า data layer ใช้งานได้จริง

สรุป: บทนี้คือแยก test ชั้น data ออกมาก่อน เพื่อให้ตอนถึง API test จะ debug ง่ายขึ้น

## 2. วิธีคิดของบทนี้

รอบนี้ยังไม่ test SQL method ตรง ๆ แบบบทก่อน

เราจะ test "พฤติกรรมของ function" แทน เช่น:

- `readTasks()` ควรคืน `Task[]`
- `findTaskById(999)` ควรคืน `undefined`
- `createTask("Study SQL")` ควรคืน task ใหม่จริง
- `deleteTask(id)` ควรคืน `true` หรือ `false` ตามกรณี

สรุป: เราเริ่มขยับจาก test query result ไปเป็น test function behavior

## 3. สิ่งที่ต้องเตรียมก่อน test

แม้จะ test function แต่เรายังต้อง reset database ก่อนแต่ละ test

เพราะถ้าข้อมูลเก่าค้างอยู่:

- จำนวน rows จะเพี้ยน
- id จะไหลต่อ
- test จะเดายากว่า fail เพราะ logic หรือ fail เพราะข้อมูลเก่า

รอบนี้ให้มี helper แบบนี้:

```ts
const resetTasksTable = (): void => {
  db.prepare("DELETE FROM tasks").run();
  db.prepare("DELETE FROM sqlite_sequence WHERE name = ?").run("tasks");
};
```

สรุป: test ที่ดีต้องควบคุมสภาพเริ่มต้นให้ได้

## 4. พฤติกรรมที่ควร test

### `readTasks()`

ถ้ามี 2 rows ใน database:

- ควรคืน array
- ควรมีความยาวถูก
- ควร map `done: 0/1` เป็น `false/true`

### `findTaskById()`

- ถ้ามี id นั้น ควรคืน task
- ถ้าไม่มี id นั้น ควรคืน `undefined`

### `createTask()`

- ควรสร้าง row ใหม่จริง
- ควรคืน task ที่มี `id`, `title`, `done`
- `done` เริ่มต้นควรเป็น `false`

### `deleteTask()`

- ลบ id ที่มีอยู่ ควรได้ `true`
- ลบ id เดิมซ้ำ ควรได้ `false`

สรุป: เราไม่ได้ test ทุก function พร้อมกัน แต่ test ทีละพฤติกรรมให้ชัด

## Example

```ts
import { test } from "node:test";
import assert from "node:assert/strict";
import path from "node:path";
import { DatabaseSync } from "node:sqlite";
import { createTask } from "../exercises/ch24-task-api-sqlite/data/task-store";

const dbPath = path.join(__dirname, "../exercises/ch24-storage/tasks.db");
const db = new DatabaseSync(dbPath);

db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL
  )
`);

const resetTasksTable = (): void => {
  db.prepare("DELETE FROM tasks").run();
  db.prepare("DELETE FROM sqlite_sequence WHERE name = ?").run("tasks");
};

test("createTask should return a new task", async () => {
  resetTasksTable();

  const created = await createTask("Study SQL");

  assert.equal(created.title, "Study SQL");
  assert.equal(created.done, false);
  assert.equal(created.id, 1);
});
```

## งานที่ต้องทำ

แก้ไฟล์:

```txt
exercises/test-bridge-03-storage-function-tests.test.ts
```

ให้ทำตามนี้:

1. import:
   - `test` จาก `node:test`
   - `assert` จาก `node:assert/strict`
   - `path` จาก `node:path`
   - `DatabaseSync` จาก `node:sqlite`
   - function จาก `exercises/ch24-task-api-sqlite/data/task-store.ts`

2. สร้าง database connection ไปที่:

```txt
exercises/ch24-storage/tasks.db
```

3. ใช้ `.exec()` สร้าง table `tasks` ถ้ายังไม่มี

4. เขียน helper `resetTasksTable()`
   - ลบ rows เก่า
   - reset sequence

5. เขียน test 4 ตัว:
   - `readTasks()` ควรคืน array ของ task และ map `done` เป็น boolean
   - `findTaskById()` ควรคืน task เมื่อเจอ และคืน `undefined` เมื่อไม่เจอ
   - `createTask()` ควรสร้าง task ใหม่และคืนค่าถูก
   - `deleteTask()` ควรคืน `true` รอบแรก และ `false` รอบที่สอง

6. ใช้ assert ให้ตรงชนิดข้อมูล:
   - `assert.equal(...)` สำหรับ primitive
   - `assert.deepEqual(...)` สำหรับ array/object
   - `assert.ok(...)` ถ้าต้องเช็กเงื่อนไขหรือชนิด

## Run

ใช้คำสั่ง:

```bash
cmd /c node --test -r ts-node/register exercises/test-bridge-03-storage-function-tests.test.ts
```

## Expected Outcome

เมื่อรันแล้วควรผ่าน 4 tests และอธิบายได้ว่า:

- storage function test ต่างจาก SQL result test ยังไง
- ทำไมต้อง reset database ก่อนแต่ละ test
- ทำไม `done` ใน app เป็น boolean แม้ใน SQLite จะเก็บเป็นเลข
- ทำไมควร test not found แยกจาก found

เสร็จแล้วพิมพ์:

```txt
ตรวจ Test Bridge 03
```
