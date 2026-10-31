# บทที่ 22: ทดสอบ API ด้วย `node:test`

## ทบทวน

ตอนนี้นายมี API ที่:

- แยกไฟล์เป็นระบบ
- มี validation
- เขียนข้อมูลลงไฟล์ได้
- restart แล้วข้อมูลยังอยู่

ปัญหาถัดไปคือทุกครั้งที่แก้โค้ด เราต้องคอย:

- เปิด server
- ยิง request เอง
- เช็ก response เอง

ซึ่งช้าและพลาดง่าย

บทนี้จะเพิ่ม "การทดสอบอัตโนมัติ" ให้ API

## 1. Why Testing Matters

test ช่วยตอบคำถาม 3 อย่าง:

- โค้ดยังทำงานเหมือนเดิมไหม
- ตอน refactor พังตรงไหนหรือเปล่า
- requirement ที่สำคัญถูกล็อกไว้หรือยัง

กับ API สิ่งที่เรามักอยาก test คือ:

- status code
- body ของ response
- behavior ตอน success
- behavior ตอน error

## 2. `node:test`

Node.js มี test runner ในตัวชื่อ `node:test`

เราไม่ต้องลง Jest ก่อนก็เริ่มเขียน test ได้

ตัวอย่าง:

```js
import test from 'node:test';
import assert from 'node:assert/strict';

test('1 + 1 should equal 2', () => {
  assert.equal(1 + 1, 2);
});
```

รันด้วย:

```bash
node --test
```

## 3. Testing HTTP APIs

แนวคิดคือ:

1. เปิด app บน port ชั่วคราว
2. ใช้ `fetch(...)` ยิง request
3. เช็ก status และ body
4. ปิด server หลังจบ test

ตัวอย่าง:

```js
const server = app.listen(3001);
const baseUrl = 'http://localhost:3001';

const response = await fetch(`${baseUrl}/tasks`);
const data = await response.json();
```

แล้วค่อย assert:

```js
assert.equal(response.status, 200);
assert.ok(Array.isArray(data));
```

## 4. Isolate Test Data

เวลา test API ที่เขียนลงไฟล์จริง ต้องระวัง:

- test ไปลบข้อมูลจริง
- test ไปรบกวนงานรอบอื่น

ดังนั้นบทนี้จะให้แยก `storage/test-tasks.json` สำหรับ test

และใช้ environment variable เพื่อบอก app ว่าจะอ่านไฟล์ไหน

## 5. Environment-Based Storage Path

แทนที่จะ hardcode path เดียว:

```js
const filePath = '...';
```

เราจะเปิดทางให้ใช้:

```js
import path from 'node:path';

const filePath =
  process.env.TASKS_FILE_PATH ??
  path.join(import.meta.dirname, '..', 'storage', 'tasks.json');
```

`import.meta.dirname` คือโฟลเดอร์ของไฟล์ที่กำลังรันอยู่ ซึ่งใน ESM ใช้แทนตัวแปร global แบบเก่าได้เลย

ข้อดีคือ:

- ตอนใช้งานจริงอ่านไฟล์เดิม
- ตอน test ชี้ไปไฟล์ทดสอบได้

## 6. Test Lifecycle

test ที่ดีควร:

- ตั้ง `process.env.TASKS_FILE_PATH` ก่อน import app
- import app ด้วย dynamic import
- เปิด server
- ลบไฟล์ทดสอบก่อนทุก test
- ยิง request
- ตรวจสอบผลด้วย assert
- ปิด server ใน `after`

## 7. ตัวอย่าง

```js
import { after, beforeEach, test } from 'node:test';
import assert from 'node:assert/strict';
import { rm } from 'node:fs/promises';
import path from 'node:path';

const storagePath = path.join(import.meta.dirname, 'storage', 'test-tasks.json');
process.env.TASKS_FILE_PATH = storagePath;

const { app } = await import('../ch21-persistent-task-api/app.js');

const server = app.listen(3001);
const baseUrl = 'http://localhost:3001';

beforeEach(async () => {
  await rm(storagePath, { force: true });
});

after(async () => {
  await rm(storagePath, { force: true });

  await new Promise((resolve, reject) => {
    server.close((error) => {
      if (error) reject(error);
      else resolve();
    });
  });
});

test('GET /tasks should return 200 and an array', async () => {
  const response = await fetch(`${baseUrl}/tasks`);
  const data = await response.json();

  assert.equal(response.status, 200);
  assert.ok(Array.isArray(data));
});
```

ทำไมต้องใช้ dynamic import:

static `import` ถูก hoist ขึ้นไปทำงานก่อน statement อื่นทั้งหมดในไฟล์

ถ้าเราเขียน `import { app } ...` ไว้บนสุด แล้วค่อยตั้ง `process.env.TASKS_FILE_PATH` ข้างล่าง app จะถูกโหลดก่อนที่ env จะถูกตั้ง

ผลคือ `task-store.js` อ่าน path ตอน import และได้ค่า default ไปแล้ว

`await import(...)` เป็น expression ที่ทำงานตามลำดับ จึงต้องวางไว้หลังบรรทัดที่ตั้ง env

ส่วน `beforeEach` ที่ลบไฟล์ด้วย `rm(path, { force: true })` ทำให้ทุก test เริ่มจากข้อมูลว่าง

`force: true` หมายความว่าถ้าไฟล์ยังไม่มีก็ไม่ต้อง error

## โจทย์ที่ต้องทำ

ให้แก้ไฟล์ในโฟลเดอร์:

```txt
exercises/ch22-api-tests/
```

ให้ทำตามนี้:

1. ปรับ `exercises/ch21-persistent-task-api/data/task-store.js`
   - ให้รองรับ `process.env.TASKS_FILE_PATH`
   - ถ้าไม่มี env นี้ ให้ fallback ไปไฟล์เดิม
   - สร้าง path ด้วย `import.meta.dirname`

2. ใน `exercises/ch22-api-tests/api.test.js`
   - ใช้ `node:test`
   - ใช้ `node:assert/strict`
   - ตั้ง `process.env.TASKS_FILE_PATH` ให้ชี้ไป `storage/test-tasks.json` ก่อน import
   - import `app` จาก Ch21 ด้วย `const { app } = await import('../ch21-persistent-task-api/app.js');`

3. ใช้ `beforeEach` ลบไฟล์ `storage/test-tasks.json` ด้วย `rm(storagePath, { force: true })`
   - เพื่อให้ทุก test เริ่มจากข้อมูลว่าง

4. เขียน test อย่างน้อย 4 ตัว:
   - `GET /tasks` ควรได้ `200` และเป็น array
   - `POST /tasks` ควรสร้าง task ใหม่ได้
   - `PUT /tasks/999` ควรได้ `404`
   - `DELETE /tasks/999` ควรได้ `404`

5. ใช้ `after` ปิด server ที่เปิดใน test

รันด้วย:

```bash
node --test exercises/ch22-api-tests/api.test.js
```

## ข้อควรระวัง

บทนี้ไม่ได้วัดว่า test ต้องสวยที่สุด

แต่วัดว่า:

- รัน test ได้
- ไม่ใช้ข้อมูลจริงปนกับ test
- assert behavior สำคัญของ API ได้

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch22
```
