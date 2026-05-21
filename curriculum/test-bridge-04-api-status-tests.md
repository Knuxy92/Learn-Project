# Test Bridge 04: API Status Tests

## Why This Bridge Exists

ก่อนหน้านี้เรา test มา 3 ชั้นแล้ว:

- assert พื้นฐาน
- SQLite result
- storage function

บทนี้ค่อยขยับมาที่ API จริง

เป้าหมายของรอบนี้ยังไม่ใช่ test ทุกอย่างของ route แต่โฟกัสที่:

- status code
- response body พื้นฐาน
- behavior ตอน success
- behavior ตอน not found
- behavior ตอน bad request

## Goal

ฝึก 4 อย่าง:

1. เปิด app สำหรับ test
2. ยิง request ด้วย `fetch(...)`
3. เช็ก `response.status`
4. ปิด server หลัง test จบ

## 1. ทำไม API test ต้องแยกจาก storage test

storage test ตอบคำถามว่า function ใน data layer ทำงานไหม

API test ตอบคำถามเพิ่มอีกว่า:

- route ถูก mount ถูกไหม
- middleware validation ทำงานไหม
- status code ถูกไหม
- response body ถูกไหม

สรุป: storage test กับ API test คนละชั้น และควร test แยกกัน

## 2. สิ่งที่ต้องมีใน API test

รอบนี้เราจะใช้:

- `app` จาก `ch24-task-api-sqlite/app.ts`
- `node:test`
- `node:assert/strict`
- `fetch`

และต้องเปิด server ชั่วคราว เช่น:

```ts
const server = app.listen(3002);
```

พอจบแล้วต้องปิด:

```ts
await new Promise<void>((resolve, reject) => {
  server.close((error) => {
    if (error) reject(error);
    else resolve();
  });
});
```

สรุป: API test ใช้ server ชั่วคราว และต้อง cleanup ให้ครบ

## 3. ทำไมยังต้อง reset database

ถึงจะ test ผ่าน HTTP แต่ข้อมูลปลายทางยังอยู่ใน SQLite

ถ้าไม่ reset ก่อนแต่ละ test:

- จำนวน task จะค้างจาก test ก่อน
- id จะไหลต่อ
- ผล `GET`, `POST`, `DELETE` จะเดายาก

รอบนี้ยังใช้ helper เดิม:

```ts
const resetTasksTable = (): void => {
  db.prepare("DELETE FROM tasks").run();
  db.prepare("DELETE FROM sqlite_sequence WHERE name = ?").run("tasks");
};
```

สรุป: API test ที่ดีต้องควบคุม data state ให้ได้เหมือน storage test

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

## Example

```ts
import { test, after } from "node:test";
import assert from "node:assert/strict";
import { app } from "../../exercises/ch24-task-api-sqlite/app";

const server = app.listen(3002);

after(async () => {
  await new Promise<void>((resolve, reject) => {
    server.close((error) => {
      if (error) reject(error);
      else resolve();
    });
  });
});

test("GET /tasks should return 200", async () => {
  const response = await fetch("http://localhost:3002/tasks");

  assert.equal(response.status, 200);
});
```

## งานที่ต้องทำ

แก้ไฟล์:

```txt
exercises/test-bridge-04-api-status-tests.test.ts
```

ให้ทำตามนี้:

1. import:
   - `test` และ `after` จาก `node:test`
   - `assert` จาก `node:assert/strict`
   - `path` จาก `node:path`
   - `DatabaseSync` จาก `node:sqlite`
   - `app` จาก `exercises/ch24-task-api-sqlite/app.ts`

2. สร้าง database connection ไปที่:

```txt
exercises/ch24-storage/tasks.db
```

3. เขียน helper `resetTasksTable()`
   - ลบ rows เก่า
   - reset sequence

4. เปิด server บน port `3002`

5. ใช้ `after(...)` ปิด server ให้เรียบร้อย

6. เขียน test 4 ตัว:
   - `GET /tasks` ควรได้ `200` และ body เป็น array
   - `GET /tasks/999` ควรได้ `404`
   - `POST /tasks` ด้วย body ไม่ถูก ควรได้ `400`
   - `DELETE /tasks/999` ควรได้ `404`

7. ถ้าจะเพิ่ม test success อีกตัวก็ได้ เช่น `POST /tasks` แล้วค่อยเช็กว่าได้ object กลับมา

## Run

ใช้คำสั่ง:

```bash
cmd /c node --test -r ts-node/register exercises/test-bridge-04-api-status-tests.test.ts
```

## Expected Outcome

เมื่อรันแล้วควรผ่าน 4 tests และอธิบายได้ว่า:

- API test ต่างจาก storage test ยังไง
- ทำไมต้องเปิดและปิด server ใน test
- ทำไม status `400` กับ `404` เป็นคนละกรณี
- ทำไมต้อง reset database แม้ test ผ่าน HTTP

เสร็จแล้วพิมพ์:

```txt
ตรวจ Test Bridge 04
```
