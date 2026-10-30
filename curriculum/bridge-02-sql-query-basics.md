# ช่วงเชื่อม 02: พื้นฐาน SQL query

## ทำไมต้องมีช่วงเชื่อมนี้

หลัง `Ch24` เห็นแล้วว่าแค่รู้ SQLite แบบผิวๆ ยังไม่พอสำหรับอ่านและแก้ backend code จริง

จุดที่ยังสับสนอยู่ไม่ใช่แค่ syntax แต่เป็นการตัดสินใจว่า:

- query แบบไหนควรใช้ในสถานการณ์ไหน
- `SELECT *` ใช้ได้ไหม
- ทำไมบาง query ต้องมี `WHERE`
- ทำไมบาง API ควรใส่ `ORDER BY`

ดังนั้น bridge นี้จะหยุดจากการแก้ API ชั่วคราว แล้วกลับมาทำพื้นฐาน query ให้แน่นก่อน

## จุดเข้า

เราเข้า bridge นี้หลังจาก:

- ผ่าน `Ch23` และ `Ch24`
- เริ่มใช้ SQLite จริงแล้ว
- แต่ยังรู้สึกว่า query ถูกเขียนตาม pattern มากกว่าตามความเข้าใจ

## จุดออก

ออกจาก bridge นี้ได้เมื่อทำได้ครบ:

1. อธิบายได้ว่า `SELECT`, `INSERT`, `UPDATE`, `DELETE` ต่างกันยังไง
2. อธิบายได้ว่า `WHERE id = ?` ใช้กรอง row ยังไง
3. แยกได้ว่าเมื่อไร `SELECT *` พอใช้ได้ และเมื่อไรควรเขียนชื่อ column ชัดๆ
4. ใช้ `ORDER BY id ASC` และ `ORDER BY id DESC` ได้
5. อ่าน SQL แล้วบอกได้ว่า query นั้นกำลัง "อ่าน", "สร้าง", "แก้", หรือ "ลบ" ข้อมูล

## กลับเข้าสายหลัก

หลังจบ bridge นี้ เราจะไปต่อที่:

- `SQL Bridge 03 - SQLite Driver Return Values`

เหตุผลคือพอพื้นฐาน query แน่นแล้ว ค่อยผูกเข้ากับ `.all()`, `.get()`, `.run()`, `.exec()` จะเข้าใจง่ายกว่า

## เป้าหมายหลัก

bridge นี้เน้น 4 เรื่อง:

1. คำสั่ง SQL แบบ CRUD
2. `WHERE` และ placeholder `?`
3. `SELECT *` กับ column ที่ระบุชัดเจน
4. `ORDER BY`

## 1. Four Core SQL Commands

### `SELECT`

ใช้ "อ่าน" ข้อมูล

```sql
SELECT id, title, done FROM tasks;
```

### `INSERT`

ใช้ "สร้าง" ข้อมูลใหม่

```sql
INSERT INTO tasks (title, done) VALUES (?, ?);
```

### `UPDATE`

ใช้ "แก้" ข้อมูลเดิม

```sql
UPDATE tasks
SET title = ?, done = ?
WHERE id = ?;
```

### `DELETE`

ใช้ "ลบ" ข้อมูล

```sql
DELETE FROM tasks
WHERE id = ?;
```

## 2. `WHERE` and Placeholder `?`

ถ้าไม่มี `WHERE` query จะกระทบหลาย row ได้

ตัวอย่าง:

```sql
SELECT id, title, done FROM tasks WHERE id = ?;
```

ความหมายคือ:

- อ่านจาก table `tasks`
- เอาเฉพาะ row ที่ `id` ตรงกับค่าที่ส่งเข้ามา

`?` คือ placeholder สำหรับค่าที่จะส่งจาก code เข้า SQL

เหตุผลที่ใช้ `?`:

- query อ่านง่าย
- ไม่ต้องต่อ string เอง
- ปลอดภัยกว่าการเอาค่าจาก input ไปต่อ SQL ตรงๆ

## 3. `SELECT *` vs Explicit Columns

`SELECT *` แปลว่าเลือกทุก column

```sql
SELECT * FROM tasks WHERE id = ?;
```

ข้อดี:

