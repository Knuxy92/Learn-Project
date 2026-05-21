# SQL Learning Plan

เป้าหมายของแผนนี้คือทำให้การใช้ SQLite ใน backend ไม่ใช่แค่ "เขียนให้ผ่าน" แต่เข้าใจว่าแต่ละสถานการณ์ต้องใช้ SQL แบบไหน, SQLite driver คืนค่าอะไร, route ต้องแปลงผลลัพธ์เป็น HTTP response ยังไง, และควรแก้ปัญหาแบบไหน

## Current Problem

`Ch24` เริ่มเอา SQLite มาใช้กับ Task API แล้ว แต่ยังมีช่องว่างสำคัญ:

- ยังไม่แยกชัดว่า SQL command แต่ละแบบใช้กับสถานการณ์ไหน
- ยังไม่รู้ครบว่า `.all()`, `.get()`, `.run()`, `.exec()` ต่างกันยังไง
- ยังไม่รู้ว่า `changes` และ `lastInsertRowid` เอาไปใช้ตอนไหน
- ยังมีแนวคิดแบบ JSON file เช่น `read all -> push -> write all` ปนอยู่
- ยังไม่รู้ว่า `SELECT *` ใช้ได้ไหม และควรเลี่ยงตอนไหน
- ยังไม่ชัดว่า row จาก database ต้อง map เป็น app type ยังไง
- ยังไม่แยกชัดว่า "ไม่เจอข้อมูล" ต่างจาก "database/query พัง" ยังไง
- ยังไม่ชัดว่า database result ต้องกลายเป็น `200`, `201`, `204`, `400`, `404`, หรือ `500` ตอนไหน

ดังนั้นก่อนเดินต่อหลัง `Ch24` ต้องมี SQL bridge ก่อน

## SQL Bridge 02 - Query Basics

### สิ่งที่จะเรียน

- Database, table, row, column คืออะไร
- Schema คือข้อตกลงของข้อมูลใน table
- `CREATE TABLE IF NOT EXISTS` ใช้สร้าง table ตอนเริ่ม app
- `SELECT` ใช้อ่านข้อมูล
- `INSERT` ใช้สร้างข้อมูลใหม่
- `UPDATE` ใช้แก้ข้อมูลเดิม
- `DELETE` ใช้ลบข้อมูล
- `WHERE` ใช้เจาะ row ที่ต้องการ
- `?` placeholder ใช้ส่งค่าจากตัวแปรเข้า SQL อย่างปลอดภัย

### เรื่อง `SELECT *`

`SELECT *` แปลว่าเลือกทุก column

ใช้ได้ในช่วงเรียนหรือ debug เพราะอ่านง่าย:

```sql
SELECT * FROM tasks WHERE id = ?
```

แต่ใน app code ควรเริ่มฝึกใช้ column ชัดเจน:

```sql
SELECT id, title, done FROM tasks WHERE id = ?
```

เหตุผลคือถ้า table มี column เพิ่มในอนาคต app จะไม่เผลอรับข้อมูลที่ไม่ได้ตั้งใจ และ type mapping จะชัดกว่า

### Exit Criteria

ออกจาก bridge นี้ได้เมื่อ:

- อธิบายได้ว่า command ไหนอ่าน สร้าง แก้ ลบ
- รู้ว่า `WHERE id = ?` ต่างจากอ่านทั้ง table ยังไง
- รู้ว่า `SELECT *` สะดวกแต่ไม่ควรใช้เป็น default ใน app code
- เขียน query CRUD พื้นฐานเองได้โดยไม่พึ่งจำ pattern อย่างเดียว

## Basic ORDER BY

เวลาอ่านหลาย row จาก database อย่า assume ว่า order จะเรียงเหมือนที่คิดเสมอ

ถ้า API ต้องการ order ชัดเจน ให้เขียนใน SQL ตรงๆ:

```sql
SELECT id, title, done
FROM tasks
ORDER BY id DESC;
```

`ORDER BY id DESC` คือ id มากไปน้อย เหมาะกับกรณีอยากให้ task ใหม่ขึ้นก่อน

```sql
SELECT id, title, done
FROM tasks
ORDER BY id ASC;
```

`ORDER BY id ASC` คือ id น้อยไปมาก เหมาะกับกรณีอยากให้ task เก่าขึ้นก่อน

### Recommended Beginner Rule

สำหรับ `GET /tasks` ให้ใช้ order ชัดเจน:

