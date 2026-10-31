import { test } from 'node:test';
import assert from 'node:assert/strict';

const tasks = [
  { id: 1, title: 'Study Node', done: true },
  { id: 2, title: 'Write API', done: false },
  { id: 3, title: 'Test API', done: true },
];

// TODO 1: คืนจำนวน task ที่ done เป็น true
const countDoneTasks = (tasks) => {};

// TODO 2: คืน title ของ task ที่ id ตรงกัน ถ้าไม่เจอคืน undefined
const findTaskTitle = (tasks, id) => {};

test('countDoneTasks should count only done tasks', () => {
  assert.fail('ยังไม่ได้ทำ test นี้');
});

test('findTaskTitle should return title when id exists', () => {
  assert.fail('ยังไม่ได้ทำ test นี้');
});

test('findTaskTitle should return undefined when id does not exist', () => {
  assert.fail('ยังไม่ได้ทำ test นี้');
});

test('tasks fixture should be an array with at least one item', () => {
  assert.fail('ยังไม่ได้ทำ test นี้');
});
