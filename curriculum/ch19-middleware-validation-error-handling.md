# บทที่ 19: middleware, validation และการจัดการ error

## ทบทวน

บทที่แล้วเราใช้ Express ทำ CRUD API กับข้อมูลใน array ได้แล้ว

ตอนนี้ปัญหาคือ API ของเรายัง "เชื่อ" request มากเกินไป

ตัวอย่างเช่น:

- client อาจไม่ส่ง `title`
- client อาจส่ง `title` เป็นเลข
- client อาจส่ง `done` เป็น string แทน boolean

ดังนั้นบทนี้จะเพิ่ม 3 อย่าง:

- middleware
- validation เบื้องต้น
- error handling ที่สม่ำเสมอขึ้น

## 1. Middleware คืออะไร

middleware คือ function ที่รัน "ก่อน" หรือ "ระหว่าง" route handler

มันมักใช้ทำงานแบบนี้:

- แปลง body
- บันทึก log ของ request
- ตรวจ auth
- ตรวจสอบ input

รูปแบบพื้นฐาน:

```ts
const middleware = (req, res, next) => {
  console.log('Before route');
  next();
};
```

ถ้าเรียก `next()`:

- request จะไหลต่อไป middleware/route ถัดไป

ถ้าไม่เรียก `next()`:

- request จะหยุดตรงนั้น

## 2. Route-Level Middleware

เราไม่จำเป็นต้องใช้ middleware ทั้งแอปเสมอไป

เราสามารถใช้เฉพาะ route บางตัวได้:

```ts
app.post('/tasks', validateTaskBody, (req, res) => {
  res.json({ ok: true });
});
```

ลำดับคือ:

1. request เข้า `validateTaskBody`
2. ถ้าผ่าน ค่อยไป route handler
3. ถ้าไม่ผ่าน middleware สามารถตอบ error ได้เลย

## 3. Validation เบื้องต้น

ในบทนี้เราจะยังไม่ใช้ library ภายนอก

เราจะเช็กแบบง่ายก่อนว่า:

- `title` ต้องเป็น string
- `title` ต้องไม่ว่าง
- `done` ถ้ามี ต้องเป็น boolean

ตัวอย่าง:

```ts
const validateTaskBody = (req, res, next) => {
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

## 4. Why This Matters

ถ้าไม่ validate:

- data ใน array จะ shape เพี้ยน
- route อื่นจะเริ่มพังตาม
- bug จะย้ายจาก "รับ input" ไป "logic ส่วนอื่น"

validation ที่ดีคือกันปัญหาตั้งแต่หน้าประตู

## 5. Error Response Shape

API ควรตอบ error shape ให้สม่ำเสมอ

เช่น:

```json
{ "message": "Title is required" }
```

หรือ:

```json
{ "message": "Task not found" }
```

ข้อดีคือ:

- ฝั่ง frontend เดาได้ง่าย
- debug ง่าย
- API อ่านพฤติกรรมได้ชัด

## 6. ตัวอย่าง

```ts
import express from 'express';

type Task = {
  id: number;
  title: string;
  done: boolean;
};

const app = express();
app.use(express.json());

const tasks: Task[] = [];

const validateTaskBody = (req, res, next) => {
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

app.post('/tasks', validateTaskBody, (req, res) => {
  const newTask: Task = {
    id: 1,
    title: req.body.title.trim(),
    done: req.body.done ?? false,
  };

  tasks.push(newTask);
  res.json(newTask);
});
```

## โจทย์ที่ต้องทำ

ให้แก้ไฟล์:

```txt
exercises/ch19-task-validation.ts
```

ให้ทำตามนี้:

1. คัดลอก API จาก Ch18 มาเป็นฐาน

2. สร้าง middleware `validateCreateTask`
   - ใช้กับ `POST /tasks`
   - ถ้า `title` ไม่เป็น string หรือเป็น string ว่าง
     - คืน `400`
     - คืน `{ message: 'Title is required' }`

3. สร้าง middleware `validateUpdateTask`
   - ใช้กับ `PUT /tasks/:id`
   - ถ้ามี `title` มาแล้วไม่เป็น string หรือว่าง
     - คืน `400`
     - คืน `{ message: 'Title must be a non-empty string' }`
   - ถ้ามี `done` มาแล้วไม่เป็น boolean
     - คืน `400`
     - คืน `{ message: 'Done must be a boolean' }`

4. เอา `validateCreateTask` ไปใช้กับ route `POST /tasks`

5. เอา `validateUpdateTask` ไปใช้กับ route `PUT /tasks/:id`

6. ใน `POST /tasks`
   - ใช้ `req.body.title.trim()`
   - ให้ `done` เป็น `false`

7. ใน `PUT /tasks/:id`
   - ถ้ามี `title` ให้ update ด้วย `req.body.title.trim()`
   - ถ้ามี `done` ให้ update ได้ทั้ง `true` และ `false`

8. ให้ `GET`, `DELETE`, และ `404` behavior เดิมยังทำงานเหมือน Ch18

## Expected Test Cases

ตอนทดสอบ ให้ลองกรณีพวกนี้:

- `POST /tasks` พร้อม body ถูก
- `POST /tasks` โดยไม่มี `title`
- `POST /tasks` โดย `title` เป็น `123`
- `PUT /tasks/1` พร้อม `{ "done": false }`
- `PUT /tasks/1` พร้อม `{ "done": "yes" }`
- `PUT /tasks/1` พร้อม `{ "title": "   " }`

## ข้อควรระวัง

บทนี้ยังเป็น validation แบบ manual

จุดประสงค์คือให้เข้าใจ:

- middleware แทรกตรงไหน
- request ถูกกันก่อนถึง route ยังไง
- error response ควร shape ยังไง

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch19
```
