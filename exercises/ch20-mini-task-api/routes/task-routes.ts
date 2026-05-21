import express from "express";
import { tasks } from "../data/tasks";
import {
  validateCreateTask,
  validateUpdateTask,
} from "../middleware/validate-task";

const taskRouter = express.Router();

taskRouter.get("/", (req, res) => {
  res.json(tasks);
});

taskRouter.get("/:id", (req, res) => {
  const taskId = Number(req.params.id);
  const task = tasks.find((item) => item.id === taskId);
  if (task === undefined)
    return res.status(404).json({ message: "Task not found" });

  return res.json(task);
});

taskRouter.post("/", validateCreateTask, (req, res) => {
  const title = req.body.title.trim();
  const nextId = tasks[tasks.length - 1].id;
  const newTask = {
    id: nextId + 1,
    title: title,
    done: false,
  };

  tasks.push(newTask);
  return res.json(newTask);
});

taskRouter.put("/:id", validateUpdateTask, (req, res) => {
  const taskId = Number(req.params.id);
  const task = tasks.find((item) => item.id === taskId);
  if (task === undefined)
    return res.status(404).json({ message: "Task not found" });
  if (req.body.title !== undefined) task.title = req.body.title.trim();
  if (req.body.done !== undefined) task.done = req.body.done;

  return res.json(task);
});

taskRouter.delete("/:id", (req, res) => {
  const taskId = Number(req.params.id);
  const task = tasks.findIndex((item) => item.id === taskId);
  if (task === -1) return res.status(404).json({ message: "Task not found" });
  tasks.splice(task, 1);

  return res.json({ message: "Task deleted" });
});

export { taskRouter };
