import path from "node:path";
import { DatabaseSync } from "node:sqlite";

const dbPath = path.join(__dirname, "bridge-03-storage/tasks.db");
const db = new DatabaseSync(dbPath);

interface TaskRow {
  id: number;
  title: string;
  done: number;
}

db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL DEFAULT 0
  )
`);

// TODO 1:
db.prepare("DELETE FROM tasks").run();

// TODO 2:
db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run("Study SQL", 0);
const insertResult = db
  .prepare("INSERT INTO tasks (title, done) VALUES (?, ?)")
  .run("Build API", 1);

// TODO 3:
const lastId = Number(insertResult.lastInsertRowid);

// TODO 4:
const orders = db
  .prepare("SELECT id, title, done FROM tasks ORDER BY id DESC")
  .all() as unknown as TaskRow[];

// TODO 5:
const onetask = db
  .prepare("SELECT id, title, done FROM tasks WHERE id = ?")
  .get(lastId) as unknown as TaskRow | undefined;

// TODO 6:
const missingTask = db
  .prepare("SELECT id, title, done FROM tasks WHERE id = ?")
  .get(9999) as unknown as TaskRow | undefined;

// TODO 7:
const deleteResult = db.prepare("DELETE FROM tasks WHERE id = ?").run(lastId);
db.prepare("DELETE FROM sqlite_sequence WHERE name = ?").run("tasks");

// TODO 8:
const deleteMissingResult = db.prepare("DELETE FROM tasks WHERE id = ?").run(lastId);

// TODO 9:
console.log(lastId)
console.log(orders)
console.log(onetask)
console.log(missingTask)
console.log(deleteResult.changes)
console.log(deleteMissingResult.changes)

// TODO 10:
// ตอบเป็นคอมเมนต์สั้น ๆ:
// - what does .all() return when there are no rows จะคืน Arry เปล่า [] ไม่มีอะไรเลย
// - what does .get() return when no row is found จะคืน undefined
// - what is lastInsertRowid used for ไว้เช็ค rowid ล่าสุดที่ instant ไป
// - what does changes === 0 mean หมายถึงไม่มีอะไรเปลี่ยนจากการ run ครั้งนั้น
