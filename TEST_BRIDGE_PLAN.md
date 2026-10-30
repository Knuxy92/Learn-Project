# Test Bridge Plan

ช่วงนี้เป็นช่วงคั่นก่อนกลับไปต่อ SQL/backend หลัก เป้าหมายคือฝึกเขียน test แบบใช้งานจริง แต่ไม่ยัดเนื้อหาใหม่เยอะเกินไป

## กติกา

- ใช้แค่ `node:test` และ `node:assert/strict`
- ยังไม่ใช้ Jest, Vitest หรือ library ใหม่
- แต่ละบทต้องมีโจทย์ชัดเจนและรันได้จริง
- ถ้ามี server ใน test ต้องปิดด้วย `after()`
- ถ้ามี database/file test ต้องแยก data ออกจากของจริง

## Test Bridge 01 - Assert Basics

เป้าหมาย:

- เข้าใจ `test(...)`
- เข้าใจ `assert.equal(...)`
- เข้าใจ `assert.deepEqual(...)`
- เข้าใจ `assert.ok(...)`

โจทย์:

- test ค่าพื้นฐาน
- test กับ array
- test กับ object
- test function ง่ายๆ

## Test Bridge 02 - SQLite Result Tests

เป้าหมาย:

- test ผลลัพธ์ของ `.all()`
- test ผลลัพธ์ของ `.get()`
- test ค่า `lastInsertRowid`
- test ค่า `changes`

โจทย์:

- สร้าง test database
- ใส่ seed data
- assert ผลลัพธ์ของ query
- reset database ก่อน test

## Test Bridge 03 - Storage Function Tests

เป้าหมาย:

- test function ชั้น data แบบไม่เปิด server
- ฝึกแยก setup/query/assert
- ฝึก not found case

โจทย์:

- สร้าง function เช่น `createTask`, `findTaskById`, `deleteTask`
- test เคสสำเร็จ
- test เคส not found
- test กรณี `changes === 0`

## Test Bridge 04 - API Status Tests

เป้าหมาย:

- test HTTP API แบบเปิด server ชั่วคราว
- assert ค่า status code
- assert ค่า response body
- ปิด server ด้วย `after()`

โจทย์:

- `GET /tasks` ได้ `200`
- `GET /tasks/:id` not found ได้ `404`
- bad body ได้ `400`
- broken/internal case ค่อยเรียนหลังจากเข้า error flow ชัดขึ้น

## หลังจากนี้

หลังผ่าน 3-4 test bridges แล้วค่อยกลับไปต่อเส้นหลักที่วางไว้:

- ตรวจ input ก่อนยิง query ลง database
- map ผลลัพธ์เป็น HTTP response
- แก้ revision ของ `Ch24` ที่ใช้ SQLite

