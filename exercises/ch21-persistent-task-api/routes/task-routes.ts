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
  if (task === undefined)
    return res.status(404).json({ message: "Task not found" });

  return res.json(task);
});

taskRouter.post("/", validateCreateTask, async (req, res) => {
  const title = req.body.title.trim();
  const create = await createTask(title);

  return res.json(create);
});

taskRouter.put("/:id", validateUpdateTask, async (req, res) => {
  const taskId = Number(req.params.id);
  const update = await updateTask(taskId, req.body);
  if (update === undefined)
    return res.status(404).json({ "message": "Task not found" });
  return res.json(update);
});

taskRouter.delete("/:id", async (req, res) => {
  const taskId = Number(req.params.id);
  const deltask = await deleteTask(taskId);
  if (deltask === false)
    return res.status(404).json({ "message": "Task not found" });
  return res.json({ message: "Task deleted" });
});

export { taskRouter };
