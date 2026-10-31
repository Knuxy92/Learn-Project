import express from 'express';

const tasks = [
  { id: 1, title: 'Do project', done: false },
  { id: 2, title: 'Learn JavaScript', done: false },
];

const app = express();
app.use(express.json());

const validateCreateTask = (req, res, next) => {
  // TODO: title ต้องเป็น string ที่ไม่ว่างหลัง trim() ไม่งั้น 400
  // TODO: done ถ้ามี ต้องเป็น boolean ไม่งั้น 400
  // TODO: ผ่านแล้วเรียก next()
};

const validateUpdateTask = (req, res, next) => {
  // TODO: title ถ้ามี ต้องเป็น string ที่ไม่ว่างหลัง trim() ไม่งั้น 400
  // TODO: done ถ้ามี ต้องเป็น boolean ไม่งั้น 400
  // TODO: ผ่านแล้วเรียก next()
};

// TODO: ทำ CRUD ให้ครบ โดยใช้ middleware ทั้งสองตัว
// POST /tasks ต้องคืน status 201

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
