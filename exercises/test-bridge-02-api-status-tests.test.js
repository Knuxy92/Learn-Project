import { after, test } from 'node:test';
import assert from 'node:assert/strict';
import { rm } from 'node:fs/promises';
import path from 'node:path';

const storagePath = path.join(
  import.meta.dirname,
  'storage',
  'test-bridge-tasks.json',
);
process.env.TASKS_FILE_PATH = storagePath;

const { app } = await import('./ch21-persistent-task-api/app.js');

const server = app.listen(3002);
const baseUrl = 'http://localhost:3002';

after(async () => {
  await rm(storagePath, { force: true });

  await new Promise((resolve, reject) => {
    server.close((error) => {
      if (error) reject(error);
      else resolve();
    });
  });
});

test('GET /tasks should return 200', async () => {
  assert.fail('ยังไม่ได้ทำ test นี้');
});

test('GET /tasks/999 should return 404', async () => {
  assert.fail('ยังไม่ได้ทำ test นี้');
});

test('POST /tasks with invalid body should return 400', async () => {
  assert.fail('ยังไม่ได้ทำ test นี้');
});

test('DELETE /tasks/999 should return 404', async () => {
  assert.fail('ยังไม่ได้ทำ test นี้');
});