```ts
const rows = db
  .prepare(`
    SELECT id, title, done
    FROM tasks
    ORDER BY id DESC
  `)
  .all();
```

### Exit Criteria

ออกจาก section นี้ได้เมื่อ:

- อธิบายได้ว่าทำไมไม่ควร assume row order
- ใช้ `ORDER BY id DESC` ได้
- ใช้ `ORDER BY id ASC` ได้
- เลือก order ง่ายๆ ให้ `GET /tasks` ได้

## Mini Exercises for SQL Bridge 02

เขียน SQL query สำหรับงานเหล่านี้:

1. Get all tasks
2. Get one task by id
3. Create a new task
4. Update a task title and done value
5. Delete a task by id

ตอบคำถาม:

1. command ไหนอ่านข้อมูล
2. command ไหนสร้างข้อมูล
3. command ไหนแก้ข้อมูล
4. command ไหนลบข้อมูล
5. `WHERE id = ?` ทำอะไร
6. ทำไม app code ไม่ควรใช้ `SELECT *` เป็น default

## SQL Bridge 03 - SQLite Driver Return Values

SQLite ใน Node ไม่ได้คืนค่าเหมือนกันทุก method

| Method | ใช้กับ | คืนค่า | สถานการณ์หลัก |
| --- | --- | --- | --- |
| `.exec(sql)` | SQL setup หลาย statement | ไม่มี row data | สร้าง table ตอนเริ่ม app |
| `.all()` | `SELECT` หลาย rows | array | อ่านรายการทั้งหมด |
| `.get()` | `SELECT` row เดียว | row หรือ `undefined` | หา task ด้วย id |
| `.run()` | `INSERT`, `UPDATE`, `DELETE` | result info | เขียนข้อมูลลง DB |

### `.exec()`

ใช้กับ setup SQL เช่นสร้าง table ตอนเริ่ม app

```ts
db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL DEFAULT 0
  )
`);
```

ไม่ใช้ `.exec()` เพื่ออ่าน row กลับมา

### `.all()`

ใช้เมื่อคาดว่าจะได้หลาย row

```ts
const rows = db.prepare("SELECT id, title, done FROM tasks").all();
```

ถ้า table ว่าง จะได้ `[]` ไม่ใช่ `undefined`

### `.get()`

ใช้เมื่อคาดว่าจะได้ row เดียว

```ts
const row = db
  .prepare("SELECT id, title, done FROM tasks WHERE id = ?")
  .get(id);
```

ถ้าไม่เจอ id จะได้ `undefined`

### `.run()`

ใช้กับคำสั่งที่เปลี่ยนข้อมูล

```ts
const result = db
  .prepare("INSERT INTO tasks (title, done) VALUES (?, ?)")
  .run(title, 0);
```

ค่าที่ต้องรู้:

- `result.lastInsertRowid` คือ id ล่าสุดที่ database สร้างจาก `INSERT`
- `result.changes` คือจำนวน row ที่ได้รับผลจากคำสั่งนั้น

### ใช้ `lastInsertRowid` ตอนไหน

ใช้หลัง `INSERT` เมื่อ table มี `INTEGER PRIMARY KEY AUTOINCREMENT`

สถานการณ์:

- สร้าง task ใหม่
- ต้อง return object ที่มี id กลับไปให้ client
- ไม่ควรหา id เองจาก array เหมือนตอนใช้ JSON file

ตัวอย่าง:

```ts
const result = db
  .prepare("INSERT INTO tasks (title, done) VALUES (?, ?)")
  .run(title, 0);

const id = Number(result.lastInsertRowid);
```

### ใช้ `changes` ตอนไหน

ใช้หลัง `UPDATE` หรือ `DELETE` เพื่อดูว่ามี row ถูกกระทบไหม

สถานการณ์:

- `DELETE /tasks/:id` ต้องรู้ว่าลบสำเร็จไหม
- ถ้า `changes === 0` แปลว่าไม่มี row ที่ตรงเงื่อนไข หรือไม่มี row ถูกเปลี่ยน
- ใช้ช่วยตัดสินใจว่าจะตอบ success หรือ `404`

ตัวอย่าง:

```ts
const result = db
  .prepare("DELETE FROM tasks WHERE id = ?")
  .run(id);

