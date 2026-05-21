import path from "node:path";
import { DatabaseSync } from "node:sqlite";

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

const dbPath = path.join(__dirname, "../ch24-storage/example.db");
const db = new DatabaseSync(dbPath);

db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL
  )
`);

const mapTaskRow = (row: DbTaskRow): Task => ({
  id: row.id,
  title: row.title,
  done: row.done === 1,
});

const rows = db.prepare("SELECT id, title, done FROM tasks").all() as DbTaskRow[];
console.log(rows.map(mapTaskRow));
