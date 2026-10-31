# บทที่ 23: งานท้าย — Task API ที่ใช้งานได้จริง

## ทบทวน

ตอนนี้เรามีครบทุกชิ้นส่วนแล้ว:

- JavaScript พื้นฐานถึงขั้นกลาง
- Express server และ router
- CRUD API
- middleware ตรวจข้อมูล
- เก็บข้อมูลลงไฟล์ JSON
- เขียน test ด้วย `node:test`

บทนี้คือการประกอบทุกอย่างเข้าด้วยกันเป็นงานชิ้นเดียวที่เอาไปใช้ต่อได้

## 1. เป้าหมายของงานท้าย

ทำ Task API ที่:

- รันได้จริงด้วย `node src/server.js`
- ข้อมูลไม่หายเมื่อปิด server
- ตรวจ input ก่อนบันทึกทุกครั้ง
- มี test ครอบคลุมเส้นทางหลัก
- อ่านโค้ดแล้วรู้ว่าแต่ละไฟล์ทำอะไร

นี่คือระดับที่เอาไปใส่ portfolio ได้ เพราะไม่ใช่แค่ตัวอย่าง แต่เป็นของที่รันได้

## 2. โครงสร้างที่ต้องได้

```txt
exercises/final-task-api/
  server.js
  src/
    app.js
    config.js
    data/
      task-store.js
    middleware/
      validate-task.js
      error-handler.js
    routes/
      task-routes.js
  test/
    api.test.js
  storage/
    .gitkeep
```

เหตุผลที่แยกแบบนี้:

- `server.js` ทำหน้าที่เดียว คือเปิด port
- `src/app.js` ประกอบ app แต่ไม่เปิด port (เพื่อให้ test import ไปใช้ได้)
- `src/config.js` รวมค่าที่มาจาก environment ไว้ที่เดียว
- `data/task-store.js` เป็นที่เดียวที่แตะไฟล์
- `middleware/` เก็บตัวตรวจและตัวจัดการ error
- `routes/` เก็บ route ของ resource
- `test/` แยกจากโค้ดหลัก

## 3. `config.js`

ค่า environment ควรอ่านที่เดียว ไม่กระจายทั้งโปรเจกต์

```js
import path from 'node:path';

const storagePath =
  process.env.TASKS_FILE_PATH ??
  path.join(import.meta.dirname, '..', 'storage', 'tasks.json');

export { storagePath };
```

## 4. `task-store.js`

ชั้นนี้เป็นเจ้าของไฟล์ JSON ทั้งไฟล์ ออกแบบให้ทุกฟังก์ชันเป็น async

```js
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { storagePath } from '../config.js';

const readTasks = async () => {
  try {
    const raw = await readFile(storagePath, 'utf-8');

    return JSON.parse(raw);
  } catch (error) {
    if (error.code === 'ENOENT') return [];

    throw error;
  }
};

const writeTasks = async (tasks) => {
  await mkdir(path.dirname(storagePath), { recursive: true });
  await writeFile(storagePath, JSON.stringify(tasks, null, 2));
};
```

จุดสำคัญ: `ENOENT` คือกรณี "ไฟล์ยังไม่มี" ซึ่งไม่ใช่ error จริงสำหรับเรา

## 5. `error-handler.js`

middleware จัดการ error ต้องมี signature สี่พารามิเตอร์ Express ถึงจะรู้ว่านี่คือ error handler

```js
const errorHandler = (error, req, res, next) => {
  console.error(error);

  res.status(500).json({ message: 'Internal server error' });
};

export { errorHandler };
```

## 6. route ที่ต้องมี

| Method | Path | ผลลัพธ์ |
|---|---|---|
| `GET` | `/tasks` | `200` + array |
| `GET` | `/tasks/:id` | `200` + task หรือ `404` |
| `POST` | `/tasks` | `201` + task ที่สร้าง |
| `PUT` | `/tasks/:id` | `200` + task ที่แก้ หรือ `404` |
| `DELETE` | `/tasks/:id` | `200` + ข้อความ หรือ `404` |

status code ต้องตรงตามนี้ เพราะ test จะเช็กค่านี้

## 7. เรื่องที่ต้องระวัง

- route ที่เป็น async ต้องมี `try/catch` หรือส่งต่อ error ให้ `errorHandler`
- อย่าเปิด port ใน `app.js` เพราะ test จะ import ไปใช้
- อย่าเขียนไฟล์จริงตอน test ให้ชี้ `TASKS_FILE_PATH` ไปที่ไฟล์ test
- `express.json()` ต้องมาก่อน route ที่อ่าน `req.body`

## 8. เกณฑ์ผ่าน

งานนี้ถือว่าผ่านเมื่อ:

1. `node src/server.js` แล้วยิงด้วย `curl` ได้ครบทั้ง 5 route
2. ปิด server แล้วเปิดใหม่ ข้อมูลยังอยู่
3. `node --test test/api.test.js` ผ่านทุกตัว
4. `pnpm lint` ไม่มี error
5. อ่านโครงสร้างแล้วบอกได้ว่าแต่ละไฟล์มีหน้าที่อะไร

## โจทย์ที่ต้องทำ

สร้างโฟลเดอร์:

```txt
exercises/final-task-api/
```

ให้ทำตามนี้:

1. สร้างโครงสร้างไฟล์ตามหัวข้อ 2

2. เขียน `src/config.js` ตามหัวข้อ 3

3. เขียน `src/data/task-store.js` ให้มี:
   - `readTasks()`
   - `writeTasks(tasks)`
   - `findTaskById(id)`
   - `createTask(title)`
   - `updateTask(id, updates)`
   - `deleteTask(id)`

4. เขียน `src/middleware/validate-task.js` ให้มี:
   - `validateCreateTask`
   - `validateUpdateTask`

5. เขียน `src/middleware/error-handler.js`

6. เขียน `src/routes/task-routes.js` ให้ครบ 5 route ตามตาราง

7. เขียน `src/app.js` ที่ประกอบทุกอย่างและ `export { app }`

8. เขียน `server.js` ที่ import `app` แล้ว `listen` ที่ port `3000`

9. เขียน `test/api.test.js` ที่:
   - ตั้ง `process.env.TASKS_FILE_PATH` ไปที่ไฟล์ test
   - `await import('../src/app.js')`
   - ลบไฟล์ test ก่อนทุก test
   - ปิด server ใน `after`
   - test อย่างน้อย 5 เคส ตามตาราง route

## วิธีรัน

รัน server:

```bash
node exercises/final-task-api/server.js
```

ยิงทดสอบด้วย curl:

```bash
curl http://localhost:3000/tasks
curl -X POST http://localhost:3000/tasks -H "Content-Type: application/json" -d '{"title":"งานแรก"}'
```

รัน test:

```bash
node --test exercises/final-task-api/test/api.test.js
```

## ผลลัพธ์ที่คาดหวัง

ทำครบทั้ง 5 เกณฑ์ในหัวข้อ 8

เสร็จแล้วพิมพ์:

```txt
ตรวจ Final Project
```
