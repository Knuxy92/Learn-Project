# แผนช่วงเชื่อมทดสอบ

ช่วงนี้เป็นช่วงคั่นก่อนทำงานท้าย เป้าหมายคือฝึกเขียน test แบบใช้งานจริง แต่ไม่ยัดเนื้อหาใหม่เยอะเกินไป

## กติกา

- ใช้แค่ `node:test` และ `node:assert/strict`
- ไม่ใช้ Jest, Vitest หรือ library ใหม่
- แต่ละบทต้องมีโจทย์ชัดเจนและรันได้จริง
- ถ้ามี server ใน test ต้องปิดด้วย `after()`
- ถ้า test เขียนไฟล์ ต้องชี้ไปที่ไฟล์ test และล้างก่อนรัน

## Test Bridge 01 - พื้นฐาน assert

เป้าหมาย:

- เข้าใจ `test(...)`
- เข้าใจ `assert.equal(...)`
- เข้าใจ `assert.deepEqual(...)`
- เข้าใจ `assert.ok(...)`

โจทย์:

- test ค่าพื้นฐาน
- test array
- test object
- test function ง่ายๆ

## Test Bridge 02 - ทดสอบสถานะของ API

เป้าหมาย:

- test HTTP API แบบเปิด server ชั่วคราว
- assert status code
- assert response body
- ปิด server ด้วย `after()`

โจทย์:

- `GET /tasks` ได้ `200`
- `GET /tasks/:id` not found ได้ `404`
- bad body ได้ `400`
- `DELETE /tasks/:id` not found ได้ `404`

## หลังจากนี้

หลังผ่าน 2 ช่วงเชื่อมนี้แล้ว ให้ไปทำงานท้ายที่:

- `Ch23` - Task API ที่ใช้งานได้จริง
