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
db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run("Study Status Codes", 1);

const foundTask = db
  .prepare("SELECT id, title, done FROM tasks WHERE id = ?")
  .get(1);

const missingTask = db
  .prepare("SELECT id, title, done FROM tasks WHERE id = ?")
  .get(9999);

const emptyRows = db
  .prepare("SELECT id, title, done FROM tasks WHERE done = ?")
  .all(2);

let queryStatus = "ok";

try {
  db.prepare("SELECT id, title, done FROM wrong_table WHERE id = ?").get(1);
} catch {
  queryStatus = "sql error";
}

console.log("foundTask:", foundTask);
console.log("missingTask:", missingTask);
console.log("emptyRows:", emptyRows);
console.log("queryStatus:", queryStatus);
