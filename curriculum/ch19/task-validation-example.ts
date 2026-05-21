import express from 'express';

type Task = {
  id: number;
  title: string;
  done: boolean;
};

const app = express();
app.use(express.json());

const tasks: Task[] = [
  { id: 1, title: 'Learn middleware', done: false },
  { id: 2, title: 'Validate input', done: false },
];

const validateCreateTask = (
  req: express.Request,
  res: express.Response,
  next: express.NextFunction,
): void => {
  if (typeof req.body.title !== 'string' || req.body.title.trim() === '') {
    res.status(400).json({ message: 'Title is required' });
    return;
  }

  next();
};

app.post('/tasks', validateCreateTask, (req, res) => {
  const nextId = tasks[tasks.length - 1].id + 1;

  const newTask: Task = {
    id: nextId,
    title: req.body.title.trim(),
    done: false,
  };

  tasks.push(newTask);
  res.json(newTask);
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
