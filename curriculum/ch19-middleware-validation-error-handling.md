# บทที่ 19: ตัวกลาง การตรวจสอบ และการจัดการข้อผิดพลาด

## ทบทวน

บทที่แล้วเราใช้ Express ทำ CRUD API กับข้อมูลใน array ได้แล้ว

ตอนนี้ปัญหาคือ API ของเรายัง "เชื่อ" คำขอ (request) มากเกินไป

ตัวอย่างเช่น:

- ฝั่งผู้เรียก (client) อาจไม่ส่ง `title`
- ฝั่งผู้เรียกอาจส่ง `title` เป็นเลข
- ฝั่งผู้เรียกอาจส่ง `done` เป็นข้อความ (string) แทนค่าจริงเท็จ (boolean)

ดังนั้นบทนี้จะเพิ่ม 3 อย่าง:

- ตัวกลาง (middleware)
- การตรวจสอบ (validation) เบื้องต้น
- การจัดการข้อผิดพลาด (error handling) ที่สม่ำเสมอขึ้น

## 1. ตัวกลางคืออะไร

ตัวกลางคือฟังก์ชัน (function) ที่รัน "ก่อน" หรือ "ระหว่าง" ตัวจัดการเส้นทาง (route handler)

มันมักใช้ทำงานแบบนี้:

- แปลงเนื้อหาคำขอ (body)
- บันทึกเหตุการณ์ (log) ของคำขอ
- ตรวจการยืนยันตัวตน (auth)
- ตรวจสอบข้อมูลที่รับเข้ามา (input)

รูปแบบพื้นฐาน:

```js
const middleware = (req, res, next) => {
  console.log('Before route');
  next();
};
```

ถ้าเรียก `next()`:

- คำขอจะไหลต่อไปยังตัวกลางหรือเส้นทางถัดไป

ถ้าไม่เรียก `next()`:

- คำขอจะหยุดตรงนั้น

## 2. ตัวกลางระดับเส้นทาง

เราไม่จำเป็นต้องใช้ตัวกลางกับทั้งแอปเสมอไป

เราใช้เฉพาะเส้นทางบางตัวได้:

```js
app.post('/tasks', validateCreateTask, (req, res) => {
  res.json({ ok: true });
});
```

ลำดับคือ:

1. คำขอเข้า `validateCreateTask`
2. ถ้าผ่าน ค่อยไปตัวจัดการเส้นทาง
3. ถ้าไม่ผ่าน ตัวกลางตอบข้อผิดพลาดได้เลย

## 3. การตรวจสอบเบื้องต้น

ในบทนี้เราจะยังไม่ใช้ไลบรารีภายนอก

เราจะตรวจแบบง่ายก่อนว่า:

- `title` ต้องเป็นข้อความ
- `title` ต้องไม่ว่าง
- `done` ถ้ามี ต้องเป็นค่าจริงเท็จ

ตัวอย่าง:

```js
const validateCreateTask = (req, res, next) => {
  const { title, done } = req.body;

  if (typeof title !== 'string' || title.trim() === '') {
    res.status(400).json({ message: 'Title is required' });
    return;
  }

  if (done !== undefined && typeof done !== 'boolean') {
    res.status(400).json({ message: 'Done must be a boolean' });
    return;
  }

  next();
};
```

## 4. ทำไมเรื่องนี้สำคัญ

ถ้าไม่ตรวจสอบ:

- ข้อมูลใน array จะมีรูปร่างเพี้ยน
- เส้นทางอื่นจะเริ่มพังตาม
- ข้อบกพร่อง (bug) จะย้ายจาก "การรับข้อมูล" ไป "ตรรกะส่วนอื่น"

การตรวจสอบที่ดีคือการกันปัญหาตั้งแต่หน้าประตู

## 5. รูปร่างคำตอบข้อผิดพลาด

API ควรตอบข้อผิดพลาดด้วยรูปร่างที่สม่ำเสมอ

เช่น:

```json
{ "message": "Title is required" }
```

หรือ:

