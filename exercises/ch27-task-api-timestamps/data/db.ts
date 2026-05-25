import { DatabaseSync } from "node:sqlite";
import path from "node:path";

const dbPath = path.join(__dirname, "../../ch27-storage/tasks.db");
const db = new DatabaseSync(dbPath);

// Ch27 starter:
// add created_at and updated_at to this schema.
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
