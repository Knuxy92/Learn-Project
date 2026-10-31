# บทที่ 18: ออกแบบ REST API และ CRUD

## ทบทวน

บทที่แล้วเราเริ่มเปิดเซิร์ฟเวอร์ (server) Express และสร้างเส้นทาง (route) แบบ `GET` ง่าย ๆ ได้แล้ว

บทนี้เราจะขยับจาก "เซิร์ฟเวอร์ตอบข้อความ" ไปเป็น "API จัดการข้อมูล" แบบพื้นฐาน

เป้าหมายของบทนี้คือ:

- เข้าใจคำว่า CRUD
- ใช้เมธอด (method) HTTP หลัก ๆ
- รับ `req.params` และ `req.body`
- แก้ไขข้อมูลใน array ชั่วคราวแบบเก็บไว้ในหน่วยความจำ

## 1. CRUD คืออะไร

CRUD คือ 4 งานพื้นฐานของระบบข้อมูล:

- `Create` = สร้างข้อมูลใหม่
- `Read` = อ่านข้อมูล
- `Update` = แก้ข้อมูล
- `Delete` = ลบข้อมูล

ในโลกของ API มักจับคู่กับเมธอด HTTP แบบนี้:

- `GET` -> อ่านข้อมูล
- `POST` -> สร้างข้อมูล
- `PUT` -> แก้ไขข้อมูล
- `DELETE` -> ลบข้อมูล

## 2. รูปแบบเส้นทางแบบ REST

ตัวอย่างเส้นทางที่ใช้บ่อย:

```txt
GET /tasks
GET /tasks/:id
POST /tasks
PUT /tasks/:id
DELETE /tasks/:id
```

ความหมาย:

- `GET /tasks` = ขอรายการ (item) ทั้งหมด
- `GET /tasks/:id` = ขอรายการเดียว
- `POST /tasks` = สร้างรายการใหม่
- `PUT /tasks/:id` = แก้รายการเดิม
- `DELETE /tasks/:id` = ลบรายการเดิม

## 3. `req.params`

`req.params` ใช้อ่านค่าจากเส้นทางใน URL

```js
app.get('/tasks/:id', (req, res) => {
  console.log(req.params.id);
});
```

ถ้าเรียก:

```txt
/tasks/2
```

ค่า `req.params.id` จะเป็นข้อความ (string) `'2'`

เพราะฉะนั้นถ้าจะเอาไปเทียบกับ number เรามักแปลงก่อน:

```js
const taskId = Number(req.params.id);
```

## 4. `req.body`

`req.body` ใช้อ่านข้อมูลที่ฝั่งผู้เรียก (client) ส่งมาในเนื้อหาคำขอ (body)

แต่ก่อนใช้ ต้องเปิดตัวกลาง (middleware) นี้ก่อน:

```js
app.use(express.json());
```

ตัวอย่าง:

```js
app.post('/tasks', (req, res) => {
  console.log(req.body);
});
```

ถ้าฝั่งผู้เรียกส่ง:

```json
{ "title": "Learn Express" }
```

เราจะอ่าน `req.body.title` ได้

## 5. ข้อมูลในหน่วยความจำ

ในบทนี้เรายังไม่ใช้ฐานข้อมูล (database)

เราจะเก็บข้อมูลไว้ใน array ชั่วคราว โดยแต่ละงาน (task) เป็นออบเจ็กต์ (object) ที่มี `id`, `title`, `done` แบบนี้:

```js
const tasks = [
  { id: 1, title: 'Learn Express', done: false },
  { id: 2, title: 'Build CRUD API', done: false },
];
```

ข้อสำคัญ:

- ข้อมูลแบบนี้จะหายเมื่อปิดเซิร์ฟเวอร์
- แต่เหมาะมากสำหรับฝึกลำดับการทำงานของ API ก่อนเข้าใช้ฐานข้อมูลจริง

## 6. ตัวอย่าง

```js
import express from 'express';

const app = express();
app.use(express.json());

const tasks = [
  { id: 1, title: 'Learn Express', done: false },
  { id: 2, title: 'Build CRUD API', done: true },
];

app.get('/tasks', (req, res) => {
  res.json(tasks);
});

app.get('/tasks/:id', (req, res) => {
  const taskId = Number(req.params.id);
  const task = tasks.find((item) => item.id === taskId);

  if (!task) {
    res.status(404).json({ message: 'Task not found' });
    return;
  }

  res.json(task);
});
```

## โจทย์ที่ต้องทำ

ให้แก้ไฟล์:

```txt
exercises/ch18-task-api.js
```

ให้ทำตามนี้:

1. กำหนดรูปร่างของงานแต่ละรายการเป็นออบเจ็กต์ที่มี
   - `id` เป็น number
   - `title` เป็นข้อความ
   - `done` เป็นค่าจริงเท็จ (boolean)

   ตัวอย่าง:

```js
const task = { id: 1, title: 'Learn Express', done: false };
```

2. สร้าง array `tasks` เริ่มต้นอย่างน้อย 2 งาน

3. เปิดใช้:

```js
app.use(express.json());
```

4. สร้างเส้นทาง `GET /tasks`
   - คืนงานทั้งหมด

5. สร้างเส้นทาง `GET /tasks/:id`
   - หางานตาม id
   - ถ้าไม่เจอ ให้คืนรหัสสถานะ (status code) `404`
   - คำตอบ (response) เป็น:

```json
{ "message": "Task not found" }
```

6. สร้างเส้นทาง `POST /tasks`
   - รับ `title` จาก `req.body`
   - สร้างงานใหม่
   - ให้ `id` เป็นเลขถัดไป
   - ให้ `done` เริ่มต้นเป็น `false`
   - คืนงานที่สร้างใหม่

7. สร้างเส้นทาง `PUT /tasks/:id`
   - หางานตาม id
   - ถ้าไม่เจอ คืน `404`
   - ถ้าเจอ ให้อัปเดต `title` และ `done` จาก `req.body`
   - คืนงานที่อัปเดตแล้ว

8. สร้างเส้นทาง `DELETE /tasks/:id`
   - หางานตาม id
   - ถ้าไม่เจอ คืน `404`
   - ถ้าเจอ ให้ลบงานนั้นออกจาก array
   - คืน:

```json
{ "message": "Task deleted" }
```

9. ให้เซิร์ฟเวอร์เริ่มรับฟังที่พอร์ต (port) `3000`

## ลำดับการฝึกที่คาดหวัง

ตอนทดสอบ ให้ลองแบบนี้:

- `GET /tasks`
- `GET /tasks/1`
- `GET /tasks/999`
- `POST /tasks`
- `PUT /tasks/1`
- `DELETE /tasks/1`

## ข้อควรระวัง

บทนี้ยังไม่เน้นการตรวจสอบ (validation) ลึก

ดังนั้นเรา "สมมุติ" ไปก่อนว่าเนื้อหาคำขอที่ส่งมามีรูปร่างถูกต้อง

แต่ JavaScript ไม่มีตัวตรวจชนิดข้อมูลมาช่วยเตือนตอนรัน เลยต้องตรวจ `typeof` เองถ้าสงสัยว่าค่าที่ได้มาเป็นชนิดที่ต้องการจริง

เช่น `req.body.title` อาจไม่ใช่ข้อความถ้าฝั่งผู้เรียกส่งมาแปลก ๆ

เรื่องตรวจข้อมูลจริงจังจะไปอยู่ในบทถัดไป

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch18
```
