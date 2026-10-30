# ช่วงเชื่อม 04: SQL error กับ not found

## ทำไมต้องมีช่วงเชื่อมนี้

หลัง `Bridge 03` ตอนนี้รู้แล้วว่า:

- `.all()` คืน array
- `.get()` คืน row เดียวหรือ `undefined`
- `.run()` คืน result object

แต่ยังมีความเข้าใจอีกชั้นที่สำคัญสำหรับ backend:

- query รันได้ แต่ไม่เจอ row
- query พังจริง เพราะ SQL หรือ schema ผิด

สองกรณีนี้ไม่เหมือนกัน

ถ้าไม่แยกให้ชัด ผู้เรียนจะเริ่มมองทุกปัญหาใน database ว่าเป็น error ทั้งหมด ซึ่งทำให้ route logic และ HTTP status code ผิดตั้งแต่ต้น

## จุดเข้า

เราเข้า bridge นี้หลังจาก:

- จบ `Bridge 03 - SQLite Driver Return Values`
- รู้แล้วว่า `.get()` อาจคืน `undefined`
- พร้อมแปลความหมายของผลลัพธ์แต่ละแบบ

## จุดออก

ออกจาก bridge นี้ได้เมื่อทำได้ครบ:

1. อธิบายได้ว่า `undefined` จาก `.get()` ไม่ใช่ SQL error
2. อธิบายได้ว่า `[]` จาก `.all()` ไม่ใช่ SQL error
3. อธิบายได้ว่า SQL throw คือคนละเรื่องกับ not found
4. แยกได้ว่า backend ควรตอบ `404` ตอนไหน
5. แยกได้ว่า backend ควรตอบ `500` ตอนไหน

## กลับเข้าสายหลัก

หลังจบ bridge นี้ เราจะไปต่อที่:

- `Input Validation Before Database Queries`

เหตุผลคือเมื่อแยก not found กับ SQL error ได้แล้ว ขั้นถัดไปคือกัน bad input ตั้งแต่ก่อน query จะถูกรัน

## เป้าหมายหลัก

bridge นี้เน้น 4 เรื่อง:

1. not found
2. empty list
3. SQL error
4. ความหมายฝั่ง backend

## 1. Not Found Is Normal

กรณีนี้ query ถูกต้อง แต่ไม่มี row ที่ตรงเงื่อนไข

```ts
const row = db
  .prepare("SELECT id, title, done FROM tasks WHERE id = ?")
  .get(id);
```

ถ้า `id` นั้นไม่มีอยู่จริง:

- query ยังรันสำเร็จ
- database ไม่ได้พัง
- จะได้ `undefined`

นี่คือ not found ไม่ใช่ SQL error

## 2. Empty List Is Also Normal

กรณีอ่านหลาย rows:

```ts
const rows = db
  .prepare("SELECT id, title, done FROM tasks ORDER BY id DESC")
  .all();
```

ถ้า table ว่าง:

- query ยังรันสำเร็จ
- database ไม่ได้พัง
- จะได้ `[]`

นี่คือ empty result ไม่ใช่ SQL error

## 3. SQL Error Means the Query Failed

กรณีนี้ query เองมีปัญหา หรือ schema ไม่ตรงกับที่ query ต้องการ

ตัวอย่าง:

```ts
const row = db
  .prepare("SELECT id, title, done FROM wrong_table WHERE id = ?")
  .get(1);
```

อันนี้จะ throw เพราะ table `wrong_table` ไม่มีอยู่จริง

ตัวอย่าง SQL error ที่พบบ่อย:

- table name ผิด
- column name ผิด
- SQL syntax ผิด
- query ใช้ schema ที่ไม่มีอยู่จริง
- placeholder กับค่าที่ส่งเข้าไปไม่สัมพันธ์กับ query

## 4. Backend Meaning

backend ต้องแปลผลลัพธ์ให้ถูก ไม่ใช่แค่ดูว่า "มีค่า" หรือ "ไม่มีค่า"

