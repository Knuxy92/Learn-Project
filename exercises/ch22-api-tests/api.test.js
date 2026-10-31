import { after, beforeEach, test } from 'node:test';
import assert from 'node:assert/strict';
import { rm } from 'node:fs/promises';
import path from 'node:path';

const storagePath = path.join(import.meta.dirname, 'storage', 'test-tasks.json');
process.env.TASKS_FILE_PATH = storagePath;

const { app } = await import('../ch21-persistent-task-api/app.js');

const server = app.listen(3001);
const baseUrl = 'http://localhost:3001';

beforeEach(async () => {
  await rm(storagePath, { force: true });
});

after(async () => {
  await rm(storagePath, { force: true });

  await new Promise((resolve, reject) => {
    server.close((error) => {
      if (error) reject(error);
      else resolve();
    });
  });
});

test('GET /tasks should return 200 and an array', async () => {
  const response = await fetch(`${baseUrl}/tasks`);
  const data = await response.json();

  assert.equal(response.status, 200);
  assert.ok(Array.isArray(data));
});

test('POST /tasks should create a task', async () => {
  const response = await fetch(`${baseUrl}/tasks`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title: 'Testing API' }),
  });
  const data = await response.json();

  assert.equal(response.status, 201);
  assert.equal(data.title, 'Testing API');
  assert.equal(data.done, false);
});

test('POST /tasks with empty title should return 400', async () => {
  const response = await fetch(`${baseUrl}/tasks`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title: '  ' }),
  });

  assert.equal(response.status, 400);
});

test('PUT /tasks/999 should return 404', async () => {
  const response = await fetch(`${baseUrl}/tasks/999`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ done: true }),
  });

  assert.equal(response.status, 404);
});

test('DELETE /tasks/999 should return 404', async () => {
  const response = await fetch(`${baseUrl}/tasks/999`, { method: 'DELETE' });

  assert.equal(response.status, 404);
});
