import express from "express";

type Task = {
  id: number;
  title: string;
  done: boolean;
};

const tasks: Task[] = [
  {
    id: 1,
    title: "Do project",
    done: false,
  },
  {
    id: 2,
    title: "Learn type script",
    done: false,
  },
];

const app = express();
app.use(express.json());

const validateCreateTask = (
  req: express.Request,
  res: express.Response,
  next: express.NextFunction,
): void => {
  const { title, done } = req.body;

  if (typeof title !== "string" || title.trim() === "") {
    res.status(400).json({ message: "Title is required" });
    return;
  }

  if (done !== undefined && typeof done !== "boolean") {
    res.status(400).json({ message: "Done must be a boolean" });
    return;
  }

  next();
};

const validateUpdateTask = (
  req: express.Request,
  res: express.Response,
  next: express.NextFunction,
): void => {
  const { title, done } = req.body;

  if (title !== undefined && (typeof title !== "string" || title.trim() === "")) {
    res.status(400).json({ message: "Title must be a non-empty string" });
    return;
  }

  if (done !== undefined && typeof done !== "boolean") {
    res.status(400).json({ message: "Done must be a boolean" });
    return;
  }

  next();
};


app.get("/tasks", (req, res) => {
  res.json(tasks);
});

app.get("/tasks/:id", (req, res) => {
  const taskId = Number(req.params.id);
  const task = tasks.find((item) => item.id === taskId);
  if (task === undefined)
    return res.status(404).json({ message: "Task not found" });

  return res.json(task);
});

app.post("/tasks", validateCreateTask, (req, res) => {
  const Title = req.body.title.trim();
  const nextId = tasks[tasks.length - 1].id;
  const newTask = {
    id: nextId + 1,
    title: Title,
    done: false,
  };

  tasks.push(newTask);
  return res.json(newTask);
});

app.put("/tasks/:id", validateUpdateTask, (req, res) => {
  const taskId = Number(req.params.id);
  const task = tasks.find((item) => item.id === taskId);
  if (task === undefined)
    return res.status(404).json({ message: "Task not found" });
  if (req.body.title !== undefined) task.title = req.body.title.trim();
  if (req.body.done !== undefined) task.done = req.body.done;

  return res.json(task);
});

app.delete("/tasks/:id", (req, res) => {
  const taskId = Number(req.params.id);
  const task = tasks.findIndex((item) => item.id === taskId);
  if (task === -1) return res.status(404).json({ message: "Task not found" });
  tasks.splice(task, 1);

  return res.json({ message: "Task deleted" });
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
