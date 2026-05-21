import express from 'express';

const taskRouter = express.Router();

taskRouter.get('/', (req, res) => {
  res.json([{ id: 1, title: 'Example task', done: false }]);
});

export { taskRouter };
