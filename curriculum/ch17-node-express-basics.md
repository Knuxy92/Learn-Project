# บทที่ 17: พื้นฐาน Node.js และ Express

## ทบทวน

ตอนนี้เราเรียนพื้นฐาน JavaScript ครบแล้ว

บทนี้เราจะเริ่มทำงานฝั่งเซิร์ฟเวอร์ (backend) จริงด้วย Node.js และ Express

## 1. Node.js คืออะไร

Node.js คือสภาพแวดล้อมการทำงานที่ทำให้ JavaScript รันนอกเบราว์เซอร์ได้

เราต้องใช้มันเพราะเซิร์ฟเวอร์ (server) ของเราจะรันด้วย Node.js

## 2. Express คืออะไร

Express คือเฟรมเวิร์กที่ช่วยให้สร้างเว็บเซิร์ฟเวอร์ได้ง่ายขึ้น

เราต้องใช้มันเพราะมันช่วยจัดการเส้นทาง (route), คำขอ (request) และคำตอบ (response) ได้สะดวก

## 3. เซิร์ฟเวอร์พื้นฐาน

```js
import express from 'express';

const app = express();

app.get('/', (req, res) => {
  res.json({ message: 'Hello' });
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

## 4. คำขอและคำตอบ

- `req` คือข้อมูลที่เข้ามาจากคนเรียกเส้นทาง
- `res` คือสิ่งที่เราส่งกลับไป

## โจทย์ที่ต้องทำ

ให้แก้ไฟล์:

```txt
exercises/ch17-basic-server.js
```

ให้ทำตามนี้:

1. สร้างแอป Express
2. สร้างเส้นทาง `GET /`
   - คืน `{ message: 'Hello from server' }`
3. สร้างเส้นทาง `GET /about`
   - คืน `{ project: 'Learn Project', type: 'backend practice' }`
4. สร้างเส้นทาง `GET /status`
   - คืน `{ ok: true }`
5. ให้เซิร์ฟเวอร์เริ่มรับฟังที่พอร์ต (port) `3000`

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch17
```
