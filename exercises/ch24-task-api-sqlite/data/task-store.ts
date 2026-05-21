import { Task, RawTask } from "../types/task";
import { DatabaseSync } from "node:sqlite";
import path from "node:path";

const dbPath = path.join(__dirname, "../../ch24-storage/tasks.db");
const db = new DatabaseSync(dbPath);

db.exec(/* SQL */ `
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        done INTEGER NOT NULL
    )
`);

const readTasks = async (): Promise<Task[]> => {
  const raws = db.prepare(/* SQL */ `SELECT id, title, done FROM tasks`).all() as unknown as RawTask[];

  return raws.map((raw) => {
    return {
      id: raw.id,
      title: raw.title,
      done: raw.done === 1,
    };
  }) as Task[];
};

const writeTasks = async (tasks: Task[]): Promise<void> => {
  const stmt = db.prepare(`INSERT INTO tasks (title, done) VALUES (?, ?)`);

  for (const task of tasks) {
    stmt.run(task.title, task.done ? 1 : 0);
  }
};

const findTaskById = async (id: number): Promise<Task | undefined> => {
  const raw = db.prepare("SELECT * FROM tasks WHERE id = ?").get(id) as unknown as RawTask;
  if (raw === undefined) return undefined
  return {
    ...raw,
    done: raw.done === 1
  } as Task;
};

const createTask = async (title: string): Promise<Task> => {
  const result = db
    .prepare(`INSERT INTO tasks (title, done) VALUES (?, ?)`)
    .run(title, 0);

  return {
    id: Number(result.lastInsertRowid),
    title,
    done: false,
  } as Task;
};


const updateTask = async (
  id: number,
  updates: { title?: string; done?: boolean },
): Promise<Task | undefined> => {
  const task = db.prepare(`SELECT * FROM tasks WHERE id = ?`).get(id) as unknown as RawTask
  if (task === undefined) return undefined
  if (updates.title !== undefined) {
    db.prepare("UPDATE tasks SET title = ? WHERE id = ?").run(
      updates.title,
      id,
    );
  };

  if (updates.done !== undefined) {
    db.prepare("UPDATE tasks SET done = ? WHERE id = ?").run(
      updates.done ? 1 : 0,
      id,
    );
  };
  
  const raw = db.prepare("SELECT * FROM tasks WHERE id = ?").get(id) as unknown as RawTask;

  if (raw === undefined) return undefined;
  return {
    ...raw,
    done: raw.done === 1
  } as Task;
};

const deleteTask = async (id: number): Promise<boolean> => {
  const info = db.prepare("DELETE FROM tasks WHERE id = ?").run(id) ;
  return info.changes > 0;
};

export {
  readTasks,
  writeTasks,
  findTaskById,
  createTask,
  updateTask,
  deleteTask,
  type Task
};
