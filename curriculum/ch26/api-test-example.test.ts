import { after, test } from "node:test";
import assert from "node:assert/strict";
import path from "node:path";
import { DatabaseSync } from "node:sqlite";

process.env.TASKS_DB_PATH = path.join(
  __dirname,
  "../ch26-storage/example-test.db",
);

const { app } = require("../../exercises/ch26-task-api-database-tests/app");

const db = new DatabaseSync(process.env.TASKS_DB_PATH);

const resetTasksTable = (): void => {
  db.prepare("DELETE FROM tasks").run();
  db.prepare("DELETE FROM sqlite_sequence WHERE name = ?").run("tasks");
};

const seedTask = (title: string, done = false): void => {
  db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)")
    .run(title, done ? 1 : 0);
};

const server = app.listen(3005);

after(async () => {
  await new Promise<void>((resolve, reject) => {
    server.close((error?: Error) => {
      if (error) reject(error);
      else resolve();
    });
  });
});

test("GET /tasks should return seeded tasks", async () => {
  resetTasksTable();
  seedTask("Write tests");

  const response = await fetch("http://localhost:3005/tasks");
  const body = await response.json();

  assert.equal(response.status, 200);
  assert.equal(Array.isArray(body), true);
  assert.equal(body.length, 1);
  assert.equal(body[0].title, "Write tests");
});
