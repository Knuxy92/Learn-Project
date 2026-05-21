import express from 'express';

const app = express();

app.get('/', (req, res) => {
  res.json({ message: 'Hello from server' });
});

app.get('/about', (req, res) => {
  res.json({ project: 'Learn Project', type: 'backend practice' });
});

app.get('/status', (req, res) => {
  res.json({ ok: true });
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});