# Chapter 21: JSON File Persistence

## Recap

ตอนนี้ API ของนายมี:

- โครงสร้างหลายไฟล์
- CRUD
- middleware
- validation

ครบแล้ว

ปัญหาที่ยังเหลือคือข้อมูลยังอยู่แค่ใน memory

ผลคือ:

- สร้าง task ใหม่ได้
- ลบ task ได้
- แก้ task ได้
- แต่พอปิด server แล้วข้อมูลหายหมด

บทนี้จะเพิ่ม persistence แบบง่ายที่สุดก่อน:

- อ่านข้อมูลจากไฟล์ JSON
- เขียนข้อมูลกลับลงไฟล์ JSON

## 1. Why JSON Persistence

ก่อนจะไป database จริง เราควรเห็นปัญหานี้ก่อน:

- state ใน array ใช้ง่าย
- แต่ไม่ถาวร

JSON file เป็น step กลางที่ดี เพราะ:

- ไม่ต้องลง database
- เห็น flow ของ read/write ชัด
- เข้าใจคำว่า persistence แบบจับต้องได้

## 2. `fs/promises`

ใน Node.js เราใช้ `fs/promises` เพื่ออ่านและเขียนไฟล์แบบ async ได้

```ts
import { readFile, writeFile } from 'node:fs/promises';
```

ตัวอย่าง:

```ts
const raw = await readFile('tasks.json', 'utf-8');
const tasks = JSON.parse(raw);

await writeFile('tasks.json', JSON.stringify(tasks, null, 2));
```

## 3. Read and Parse

ไฟล์ JSON เป็น text

ดังนั้น flow คือ:

1. อ่าน text จากไฟล์
2. parse ด้วย `JSON.parse(...)`
3. ได้ array/object กลับมา

```ts
const raw = await readFile(filePath, 'utf-8');
const tasks = JSON.parse(raw);
```

## 4. Save Back to File

ตอนเขียนกลับ:

1. แปลง object/array เป็น text ด้วย `JSON.stringify(...)`
2. เขียนทับลงไฟล์

```ts
await writeFile(filePath, JSON.stringify(tasks, null, 2));
```

`null, 2` ทำให้ไฟล์อ่านง่ายขึ้น

## 5. A Small Storage Layer

แทนที่จะให้ route ไปแตะไฟล์ตรง ๆ เราควรมี layer กลาง

เช่น:

- `readTasks()`
- `writeTasks(tasks)`
- `getTaskById(id)`
- `createTask(title)`
- `updateTask(...)`
- `deleteTask(id)`

ข้อดีคือ:

- route สั้นลง
- logic เรื่องไฟล์ถูกรวมไว้ที่เดียว
- วันหลังย้ายไป database ง่ายขึ้น

## 6. Example

```ts
import { readFile, writeFile } from 'node:fs/promises';

const filePath = './storage/tasks.json';

const readTasks = async () => {
  const raw = await readFile(filePath, 'utf-8');
  return JSON.parse(raw);
};

const writeTasks = async (tasks: unknown) => {
  await writeFile(filePath, JSON.stringify(tasks, null, 2));
};
```

## 7. Important Constraint

บทนี้ยังไม่เน้นเรื่อง:

- concurrent writes
- file locking
- race condition
- database transactions

เราจะสมมุติว่า request มาไม่ซ้อนกันหนัก

เป้าหมายคือเข้าใจ persistence flow ก่อน

## Guided Exercise

ให้แก้ไฟล์ในโฟลเดอร์:

```txt
exercises/ch21-persistent-task-api/
```

ให้ทำตามนี้:

1. ใน `types/task.ts`
   - สร้าง `type Task`

2. ใน `storage/tasks.json`
   - ให้มี task เริ่มต้นอย่างน้อย 2 ตัว

3. ใน `data/task-store.ts`
   - สร้างและ export functions:
     - `readTasks()`
     - `writeTasks(tasks)`
     - `findTaskById(id)`
     - `createTask(title)`
     - `updateTask(id, updates)`
     - `deleteTask(id)`

4. ใน `middleware/validate-task.ts`
   - ย้าย validation จาก Ch20 มาใช้ต่อ

5. ใน `routes/task-routes.ts`
   - เปลี่ยน CRUD routes ให้เรียกผ่าน storage functions แทนการแตะ array ตรง ๆ

6. ใน `app.ts`
   - ใช้ `express.json()`
   - mount `taskRouter` ที่ `/tasks`

7. ใน `server.ts`
   - เปิด server ที่ port `3000`

## Expected Behavior

หลังทำเสร็จ:

- `POST /tasks` แล้วข้อมูลควรถูกเขียนลง `tasks.json`
- `PUT /tasks/:id` แล้วไฟล์ควรถูกอัปเดต
- `DELETE /tasks/:id` แล้วไฟล์ควรถูกอัปเดต
- ปิดแล้วเปิด server ใหม่ ข้อมูลล่าสุดยังอยู่

## Important Note

ถ้า route เปลี่ยนเป็น async แล้ว ต้องระวังเรื่อง `await`

เช่น:

```ts
taskRouter.get('/', async (req, res) => {
  const tasks = await readTasks();
  res.json(tasks);
});
```

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch21
```