- เขียนเร็ว
- เหมาะกับการเรียนหรือ debug

ข้อเสีย:

- app จะรับทุก column แม้ไม่จำเป็น
- ถ้า schema เปลี่ยน ภายหลัง code จะไม่ชัดว่าตั้งใจใช้ field ไหน
- type mapping อ่านยากขึ้น

ดังนั้นใน app code ควรเริ่มระบุชื่อ column ให้ชัดเจนเป็นค่าเริ่มต้น:

```sql
SELECT id, title, done FROM tasks WHERE id = ?;
```

## 4. `ORDER BY`

เวลาอ่านหลาย row อย่าคิดว่า database จะคืนลำดับเดิมเสมอ

ถ้า API ต้องการลำดับชัดเจน ให้เขียนลงใน query

### เก่าก่อน ใหม่ทีหลัง

```sql
SELECT id, title, done
FROM tasks
ORDER BY id ASC;
```

### ใหม่ก่อน เก่าทีหลัง

```sql
SELECT id, title, done
FROM tasks
ORDER BY id DESC;
```

สำหรับ task list ในโปรเจกต์นี้ ให้เริ่มคิดแบบง่ายก่อน:

- ถ้าอยากเห็น task ใหม่ก่อน ใช้ `ORDER BY id DESC`
- ถ้าอยากเห็น task เก่าก่อน ใช้ `ORDER BY id ASC`

## ตัวอย่าง

```ts
import path from "node:path";
import { DatabaseSync } from "node:sqlite";

const dbPath = path.join(__dirname, "../bridge-02-storage/example.db");
const db = new DatabaseSync(dbPath);

db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL DEFAULT 0
  )
`);

db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run("Study SQL", 0);
db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run("Build API", 1);

const allTasks = db
  .prepare("SELECT id, title, done FROM tasks ORDER BY id DESC")
  .all();

const oneTask = db
  .prepare("SELECT id, title, done FROM tasks WHERE id = ?")
  .get(1);

console.log(allTasks);
console.log(oneTask);
```

## งานที่ต้องทำ

แก้ไฟล์:

```txt
exercises/bridge-02-sql-query-basics.ts
```

ให้ทำตามนี้:

1. ทำการ import:
   - `path` จาก `node:path`
   - `DatabaseSync` จาก `node:sqlite`

2. สร้าง database file ที่:

```txt
exercises/bridge-02-storage/tasks.db
```

3. สร้าง table `tasks`
   - `id INTEGER PRIMARY KEY AUTOINCREMENT`
   - `title TEXT NOT NULL`
   - `done INTEGER NOT NULL DEFAULT 0`

4. insert task 3 ตัว
   - 2 ตัวเป็น `done = 0`
   - 1 ตัวเป็น `done = 1`

5. query ทั้งหมดด้วย:

```sql
SELECT id, title, done FROM tasks ORDER BY id DESC
```

6. query task เดียวด้วย:

```sql
SELECT id, title, done FROM tasks WHERE id = ?
```

7. query update 1 ครั้ง
   - เปลี่ยน `title`
   - เปลี่ยน `done`

8. query delete 1 ครั้ง
   - ลบตาม `id`

9. พิมพ์ผลออกมา 4 รอบ
   - tasks ทั้งหมดหลัง insert
   - task เดียวตาม id
   - tasks ทั้งหมดหลัง update
   - tasks ทั้งหมดหลัง delete

10. ตอบใน comment สั้นๆ ในไฟล์
   - ทำไม `WHERE id = ?` สำคัญ
   - ทำไมใน app code ควรเลือกใช้ `SELECT id, title, done` มากกว่า `SELECT *`
   - ทำไม `GET /tasks` ควรมี `ORDER BY`

## ผลลัพธ์ที่คาดหวัง

หลังทำเสร็จ นายควรอธิบายได้ว่า:

- SQL command ไหนใช้ทำอะไร
- query ไหนอ่านรายการทั้งหมด
- query ไหนอ่าน row เดียว
- `WHERE` ช่วยจำกัด row ยังไง
- `ORDER BY` ช่วยทำให้ API behavior ชัดขึ้นยังไง

เสร็จแล้วพิมพ์:

```txt
ตรวจ Bridge 02
```
