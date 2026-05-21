# Chapter 24: Task API with SQLite

## Recap

ตอนนี้นายผ่าน 2 ขั้นสำคัญแล้ว:

- `Ch21` JSON file persistence
- `Ch23` SQLite basics

ดังนั้นก้าวถัดไปคือ:

- เอา task API ที่นายมีอยู่แล้ว
- ย้าย data layer จาก JSON file ไป SQLite

เป้าหมายของบทนี้ไม่ใช่ทำ API ใหม่

แต่คือ "เปลี่ยน backend storage โดยให้ API contract เดิมยังอยู่"

## 1. What Should Stay the Same

สิ่งที่ไม่ควรเปลี่ยน:

- routes
- request shape
- response shape
- validation behavior
- status code หลัก

สิ่งที่เปลี่ยน:

- data source
- query logic
- id generation

## 2. Why This Step Matters

นี่คือ skill สำคัญของ backend จริง:

- เปลี่ยน implementation ข้างใน
- โดยไม่ทำให้สัญญาภายนอกพัง

พูดอีกแบบคือ:

- UI/client ควรไม่ต้องรู้ว่าเมื่อก่อนเก็บ JSON
- ตอนนี้เปลี่ยนเป็น SQLite แล้ว client ก็ควรยังเรียก API ได้เหมือนเดิม

## 3. Data Layer Responsibilities

ในบทนี้ data layer ควรรับผิดชอบ:

- connect database
- create table ถ้ายังไม่มี
- map row -> `Task`
- CRUD ผ่าน SQL

route layer ควรทำแค่:

- parse params/body
- เรียก storage function
- ตอบ response

## 4. Suggested SQLite Storage Functions

จากเดิมใน `Ch21` เราเคยมี:

- `readTasks()`
- `findTaskById(id)`
- `createTask(title)`
- `updateTask(id, updates)`
- `deleteTask(id)`

ใน SQLite version ก็ควรยังมีชื่อใกล้เดิม เพื่อให้ route เปลี่ยนน้อยที่สุด

## 5. Row Mapping Reminder

ใน SQLite:

- `done` เก็บเป็น `0 | 1`

แต่ใน API:

- `done` ต้องเป็น `boolean`

ดังนั้นทุก row ที่อ่านจาก DB ต้อง map ก่อน

```ts
const mapTaskRow = (row: DbTaskRow): Task => ({
  id: row.id,
  title: row.title,
  done: row.done === 1,
});
```

## 6. Example Query Flow

สร้าง task:

```ts
db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run(title, 0);
```

หา task ทั้งหมด:

```ts
const rows = db.prepare("SELECT id, title, done FROM tasks").all() as DbTaskRow[];
return rows.map(mapTaskRow);
```

อัปเดต:

```ts
db.prepare("UPDATE tasks SET title = ?, done = ? WHERE id = ?").run(
  title,
  done,
  id,
);
```

ลบ:

```ts
db.prepare("DELETE FROM tasks WHERE id = ?").run(id);
```

## Guided Exercise

ให้แก้ไฟล์ในโฟลเดอร์:

```txt
exercises/ch24-task-api-sqlite/
```

ให้ทำตามนี้:

1. คัดลอกโครงจาก `Ch21` มาเป็นฐาน

2. ใน `types/task.ts`
   - สร้าง `DbTaskRow`
   - สร้าง `Task`

3. ใน `data/task-store.ts`
   - ใช้ `DatabaseSync` จาก `node:sqlite`
   - ใช้ไฟล์ DB ที่:

```txt
exercises/ch24-storage/tasks.db
```

4. ใน `data/task-store.ts`
   - สร้าง table `tasks` ถ้ายังไม่มี
   - สร้าง function:
     - `getAllTasks()`
     - `findTaskById(id)`
     - `createTask(title)`
     - `updateTask(id, updates)`
     - `deleteTask(id)`

5. ให้ทุก function map row กลับเป็น `Task`

6. ใน `routes/task-routes.ts`
   - ใช้ route contract เดิมจาก Ch21
   - แต่เปลี่ยนมาเรียก SQLite storage functions

7. ใน `middleware/validate-task.ts`
   - reuse logic เดิมจาก Ch21

8. ใน `app.ts` และ `server.ts`
   - โครงเหมือนเดิม

## Expected Behavior

หลังทำเสร็จ:

- `GET /tasks`
- `GET /tasks/:id`
- `POST /tasks`
- `PUT /tasks/:id`
- `DELETE /tasks/:id`

ต้องยังทำงานเหมือน Ch21

แต่ข้อมูลจะถูกเก็บใน SQLite แทน JSON

## Important Note

ในบทนี้ยังไม่เน้น:

- transactions
- migrations
- foreign keys
- joins

เราโฟกัสแค่:

- single table
- CRUD
- row mapping

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch24
```
