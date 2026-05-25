import { type DbTaskRow, type Task } from "../types/task";
import { db } from "../data/db";
const mapTaskRow = (row: DbTaskRow): Task => {
  return {
    id: row.id,
    title: row.title,
    done: row.done === 1,
  };
};

const readTasks = async (): Promise<Task[]> => {
  const rows = db
    .prepare(
      /* SQL */ `
    SELECT id, title, done
    FROM tasks
    ORDER BY id DESC
  `,
    )
    .all() as DbTaskRow[];

  return rows.map(mapTaskRow);
};

const findTaskById = async (id: number): Promise<Task | undefined> => {
  const row = db
    .prepare(
      /* SQL */ `
    SELECT id, title, done
    FROM tasks
    WHERE id = ?
  `,
    )
    .get(id) as DbTaskRow | undefined;

  if (!row) {
    return undefined;
  }

  return mapTaskRow(row);
};

const createTask = async (title: string): Promise<Task> => {
  const result = db
    .prepare(
      /* SQL */ `
    INSERT INTO tasks (title, done)
    VALUES (?, ?)
  `,
    )
    .run(title, 0);

  return {
    id: Number(result.lastInsertRowid),
    title,
    done: false,
  };
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

  db.prepare(
    /* SQL */ `
    UPDATE tasks
    SET title = ?, done = ?
    WHERE id = ?
  `,
  ).run(nextTitle, nextDone ? 1 : 0, id);

  return findTaskById(id);
};

const deleteTask = async (id: number): Promise<boolean> => {
  const result = db
    .prepare(
      /* SQL */ `
    DELETE FROM tasks
    WHERE id = ?
  `,
    )
    .run(id);

  return result.changes > 0;
};

export {
  readTasks,
  findTaskById,
  createTask,
  updateTask,
  deleteTask,
  mapTaskRow,
};
