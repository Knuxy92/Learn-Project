# Chapter 20: Project Structure & Mini Project

## Recap

ตอนนี้นายทำ API ที่มี:

- routes
- CRUD
- middleware
- validation
- error response

ได้ครบแล้ว

ปัญหาที่จะเกิดต่อไปคือ ถ้าใส่ทุกอย่างไว้ในไฟล์เดียว ไฟล์จะเริ่ม:

- ยาว
- อ่านยาก
- แก้ยาก
- reuse ยาก

บทนี้เลยไม่ใช่เรื่อง "syntax ใหม่" แต่เป็นเรื่อง "จัดโครงสร้างให้โปรเจกต์อยู่ได้"

## 1. Why Structure Matters

เมื่อโปรเจกต์โตขึ้น เรามักจะแยกความรับผิดชอบ:

- server setup
- routes
- middleware
- data
- types

เป้าหมายคือให้แต่ละไฟล์มีหน้าที่ชัด

## 2. A Simple Backend Structure

โครงแบบเล็กที่เหมาะกับตอนนี้:

```txt
mini-task-api/
  server.ts
  app.ts
  data/
    tasks.ts
  middleware/
    validate-task.ts
  routes/
    task-routes.ts
  types/
    task.ts
```

ความหมาย:

- `server.ts` = เปิด port
- `app.ts` = ประกอบ express app
- `data/tasks.ts` = เก็บ array ข้อมูล
- `middleware/validate-task.ts` = validation middleware
- `routes/task-routes.ts` = รวม task routes
- `types/task.ts` = type ของ Task

## 3. Separation of Responsibility

ถ้าฟังก์ชันหนึ่งทำหลายอย่างเกินไป มักจะแยกยาก

ตัวอย่างที่ควรแยก:

- type definition
- route handler
- validation middleware
- in-memory data source

ข้อดีคือ:

- อ่านง่ายขึ้น
- หา bug ง่ายขึ้น
- ย้ายไป database จริงทีหลังง่ายขึ้น

## 4. `app.ts` vs `server.ts`

แนวคิดนี้ใช้บ่อยมาก

`app.ts`
- สร้าง express app
- ใส่ middleware
- register routes
- export app

`server.ts`
- import app
- เรียก `app.listen(...)`

ตัวอย่าง:

```ts
// app.ts
import express from 'express';
import { taskRouter } from './routes/task-routes';

const app = express();
app.use(express.json());
app.use('/tasks', taskRouter);

export { app };
```

```ts
// server.ts
import { app } from './app';

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

## 5. Router

แทนที่จะเขียนทุก route ใน `app.ts` เราสามารถใช้ `express.Router()`

```ts
import express from 'express';

const taskRouter = express.Router();

taskRouter.get('/', (req, res) => {
  res.json([]);
});

export { taskRouter };
```

แล้วเอาไปต่อใน app:

```ts
app.use('/tasks', taskRouter);
```

ผลคือ:

- `GET /tasks`
- `POST /tasks`
- `PUT /tasks/:id`

จะอยู่รวมกันเป็นหมวดเดียว

## 6. Mini Project Goal

บทนี้ให้นาย refactor จาก API ที่ทำมาแล้ว ให้เป็น mini project แบบแยกไฟล์

ยังใช้ in-memory array เหมือนเดิม

ยังไม่ต้องมี database

ยังไม่ต้องมี auth

เป้าหมายคือ:

- โครงสร้างดีขึ้น
- อ่านง่ายขึ้น
- พร้อมต่อยอดหลังจากจบ chapter นี้

## Guided Exercise

ให้แก้ไฟล์ในโฟลเดอร์:

```txt
exercises/ch20-mini-task-api/
```

ให้ทำตามนี้:

1. ใน `types/task.ts`
   - สร้าง `type Task`

2. ใน `data/tasks.ts`
   - สร้างและ export `tasks`
   - ให้มี task เริ่มต้นอย่างน้อย 2 ตัว

3. ใน `middleware/validate-task.ts`
   - สร้างและ export:
     - `validateCreateTask`
     - `validateUpdateTask`

4. ใน `routes/task-routes.ts`
   - สร้าง `taskRouter`
   - ย้าย CRUD routes ของ task มาไว้ที่นี่
   - ใช้ `tasks` จาก `data/tasks.ts`
   - ใช้ middleware จาก `middleware/validate-task.ts`

5. ใน `app.ts`
   - สร้าง express app
   - ใช้ `express.json()`
   - mount route ด้วย:

```ts
app.use('/tasks', taskRouter);
```

6. ใน `server.ts`
   - import `app`
   - เปิด server ที่ port `3000`

## Expected Flow

หลังทำเสร็จ โปรเจกต์ควรยังรองรับ:

- `GET /tasks`
- `GET /tasks/:id`
- `POST /tasks`
- `PUT /tasks/:id`
- `DELETE /tasks/:id`

และ validation behavior ควรเหมือน Ch19

## Important Note

บทนี้ไม่ได้วัดว่า "เขียน route ใหม่ได้ไหม"

แต่วัดว่า:

- แยกไฟล์ถูกไหม
- import/export ถูกไหม
- โครงสร้างชัดไหม
- behavior เดิมยังอยู่ไหม

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch20
```
