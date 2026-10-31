import express from 'express';
import { taskRouter } from './routes-example.js';

const app = express();

app.use(express.json());
app.use('/tasks', taskRouter);

export { app };
