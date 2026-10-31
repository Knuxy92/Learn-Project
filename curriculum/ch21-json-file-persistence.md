# บทที่ 21: เก็บข้อมูลด้วยไฟล์ JSON

## ทบทวน

ตอนนี้ API ของเรามี:

- โครงสร้างหลายไฟล์
- CRUD
- ตัวกลาง (middleware)
- การตรวจสอบ (validation)

ครบแล้ว

ปัญหาที่ยังเหลือคือข้อมูลยังอยู่แค่ในหน่วยความจำ (memory)

ผลคือ:

- สร้างงาน (task) ใหม่ได้
- ลบงานได้
- แก้งานได้
- แต่พอปิดเซิร์ฟเวอร์ (server) แล้วข้อมูลหายหมด

บทนี้จะเพิ่มความคงอยู่ของข้อมูล (persistence) แบบง่ายที่สุดก่อน:

- อ่านข้อมูลจากไฟล์ JSON
- เขียนข้อมูลกลับลงไฟล์ JSON

## 1. ทำไมต้องเก็บข้อมูลลงไฟล์ JSON

ก่อนจะไปฐานข้อมูล (database) จริง เราควรเห็นปัญหานี้ก่อน:

- สถานะ (state) ใน array ใช้ง่าย
- แต่ไม่ถาวร

ไฟล์ JSON เป็นขั้นกลางที่ดี เพราะ:

- ไม่ต้องลงฐานข้อมูล
- เห็นลำดับการอ่าน/เขียนชัด
- เข้าใจคำว่าความคงอยู่ของข้อมูลแบบจับต้องได้

## 2. `fs/promises`

ใน Node.js เราใช้ `fs/promises` เพื่ออ่านและเขียนไฟล์แบบอะซิงค์ (async) ได้

```js
import { readFile, writeFile } from 'node:fs/promises';
```

ตัวอย่าง:

```js
const raw = await readFile('tasks.json', 'utf-8');
const tasks = JSON.parse(raw);

await writeFile('tasks.json', JSON.stringify(tasks, null, 2));
```

## 3. อ่านและแปลงข้อความ

ไฟล์ JSON เป็นข้อความ (text)

ดังนั้นลำดับการทำงานคือ:

1. อ่านข้อความจากไฟล์
2. แปลงข้อความ (parse) ด้วย `JSON.parse(...)`
3. ได้ array หรือออบเจ็กต์ (object) กลับมา

```js
const raw = await readFile(filePath, 'utf-8');
const tasks = JSON.parse(raw);
```

## 4. เขียนกลับลงไฟล์

ตอนเขียนกลับ:

1. แปลงออบเจ็กต์/array เป็นข้อความด้วย `JSON.stringify(...)`
2. เขียนทับลงไฟล์

```js
await writeFile(filePath, JSON.stringify(tasks, null, 2));
```

`null, 2` ทำให้ไฟล์อ่านง่ายขึ้น

## 5. ชั้นที่เก็บข้อมูลขนาดเล็ก

แทนที่จะให้เส้นทาง (route) ไปแตะไฟล์ตรง ๆ เราควรมีชั้นกลาง

เช่น:

- `readTasks()`
- `writeTasks(tasks)`
- `getTaskById(id)`
- `createTask(title)`
- `updateTask(...)`
- `deleteTask(id)`

ข้อดีคือ:

- เส้นทางสั้นลง
- ตรรกะ (logic) เรื่องไฟล์ถูกรวมไว้ที่เดียว
- วันหลังย้ายไปฐานข้อมูลง่ายขึ้น

## 6. ตัวอย่าง

```js
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';

const filePath =
  process.env.TASKS_FILE_PATH ??
  path.join(import.meta.dirname, '..', 'storage', 'tasks.json');

const readTasks = async () => {
  try {
    const raw = await readFile(filePath, 'utf-8');

    return JSON.parse(raw);
  } catch (error) {
    if (error.code === 'ENOENT') return [];

    throw error;
  }
};

const writeTasks = async (tasks) => {
  await mkdir(path.dirname(filePath), { recursive: true });
  await writeFile(filePath, JSON.stringify(tasks, null, 2));
};
```

## 7. ข้อจำกัดที่สำคัญ

บทนี้ยังไม่เน้นเรื่อง:

- การเขียนพร้อมกัน
- การล็อกไฟล์
- สภาวะแข่งกัน (race condition)
- ทรานแซกชัน (transaction) ของฐานข้อมูล

เราจะสมมุติว่าคำขอ (request) มาไม่ซ้อนกันหนัก

เป้าหมายคือเข้าใจลำดับการทำงานของความคงอยู่ของข้อมูลก่อน

## โจทย์ที่ต้องทำ

ให้แก้ไฟล์ในโฟลเดอร์:

```txt
exercises/ch21-persistent-task-api/
```

ให้ทำตามนี้:

1. ใน `storage/tasks.json`
   - ให้มีงานเริ่มต้นอย่างน้อย 2 ตัว

2. ใน `data/task-store.js`
   - สร้างและส่งออก (export) ฟังก์ชัน (function):
     - `readTasks()`
     - `writeTasks(tasks)`
     - `findTaskById(id)`
     - `createTask(title)`
     - `updateTask(id, updates)`
     - `deleteTask(id)`

3. ใน `middleware/validate-task.js`
   - ย้ายการตรวจสอบจากบทที่ 20 มาใช้ต่อ

4. ใน `routes/task-routes.js`
   - เปลี่ยนเส้นทาง CRUD ให้เรียกผ่านฟังก์ชันของที่เก็บข้อมูล แทนการแตะ array ตรง ๆ

5. ใน `app.js`
   - ใช้ `express.json()`
   - ผูก `taskRouter` ที่ `/tasks`

6. ใน `server.js`
   - เปิดเซิร์ฟเวอร์ที่พอร์ต (port) `3000`

## พฤติกรรมที่คาดหวัง

หลังทำเสร็จ:

- `POST /tasks` แล้วข้อมูลควรถูกเขียนลง `tasks.json`
- `PUT /tasks/:id` แล้วไฟล์ควรถูกอัปเดต
- `DELETE /tasks/:id` แล้วไฟล์ควรถูกอัปเดต
- ปิดแล้วเปิดเซิร์ฟเวอร์ใหม่ ข้อมูลล่าสุดยังอยู่

## ข้อควรระวัง

ถ้าเส้นทางเปลี่ยนเป็นอะซิงค์แล้ว ต้องระวังเรื่อง `await`

เช่น:

```js
taskRouter.get('/', async (req, res) => {
  const tasks = await readTasks();
  res.json(tasks);
});
```

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch21
```
