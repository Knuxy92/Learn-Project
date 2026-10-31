# บทที่ 15: Node.js built-in modules

## ทบทวน

บทที่แล้วเราเรียนการแยกค่าออกจากโครงสร้าง การกระจายค่า และการเก็บค่าที่เหลือ

บทนี้เราจะรู้จักโมดูล (module) ที่ Node.js ให้มาใช้เลยโดยไม่ต้องติดตั้งอะไรเพิ่ม

## 1. Node.js ให้อะไรมาบ้าง

Node.js มีโมดูลที่มีมาให้ (built-in module) หลายตัวที่ฝั่งเซิร์ฟเวอร์ (backend) ใช้เป็นประจำ:

- `node:fs/promises` อ่านเขียนไฟล์
- `node:path` จัดการเส้นทางไฟล์ (path)
- `node:http` สร้างเซิร์ฟเวอร์ (server) ดิบ
- `node:url` จัดการ URL
- `node:crypto` สร้างรหัส (id) หรือค่าแฮช (hash)

เราไม่ต้อง `npm install` เพราะมันมากับ Node เอง

## 2. `node:path`

`path` ช่วยต่อเส้นทางไฟล์ให้ถูกต้องในทุกระบบปฏิบัติการ เราไม่ควรต่อข้อความ (string) เอง

```js
import path from 'node:path';

const filePath = path.join('data', 'tasks.json');

console.log(filePath);
console.log(path.basename(filePath));
console.log(path.dirname(filePath));
```

ผลลัพธ์:

```txt
data/tasks.json
tasks.json
data
```

## 3. `node:fs/promises`

`fs/promises` ใช้ทำงานกับไฟล์แบบอะซิงค์ (async)

```js
import { writeFile, readFile } from 'node:fs/promises';

const run = async () => {
  await writeFile('note.txt', 'hello');

  const content = await readFile('note.txt', 'utf-8');
  console.log(content);
};

run();
```

ผลลัพธ์:

```txt
hello
```

ต้องใส่ `'utf-8'` ตอนอ่าน ไม่อย่างนั้นจะได้ `Buffer` ไม่ใช่ข้อความ

## 4. ตรวจว่าไฟล์มีอยู่จริง

```js
import { access } from 'node:fs/promises';

const exists = async (filePath) => {
  try {
    await access(filePath);
    return true;
  } catch {
    return false;
  }
};
```

เราใช้ `try/catch` เพราะ `access` โยนข้อผิดพลาด (throw error) เมื่อไฟล์ไม่มี

## 5. `import.meta.dirname`

เวลาเปิดไฟล์ด้วยเส้นทางไฟล์แบบสัมพัทธ์ มันอ้างจากโฟลเดอร์ที่เรารันคำสั่ง ไม่ใช่ที่อยู่ไฟล์

ถ้าอยากได้เส้นทางไฟล์ของไฟล์ที่กำลังรันอยู่ ให้ใช้ `import.meta.dirname`

```js
import path from 'node:path';

const dataPath = path.join(import.meta.dirname, 'data', 'tasks.json');

console.log(dataPath);
```

วิธีนี้ทำให้รันจากโฟลเดอร์ไหนก็ได้ผลเหมือนกัน

## 6. `node:crypto` สำหรับ id

```js
import { randomUUID } from 'node:crypto';

console.log(randomUUID());
```

ผลลัพธ์ (ค่าจะเปลี่ยนทุกครั้ง):

```txt
9f1c2b7a-3d4e-4f5a-8b6c-1d2e3f4a5b6c
```

## 7. ตัวอย่าง: อ่านและเขียน JSON ด้วย built-in modules

```js
import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';

const filePath = path.join(import.meta.dirname, 'tasks.json');

const readTasks = async () => {
  const raw = await readFile(filePath, 'utf-8');

  return JSON.parse(raw);
};

const writeTasks = async (tasks) => {
  await writeFile(filePath, JSON.stringify(tasks, null, 2));
};

const run = async () => {
  await writeTasks([{ id: 1, title: 'Learn Node', done: false }]);
  console.log(await readTasks());
};

run();
```

## โจทย์ที่ต้องทำ

สร้างไฟล์:

```txt
exercises/ch15-node-modules.js
```

ให้ทำตามนี้:

1. นำเข้า (import) `readFile`, `writeFile` จาก `node:fs/promises` และ `path` จาก `node:path`

2. สร้างเส้นทางไฟล์ของไฟล์ `exercises/ch15-data/note.json` โดยใช้ `import.meta.dirname` และ `path.join`

3. เขียนฟังก์ชัน (function) `saveNote(text)`
   - สร้างออบเจ็กต์ (object) `{ text, savedAt }` โดย `savedAt` เป็น `new Date().toISOString()`
   - เขียนลงไฟล์เป็น JSON

4. เขียนฟังก์ชัน `loadNote()`
   - อ่านไฟล์และ `JSON.parse`
   - คืนออบเจ็กต์ที่ได้

5. เขียนฟังก์ชัน `noteExists()`
   - ใช้ `access` ตรวจว่าไฟล์มีอยู่
   - คืน `true` หรือ `false`

6. ใน `run()`:
   - ตรวจ `noteExists()` ก่อน
   - ถ้าไม่มี ให้ `saveNote('first note')`
   - แล้ว `loadNote()` และพิมพ์ `text`

## วิธีรัน

```bash
node exercises/ch15-node-modules.js
```

## ผลลัพธ์ที่คาดหวัง

รันครั้งแรกเห็น `first note` และมีไฟล์ `exercises/ch15-data/note.json` เกิดขึ้น

เสร็จแล้วพิมพ์:

```txt
ตรวจ Ch15
```