const deleted = result.changes > 0;
```

สำหรับ `UPDATE` ถ้าต้อง return task ตัวล่าสุด วิธีที่ชัดสุดสำหรับผู้เรียนคือ:

1. `SELECT` ก่อนว่า id มีจริงไหม
2. `UPDATE`
3. `SELECT` อีกรอบเพื่อคืนข้อมูลล่าสุด

### Exit Criteria

ออกจาก bridge นี้ได้เมื่อ:

- เลือก `.all()`, `.get()`, `.run()`, `.exec()` ได้ถูกสถานการณ์
- รู้ว่า `.all()` ได้ `[]` เมื่อไม่มี row
- รู้ว่า `.get()` ได้ `undefined` เมื่อไม่เจอ row
- รู้ว่า `lastInsertRowid` ใช้หลัง `INSERT`
- รู้ว่า `changes` ใช้หลัง `UPDATE` หรือ `DELETE`

## SQL Error vs Not Found

มือใหม่มักรวมทุกปัญหา database เป็นเรื่องเดียวกัน แต่ backend ต้องแยกให้ออก

### Not Found

กรณีนี้ query ถูกต้อง แต่ไม่มี row ที่ตรงเงื่อนไข:

```ts
const row = db
  .prepare("SELECT id, title, done FROM tasks WHERE id = ?")
  .get(id);

if (!row) {
  return undefined;
}
```

นี่ไม่ใช่ database error เพราะ SQL ทำงานได้ปกติ แค่ task id นั้นไม่มีอยู่

### SQL Error

กรณีนี้ query เองมีปัญหา:

```ts
try {
  const row = db
    .prepare("SELECT id, title, done FROM wrong_table WHERE id = ?")
    .get(id);
} catch (error) {
  console.error(error);
}
```

ตัวอย่าง SQL error:

- table ไม่มีอยู่จริง
- column name ผิด
- จำนวน `?` ไม่เท่ากับจำนวนค่าที่ส่งเข้า `.run()` หรือ `.get()`
- required value หายไป
- `NOT NULL` column ได้ `null`
- `UNIQUE` value ซ้ำ

### Backend Mapping

| Situation | Meaning | HTTP Response |
| --- | --- | --- |
| `.get()` returns `undefined` | row not found | `404 Not Found` |
| `.all()` returns `[]` | ไม่มี row ในรายการ | `200 OK` with empty array |
| SQL throws an error | database/query พัง | `500 Internal Server Error` |

### Exit Criteria

ออกจาก section นี้ได้เมื่อ:

- อธิบายได้ว่า `undefined` ไม่ใช่ error เสมอไป
- อธิบายได้ว่า `[]` ไม่ใช่ error
- อธิบายได้ว่า SQL error ควรกลายเป็น `500` ใน API
- แยก "data not found" กับ "database failed" ได้

## Mini Exercises for SQL Bridge 03

ตอบคำถาม:

1. method ไหนใช้อ่านหลาย rows
2. method ไหนใช้อ่าน row เดียว
3. method ไหนใช้กับ `INSERT`, `UPDATE`, `DELETE`
4. `.all()` คืนอะไรเมื่อไม่มี rows
5. `.get()` คืนอะไรเมื่อไม่เจอ row
6. `lastInsertRowid` ใช้ทำอะไร
7. `changes` ใช้ทำอะไร

อธิบาย code นี้:

```ts
const result = db
  .prepare("DELETE FROM tasks WHERE id = ?")
  .run(id);
```

แล้วตอบว่าอันนี้แปลว่าอะไร:

```ts
result.changes === 0
```

## SQL Bridge 04 - Mapping DB Rows to App Types

### ปัญหาที่ต้องเข้าใจ

ข้อมูลใน database ไม่จำเป็นต้องเป็น type เดียวกับใน TypeScript

ตัวอย่าง:

- SQLite เก็บ boolean เป็น `0` หรือ `1`
- App อยากใช้ `done: boolean`

ดังนั้นต้องมี mapper:

```ts
type TaskRow = {
  id: number;
  title: string;
  done: number;
};

type Task = {
  id: number;
  title: string;
  done: boolean;
};

