# Chapter 17: Node.js & Express Basics

## Recap

ตอนนี้เราเรียน JavaScript และ TypeScript foundation ครบแล้ว

บทนี้เราจะเริ่มเข้า backend จริงด้วย Node.js และ Express

## 1. Node.js คืออะไร

Node.js คือ runtime ที่ทำให้ JavaScript รันนอก browser ได้

เราต้องใช้มันเพราะ backend server ของเราจะรันด้วย Node.js

## 2. Express คืออะไร

Express คือ framework ที่ช่วยให้สร้าง web server ได้ง่ายขึ้น

เราต้องใช้มันเพราะมันช่วยจัดการ routes, request, และ response ได้สะดวก

## 3. Basic Server

```ts
import express from 'express';

const app = express();

app.get('/', (req, res) => {
  res.json({ message: 'Hello' });
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

## 4. Request และ Response

- `req` คือข้อมูลที่เข้ามาจากคนเรียก route
- `res` คือสิ่งที่เราส่งกลับไป

## Guided Exercise

ให้แก้ไฟล์:

```txt
exercises/ch17-basic-server.ts
```

ให้ทำตามนี้:

1. สร้าง Express app
2. สร้าง route `GET /`
   - คืน `{ message: 'Hello from server' }`
3. สร้าง route `GET /about`
   - คืน `{ project: 'Learn Project', type: 'backend practice' }`
4. สร้าง route `GET /status`
   - คืน `{ ok: true }`
5. ให้ server listen ที่ port `3000`

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch17
```
