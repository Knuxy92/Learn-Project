# ช่วงเชื่อมทดสอบ 02: ทดสอบสถานะของ API

## ทำไมต้องมีช่วงเชื่อมนี้

ก่อนหน้านี้เราทดสอบ (test) ชั้นล่างมาแล้ว:

- การตรวจสอบ (assert) พื้นฐาน
- ฟังก์ชัน (function) ของที่เก็บข้อมูล (storage) ที่อ่านเขียนไฟล์ JSON

บทนี้ค่อยขยับมาที่ API จริง

เป้าหมายของรอบนี้ยังไม่ใช่การทดสอบทุกอย่างของเส้นทาง (route) แต่โฟกัสที่:

- รหัสสถานะ (status code)
- เนื้อหาคำตอบ (response body) พื้นฐาน
- พฤติกรรม (behavior) ตอนสำเร็จ
- พฤติกรรมตอนไม่เจอข้อมูล
- พฤติกรรมตอนคำขอ (request) ผิดรูปแบบ

## เป้าหมาย

ฝึก 4 อย่าง:

1. เปิดแอปสำหรับการทดสอบ
2. ยิงคำขอด้วย `fetch(...)`
3. เช็ก `response.status`
4. ปิดเซิร์ฟเวอร์ (server) หลังการทดสอบจบ

## 1. ทำไมการทดสอบ API ต้องแยกจากการทดสอบที่เก็บข้อมูล

การทดสอบที่เก็บข้อมูลตอบคำถามว่าฟังก์ชันในชั้นข้อมูลทำงานไหม

การทดสอบ API ตอบคำถามเพิ่มอีกว่า:

- เส้นทางถูกผูก (mount) ถูกไหม
- ตัวกลาง (middleware) ที่ทำการตรวจสอบ (validation) ทำงานไหม
- รหัสสถานะถูกไหม
- เนื้อหาคำตอบถูกไหม

สรุป: การทดสอบที่เก็บข้อมูลกับการทดสอบ API คนละชั้น และควรทดสอบแยกกัน

## 2. สิ่งที่ต้องมีในการทดสอบ API

รอบนี้เราจะใช้:

- `app` จาก `exercises/ch21-persistent-task-api/app.js`
- `node:test`
- `node:assert/strict`
- `fetch`

และต้องเปิดเซิร์ฟเวอร์ชั่วคราว เช่น:

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

สรุป: การทดสอบ API ใช้เซิร์ฟเวอร์ชั่วคราว และต้องเก็บกวาด (cleanup) ให้ครบ

## 3. ทำไมยังต้องล้างฐานข้อมูล (database)

ถึงจะทดสอบผ่าน HTTP แต่ข้อมูลปลายทางยังอยู่ในไฟล์ JSON

ถ้าไม่ลบไฟล์ก่อนแต่ละการทดสอบ:

- จำนวนงาน (task) จะค้างจากการทดสอบก่อน
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

`force: true` ทำให้ไม่เกิดข้อผิดพลาด (error) ถ้าไฟล์ยังไม่มี

สรุป: การทดสอบ API ที่ดีต้องควบคุมสถานะข้อมูลให้ได้เหมือนการทดสอบที่เก็บข้อมูล

## 4. พฤติกรรมที่ควรทดสอบ

### `GET /tasks`

- ควรได้ `200`
- เนื้อหาคำตอบควรเป็น array

### `GET /tasks/:id`

- ถ้าไม่เจองานควรได้ `404`

### `POST /tasks`

- ถ้าเนื้อหาคำขอถูก ควรสร้างงานได้
- ถ้าเนื้อหาคำขอผิด เช่น `title` ว่าง ควรได้ `400`

### `DELETE /tasks/:id`

- ถ้าไม่มี id นั้น ควรได้ `404`

สรุป: บทนี้เน้นรหัสสถานะก่อน ยังไม่บังคับทดสอบทุกเส้นทางแบบละเอียด

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

1. นำเข้า (import):
   - `test`, `after`, `beforeEach` จาก `node:test`
   - `assert` จาก `node:assert/strict`
   - `path` จาก `node:path`
   - `rm` จาก `node:fs/promises`

2. กำหนดเส้นทางไฟล์ (path) ของไฟล์ที่เก็บข้อมูลสำหรับการทดสอบ:

```js
const storagePath = path.join(
  import.meta.dirname,
  "storage",
  "test-bridge-tasks.json",
);

process.env.TASKS_FILE_PATH = storagePath;
```

   - ต้องตั้ง `process.env.TASKS_FILE_PATH` ก่อนนำเข้า `app`
   - เพราะ `task-store.js` อ่านสภาพแวดล้อม (environment) ตอนโหลดโมดูล (module)

3. นำเข้า `app` แบบไดนามิก (dynamic) หลังตั้งสภาพแวดล้อมแล้ว:

```js
const { app } = await import("./ch21-persistent-task-api/app.js");
```

4. เขียน `beforeEach(...)` ลบไฟล์ที่เก็บข้อมูล:
   - `await rm(storagePath, { force: true })`

5. เปิดเซิร์ฟเวอร์บนพอร์ต (port) `3002`

6. ใช้ `after(...)` ปิดเซิร์ฟเวอร์ให้เรียบร้อย

7. เขียนการทดสอบ 4 ตัว:
   - `GET /tasks` ควรได้ `200` และเนื้อหาคำตอบเป็น array
   - `GET /tasks/999` ควรได้ `404`
   - `POST /tasks` ด้วยเนื้อหาคำขอไม่ถูก ควรได้ `400`
   - `DELETE /tasks/999` ควรได้ `404`

8. ถ้าจะเพิ่มการทดสอบกรณีสำเร็จอีกตัวก็ได้ เช่น `POST /tasks` แล้วค่อยเช็กว่าได้ออบเจ็กต์ (object) กลับมา

## วิธีรัน

ใช้คำสั่ง:

```bash
node --test exercises/test-bridge-02-api-status-tests.test.js
```

## ผลลัพธ์ที่คาดหวัง

เมื่อรันแล้วควรผ่านครบ 4 ตัว และอธิบายได้ว่า:

- การทดสอบ API ต่างจากการทดสอบที่เก็บข้อมูลยังไง
- ทำไมต้องเปิดและปิดเซิร์ฟเวอร์ในการทดสอบ
- ทำไมสถานะ `400` กับ `404` เป็นคนละกรณี
- ทำไมต้องลบไฟล์ที่เก็บข้อมูลแม้ทดสอบผ่าน HTTP

เสร็จแล้วพิมพ์:

```txt
ตรวจ Test Bridge 02
```