const mapTaskRow = (row: TaskRow): Task => {
  return {
    id: row.id,
    title: row.title,
    done: row.done === 1,
  };
};
```

### ทำไม mapper ดีกว่า `as Task` กระจายหลายจุด

`as Task` แค่บอก TypeScript ว่า "เชื่อฉัน" แต่ไม่ได้แปลงข้อมูลจริง

ถ้า database คืน `done: 0` แล้วเรา cast เป็น `Task` ทันที app อาจคิดว่า `done` เป็น boolean ทั้งที่ runtime เป็น number

mapper ทำให้การแปลงชัดเจน:

- database row ใช้ `done: number`
- app object ใช้ `done: boolean`
- ถ้า schema เปลี่ยนในอนาคต จะรู้ว่าต้องแก้จุดไหน

### Exit Criteria

ออกจาก bridge นี้ได้เมื่อ:

- อธิบายได้ว่า database type กับ app type ต่างกันยังไง
- เขียน mapper จาก row เป็น object ได้
- ไม่ใช้ `as Task` เพื่อกลบปัญหา type โดยไม่ map จริง
- จัดการ `.get()` ที่คืน `undefined` ได้
- จัดการ `.all()` ที่คืน array ว่างได้

## Mini Exercises for SQL Bridge 04

ให้ database row นี้:

```ts
const row = {
  id: 1,
  title: "Study SQL",
  done: 0,
};
```

แปลงเป็น app object นี้:

```ts
const task = {
  id: 1,
  title: "Study SQL",
  done: false,
};
```

ตอบคำถาม:

1. ทำไม SQLite มักเก็บ boolean เป็น `0` หรือ `1`
2. ทำไม app ควรใช้ `done: boolean`
3. ทำไม mapper ดีกว่าใช้ `as Task` ทุกที่

## Input Validation Before Database Queries

ก่อน `INSERT` หรือ `UPDATE` backend ควรตรวจ input ก่อน

อย่าส่ง bad data เข้า database แล้วหวังให้ SQL จัดการทุกอย่าง เพราะจะทำให้ debug ยาก และมือใหม่อาจเข้าใจผิดว่า database พัง ทั้งที่ปัญหาคือ request body ผิด

### Create Task Validation

```ts
app.post("/tasks", (req, res) => {
  const { title } = req.body;

  if (typeof title !== "string" || title.trim() === "") {
    return res.status(400).json({
      error: "title is required",
    });
  }

  const result = db
    .prepare("INSERT INTO tasks (title, done) VALUES (?, ?)")
    .run(title, 0);

  const id = Number(result.lastInsertRowid);
  const task = getTaskById(id);

  return res.status(201).json(task);
});
```

### Update Task Validation

```ts
app.put("/tasks/:id", (req, res) => {
  const id = Number(req.params.id);
  const { title, done } = req.body;

  if (!Number.isInteger(id)) {
    return res.status(400).json({
      error: "invalid task id",
    });
  }

  if (typeof title !== "string" || title.trim() === "") {
    return res.status(400).json({
      error: "title is required",
    });
  }

  if (typeof done !== "boolean") {
    return res.status(400).json({
      error: "done must be a boolean",
    });
  }

  const existing = getTaskById(id);

  if (!existing) {
    return res.status(404).json({
      error: "task not found",
    });
  }

  db.prepare("UPDATE tasks SET title = ?, done = ? WHERE id = ?")
    .run(title, done ? 1 : 0, id);

  const updated = getTaskById(id);

  return res.json(updated);
});
```

### Exit Criteria

ออกจาก section นี้ได้เมื่อ:

- check required fields ก่อน `INSERT` ได้
- check required fields ก่อน `UPDATE` ได้
- return `400 Bad Request` สำหรับ bad input ได้
- ไม่ส่ง obvious invalid values เข้า SQL

## Mapping Database Results to HTTP Responses

backend route ไม่ได้มีหน้าที่แค่ run SQL แต่ต้องแปลง database result เป็น HTTP response ที่ถูกต้องด้วย

### Common Mapping Rules

| API Situation | Database Result | HTTP Response |
| --- | --- | --- |
| Get all tasks | `.all()` returns array | `200 OK` |
| Get all tasks, table is empty | `.all()` returns `[]` | `200 OK` with `[]` |
| Get task by id, found | `.get()` returns row | `200 OK` |
| Get task by id, not found | `.get()` returns `undefined` | `404 Not Found` |
| Create task | `.run()` returns `lastInsertRowid` | `201 Created` |
| Update task, id exists | update succeeds | `200 OK` |
| Update task, id not found | check returns `undefined` | `404 Not Found` |
| Delete task, id exists | `changes > 0` | `204 No Content` or `200 OK` |
| Delete task, id not found | `changes === 0` | `404 Not Found` |
| Bad request body | validation fails | `400 Bad Request` |
| SQL error | query throws | `500 Internal Server Error` |

### Get Task by ID

```ts
app.get("/tasks/:id", (req, res) => {
  const id = Number(req.params.id);

  if (!Number.isInteger(id)) {
    return res.status(400).json({
      error: "invalid task id",
    });
  }

  const task = getTaskById(id);

  if (!task) {
    return res.status(404).json({
      error: "task not found",
    });
  }

  return res.json(task);
});
```

### Delete Task

```ts
app.delete("/tasks/:id", (req, res) => {
  const id = Number(req.params.id);

  if (!Number.isInteger(id)) {
    return res.status(400).json({
      error: "invalid task id",
    });
  }

  const result = db
    .prepare("DELETE FROM tasks WHERE id = ?")
    .run(id);

  if (result.changes === 0) {
    return res.status(404).json({
      error: "task not found",
    });
  }

  return res.status(204).send();
});
```

### Exit Criteria

ออกจาก section นี้ได้เมื่อ:

- อธิบายได้ว่าทำไม empty array ควร return `200`
- อธิบายได้ว่าทำไม missing row ควร return `404`
- อธิบายได้ว่าทำไม invalid request data ควร return `400`
- อธิบายได้ว่าทำไม database error ควร return `500`
- ใช้ `changes` ช่วยตัดสินใจ success กับ `404` ได้

## Mini Exercises for HTTP Response Mapping

เลือก HTTP response ที่ถูกต้อง:

1. `.get()` returns `undefined`
2. `.all()` returns `[]`
3. request body ไม่มี `title`
4. `INSERT` สำเร็จและได้ `lastInsertRowid`
5. `DELETE` returns `changes === 0`
6. SQL query throws an error

Expected answers:

| Case | Response |
| --- | --- |
| `.get()` returns `undefined` | `404 Not Found` |
| `.all()` returns `[]` | `200 OK` |
| Missing `title` | `400 Bad Request` |
| `INSERT` succeeds | `201 Created` |
| `DELETE` changes is `0` | `404 Not Found` |
| SQL throws | `500 Internal Server Error` |

## Ch24 Revision - Task API with SQLite

หลังจบ SQL bridge ให้ย้อนมา refactor `Ch24`

### สิ่งที่จะแก้

- ลบแนวคิด `writeTasks(tasks)` แบบ JSON file ถ้าไม่ได้ใช้จริง
- เปลี่ยนชื่อ `RawTask` เป็น `TaskRow` หรือ `DbTaskRow`
- รวม logic map row ไว้จุดเดียว
- ใช้ `SELECT id, title, done` แทน `SELECT *` ใน app code
- ใช้ `ORDER BY id DESC` ใน `readTasks`
- ใช้ `lastInsertRowid` ใน `createTask`
- ใช้ `changes` ใน `deleteTask`
- ทำ `updateTask` เป็น flow ที่อ่านง่าย: check exists -> update -> read latest
- route ต้องแยก `400`, `404`, `500` ให้ชัดเจน

### สถานการณ์ที่ต้องครอบคลุม

| สถานการณ์ | สิ่งที่ควรใช้ |
| --- | --- |
| อ่าน task ทั้งหมด | `SELECT ... ORDER BY id DESC` + `.all()` |
| อ่าน task ตาม id | `SELECT ... WHERE id = ?` + `.get()` |
| สร้าง task | `INSERT ...` + `.run()` + `lastInsertRowid` |
| แก้ task | `SELECT` เช็คก่อน + `UPDATE ... WHERE id = ?` + `.run()` |
| ลบ task | `DELETE ... WHERE id = ?` + `.run()` + `changes` |
| table ว่าง | `.all()` ได้ `[]` |
| id ไม่เจอ | `.get()` ได้ `undefined` |
| request body ผิด | validation fail แล้วตอบ `400` |
| SQL พัง | catch error แล้วตอบ `500` |
| boolean จาก DB | map `0/1` เป็น `false/true` |

## Basic Database Initialization Structure

app ควรสร้าง database table ตอน app start ไม่ใช่สร้าง table ใน route ทุก request

โครงสร้างแบบ beginner ที่เข้ากับโปรเจกต์นี้:

```txt
data/
  db.ts
  task-queries.ts
