# Chapter 27: Timestamps and Richer Schema

## Recap

ตอนนี้เราได้ครบ 3 ชั้นสำคัญแล้ว:

- SQLite task API ทำงานได้
- query layer แยกชัดขึ้น
- API test ใช้ test database แยกได้

ก้าวถัดไปคือทำ schema ให้ใกล้ของจริงขึ้นอีกนิด

## 1. Goal Of This Chapter

บทนี้ยังไม่ใช่เรื่อง relation หรือ join

เราโฟกัสแค่:

- เพิ่ม `created_at`
- เริ่มคิดเรื่อง `updated_at`
- map field ใหม่จาก database ไปเป็น app type

## 2. Why Timestamps Matter

ในงานจริง เรามักไม่ได้อยากรู้แค่ว่า task มีอะไร

เรายังอยากรู้ว่า:

- สร้างเมื่อไร
- แก้ล่าสุดเมื่อไร

field พวกนี้ช่วยทั้ง:

- debug
- sorting
- audit
- UI ที่ต้องแสดงเวลา

## 3. Suggested Schema Upgrade

เริ่มจาก `created_at` ก่อน:

```sql
CREATE TABLE IF NOT EXISTS tasks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  done INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
)
```

หลังจากนั้นค่อยเพิ่ม `updated_at`:

```sql
CREATE TABLE IF NOT EXISTS tasks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  done INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
)
```

## 4. App Type vs DB Row Type

ใน DB row:

- `done` มักเป็น `0 | 1`
- timestamp มักเป็น `TEXT`

ดังนั้น type ควรแยกให้ชัด:

```ts
type DbTaskRow = {
  id: number;
  title: string;
  done: number;
  created_at: string;
  updated_at: string;
};

type Task = {
  id: number;
  title: string;
  done: boolean;
  createdAt: string;
  updatedAt: string;
};
```

## 5. Mapping Reminder

```ts
const mapTaskRow = (row: DbTaskRow): Task => {
  return {
    id: row.id,
    title: row.title,
    done: row.done === 1,
    createdAt: row.created_at,
    updatedAt: row.updated_at,
  };
};
```

## 6. Update Flow Reminder

เวลามี `updated_at`

การ update ควรแก้ field นี้ด้วย เช่น:

```sql
UPDATE tasks
SET title = ?, done = ?, updated_at = CURRENT_TIMESTAMP
WHERE id = ?
```

## Guided Exercise

ให้ใช้โฟลเดอร์:

```txt
exercises/ch27-task-api-timestamps/
```

ให้ทำตามนี้:

1. เพิ่ม `created_at` และ `updated_at` ใน schema
2. เพิ่ม field ใหม่ใน `DbTaskRow` และ `Task`
3. map `created_at -> createdAt`
4. map `updated_at -> updatedAt`
5. ตอน create ให้ response มี timestamp fields
6. ตอน update ให้ `updated_at` เปลี่ยนตาม
7. ให้ route behavior เดิมยังอยู่

## Expected Outcome

เมื่อเสร็จ:

- task object มีเวลาเพิ่มขึ้น
- schema ใกล้ของจริงขึ้น
- app type กับ DB row type ยังแยกชัด
- API ยังทำงานเหมือนเดิม แต่ response รวยขึ้น

เสร็จแล้วพิมพ์:

```txt
ตรวจ Ch27
```
