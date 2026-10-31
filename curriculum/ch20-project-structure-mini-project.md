# บทที่ 20: โครงสร้างโปรเจกต์และ mini project

## ทบทวน

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

- การตั้งค่า server
- routes
- middleware
- ข้อมูล

เป้าหมายคือให้แต่ละไฟล์มีหน้าที่ชัด

## 2. A Simple Backend Structure

โครงแบบเล็กที่เหมาะกับตอนนี้:

```txt
ch20-mini-task-api/
  server.js
  app.js
  data/
    tasks.js
  middleware/
    validate-task.js
  routes/
    task-routes.js
```

ความหมาย:

- `server.js` = เปิด port
- `app.js` = ประกอบ express app
- `data/tasks.js` = เก็บ array ข้อมูล
- `middleware/validate-task.js` = middleware สำหรับ validation
- `routes/task-routes.js` = รวม task routes

## 3. Separation of Responsibility

ถ้าฟังก์ชันหนึ่งทำหลายอย่างเกินไป มักจะแยกยาก

ตัวอย่างที่ควรแยก:

- handler ของ route
- middleware สำหรับ validation
- แหล่งข้อมูลใน memory

ข้อดีคือ:

- อ่านง่ายขึ้น
- หา bug ง่ายขึ้น
- ย้ายไป database จริงทีหลังง่ายขึ้น

## 4. `app.js` vs `server.js`

แนวคิดนี้ใช้บ่อยมาก

`app.js`
- สร้าง express app
- ใส่ middleware
- ลงทะเบียน routes
- export `app`

`server.js`
- import `app`
- เรียก `app.listen(...)`

ตัวอย่าง:

```js
// app.js
import express from 'express';
import { taskRouter } from './routes/task-routes.js';

const app = express();
app.use(express.json());
app.use('/tasks', taskRouter);

export { app };
```

```js
// server.js
import { app } from './app.js';

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

## 5. Router

แทนที่จะเขียนทุก route ใน `app.js` เราสามารถใช้ `express.Router()`

```js
import express from 'express';

const taskRouter = express.Router();

taskRouter.get('/', (req, res) => {
  res.json([]);
});

export { taskRouter };
```

แล้วเอาไปต่อใน app:

```js
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

## โจทย์ที่ต้องทำ

ให้แก้ไฟล์ในโฟลเดอร์:

```txt
exercises/ch20-mini-task-api/
```

ให้ทำตามนี้:

1. ใน `data/tasks.js`
   - สร้างและ export `tasks`
   - ให้มี task เริ่มต้นอย่างน้อย 2 ตัว

2. ใน `middleware/validate-task.js`
   - สร้างและ export:
     - `validateCreateTask`
     - `validateUpdateTask`

3. ใน `routes/task-routes.js`
   - สร้าง `taskRouter`
   - ย้าย CRUD routes ของ task มาไว้ที่นี่
   - ใช้ `tasks` จาก `data/tasks.js`
   - ใช้ middleware จาก `middleware/validate-task.js`

4. ใน `app.js`
   - สร้าง express app
   - ใช้ `express.json()`
   - mount route ด้วย:

```js
app.use('/tasks', taskRouter);
```

5. ใน `server.js`
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

## ข้อควรระวัง

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
