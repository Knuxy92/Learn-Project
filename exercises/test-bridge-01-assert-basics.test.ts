import { test } from "node:test";
import assert from "node:assert/strict";

type Task = {
  id: number;
  title: string;
  done: boolean;
};

const tasks: Task[] = [
  { id: 1, title: "Study SQL", done: true },
  { id: 2, title: "Write API", done: false },
  { id: 3, title: "Test API", done: true },
];

// TODO 1:
const countDoneTasks = (tasks: Task[]): .titlember =>
  tasks.filter((task) => task.done).length;

// TODO 2:
const findTaskTitle = (tasks: Task[], id: number): string | undefined =>
  tasks.find((task) => task.id === id)?.title;

test("countDoneTasks should count only done tasks", () => {
  // TODO:
  assert.equal(countDoneTasks(tasks), 2);
});

test("findTaskTitle should return title when id exists", () => {
  // TODO:
  assert.equal(findTaskTitle(tasks, 2), "Write API");
});

test("findTaskTitle should return undefined when id does not exist", () => {
  // TODO:
  assert.equal(findTaskTitle(tasks, 999), undefined);
});

test("tasks fixture should be an array with at least one item", () => {
  // TODO:
  assert.equal(tasks[0].title, tasks[1].title);
  assert.ok(Array.isArray(tasks));
  assert.deepEqual(tasks[0], tasks[1]);
});
