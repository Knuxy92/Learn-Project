import { test } from "node:test";
import assert from "node:assert/strict";
import path from "node:path";
import { DatabaseSync } from "node:sqlite";
import {
  createTask,
  deleteTask,
  findTaskById,
  readTasks,
  Task,
} from "./ch24-task-api-sqlite/data/task-store";

const dbPath = path.join(__dirname, "ch24-storage/tasks.db");
const db = new DatabaseSync(dbPath);
db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL
  )
`);

const resetTasksTable = (): void => {
  db.prepare("DELETE FROM tasks").run();
  db.prepare("DELETE FROM sqlite_sequence WHERE name = ?").run("tasks");
};

test("readTasks should return mapped boolean values", async () => {
  resetTasksTable();
  await createTask("testing1");
  await createTask("testing2");

  const tasks: Task[] = await readTasks();
  assert.equal(Array.isArray(tasks), true);
  assert.deepEqual(
    {
      ...tasks[0],
    },
    {
      id: 1,
      title: "testing1",
      done: false,
    },
  );
  assert.deepEqual(
    {
      ...tasks[1],
    },
    {
      id: 2,
      title: "testing2",
      done: false,
    },
  );
});

test("findTaskById should return task when found and undefined when missing", async () => {
  resetTasksTable();
  await createTask("testing1")

  const taskNotfound: Task | undefined = await findTaskById(999)
  const taskfound: Task | undefined = await findTaskById(1)
  assert.equal(taskNotfound, undefined);
  assert.notEqual(taskfound, undefined);
  assert.equal(taskfound?.id, 1);
  assert.equal(taskfound?.title, "testing1");
  assert.equal(taskfound?.done, false);
});

test("createTask should create and return a new task", async () => {
  resetTasksTable();
  const newTask: Task = await createTask("testing1");

  assert.notEqual(newTask, undefined);
  assert.equal(newTask.title, "testing1")
});

test("deleteTask should return true first and false when repeated", async () => {
  resetTasksTable();
  await createTask("testing1")
  const delTask1 = await deleteTask(1)
  const delTask2 = await deleteTask(1)

  assert.equal(delTask1, true)
  assert.equal(delTask2, false)
});
