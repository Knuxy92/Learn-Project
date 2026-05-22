import express from "express";
import {
  readTasks,
  findTaskById,
  createTask,
  updateTask,
  deleteTask,
} from "../data/task-store";
import {
  validateCreateTask,
  validateUpdateTask,
} from "../middleware/validate-task";

const taskRouter = express.Router();

taskRouter.get("/", async (req, res) => {
  const tasks = await readTasks();
  return res.json(tasks);
});

taskRouter.get("/:id", async (req, res) => {
  const taskId = Number(req.params.id);
  const task = await findTaskById(taskId);

  if (task === undefined) {
    return res.status(404).json({ message: "Task not found" });
  }

  return res.json(task);
});

taskRouter.post("/", validateCreateTask, async (req, res) => {
  const title = req.body.title.trim();
  const createdTask = await createTask(title);

  return res.status(201).json(createdTask);
});

taskRouter.put("/:id", validateUpdateTask, async (req, res) => {
  const taskId = Number(req.params.id);
  const updatedTask = await updateTask(taskId, req.body);

  if (updatedTask === undefined) {
    return res.status(404).json({ message: "Task not found" });
  }

  return res.json(updatedTask);
});

taskRouter.delete("/:id", async (req, res) => {
  const taskId = Number(req.params.id);
  const deletedTask = await deleteTask(taskId);

  if (deletedTask === false) {
    return res.status(404).json({ message: "Task not found" });
  }

  return res.json({ message: "Task deleted" });
});

export { taskRouter };
