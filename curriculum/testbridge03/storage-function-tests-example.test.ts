import { test } from "node:test";
import assert from "node:assert/strict";
import path from "node:path";
import { DatabaseSync } from "node:sqlite";
import {
  createTask,
  deleteTask,
  findTaskById,
  readTasks,
} from "../../exercises/ch24-task-api-sqlite/data/task-store";

const dbPath = path.join(__dirname, "../../exercises/ch24-storage/tasks.db");
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

  db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run("First", 0);
  db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run("Second", 1);

  const tasks = await readTasks();

  assert.equal(tasks.length, 2);
  assert.deepEqual(tasks, [
    { id: 2, title: "Second", done: true },
    { id: 1, title: "First", done: false },
  ]);
});

test("findTaskById should return task when found and undefined when missing", async () => {
  resetTasksTable();

  db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run("Study SQL", 0);

  const found = await findTaskById(1);
  const missing = await findTaskById(999);

  assert.deepEqual(found, {
    id: 1,
    title: "Study SQL",
    done: false,
  });
  assert.equal(missing, undefined);
});

test("createTask should create and return a new task", async () => {
  resetTasksTable();

  const created = await createTask("Write tests");

  assert.deepEqual(created, {
    id: 1,
    title: "Write tests",
    done: false,
  });
});

test("deleteTask should return true first and false when repeated", async () => {
  resetTasksTable();

  const created = await createTask("Delete me");

  const firstDelete = await deleteTask(created.id);
  const secondDelete = await deleteTask(created.id);

  assert.equal(firstDelete, true);
  assert.equal(secondDelete, false);
});
