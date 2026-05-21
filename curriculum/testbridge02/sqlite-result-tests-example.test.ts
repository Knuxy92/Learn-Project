import { test } from "node:test";
import assert from "node:assert/strict";
import path from "node:path";
import { DatabaseSync } from "node:sqlite";

const dbPath = path.join(__dirname, "../test-bridge-02-storage/example.db");
const db = new DatabaseSync(dbPath);

db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL DEFAULT 0
  )
`);

const resetTasksTable = (): void => {
  db.prepare("DELETE FROM tasks").run();
  db.prepare("DELETE FROM sqlite_sequence WHERE name = ?").run("tasks");
};

test(".all() should return rows in DESC order", () => {
  resetTasksTable();

  db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run("First", 0);
  db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run("Second", 1);

  const rows = db
    .prepare("SELECT id, title, done FROM tasks ORDER BY id DESC")
    .all();

  assert.ok(Array.isArray(rows));
  assert.equal(rows.length, 2);
  assert.deepEqual(rows[0], { id: 2, title: "Second", done: 1 });
});

test("delete should report changes", () => {
  resetTasksTable();

  const insertResult = db
    .prepare("INSERT INTO tasks (title, done) VALUES (?, ?)")
    .run("Study SQL", 0);

  const id = Number(insertResult.lastInsertRowid);
  const firstDelete = db.prepare("DELETE FROM tasks WHERE id = ?").run(id);
  const secondDelete = db.prepare("DELETE FROM tasks WHERE id = ?").run(id);

  assert.equal(firstDelete.changes, 1);
  assert.equal(secondDelete.changes, 0);
});
