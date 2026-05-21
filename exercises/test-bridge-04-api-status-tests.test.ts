import { test, after } from "node:test";
import assert from "node:assert/strict";
import path from "node:path";
import { DatabaseSync } from "node:sqlite";
import { app } from "./ch24-task-api-sqlite/app";

const dbPath = path.join(__dirname, "ch24-storage/tasks.db");
const db = new DatabaseSync(dbPath);

db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL
  )
`);

// TODO 1:
const resetTasksTable = (): void => {
  assert.fail("Write resetTasksTable()");
};

const server = app.listen(3002);

after(async () => {
  await new Promise<void>((resolve, reject) => {
    server.close((error) => {
      if (error) reject(error);
      else resolve();
    });
  });
});

test("GET /tasks should return 200 and an array", async () => {
  // TODO:
  resetTasksTable();

  assert.fail("Write GET /tasks test");
});

test("GET /tasks/999 should return 404", async () => {
  // TODO:
  resetTasksTable();

  assert.fail("Write GET /tasks/:id not found test");
});

test("POST /tasks with invalid body should return 400", async () => {
  // TODO:
  resetTasksTable();

  assert.fail("Write POST /tasks invalid body test");
});

test("DELETE /tasks/999 should return 404", async () => {
  // TODO:
  resetTasksTable();

  assert.fail("Write DELETE /tasks/:id not found test");
});
