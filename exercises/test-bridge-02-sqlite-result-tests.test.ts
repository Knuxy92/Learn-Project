import { test } from "node:test";
import assert from "node:assert/strict";
import path from "node:path";
import { DatabaseSync } from "node:sqlite";

const dbPath = path.join(__dirname, "test-bridge-02-storage/tasks.db");
const db = new DatabaseSync(dbPath);

db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL DEFAULT 0
  )
`);

// TODO 1:
const resetTasksTable = (): void => {
  db.prepare("DELETE FROM tasks").run();
  db.prepare("DELETE FROM sqlite_sequence WHERE name = ?").run('tasks');
};

test(".all() should return rows in DESC order", () => {
  // TODO:
  resetTasksTable();
  db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run(
    "Study SQL",
    0,
  );

  db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run(
    "Do Test SQL",
    0,
  );

  const rows = db.prepare("SELECT * FROM tasks ORDER BY id DESC").all();
  const first = db.prepare("SELECT * FROM tasks WHERE id = ?").get(1);
  const cleanFirst = JSON.parse(JSON.stringify(first));
  const cleanRows = JSON.parse(JSON.stringify(rows));

  assert.equal(rows.length, 2);
  assert.deepEqual(cleanRows, [
    {
      id: 2,
      title: "Do Test SQL",
      done: 0,
    },
    {
      id: 1,
      title: "Study SQL",
      done: 0,
    },
  ]);
  assert.deepEqual(cleanFirst, {
    id: 1,
    title: "Study SQL",
    done: 0,
  });
});

test(".get() should return row when found and undefined when missing", () => {
  // TODO:
  resetTasksTable();
  db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run(
    "Study SQL",
    0,
  );

  const realId = db.prepare("SELECT * FROM tasks WHERE id = ?").get(1);
  const missingId = db.prepare("SELECT * FROM tasks WHERE id = ?").get(999);
  const cleanRealId = JSON.parse(JSON.stringify(realId));

  assert.deepEqual(cleanRealId, {
    id: 1,
    title: "Study SQL",
    done: 0,
  });
  assert.equal(missingId, undefined);
});

test("insert should return lastInsertRowid and create a real row", () => {
  // TODO:
  resetTasksTable();
  const result = db
    .prepare("INSERT INTO tasks (title, done) VALUES (?, ?)")
    .run("Study SQL", 0);
  const LastRowId = result.lastInsertRowid;
  const row = db.prepare("SELECT * FROM tasks WHERE id = ?").get(LastRowId);
  const cleanrow = JSON.parse(JSON.stringify(row));
  assert.deepEqual(cleanrow, {
    id: 1,
    title: "Study SQL",
    done: 0,
  });
});

test("delete should report changes for existing and missing rows", () => {
  // TODO:
  resetTasksTable();
  const result = db
    .prepare("INSERT INTO tasks (title, done) VALUES (?, ?)")
    .run("Study SQL", 0);
  const LastRowId = result.lastInsertRowid;
  const result1 = db.prepare("DELETE FROM tasks WHERE id = ?").run(LastRowId);
  const result2 = db.prepare("DELETE FROM tasks WHERE id = ?").run(LastRowId);
  assert.equal(result1.changes, 1);
  assert.equal(result2.changes, 0);
});
