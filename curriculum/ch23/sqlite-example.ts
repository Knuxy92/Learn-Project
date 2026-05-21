import path from "node:path";
import { DatabaseSync } from "node:sqlite";

const dbPath = path.join(__dirname, "../ch23-storage/example.db");
const db = new DatabaseSync(dbPath);

db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL
  )
`);

db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run(
  "Learn SQLite",
  0,
);

const rows = db.prepare("SELECT id, title, done FROM tasks").all();
console.log(rows);
