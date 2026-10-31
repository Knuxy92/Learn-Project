import express from 'express';

const tasks = [
  { id: 1, title: 'Do project', done: false },
  { id: 2, title: 'Learn JavaScript', done: false },
];

const app = express();
app.use(express.json());

// TODO: GET /tasks คืน array ทั้งหมด
// TODO: GET /tasks/:id คืน task ที่ตรง id หรือ 404
// TODO: POST /tasks รับ title สร้าง task ใหม่ด้วย id ถัดไป
// TODO: PUT /tasks/:id อัปเดต title หรือ done หรือ 404
// TODO: DELETE /tasks/:id ลบ task หรือ 404

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
