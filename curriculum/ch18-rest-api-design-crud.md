# Chapter 18: REST API Design & CRUD

## Recap

บทที่แล้วเราเริ่มเปิด Express server และสร้าง route แบบ `GET` ง่าย ๆ ได้แล้ว

บทนี้เราจะขยับจาก "server ตอบข้อความ" ไปเป็น "API จัดการข้อมูล" แบบพื้นฐาน

เป้าหมายของบทนี้คือ:

- เข้าใจคำว่า CRUD
- ใช้ HTTP methods หลัก ๆ
- รับ `req.params` และ `req.body`
- แก้ไขข้อมูลใน array ชั่วคราวแบบ in-memory

## 1. CRUD คืออะไร

CRUD คือ 4 งานพื้นฐานของระบบข้อมูล:

- `Create` = สร้างข้อมูลใหม่
- `Read` = อ่านข้อมูล
- `Update` = แก้ข้อมูล
- `Delete` = ลบข้อมูล

ในโลก API มัก map กับ HTTP methods แบบนี้:

- `GET` -> Read
- `POST` -> Create
- `PUT` -> Update
- `DELETE` -> Delete

## 2. REST Route Shape

ตัวอย่าง route ที่ใช้บ่อย:

```txt
GET /tasks
GET /tasks/:id
POST /tasks
PUT /tasks/:id
DELETE /tasks/:id
```

ความหมาย:

- `GET /tasks` = ขอรายการทั้งหมด
- `GET /tasks/:id` = ขอ item ชิ้นเดียว
- `POST /tasks` = สร้าง item ใหม่
- `PUT /tasks/:id` = แก้ item เดิม
- `DELETE /tasks/:id` = ลบ item เดิม

## 3. `req.params`

`req.params` ใช้อ่านค่าจาก URL path

```ts
app.get('/tasks/:id', (req, res) => {
  console.log(req.params.id);
});
```

ถ้าเรียก:

```txt
/tasks/2
```

ค่า `req.params.id` จะเป็น string `'2'`

เพราะงั้นถ้าจะเอาไปเทียบกับเลข เรามักแปลงก่อน:

```ts
const taskId = Number(req.params.id);
```

## 4. `req.body`

`req.body` ใช้อ่านข้อมูลที่ client ส่งมาใน request body

แต่ก่อนใช้ ต้องเปิด middleware นี้ก่อน:

```ts
app.use(express.json());
```

ตัวอย่าง:

```ts
app.post('/tasks', (req, res) => {
  console.log(req.body);
});
```

ถ้า client ส่ง:

```json
{ "title": "Learn Express" }
```

เราจะอ่าน `req.body.title` ได้

## 5. In-Memory Data

ในบทนี้เรายังไม่ใช้ database

เราจะเก็บข้อมูลไว้ใน array ชั่วคราวแบบนี้:

```ts
type Task = {
  id: number;
  title: string;
  done: boolean;
};

const tasks: Task[] = [
  { id: 1, title: 'Learn Express', done: false },
  { id: 2, title: 'Build CRUD API', done: false },
];
```

ข้อสำคัญ:

- ข้อมูลแบบนี้จะหายเมื่อปิด server
- แต่เหมาะมากสำหรับฝึก flow ของ API ก่อนเข้า database จริง

## 6. Example

```ts
import express from 'express';

type Task = {
  id: number;
  title: string;
  done: boolean;
};

const app = express();
app.use(express.json());

const tasks: Task[] = [
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

## Guided Exercise

ให้แก้ไฟล์:

```txt
exercises/ch18-task-api.ts
```

ให้ทำตามนี้:

1. สร้าง `type Task`
   - `id: number`
   - `title: string`
   - `done: boolean`

2. สร้าง array `tasks` เริ่มต้นอย่างน้อย 2 งาน

3. เปิดใช้:

```ts
app.use(express.json());
```

4. สร้าง route `GET /tasks`
   - คืน task ทั้งหมด

5. สร้าง route `GET /tasks/:id`
   - หา task ตาม id
   - ถ้าไม่เจอ ให้คืน status `404`
   - response เป็น:

```json
{ "message": "Task not found" }
```

6. สร้าง route `POST /tasks`
   - รับ `title` จาก `req.body`
   - สร้าง task ใหม่
   - ให้ `id` เป็นเลขถัดไป
   - ให้ `done` เริ่มต้นเป็น `false`
   - คืน task ที่สร้างใหม่

7. สร้าง route `PUT /tasks/:id`
   - หา task ตาม id
   - ถ้าไม่เจอ คืน `404`
   - ถ้าเจอ ให้อัปเดต `title` และ `done` จาก `req.body`
   - คืน task ที่อัปเดตแล้ว

8. สร้าง route `DELETE /tasks/:id`
   - หา task ตาม id
   - ถ้าไม่เจอ คืน `404`
   - ถ้าเจอ ให้ลบ task นั้นออกจาก array
   - คืน:

```json
{ "message": "Task deleted" }
```

9. ให้ server listen ที่ port `3000`

## Expected Practice Flow

ตอนทดสอบ ให้ลองแบบนี้:

- `GET /tasks`
- `GET /tasks/1`
- `GET /tasks/999`
- `POST /tasks`
- `PUT /tasks/1`
- `DELETE /tasks/1`

## Important Note

บทนี้ยังไม่เน้น validation ลึก

ดังนั้นเรา "สมมุติ" ไปก่อนว่า body ที่ส่งมามี shape ถูกต้อง

เรื่องตรวจข้อมูลจริงจังจะไปอยู่ในบทถัดไป

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch18
```
