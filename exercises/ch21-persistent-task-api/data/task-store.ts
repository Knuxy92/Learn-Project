import { readFile, writeFile } from "node:fs/promises";
import { Task } from "../types/task";
import 'dotenv/config';
import path from "node:path";

const filePath = process.env.TASKS_FILE_PATH ?? path.join(__dirname, "../storage/tasks.json");

const readTasks = async (): Promise<Task[]> => {
  const raw = await readFile(filePath, "utf-8");
  return JSON.parse(raw);
};

const writeTasks = async (tasks: Task[]): Promise<void> => {
  await writeFile(filePath, JSON.stringify(tasks, null, 2));
};

const findTaskById = async (id: number): Promise<Task | undefined> => {
  const tasks = await readTasks();
  return tasks.find((item) => item.id === id);
};

const createTask = async (title: string): Promise<Task> => {
  const tasks = await readTasks();
  const nextId = tasks[tasks.length - 1].id;
  const newTask: Task = {
    id: nextId + 1,
    title: title,
    done: false,
  };

  tasks.push(newTask);
  await writeTasks(tasks);
  return newTask;
};

const updateTask = async (
  id: number,
  updates: { title?: string; done?: boolean },
): Promise<Task | undefined> => {
  const tasks = await readTasks();
  const task = tasks.find((item) => item.id === id);
  if (task === undefined) return undefined;
  if (updates.title !== undefined) task.title = updates.title.trim();
  if (updates.done !== undefined) task.done = updates.done;

  await writeTasks(tasks);
  return task;
};

const deleteTask = async (id: number): Promise<boolean> => {
  const tasks = await readTasks();
  const index = tasks.findIndex((item) => item.id === id);
  if (index === -1) return false;
  tasks.splice(index, 1);

  await writeTasks(tasks);
  return true;
};

export {
  readTasks,
  writeTasks,
  findTaskById,
  createTask,
  updateTask,
  deleteTask,
};
