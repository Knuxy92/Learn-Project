import { after, test } from "node:test";
import assert from "node:assert/strict";
import path from "node:path";
import { DatabaseSync } from "node:sqlite";

process.env.TASKS_DB_PATH = path.join(
  __dirname,
  "../ch27-storage/test-tasks.db",
);

// eslint-disable-next-line @typescript-eslint/no-require-imports
const { app } = require("./app");

const db = new DatabaseSync(process.env.TASKS_DB_PATH);

const resetTasksTable = () => {
  db.prepare("DELETE FROM tasks").run();
  db.prepare("DELETE FROM sqlite_sequence WHERE name = ?").run("tasks");
};

const seedTask = (title: string, done = false): void => {
  db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run(
    title,
    done ? 1 : 0,
  );
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
  seedTask("Testing 1");
  const response = await fetch("http://localhost:3005/tasks");
  const getTasks = await response.json();
  console.log(getTasks);
  assert.strictEqual(response.status, 200);
  assert.strictEqual(Array.isArray(getTasks), true);
  assert.deepStrictEqual(getTasks[0], {
    id: 1,
    title: "Testing 1",
    done: false,
  });
});

test("POST /tasks should create a new task", async () => {
  resetTasksTable();
  const response = await fetch("http://localhost:3005/tasks", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      title: "Testing 1",
      done: false,
    }),
  });
  const getTasks = await response.json();

  assert.strictEqual(response.status, 201);
  assert.strictEqual(typeof getTasks, "object");
  assert.strictEqual(typeof getTasks.id, "number");
  assert.deepStrictEqual(getTasks, {
    id: 1,
    title: "Testing 1",
    done: false,
  });
});

test("GET /tasks/999 should return 404", async () => {
  resetTasksTable();
  const response = await fetch("http://localhost:3005/tasks/999");

  assert.strictEqual(response.status, 404);
});

test("POST /tasks with invalid body should return 400", async () => {
  resetTasksTable();
  const response2 = await fetch("http://localhost:3005/tasks", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      done: false,
    }),
  });
  assert.strictEqual(response2.status, 400);
});
