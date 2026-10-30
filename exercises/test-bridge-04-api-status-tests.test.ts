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
  db.prepare("DELETE FROM tasks").run()
  db.prepare("DELETE FROM sqlite_sequence WHERE name = ?").run("tasks");
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
  resetTasksTable();
  const response = await fetch("http://localhost:3002/tasks")
  const getTasks = await response.json();

  assert.strictEqual(response.status, 200); 
  assert.strictEqual(Array.isArray(getTasks), true)
});

test("GET /tasks/999 should return 404", async () => {
  resetTasksTable();
  const response = await fetch("http://localhost:3002/tasks/999")
  
  assert.strictEqual(response.status, 404); 
});

test("POST /tasks with invalid body should return 400", async () => {
  resetTasksTable();
  const response1 = await fetch("http://localhost:3002/tasks", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      title: "Testing Api",
      done: false,
    }),
  });
  const data = await response1.json(); 
  
  const response2 = await fetch("http://localhost:3002/tasks", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      done: false,
    }),
  });

  assert.strictEqual(response1.status, 200);
  assert.strictEqual(data?.id, 1); 
  assert.strictEqual(data?.title, "Testing Api");
  assert.strictEqual(data?.done, false); 

  assert.strictEqual(response2.status, 400); 
});


test("DELETE /tasks/999 should return 404", async () => {
  resetTasksTable();
  const response = await fetch("http://localhost:3002/tasks/999", {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
  });

  assert.strictEqual(response.status, 404)
});
