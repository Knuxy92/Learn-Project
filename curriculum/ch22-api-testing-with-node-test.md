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

```ts
import test from "node:test";
import assert from "node:assert/strict";

test("1 + 1 should equal 2", () => {
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

```ts
const response = await fetch("http://localhost:3002/tasks");
const data = await response.json();
```

แล้วค่อย assert:

```ts
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

```ts
const filePath = "...";
```

เราจะเปิดทางให้ใช้:

```ts
const filePath =
  process.env.TASKS_FILE_PATH ??
  path.join(__dirname, "../storage/tasks.json");
```

ข้อดีคือ:

- ตอนใช้งานจริงอ่านไฟล์เดิม
- ตอน test ชี้ไปไฟล์ทดสอบได้

## 6. Test Lifecycle

test ที่ดีควร:

- เตรียมข้อมูลก่อนรัน
- เปิด server
- ยิง request
- ตรวจสอบผลด้วย assert
- ปิด server
- restore ไฟล์ทดสอบกลับ

## 7. ตัวอย่าง

```ts
import test from "node:test";
import assert from "node:assert/strict";

test("GET /tasks should return an array", async () => {
  const response = await fetch("http://localhost:3002/tasks");
  const data = await response.json();

  assert.equal(response.status, 200);
  assert.ok(Array.isArray(data));
});
```

## โจทย์ที่ต้องทำ

ให้แก้ไฟล์ในโฟลเดอร์:

```txt
exercises/ch22-api-tests/
```

ให้ทำตามนี้:

1. ใน `fixtures/test-tasks.json`
   - ใส่ task เริ่มต้นอย่างน้อย 2 ตัว

2. ปรับ `exercises/ch21-persistent-task-api/data/task-store.ts`
   - ให้รองรับ `process.env.TASKS_FILE_PATH`
   - ถ้าไม่มี env นี้ ให้ fallback ไปไฟล์เดิม

3. ใน `api.test.ts`
   - ใช้ `node:test`
   - ใช้ `node:assert/strict`
   - import `app` จาก Ch21

4. ก่อนรัน test
   - ตั้ง `process.env.TASKS_FILE_PATH` ให้ชี้ไป `fixtures/test-tasks.json`
   - backup ข้อมูลเดิมในไฟล์ test

5. เขียน test อย่างน้อย 4 ตัว:
   - `GET /tasks` ควรได้ `200` และเป็น array
   - `POST /tasks` ควรสร้าง task ใหม่ได้
   - `PUT /tasks/999` ควรได้ `404`
   - `DELETE /tasks/999` ควรได้ `404`

6. หลังจบ test
   - restore ไฟล์ `fixtures/test-tasks.json` กลับค่าเดิม
   - ปิด server ที่เปิดใน test

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
