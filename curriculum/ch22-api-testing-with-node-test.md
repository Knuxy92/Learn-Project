# บทที่ 22: ทดสอบ API ด้วย `node:test`

## ทบทวน

ตอนนี้เรามี API ที่:

- แยกไฟล์เป็นระบบ
- มีการตรวจสอบ (validation)
- เขียนข้อมูลลงไฟล์ได้
- รีสตาร์ต (restart) แล้วข้อมูลยังอยู่

ปัญหาถัดไปคือทุกครั้งที่แก้โค้ด เราต้องคอย:

- เปิดเซิร์ฟเวอร์ (server)
- ยิงคำขอ (request) เอง
- เช็กคำตอบ (response) เอง

ซึ่งช้าและพลาดง่าย

บทนี้จะเพิ่ม "การทดสอบอัตโนมัติ" ให้ API

## 1. ทำไมการทดสอบจึงสำคัญ

การทดสอบ (test) ช่วยตอบคำถาม 3 อย่าง:

- โค้ดยังทำงานเหมือนเดิมไหม
- ตอนปรับโครงสร้าง (refactor) พังตรงไหนหรือเปล่า
- ข้อกำหนด (requirement) ที่สำคัญถูกล็อกไว้หรือยัง

กับ API สิ่งที่เรามักอยากทดสอบคือ:

- รหัสสถานะ (status code)
- เนื้อหาคำตอบ
- พฤติกรรม (behavior) ตอนสำเร็จ
- พฤติกรรมตอนเกิดข้อผิดพลาด (error)

## 2. `node:test`

Node.js มีตัวรันการทดสอบในตัวชื่อ `node:test`

เราไม่ต้องลง Jest ก่อนก็เริ่มเขียนการทดสอบได้

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

## 3. ทดสอบ HTTP API

แนวคิดคือ:

1. เปิดแอปบนพอร์ต (port) ชั่วคราว
2. ใช้ `fetch(...)` ยิงคำขอ
3. เช็กรหัสสถานะและเนื้อหา
4. ปิดเซิร์ฟเวอร์หลังจบการทดสอบ

ตัวอย่าง:

```js
const server = app.listen(3001);
const baseUrl = 'http://localhost:3001';

const response = await fetch(`${baseUrl}/tasks`);
const data = await response.json();
```

แล้วค่อยตรวจสอบ (assert):

```js
assert.equal(response.status, 200);
assert.ok(Array.isArray(data));
```

## 4. แยกข้อมูลสำหรับการทดสอบ

เวลาทดสอบ API ที่เขียนลงไฟล์จริง ต้องระวัง:

- การทดสอบไปลบข้อมูลจริง
- การทดสอบไปรบกวนงานรอบอื่น

ดังนั้นบทนี้จะให้แยก `storage/test-tasks.json` สำหรับการทดสอบ

และใช้ตัวแปรสภาพแวดล้อม (environment variable) เพื่อบอกแอปว่าจะอ่านไฟล์ไหน

## 5. เส้นทางไฟล์ที่เก็บข้อมูลตามสภาพแวดล้อม

แทนที่จะเขียนเส้นทางไฟล์ (path) ตายตัวเดียว:

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

`import.meta.dirname` คือโฟลเดอร์ของไฟล์ที่กำลังรันอยู่ ซึ่งใน ESM ใช้แทนตัวแปรส่วนกลางแบบเก่าได้เลย

ข้อดีคือ:

- ตอนใช้งานจริงอ่านไฟล์เดิม
- ตอนทดสอบชี้ไปไฟล์ทดสอบได้

## 6. วงจรชีวิตของการทดสอบ

การทดสอบที่ดีควร:

- ตั้ง `process.env.TASKS_FILE_PATH` ก่อนนำเข้า (import) แอป
- นำเข้าแอปแบบไดนามิก
- เปิดเซิร์ฟเวอร์
- ลบไฟล์ทดสอบก่อนทุกการทดสอบ
- ยิงคำขอ
- ตรวจสอบผลลัพธ์
- ปิดเซิร์ฟเวอร์ใน `after`

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

ทำไมต้องใช้การนำเข้าแบบไดนามิก:

`import` แบบคงที่ถูกยกขึ้นไปทำงานก่อนคำสั่งอื่นทั้งหมดในไฟล์

ถ้าเราเขียน `import { app } ...` ไว้บนสุด แล้วค่อยตั้ง `process.env.TASKS_FILE_PATH` ข้างล่าง แอปจะถูกโหลดก่อนที่ตัวแปรสภาพแวดล้อมจะถูกตั้ง

ผลคือ `task-store.js` อ่านเส้นทางไฟล์ตอนนำเข้า และได้ค่าเริ่มต้น (default) ไปแล้ว

`await import(...)` เป็นนิพจน์ (expression) ที่ทำงานตามลำดับ จึงต้องวางไว้หลังบรรทัดที่ตั้งตัวแปรสภาพแวดล้อม

ส่วน `beforeEach` ที่ลบไฟล์ด้วย `rm(path, { force: true })` ทำให้ทุกการทดสอบเริ่มจากข้อมูลว่าง

`force: true` หมายความว่าถ้าไฟล์ยังไม่มีก็ไม่ต้องเกิดข้อผิดพลาด

## โจทย์ที่ต้องทำ

ให้แก้ไฟล์ในโฟลเดอร์:

```txt
exercises/ch22-api-tests/
```

ให้ทำตามนี้:

1. ปรับ `exercises/ch21-persistent-task-api/data/task-store.js`
   - ให้รองรับ `process.env.TASKS_FILE_PATH`
   - ถ้าไม่มีตัวแปรสภาพแวดล้อมนี้ ให้ถอยไปใช้ (fallback) ไฟล์เดิม
   - สร้างเส้นทางไฟล์ด้วย `import.meta.dirname`

2. ใน `exercises/ch22-api-tests/api.test.js`
   - ใช้ `node:test`
   - ใช้ `node:assert/strict`
   - ตั้ง `process.env.TASKS_FILE_PATH` ให้ชี้ไป `storage/test-tasks.json` ก่อนนำเข้า
   - นำเข้า `app` จากบทที่ 21 ด้วย `const { app } = await import('../ch21-persistent-task-api/app.js');`

3. ใช้ `beforeEach` ลบไฟล์ `storage/test-tasks.json` ด้วย `rm(storagePath, { force: true })`
   - เพื่อให้ทุกการทดสอบเริ่มจากข้อมูลว่าง

4. เขียนการทดสอบอย่างน้อย 4 ตัว:
   - `GET /tasks` ควรได้ `200` และเป็น array
   - `POST /tasks` ควรสร้างงาน (task) ใหม่ได้
   - `PUT /tasks/999` ควรได้ `404`
   - `DELETE /tasks/999` ควรได้ `404`

5. ใช้ `after` ปิดเซิร์ฟเวอร์ที่เปิดในการทดสอบ

รันด้วย:

```bash
node --test exercises/ch22-api-tests/api.test.js
```

## ข้อควรระวัง

บทนี้ไม่ได้วัดว่าการทดสอบต้องสวยที่สุด

แต่วัดว่า:

- รันการทดสอบได้
- ไม่ใช้ข้อมูลจริงปนกับการทดสอบ
- ตรวจสอบพฤติกรรมสำคัญของ API ได้

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch22
```
