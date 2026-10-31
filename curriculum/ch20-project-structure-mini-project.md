# บทที่ 20: โครงสร้างโปรเจกต์และมินิโปรเจกต์

## ทบทวน

ตอนนี้เรามี API ที่ประกอบด้วย:

- เส้นทาง (route)
- CRUD
- ตัวกลาง (middleware)
- การตรวจสอบ (validation)
- คำตอบเมื่อเกิดข้อผิดพลาด (error response)

ได้ครบแล้ว

ปัญหาที่จะเกิดต่อไปคือ ถ้าใส่ทุกอย่างไว้ในไฟล์เดียว ไฟล์จะเริ่ม:

- ยาว
- อ่านยาก
- แก้ยาก
- ใช้ซ้ำยาก

บทนี้เลยไม่ใช่เรื่อง "ไวยากรณ์ (syntax) ใหม่" แต่เป็นเรื่อง "จัดโครงสร้างให้โปรเจกต์อยู่ได้"

## 1. ทำไมโครงสร้างจึงสำคัญ

เมื่อโปรเจกต์โตขึ้น เรามักจะแยกความรับผิดชอบ:

- การตั้งค่าเซิร์ฟเวอร์ (server)
- เส้นทาง
- ตัวกลาง
- ข้อมูล

เป้าหมายคือให้แต่ละไฟล์มีหน้าที่ชัด

## 2. โครงสร้างฝั่งเซิร์ฟเวอร์แบบง่าย

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

- `server.js` = เปิดพอร์ต (port)
- `app.js` = ประกอบแอป Express
- `data/tasks.js` = เก็บ array ข้อมูล
- `middleware/validate-task.js` = ตัวกลางสำหรับการตรวจสอบ
- `routes/task-routes.js` = รวมเส้นทางของงาน (task)

## 3. การแยกความรับผิดชอบ

ถ้าฟังก์ชันหนึ่งทำหลายอย่างเกินไป มักจะแยกยาก

ตัวอย่างที่ควรแยก:

- ตัวจัดการคำขอ (handler) ของเส้นทาง
- ตัวกลางสำหรับการตรวจสอบ
- แหล่งข้อมูลในหน่วยความจำ (memory)

ข้อดีคือ:

- อ่านง่ายขึ้น
- หาข้อบกพร่องง่ายขึ้น
- ย้ายไปฐานข้อมูล (database) จริงทีหลังง่ายขึ้น

## 4. `app.js` กับ `server.js`

แนวคิดนี้ใช้บ่อยมาก

`app.js`
- สร้างแอป Express
- ใส่ตัวกลาง
- ลงทะเบียนเส้นทาง
- ส่งออก (export) `app`

`server.js`
- นำเข้า (import) `app`
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

## 5. ตัวจัดการเส้นทาง (router)

แทนที่จะเขียนทุกเส้นทางใน `app.js` เราใช้ `express.Router()` ได้

```js
import express from 'express';

const taskRouter = express.Router();

taskRouter.get('/', (req, res) => {
  res.json([]);
});

export { taskRouter };
```

แล้วเอาไปต่อในแอป:

```js
app.use('/tasks', taskRouter);
```

ผลคือ:

- `GET /tasks`
- `POST /tasks`
- `PUT /tasks/:id`

จะอยู่รวมกันเป็นหมวดเดียว

## 6. เป้าหมายของมินิโปรเจกต์

บทนี้ให้เราปรับโครงสร้าง (refactor) จาก API ที่ทำมาแล้ว ให้เป็นมินิโปรเจกต์แบบแยกไฟล์

ยังใช้ array ในหน่วยความจำเหมือนเดิม

ยังไม่ต้องมีฐานข้อมูล

ยังไม่ต้องมีระบบยืนยันตัวตน (auth)

เป้าหมายคือ:

- โครงสร้างดีขึ้น
- อ่านง่ายขึ้น
- พร้อมต่อยอดหลังจากจบบทนี้

## โจทย์ที่ต้องทำ

ให้แก้ไฟล์ในโฟลเดอร์:

```txt
exercises/ch20-mini-task-api/
```

ให้ทำตามนี้:

1. ใน `data/tasks.js`
   - สร้างและส่งออก `tasks`
   - ให้มีงานเริ่มต้นอย่างน้อย 2 ตัว

2. ใน `middleware/validate-task.js`
   - สร้างและส่งออก:
     - `validateCreateTask`
     - `validateUpdateTask`

3. ใน `routes/task-routes.js`
   - สร้าง `taskRouter`
   - ย้ายเส้นทาง CRUD ของงานมาไว้ที่นี่
   - ใช้ `tasks` จาก `data/tasks.js`
   - ใช้ตัวกลางจาก `middleware/validate-task.js`

4. ใน `app.js`
   - สร้างแอป Express
   - ใช้ `express.json()`
   - ผูก (mount) เส้นทางด้วย:

```js
app.use('/tasks', taskRouter);
```

5. ใน `server.js`
   - นำเข้า `app`
   - เปิดเซิร์ฟเวอร์ที่พอร์ต `3000`

## ลำดับการทำงานที่คาดหวัง

หลังทำเสร็จ โปรเจกต์ควรยังรองรับ:

- `GET /tasks`
- `GET /tasks/:id`
- `POST /tasks`
- `PUT /tasks/:id`
- `DELETE /tasks/:id`

และพฤติกรรม (behavior) การตรวจสอบควรเหมือนบทที่ 19

## ข้อควรระวัง

บทนี้ไม่ได้วัดว่า "เขียนเส้นทางใหม่ได้ไหม"

แต่วัดว่า:

- แยกไฟล์ถูกไหม
- การนำเข้า/การส่งออกถูกไหม
- โครงสร้างชัดไหม
- พฤติกรรมเดิมยังอยู่ไหม

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch20
```
