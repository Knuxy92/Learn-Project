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

db.prepare("DELETE FROM tasks").run();

db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run("Study SQL", 0);
db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run("Build API", 1);
db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run("Write Tests", 0);

const allTasks = db
  .prepare("SELECT id, title, done FROM tasks ORDER BY id DESC")
  .all();

const oneTask = db
  .prepare("SELECT id, title, done FROM tasks WHERE id = ?")
  .get(1);

db.prepare("UPDATE tasks SET title = ?, done = ? WHERE id = ?").run(
  "Build SQLite API",
  1,
  1,
);

const afterUpdate = db
  .prepare("SELECT id, title, done FROM tasks ORDER BY id DESC")
  .all();

db.prepare("DELETE FROM tasks WHERE id = ?").run(2);

const afterDelete = db
  .prepare("SELECT id, title, done FROM tasks ORDER BY id DESC")
  .all();

console.log("after insert:", allTasks);
console.log("one task:", oneTask);
console.log("after update:", afterUpdate);
console.log("after delete:", afterDelete);