### `.get()` returns `undefined`

แปลว่า:

- หา row ไม่เจอ
- ปกติ
- เหมาะกับ `404 Not Found`

### `.all()` returns `[]`

แปลว่า:

- ไม่มีรายการ
- ปกติ
- เหมาะกับ `200 OK` พร้อม array ว่าง

### SQL throws

แปลว่า:

- query/database มีปัญหา
- ไม่ใช่ not found
- เหมาะกับ `500 Internal Server Error`

## ตัวอย่าง

```ts
import path from "node:path";
import { DatabaseSync } from "node:sqlite";

const dbPath = path.join(__dirname, "../bridge-04-storage/example.db");
const db = new DatabaseSync(dbPath);

db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL DEFAULT 0
  )
`);

db.prepare("DELETE FROM tasks").run();
db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run("Study Errors", 0);

const foundTask = db
  .prepare("SELECT id, title, done FROM tasks WHERE id = ?")
  .get(1);

const missingTask = db
  .prepare("SELECT id, title, done FROM tasks WHERE id = ?")
  .get(9999);

const emptyRows = db
  .prepare("SELECT id, title, done FROM tasks WHERE done = ?")
  .all(1);

try {
  const brokenQuery = db
    .prepare("SELECT id, title, done FROM wrong_table WHERE id = ?")
    .get(1);

  console.log(brokenQuery);
} catch (error) {
  console.log("sql error happened");
}

console.log("foundTask:", foundTask);
console.log("missingTask:", missingTask);
console.log("emptyRows:", emptyRows);
```

## งานที่ต้องทำ

แก้ไฟล์:

```txt
exercises/bridge-04-sql-error-vs-not-found.ts
```

ให้ทำตามนี้:

1. ทำการ import:
   - `path` จาก `node:path`
   - `DatabaseSync` จาก `node:sqlite`

2. สร้าง database file ที่:

```txt
exercises/bridge-04-storage/tasks.db
```

3. ใช้ `.exec()` สร้าง table `tasks`
   - `id INTEGER PRIMARY KEY AUTOINCREMENT`
   - `title TEXT NOT NULL`
   - `done INTEGER NOT NULL DEFAULT 0`

4. เคลียร์ rows เก่าออกก่อนเริ่ม

5. insert task 2 ตัว
   - 1 ตัว `done = 0`
   - 1 ตัว `done = 1`

6. ใช้ `.get()` หา task ที่มีอยู่จริง
   - เก็บไว้ใน `foundTask`

7. ใช้ `.get()` หา task ที่ไม่มีจริง เช่น `9999`
   - เก็บไว้ใน `missingTask`

8. ใช้ `.all()` หา tasks ที่ไม่มีผลลัพธ์
   - เช่นหา `done = 2`
   - เก็บไว้ใน `emptyRows`

9. ใช้ `try/catch` ทดลอง query ที่พังจริง
   - ใช้ table name ผิด เช่น `wrong_table`
   - ถ้า error เกิด ให้เก็บ string `"sql error"` ไว้ในตัวแปร `queryStatus`

10. พิมพ์ผลออกมา 4 อย่าง
    - `foundTask`
    - `missingTask`
    - `emptyRows`
    - `queryStatus`

11. ตอบใน comment สั้นๆ ในไฟล์
    - ทำไม `missingTask` ไม่ใช่ SQL error
    - ทำไม `emptyRows` ไม่ใช่ SQL error
    - SQL throw ต่างจาก not found ยังไง
    - backend ควรคิดถึง `404` กับ `500` ต่างกันยังไง

## ผลลัพธ์ที่คาดหวัง

หลังทำเสร็จ นายควรอธิบายได้ว่า:

- `undefined` จาก `.get()` คือ not found
- `[]` จาก `.all()` คือ empty result
- SQL throw คือ query/database ที่ล้มเหลว
- backend ไม่ควรตอบ status เดียวกันให้ทุกกรณี

เสร็จแล้วพิมพ์:

```txt
ตรวจ Bridge 04
```
