# Chapter 25: Query Layer and DB Refactor

## Recap

ตอนนี้เราได้ 2 อย่างแล้ว:

- `Ch24` ใช้ SQLite กับ task API ได้จริง
- route ยังเรียก storage functions ได้เหมือนเดิม

แต่ตอนนี้ data layer ยังรวมหลายหน้าที่ไว้ในไฟล์เดียว เช่น:

- connect database
- create table
- map row
- query CRUD

ในบทนี้เราจะเริ่มแยกหน้าที่ให้ชัดขึ้น

## 1. Goal Of This Chapter

เป้าหมายไม่ใช่เปลี่ยน behavior ของ API

เป้าหมายคือ:

- refactor ภายในให้สะอาดขึ้น
- โดยให้ route contract เดิมยังอยู่

พูดสั้น ๆ:

- ภายนอกเหมือนเดิม
- ภายในจัดระเบียบดีขึ้น

## 2. What We Want To Separate

ในบทนี้เราจะแยกเป็น 2 ส่วนหลัก:

- `data/db.ts`
  - เปิด database
  - สร้าง table ถ้ายังไม่มี
- `data/task-queries.ts`
  - query tasks
  - map row -> `Task`
  - export functions ให้ route ใช้

route layer ควรเหลือหน้าที่:

- รับ request
- เรียก query function
- ตอบ HTTP response

## 3. Why This Refactor Matters

ถ้า query logic, DB setup, และ route logic ปนกันมากเกินไป:

- อ่านยาก
- แก้ยาก
- test เฉพาะชั้นย่อยยาก
- duplicate code ง่าย

แต่ถ้าแยกดี:

- route โฟกัสที่ HTTP
- query file โฟกัสที่ SQL
- db file โฟกัสที่ connection/setup

## 4. Suggested File Structure

```txt
exercises/ch25-task-api-query-layer/
  app.ts
  server.ts
  routes/
    task-routes.ts
  middleware/
    validate-task.ts
  data/
    db.ts
    task-queries.ts
  types/
    task.ts
```

## 5. Example DB File

```ts
import { DatabaseSync } from "node:sqlite";
import path from "node:path";

const dbPath = path.join(__dirname, "../../ch25-storage/tasks.db");
const db = new DatabaseSync(dbPath);

db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL DEFAULT 0
  )
`);

export { db };
```

## 6. Example Query File

```ts
import { db } from "./db";
import { type DbTaskRow, type Task } from "../types/task";

const mapTaskRow = (row: DbTaskRow): Task => ({
  id: row.id,
  title: row.title,
  done: row.done === 1,
});

const getAllTasks = (): Task[] => {
  const rows = db.prepare(`
    SELECT id, title, done
    FROM tasks
    ORDER BY id DESC
  `).all() as DbTaskRow[];

  return rows.map(mapTaskRow);
};
```

## 7. Refactor Rule

เวลาย้ายโค้ด:

- อย่าเปลี่ยน route behavior โดยไม่จำเป็น
- อย่าเปลี่ยน request shape
- อย่าเปลี่ยน validation contract
- อย่าเปลี่ยน response shape

สิ่งที่เปลี่ยนได้:

- ชื่อไฟล์
- ที่อยู่ของ query logic
- helper functions ภายใน data layer

## Guided Exercise

ให้ใช้โฟลเดอร์:

```txt
exercises/ch25-task-api-query-layer/
```

เริ่มจากฐานของ `Ch24` แล้ว refactor ตามนี้:

1. ย้าย database connection และ table setup ไปที่ `data/db.ts`
2. ย้าย query functions ไปที่ `data/task-queries.ts`
3. ย้าย `mapTaskRow()` ไปอยู่ใน query file
4. ให้ route เปลี่ยนมา import จาก `task-queries.ts`
5. ลบหรือลดบทบาทของ `task-store.ts`
6. ให้ behavior ของ:
   - `GET /tasks`
   - `GET /tasks/:id`
   - `POST /tasks`
   - `PUT /tasks/:id`
   - `DELETE /tasks/:id`
   ยังทำงานเหมือนเดิม

## Expected Outcome

เมื่อเสร็จ:

- database setup ไม่อยู่ปนกับ route
- query logic ไม่อยู่ปนกับ app/server
- route อ่านง่ายขึ้น
- API contract ยังเหมือนเดิม

## Important Note

บทนี้ยังไม่เน้น:

- repository pattern แบบเต็ม
- dependency injection
- transactions
- test database แยกชุดใหม่

เราโฟกัสแค่:

- file responsibility
- query layer
- cleaner refactor

เสร็จแล้วพิมพ์:

```txt
ตรวจ Ch25
```
