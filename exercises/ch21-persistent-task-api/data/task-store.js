import { mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';

const filePath =
  process.env.TASKS_FILE_PATH ??
  path.join(import.meta.dirname, '..', 'storage', 'tasks.json');

const readTasks = async () => {
  try {
    const raw = await readFile(filePath, 'utf-8');

    return JSON.parse(raw);
  } catch (error) {
    if (error.code === 'ENOENT') return [];

    throw error;
  }
};

const writeTasks = async (tasks) => {
  await mkdir(path.dirname(filePath), { recursive: true });
  await writeFile(filePath, JSON.stringify(tasks, null, 2));
};

const findTaskById = async (id) => {
  const tasks = await readTasks();

  return tasks.find((item) => item.id === id);
};

const createTask = async (title) => {
  const tasks = await readTasks();
  const nextId = tasks.length === 0 ? 1 : tasks[tasks.length - 1].id + 1;
  const newTask = { id: nextId, title, done: false };

  tasks.push(newTask);
  await writeTasks(tasks);

  return newTask;
};

const updateTask = async (id, updates) => {
  const tasks = await readTasks();
  const task = tasks.find((item) => item.id === id);

  if (task === undefined) return undefined;

  if (updates.title !== undefined) task.title = updates.title.trim();
  if (updates.done !== undefined) task.done = updates.done;

  await writeTasks(tasks);

  return task;
};

const deleteTask = async (id) => {
  const tasks = await readTasks();
  const index = tasks.findIndex((item) => item.id === id);

  if (index === -1) return false;

  tasks.splice(index, 1);
  await writeTasks(tasks);

  return true;
};

export { readTasks, writeTasks, findTaskById, createTask, updateTask, deleteTask };
