import { db } from "./db-example";

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

const mapTaskRow = (row: DbTaskRow): Task => {
  return {
    id: row.id,
    title: row.title,
    done: row.done === 1,
  };
};

const getAllTasks = (): Task[] => {
  const rows = db.prepare(`
    SELECT id, title, done
    FROM tasks
    ORDER BY id DESC
  `).all() as DbTaskRow[];

  return rows.map(mapTaskRow);
};

console.log(getAllTasks());
