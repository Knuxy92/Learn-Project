import express from 'express';
import {
  readTasks,
  findTaskById,
  createTask,
  updateTask,
  deleteTask,
} from '../data/task-store.js';
import { validateCreateTask, validateUpdateTask } from '../middleware/validate-task.js';

const taskRouter = express.Router();

taskRouter.get('/', async (req, res) => {
  const tasks = await readTasks();

  res.json(tasks);
});

taskRouter.get('/:id', async (req, res) => {
  const taskId = Number(req.params.id);
  const task = await findTaskById(taskId);

  if (task === undefined) {
    res.status(404).json({ message: 'Task not found' });
    return;
  }

  res.json(task);
});

taskRouter.post('/', validateCreateTask, async (req, res) => {
  const created = await createTask(req.body.title.trim());

  res.status(201).json(created);
});

taskRouter.put('/:id', validateUpdateTask, async (req, res) => {
  const taskId = Number(req.params.id);
  const updated = await updateTask(taskId, req.body);

  if (updated === undefined) {
    res.status(404).json({ message: 'Task not found' });
    return;
  }

  res.json(updated);
});

taskRouter.delete('/:id', async (req, res) => {
  const taskId = Number(req.params.id);
  const deleted = await deleteTask(taskId);

  if (deleted === false) {
    res.status(404).json({ message: 'Task not found' });
    return;
  }

  res.json({ message: 'Task deleted' });
});

export { taskRouter };