```json
{ "message": "Task not found" }
```

ข้อดีคือ:

- ฝั่งหน้าจอ (frontend) เดาได้ง่าย
- หาสาเหตุข้อผิดพลาดได้ง่าย
- อ่านพฤติกรรม (behavior) ของ API ได้ชัด

## 6. ตัวอย่าง

```js
import express from 'express';

const app = express();
app.use(express.json());

const tasks = [];

const validateCreateTask = (req, res, next) => {
  const { title, done } = req.body;

  if (typeof title !== 'string' || title.trim() === '') {
    res.status(400).json({ message: 'Title is required' });
    return;
  }

  if (done !== undefined && typeof done !== 'boolean') {
    res.status(400).json({ message: 'Done must be a boolean' });
    return;
  }

  next();
};

app.post('/tasks', validateCreateTask, (req, res) => {
  const newTask = {
    id: 1,
    title: req.body.title.trim(),
    done: req.body.done ?? false,
  };

  tasks.push(newTask);
  res.status(201).json(newTask);
});
```

## โจทย์ที่ต้องทำ

ให้แก้ไฟล์:

```txt
exercises/ch19-task-validation.js
```

ให้ทำตามนี้:

1. คัดลอก API จาก Ch18 มาเป็นฐาน

2. สร้างตัวกลาง `validateCreateTask`
   - ใช้กับ `POST /tasks`
   - ถ้า `title` ไม่เป็นข้อความ หรือเป็นข้อความว่าง
     - คืน `400`
     - คืน `{ message: 'Title is required' }`

3. สร้างตัวกลาง `validateUpdateTask`
   - ใช้กับ `PUT /tasks/:id`
   - ถ้ามี `title` มาแล้วไม่เป็นข้อความ หรือว่าง
     - คืน `400`
     - คืน `{ message: 'Title must be a non-empty string' }`
   - ถ้ามี `done` มาแล้วไม่เป็นค่าจริงเท็จ
     - คืน `400`
     - คืน `{ message: 'Done must be a boolean' }`

4. เอา `validateCreateTask` ไปใช้กับเส้นทาง `POST /tasks`

5. เอา `validateUpdateTask` ไปใช้กับเส้นทาง `PUT /tasks/:id`

6. ใน `POST /tasks`
   - ใช้ `req.body.title.trim()`
   - ให้ `done` เป็น `false`
   - คืนรหัสสถานะ (status code) `201` พร้อมงานที่สร้างใหม่

   หมายเหตุ: `POST` ต้องคืน `201` (ไม่ใช่ `200`) เพื่อให้รหัสสถานะตรงกับส่วนอื่นของโปรเจกต์ที่ใช้ `201` ตอนสร้างข้อมูลใหม่

7. ใน `PUT /tasks/:id`
   - ถ้ามี `title` ให้อัปเดตด้วย `req.body.title.trim()`
   - ถ้ามี `done` ให้อัปเดตได้ทั้ง `true` และ `false`

8. ให้พฤติกรรมของ `GET`, `DELETE` และ `404` ยังทำงานเหมือน Ch18

## กรณีทดสอบที่คาดหวัง

ตอนทดสอบ ให้ลองกรณีพวกนี้:

- `POST /tasks` พร้อมเนื้อหาคำขอที่ถูกต้อง
- `POST /tasks` โดยไม่มี `title`
- `POST /tasks` โดย `title` เป็น `123`
- `PUT /tasks/1` พร้อม `{ "done": false }`
- `PUT /tasks/1` พร้อม `{ "done": "yes" }`
- `PUT /tasks/1` พร้อม `{ "title": "   " }`

## ข้อควรระวัง

บทนี้ยังเป็นการตรวจสอบแบบทำเองทีละขั้น

จุดประสงค์คือให้เข้าใจ:

- ตัวกลางแทรกตรงไหน
- คำขอถูกกันก่อนถึงเส้นทางอย่างไร
- คำตอบ (response) เมื่อเกิดข้อผิดพลาดควรมีรูปร่างอย่างไร

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch19
```
