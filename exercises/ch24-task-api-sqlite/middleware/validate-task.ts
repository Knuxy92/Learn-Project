import express from "express";

const validateCreateTask = (
  req: express.Request,
  res: express.Response,
  next: express.NextFunction,
): void => {
  if (req.body === undefined) {
    res.status(400).json({ message: "Miss parameter" });
    return;
  }
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
  if (req.body === undefined) {
    res.status(400).json({ message: "Miss parameter" });
    return;
  }

  const { title, done } = req.body || {};

  if (
    title !== undefined &&
    (typeof title !== "string" || title.trim() === "")
  ) {
    res.status(400).json({ message: "Title must be a non-empty string" });
    return;
  }

  if (done !== undefined && typeof done !== "boolean") {
    res.status(400).json({ message: "Done must be a boolean" });
    return;
  }

  next();
};

export { validateCreateTask, validateUpdateTask };
