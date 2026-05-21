import { test } from "node:test";
import assert from "node:assert/strict";

type Task = {
  id: number;
  title: string;
  done: boolean;
};

const countDoneTasks = (tasks: Task[]): number => {
  return tasks.filter((task) => task.done).length;
};

test("countDoneTasks should count only done tasks", () => {
  const tasks: Task[] = [
    { id: 1, title: "Study", done: true },
    { id: 2, title: "Build", done: false },
    { id: 3, title: "Review", done: true },
  ];

  assert.equal(countDoneTasks(tasks), 2);
});

test("task fixture should match expected shape", () => {
  const task: Task = { id: 1, title: "Study", done: true };

  assert.deepEqual(task, { id: 1, title: "Study", done: true });
});
