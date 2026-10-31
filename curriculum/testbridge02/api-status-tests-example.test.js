import { after, test } from 'node:test';
import assert from 'node:assert/strict';
import path from 'node:path';

process.env.TASKS_FILE_PATH = path.join(
  import.meta.dirname,
  'storage',
  'example-test.json',
);

const { app } = await import('../../exercises/ch21-persistent-task-api/app.js');

const server = app.listen(3002);
const baseUrl = 'http://localhost:3002';

after(async () => {
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

test('GET /tasks/999 should return 404', async () => {
  const response = await fetch(`${baseUrl}/tasks/999`);
  const data = await response.json();

  assert.equal(response.status, 404);
  assert.equal(data.message, 'Task not found');
});

test('POST /tasks with invalid body should return 400', async () => {
  const response = await fetch(`${baseUrl}/tasks`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title: '' }),
  });

  assert.equal(response.status, 400);
});

test('DELETE /tasks/999 should return 404', async () => {
  const response = await fetch(`${baseUrl}/tasks/999`, { method: 'DELETE' });
  const data = await response.json();

  assert.equal(response.status, 404);
  assert.equal(data.message, 'Task not found');
});
