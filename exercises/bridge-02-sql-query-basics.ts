import path from "node:path";
import { DatabaseSync } from "node:sqlite";

const dbPath = path.join(__dirname, "bridge-02-storage/tasks.db");
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
db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run("TEST API", 0);
db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run("Study SQL", 0);
db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run("Build API", 1);

// TODO 3:
const orders = db
  .prepare("SELECT id, title, done FROM tasks ORDER BY id DESC")
  .all() as unknown as TaskRow[];

// TODO 4:
const onetask = db
  .prepare("SELECT id, title, done FROM tasks WHERE id = ?")
  .get(1);

// TODO 5:
db.prepare("UPDATE tasks SET title = ?, done = ? WHERE id = ?").run(
  "Study SQL Update",
  1,
  1,
);

// TODO 6:
const orders2 = db
  .prepare("SELECT id, title, done FROM tasks ORDER BY id DESC")
  .all() as unknown as TaskRow[];

// TODO 7:
db.prepare("DELETE FROM tasks WHERE id = ?").run(1);

// TODO 8:
const orders3 = db
  .prepare("SELECT id, title, done FROM tasks ORDER BY id DESC")
  .all() as unknown as TaskRow[];

// TODO 9:
// print 4 rounds
console.log(orders);
console.log(onetask);
console.log(orders2);
console.log(orders3);

// TODO 10:
// answer in short comments:
// important เพราะเอาไว้หาแบบเฉาะจง ถ้าไม่ใช้ WHERE มันอาจะ UPDATE ทุก Row เลย
// เฉาะจงมากกว่า แล้วจะได้เอาออกมาแค่ที่ใช้ การ * มันจะดึงทุก Col ออกมาเลย
// เพื่อจัดระเบียดข้อมูลให้ Debug ง่ายและแสดงข้อมูลเป็นลำลับ
