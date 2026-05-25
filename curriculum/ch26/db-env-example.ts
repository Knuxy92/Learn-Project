import { DatabaseSync } from "node:sqlite";
import path from "node:path";

const dbPath =
  process.env.TASKS_DB_PATH ??
  path.join(__dirname, "../ch26-storage/example.db");

const db = new DatabaseSync(dbPath);

db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL DEFAULT 0
  )
`);

export { db };
