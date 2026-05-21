# Next Backend Plan

## Current Position

ตอนนี้ผ่านแล้ว:

- `Ch17` Express basics
- `Ch18` CRUD API
- `Ch19` validation middleware
- `Ch20` project structure
- `Ch21` JSON file persistence
- `Ch22` API testing with `node:test`

## Why There Is a Bridge Now

ช่วง `Ch21-Ch22` มีคำถามจริงที่โผล่มาซ้ำ:

- Promise คืออะไร
- `await` รออะไรอยู่
- ทำไม callback ต้อง wrap ก่อน
- ทำไม `after()` ต้องรอ `server.close()`

ดังนั้นเราไม่ควรกระโดดเข้า database ทันที

## Short-Term Plan

1. `Bridge 01 - Promises and Async Flow`
   - เข้าเพราะ async เริ่มเป็นแกนหลักแล้ว
   - ออกเมื่อเข้าใจ promise/callback wrapping/cleanup flow

2. `Ch23 - SQLite Basics`
   - เรียน schema, table, row, SQL พื้นฐาน

3. `Ch24 - Task API with SQLite`
   - ย้าย task API จาก JSON file ไป SQLite

4. `Ch25 - Query Layer and DB Refactor`
   - แยก query/data access ให้สะอาดเหมือน storage layer เดิม

5. `Ch26 - API Testing with Database`
   - ปรับ test ให้ใช้ DB test data แบบแยกจากของจริง

## Entry / Exit Summary

### Enter Bridge 01

เข้าเมื่อ:

- เริ่มใช้ async จริงกับ file, fetch, server, test cleanup
- ยังมีคำถามเรื่อง Promise ซ้ำอยู่

### Exit Bridge 01

ออกเมื่อ:

- แยก `Promise<T>` กับ `T` ได้
- อธิบาย `await` ได้
- wrap callback API เป็น Promise ได้
- อ่าน cleanup flow ได้

### Return to Main Line

กลับเข้าสายหลักที่:

- `Ch23 - SQLite Basics`

## Why This Order

ถ้าข้าม Promise bridge แล้วไป DB เลย:

- async query flow จะงง
- cleanup ของ DB tests จะงง
- debugging จะช้ากว่าเดิม

ถ้าเก็บ Promise ให้แน่นก่อน:

- database จะง่ายขึ้น
- testing จะนิ่งขึ้น
- code review จะคุยกันด้วยหลักที่ชัดขึ้น
