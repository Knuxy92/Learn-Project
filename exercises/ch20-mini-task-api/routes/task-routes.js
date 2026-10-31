import express from 'express';
import { tasks } from '../data/tasks.js';
import { validateCreateTask, validateUpdateTask } from '../middleware/validate-task.js';

const taskRouter = express.Router();

taskRouter.get('/', (req, res) => {
  res.json(tasks);
});

taskRouter.get('/:id', (req, res) => {
  const taskId = Number(req.params.id);
  const task = tasks.find((item) => item.id === taskId);

  if (task === undefined) {
    res.status(404).json({ message: 'Task not found' });
    return;
  }

  res.json(task);
});

taskRouter.post('/', validateCreateTask, (req, res) => {
  const nextId = tasks.length === 0 ? 1 : tasks[tasks.length - 1].id + 1;
  const newTask = {
    id: nextId,
    title: req.body.title.trim(),
    done: false,
  };

  tasks.push(newTask);
  res.status(201).json(newTask);
});

taskRouter.put('/:id', validateUpdateTask, (req, res) => {
  const taskId = Number(req.params.id);
  const task = tasks.find((item) => item.id === taskId);

  if (task === undefined) {
    res.status(404).json({ message: 'Task not found' });
    return;
  }

  if (req.body.title !== undefined) task.title = req.body.title.trim();
  if (req.body.done !== undefined) task.done = req.body.done;

  res.json(task);
});

taskRouter.delete('/:id', (req, res) => {
  const taskId = Number(req.params.id);
  const index = tasks.findIndex((item) => item.id === taskId);

  if (index === -1) {
    res.status(404).json({ message: 'Task not found' });
    return;
  }

  tasks.splice(index, 1);
  res.json({ message: 'Task deleted' });
});

export { taskRouter };