routes/
  task-routes.ts
```

### `data/db.ts`

ไฟล์นี้ดูแล database connection และ setup SQL

```ts
import { DatabaseSync } from "node:sqlite";
import path from "node:path";

const dbPath = path.join(__dirname, "../storage/tasks.db");
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

### `data/task-queries.ts`

ไฟล์นี้ดูแล SQL ที่เกี่ยวกับ tasks

```ts
import { db } from "./db";

type TaskRow = {
  id: number;
  title: string;
  done: number;
};

type Task = {
  id: number;
  title: string;
  done: boolean;
};

const mapTaskRow = (row: TaskRow): Task => {
  return {
    id: row.id,
    title: row.title,
    done: row.done === 1,
  };
};

const getTaskById = (id: number): Task | undefined => {
  const row = db
    .prepare("SELECT id, title, done FROM tasks WHERE id = ?")
    .get(id) as TaskRow | undefined;

  if (!row) return undefined;

  return mapTaskRow(row);
};

export { getTaskById };
```

### `routes/task-routes.ts`

route ควรรู้เรื่อง HTTP request/response เป็นหลัก และเรียก query function แทนการเขียน SQL กระจายหลายที่

### Exit Criteria

ออกจาก section นี้ได้เมื่อ:

- อธิบายได้ว่าทำไม database setup ควรอยู่ใกล้ app startup
- อธิบายได้ว่าทำไม route ไม่ควร create table ทุก request
- อธิบายได้ว่าทำไม query logic ควรแยกจาก route logic
- บอกได้ว่าอะไรอยู่ใน `data/db.ts`
- บอกได้ว่าอะไรอยู่ใน `data/task-queries.ts`

