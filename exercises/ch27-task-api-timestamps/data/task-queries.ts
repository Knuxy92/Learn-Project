import { db } from "./db";
import { type DbTaskRow, type Task } from "../types/task";

const mapTaskRow = (row: DbTaskRow): Task => {
  return {
    id: row.id,
    title: row.title,
    done: row.done === 1,
    createdAt: row.created_at,
    updatedAt: row.updated_at,
  };
};

const readTasks = async (): Promise<Task[]> => {
  const rows = db.prepare(`
    SELECT id, title, done, updated_at, created_at
    FROM tasks
    ORDER BY id DESC
  `).all() as DbTaskRow[];

  return rows.map(mapTaskRow);
};

const findTaskById = async (id: number): Promise<Task | undefined> => {
  const row = db.prepare(`
    SELECT id, title, done, updated_at, created_at
    FROM tasks
    WHERE id = ?
  `).get(id) as DbTaskRow | undefined;

  if (!row) {
    return undefined;
  }

  return mapTaskRow(row);
};

const createTask = async (title: string): Promise<Task> => {
  const result = db.prepare(`
    INSERT INTO tasks (title, done)
    VALUES (?, ?)
  `).run(title, 0);

  const createdTask = await findTaskById(Number(result.lastInsertRowid));

  if (!createdTask) {
    throw new Error("Created task could not be read back");
  }

  return createdTask;
};

const updateTask = async (
  id: number,
  updates: { title?: string; done?: boolean },
): Promise<Task | undefined> => {
  const existingTask = await findTaskById(id);

  if (!existingTask) {
    return undefined;
  }

  const nextTitle = updates.title ?? existingTask.title;
  const nextDone = updates.done ?? existingTask.done;

  db.prepare(`
    UPDATE tasks
    SET title = ?, done = ?, updated_at = CURRENT_TIMESTAMP
    WHERE id = ?
  `).run(nextTitle, nextDone ? 1 : 0, id);

  return findTaskById(id);
};

const deleteTask = async (id: number): Promise<boolean> => {
  const result = db.prepare(`
    DELETE FROM tasks
    WHERE id = ?
  `).run(id);

  return result.changes > 0;
};

export {
  readTasks,
  findTaskById,
  createTask,
  updateTask,
  deleteTask,
};
