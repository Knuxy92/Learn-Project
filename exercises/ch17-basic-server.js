import express from 'express';

const app = express();

// TODO: สร้าง route GET / ที่คืน { message: 'Hello from server' }
// TODO: สร้าง route GET /about ที่คืน { project: 'Learn Project', type: 'backend practice' }
// TODO: สร้าง route GET /status ที่คืน { ok: true }

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