## Ch25 - Query Layer

เมื่อ `Ch24` เข้าใจแล้ว ค่อยแยก query layer ให้สะอาด

### สิ่งที่จะเรียน

- data access layer คืออะไร
- ทำไม route ไม่ควรรู้ SQL เยอะ
- ทำ helper เช่น `mapTaskRow`, `getTaskById`, `readTaskRows`
- แยก SQL string ให้จัดการง่าย
- ลด duplicate query
- เลือกจุดที่ควร throw error กับจุดที่ควร return `undefined`
- ทำให้ route focus ที่ validation และ HTTP response

## Ch26 - Database Testing

หลัง query layer ค่อยเรียน test กับ database

### สิ่งที่จะเรียน

- test database แยกจาก database จริง
- reset table ก่อน test
- seed data สำหรับ test
- ตรวจ `400`, `404`, `200`, `201`, `204`, `500` เท่าที่ควร test
- ปิด server หลัง test
- ปิด database connection ถ้าจำเป็น
- ทำให้ test ไม่พึ่งข้อมูลเก่าค้างในเครื่อง

## Optional: created_at and updated_at

หลัง basic CRUD เข้าใจแล้ว ค่อยเรียนว่า database มักเก็บ timestamp

เริ่มจาก `created_at` ก่อน:

```sql
CREATE TABLE IF NOT EXISTS tasks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  done INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

หลังจากเข้าใจ update flow แล้ว ค่อยเพิ่ม `updated_at`:

```sql
CREATE TABLE IF NOT EXISTS tasks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  done INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

หัวข้อนี้ optional ในช่วงนี้ เพราะ main goal ยังเป็น:

- understand CRUD
- understand driver return values
- understand row mapping
- understand HTTP responses

## Later SQL Topics

หัวข้อพวกนี้สำคัญ แต่ยังไม่ควรยัดทันทีใน `Ch24`

- `UNIQUE`
- `FOREIGN KEY`
- `JOIN`
- `LIMIT`
- `COUNT`
- transactions
- migrations
- indexes
- pagination
- soft delete
- SQL injection แบบลึกขึ้น

## Final Rule

ก่อนเพิ่ม SQL topic ใหม่ทุกครั้ง ต้องตอบให้ได้ก่อนว่า:

- ผู้เรียนเคยเห็น syntax นี้หรือยัง
- topic นี้ควรอยู่ bridge, chapter หลัก, หรือ optional
- ควรใช้ SQLite driver method ไหน
- method นั้นคืนค่าอะไร
- ถ้าข้อมูลไม่มี จะได้ `undefined`, `[]`, หรือ error
- ควรกลายเป็น `400`, `404`, `200`, `201`, `204`, หรือ `500`
- route ต้อง map database row เป็น app type ไหม
- ถ้าคำตอบยังไม่ชัด ให้เพิ่ม bridge lesson สั้นๆ ก่อนเดินต่อ
