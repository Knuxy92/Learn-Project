import path from "node:path";
import { DatabaseSync } from "node:sqlite";

const dbPath = path.join(__dirname, "../bridge-03-storage/example.db");
const db = new DatabaseSync(dbPath);

db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL DEFAULT 0
  )
`);

db.prepare("DELETE FROM tasks").run();

const firstInsert = db
  .prepare("INSERT INTO tasks (title, done) VALUES (?, ?)")
  .run("Study Driver Methods", 0);

const secondInsert = db
  .prepare("INSERT INTO tasks (title, done) VALUES (?, ?)")
  .run("Practice Result Objects", 1);

const lastId = Number(secondInsert.lastInsertRowid);

const allTasks = db
  .prepare("SELECT id, title, done FROM tasks ORDER BY id DESC")
  .all();

const oneTask = db
  .prepare("SELECT id, title, done FROM tasks WHERE id = ?")
  .get(lastId);

const missingTask = db
  .prepare("SELECT id, title, done FROM tasks WHERE id = ?")
  .get(9999);

const deleteResult = db
  .prepare("DELETE FROM tasks WHERE id = ?")
  .run(lastId);

const deleteMissingResult = db
  .prepare("DELETE FROM tasks WHERE id = ?")
  .run(lastId);

console.log("first insert id:", Number(firstInsert.lastInsertRowid));
console.log("lastId:", lastId);
console.log("allTasks:", allTasks);
console.log("oneTask:", oneTask);
console.log("missingTask:", missingTask);
console.log("delete changes:", deleteResult.changes);
console.log("delete missing changes:", deleteMissingResult.changes);
