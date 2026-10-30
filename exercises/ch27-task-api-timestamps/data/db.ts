import { DatabaseSync } from "node:sqlite";
import path from "node:path";

const dbPath =
  process.env.TASKS_DB_PATH ??
  path.join(__dirname, "../../ch27-storage/tasks.db");

const db = new DatabaseSync(dbPath);

// จุดเริ่มต้นของ Ch27:
// เพิ่ม created_at และ updated_at เข้าไปใน schema นี้
db.exec(`
CREATE TABLE IF NOT EXISTS tasks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  done INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
)
`);

export { db };
