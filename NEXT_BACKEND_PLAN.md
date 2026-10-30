# แผน Backend ขั้นต่อไป

## ตำแหน่งปัจจุบัน

ตอนนี้ผ่านแล้ว:

- `Ch17` พื้นฐาน Express
- `Ch18` CRUD API
- `Ch19` validation middleware
- `Ch20` โครงสร้างโปรเจกต์
- `Ch21` เก็บข้อมูลลง JSON file
- `Ch22` ทดสอบ API ด้วย `node:test`

## ทำไมตอนนี้ต้องมี bridge

ช่วง `Ch21-Ch22` มีคำถามจริงที่โผล่มาซ้ำ:

- Promise คืออะไร
- `await` รออะไรอยู่
- ทำไม callback ต้อง wrap ก่อน
- ทำไม `after()` ต้องรอ `server.close()`

ดังนั้นเราไม่ควรกระโดดเข้า database ทันที

## แผนระยะสั้น

1. `Bridge 01` - Promise และลำดับการทำงานของ async
   - เข้าเพราะ async เริ่มเป็นแกนหลักแล้ว
   - ออกเมื่อเข้าใจ promise/callback wrapping/cleanup flow

2. `Ch23` - พื้นฐาน SQLite
   - เรียน schema, table, row, SQL พื้นฐาน

3. `Ch24` - Task API กับ SQLite
   - ย้าย task API จาก JSON file ไป SQLite

4. `Ch25` - query layer และ refactor ชั้น database
   - แยก query/data access ให้สะอาดเหมือน storage layer เดิม

5. `Ch26` - ทดสอบ API กับ database
   - ปรับ test ให้ใช้ DB test data แยกจากของจริง

## สรุปจุดเข้าและจุดออก

### จุดเข้า Bridge 01

เข้าเมื่อ:

- เริ่มใช้ async จริงกับ file, fetch, server, test cleanup
- ยังมีคำถามเรื่อง Promise ซ้ำอยู่

### จุดออก Bridge 01

ออกเมื่อ:

- แยก `Promise<T>` กับ `T` ได้
- อธิบาย `await` ได้
- wrap callback API เป็น Promise ได้
- อ่าน cleanup flow ได้

### กลับเข้าสายหลัก

กลับเข้าสายหลักที่:

- `Ch23` - พื้นฐาน SQLite

## ทำไมต้องเรียงแบบนี้

ถ้าข้าม Promise bridge แล้วไป DB เลย:

- async query flow จะงง
- cleanup ของ DB tests จะงง
- debugging จะช้ากว่าเดิม

ถ้าเก็บ Promise ให้แน่นก่อน:

- database จะง่ายขึ้น
- testing จะนิ่งขึ้น
- code review จะคุยกันด้วยหลักที่ชัดขึ้น
