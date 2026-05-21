import path from "node:path";
import { DatabaseSync } from "node:sqlite";

const dbPath = path.join(__dirname, "ch23-storage/tasks.db");
const db = new DatabaseSync(dbPath);
type DbTaskRow = {
  id: number;
  title: string;
  done: number;
};

type Task = {
  id: number;
  title: string;
  done: boolean;
};

db.exec(/* SQL */ `
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        done INTEGER NOT NULL
    )
`);

db.prepare(/* SQL */ `INSERT INTO tasks (title, done) VALUES (?, ?)`).run(
  "Learn SQLite",
  1,
);

db.prepare(/* SQL */ `INSERT INTO tasks (title, done) VALUES (?, ?)`).run(
  "Learn Type Script",
  0,
);
const rows = db.prepare(/* SQL */ `SELECT id, title, done FROM tasks`).all();
const taskRows = rows.map((row) => {
    return {
        id: row.id,
        title: row.title,
        done: row.done,
    } as DbTaskRow;
});

console.log(taskRows);
const mapping = rows.map((row) => {
    return {
      id: row.id,
      title: row.title,
      done: row.done === 1,
    } as Task;
  })
console.log(mapping);
