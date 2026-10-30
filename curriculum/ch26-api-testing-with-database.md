# บทที่ 26: ทดสอบ API กับ database

## ทบทวน

ตอนนี้เราได้ครบ 2 ส่วนสำคัญแล้ว:

- `Ch25` แยก query layer ออกจาก DB setup
- API ของ task app ทำงานกับ SQLite ได้จริง

ขั้นถัดไปคือ:

- test API โดยใช้ database test แยกจากของจริง

## 1. เป้าหมายของบทนี้

บทนี้ไม่ได้เน้นเพิ่ม feature ใหม่

แต่เน้นทำให้เราเชื่อ behavior ของ API ได้จาก test

เป้าหมายคือ:

- มี test database แยก
- reset ข้อมูลก่อนแต่ละ test
- seed data ให้ predictable
- ยิง request จริงไปที่ app
- ปิด server หลัง test จบ

## 2. Why We Need A Separate Test Database

ถ้า test ใช้ database เดียวกับของจริง:

- ข้อมูลเก่าจะปน
- id จะไหลต่อแบบเดายาก
- test จะไม่ stable
- อาจเผลอลบหรือแก้ข้อมูลจริง

ดังนั้น test ควรมี DB ของตัวเอง เช่น:

```txt
exercises/ch26-storage/test-tasks.db
```

## 3. What We Usually Test Here

บทนี้ควรเริ่มจากพฤติกรรมหลักของ API:

- `GET /tasks` ได้ `200`
- `POST /tasks` ได้ `201`
- `GET /tasks/:id` ที่ไม่เจอได้ `404`
- `POST /tasks` body ผิดได้ `400`
- `DELETE /tasks/:id` ที่มีจริงลบสำเร็จ

ยังไม่จำเป็นต้อง test ทุก edge case

เราเน้น:

- flow ที่สำเร็จ
- กรณีไม่เจอข้อมูล
- กรณี request ผิดรูปแบบ

## 4. Test Setup Shape

โครงทั่วไปของ test บทนี้:

1. ชี้ app ไปที่ test database
2. reset table ก่อนแต่ละ test
3. seed data ถ้าจำเป็น
4. เปิด server test port
5. ยิง `fetch(...)`
6. assert status และ body
7. ปิด server หลังจบ

## 5. Environment Override For Test DB

วิธี beginner-friendly ที่ใช้ได้ดีคือ:

- ให้ `data/db.ts` อ่าน path จาก env ก่อน
- ถ้าไม่มี env ค่อย fallback ไปไฟล์จริง

ตัวอย่าง:

```ts
const dbPath =
  process.env.TASKS_DB_PATH ??
  path.join(__dirname, "../../ch26-storage/tasks.db");
```

ข้อดีคือ:

- app code ชุดเดียว
- test เปลี่ยน DB path ได้
- ไม่ต้องแก้ query logic เพื่อ test

## 6. Reset And Seed Example

```ts
const resetTasksTable = (): void => {
  db.prepare("DELETE FROM tasks").run();
  db.prepare("DELETE FROM sqlite_sequence WHERE name = ?").run("tasks");
};

const seedTask = (title: string, done = false): void => {
  db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)")
    .run(title, done ? 1 : 0);
};
```

## 7. Example Test Shape

```ts
test("GET /tasks should return seeded tasks", async () => {
  resetTasksTable();
  seedTask("Write tests");

  const response = await fetch("http://localhost:3005/tasks");
  const body = await response.json();

  assert.equal(response.status, 200);
  assert.equal(Array.isArray(body), true);
  assert.equal(body.length, 1);
});
```

## โจทย์ที่ต้องทำ

ให้ใช้โฟลเดอร์:

```txt
exercises/ch26-task-api-database-tests/
```

ให้ทำตามนี้:

1. ให้ `data/db.ts` รองรับ `TASKS_DB_PATH`
2. สร้าง test database path สำหรับรัน test
3. เขียน helper reset table
4. เขียน helper seed data
5. เปิด server บน test port
6. ปิด server ด้วย `after(...)`
7. เขียน test อย่างน้อย 4 ตัว:
   - `GET /tasks` สำเร็จ
   - `POST /tasks` สำเร็จ
   - `GET /tasks/:id` ที่ไม่เจอ
   - `POST /tasks` ที่ข้อมูลผิดได้ `400`

## ผลลัพธ์ที่คาดหวัง

เมื่อเสร็จ:

- test ไม่แตะ DB จริง
- ข้อมูลในแต่ละ test เดาได้
- API behavior ถูกยืนยันจาก automated test
- พร้อมต่อยอดไป integration testing ที่แน่นขึ้น

## ข้อควรระวัง

บทนี้ยังไม่เน้น:

- การ mocking DB
- กลยุทธ์ transaction rollback
- parallel test isolation ซับซ้อน
- supertest หรือ test library เพิ่ม

เราโฟกัสแค่:

- HTTP request จริง
- test DB แยกจากของจริง
- setup/reset flow ที่ stable

เสร็จแล้วพิมพ์:

```txt
ตรวจ Ch26
```
