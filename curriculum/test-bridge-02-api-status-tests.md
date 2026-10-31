# ช่วงเชื่อมทดสอบ 02: ทดสอบสถานะของ API

## ทำไมต้องมีช่วงเชื่อมนี้

ก่อนหน้านี้เรา test ชั้นล่างมาแล้ว:

- assert พื้นฐาน
- storage function ที่อ่านเขียนไฟล์ JSON

บทนี้ค่อยขยับมาที่ API จริง

เป้าหมายของรอบนี้ยังไม่ใช่ test ทุกอย่างของ route แต่โฟกัสที่:

- status code
- response body พื้นฐาน
- behavior ตอนสำเร็จ
- behavior ตอนไม่เจอข้อมูล
- behavior ตอน request ผิดรูปแบบ

## เป้าหมาย

ฝึก 4 อย่าง:

1. เปิด app สำหรับ test
2. ยิง request ด้วย `fetch(...)`
3. เช็ก `response.status`
4. ปิด server หลัง test จบ

## 1. ทำไม API test ต้องแยกจาก storage test

storage test ตอบคำถามว่า function ในชั้นข้อมูลทำงานไหม

API test ตอบคำถามเพิ่มอีกว่า:

- route ถูก mount ถูกไหม
- middleware validation ทำงานไหม
- status code ถูกไหม
- response body ถูกไหม

สรุป: storage test กับ API test คนละชั้น และควร test แยกกัน

## 2. สิ่งที่ต้องมีใน API test

รอบนี้เราจะใช้:

- `app` จาก `exercises/ch21-persistent-task-api/app.js`
- `node:test`
- `node:assert/strict`
- `fetch`

และต้องเปิด server ชั่วคราว เช่น:

```js
const server = app.listen(3002);
```

พอจบแล้วต้องปิด:

```js
await new Promise((resolve, reject) => {
  server.close((error) => {
    if (error) reject(error);
    else resolve();
  });
});
```

สรุป: API test ใช้ server ชั่วคราว และต้อง cleanup ให้ครบ

## 3. ทำไมยังต้อง reset database

ถึงจะ test ผ่าน HTTP แต่ข้อมูลปลายทางยังอยู่ในไฟล์ JSON

ถ้าไม่ลบไฟล์ก่อนแต่ละ test:

- จำนวน task จะค้างจาก test ก่อน
- id จะไหลต่อ
- ผล `GET`, `POST`, `DELETE` จะเดายาก

รอบนี้ใช้ `beforeEach` ลบไฟล์ทิ้ง:

```js
import { beforeEach } from "node:test";
import { rm } from "node:fs/promises";

beforeEach(async () => {
  await rm(storagePath, { force: true });
});
```

`force: true` ทำให้ไม่ error ถ้าไฟล์ยังไม่มี

สรุป: API test ที่ดีต้องควบคุมสถานะข้อมูลให้ได้เหมือน storage test

## 4. พฤติกรรมที่ควร test

### `GET /tasks`

- ควรได้ `200`
- body ควรเป็น array

### `GET /tasks/:id`

- ถ้าไม่เจอ task ควรได้ `404`

### `POST /tasks`

- ถ้า body ถูก ควรสร้าง task ได้
- ถ้า body ผิด เช่น `title` ว่าง ควรได้ `400`

### `DELETE /tasks/:id`

- ถ้าไม่มี id นั้น ควรได้ `404`

สรุป: บทนี้เน้น status code ก่อน ยังไม่บังคับ test ทุก route แบบละเอียด

## ตัวอย่าง

```js
import { test, after, beforeEach } from "node:test";
import assert from "node:assert/strict";
import path from "node:path";
import { rm } from "node:fs/promises";

const storagePath = path.join(
  import.meta.dirname,
  "storage",
  "test-bridge-tasks.json",
);

process.env.TASKS_FILE_PATH = storagePath;

const { app } = await import("./ch21-persistent-task-api/app.js");

const server = app.listen(3002);
const baseUrl = "http://localhost:3002";

beforeEach(async () => {
  await rm(storagePath, { force: true });
});

after(async () => {
  await new Promise((resolve, reject) => {
    server.close((error) => {
      if (error) reject(error);
      else resolve();
    });
  });
});

test("GET /tasks should return 200", async () => {
  const response = await fetch(`${baseUrl}/tasks`);

  assert.equal(response.status, 200);
});
```

## งานที่ต้องทำ

แก้ไฟล์:

```txt
exercises/test-bridge-02-api-status-tests.test.js
```

ให้ทำตามนี้:

1. import:
   - `test`, `after`, `beforeEach` จาก `node:test`
   - `assert` จาก `node:assert/strict`
   - `path` จาก `node:path`
   - `rm` จาก `node:fs/promises`

2. กำหนด path ของไฟล์ storage สำหรับ test:

```js
const storagePath = path.join(
  import.meta.dirname,
  "storage",
  "test-bridge-tasks.json",
);

process.env.TASKS_FILE_PATH = storagePath;
```

   - ต้องตั้ง `process.env.TASKS_FILE_PATH` ก่อน import `app`
   - เพราะ `task-store.js` อ่าน env ตอนโหลด module

3. import `app` แบบ dynamic หลังตั้ง env แล้ว:

```js
const { app } = await import("./ch21-persistent-task-api/app.js");
```

4. เขียน `beforeEach(...)` ลบไฟล์ storage:
   - `await rm(storagePath, { force: true })`

5. เปิด server บน port `3002`

6. ใช้ `after(...)` ปิด server ให้เรียบร้อย

7. เขียน test 4 ตัว:
   - `GET /tasks` ควรได้ `200` และ body เป็น array
   - `GET /tasks/999` ควรได้ `404`
   - `POST /tasks` ด้วย body ไม่ถูก ควรได้ `400`
   - `DELETE /tasks/999` ควรได้ `404`

8. ถ้าจะเพิ่ม test กรณีสำเร็จอีกตัวก็ได้ เช่น `POST /tasks` แล้วค่อยเช็กว่าได้ object กลับมา

## วิธีรัน

ใช้คำสั่ง:

```bash
node --test exercises/test-bridge-02-api-status-tests.test.js
```

## ผลลัพธ์ที่คาดหวัง

เมื่อรันแล้วควรผ่าน 4 tests และอธิบายได้ว่า:

- API test ต่างจาก storage test ยังไง
- ทำไมต้องเปิดและปิด server ใน test
- ทำไม status `400` กับ `404` เป็นคนละกรณี
- ทำไมต้องลบไฟล์ storage แม้ test ผ่าน HTTP

เสร็จแล้วพิมพ์:

```txt
ตรวจ Test Bridge 02
```
