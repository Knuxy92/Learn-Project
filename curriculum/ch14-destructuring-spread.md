# บทที่ 14: destructuring, spread และข้อมูลซ้อนกัน

## ทบทวน

บทที่แล้วเราแยกโค้ดเป็นโมดูล (module) ด้วย `export` / `import`

บทนี้เราจะเรียนไวยากรณ์ที่เจอบ่อยมากในโค้ดฝั่งเซิร์ฟเวอร์ (backend) สมัยใหม่

## 1. Object destructuring

การแยกค่าออกจากโครงสร้าง (destructuring) คือการดึงค่าออกจากออบเจ็กต์ (object) หรือ array มาใส่ตัวแปรทีเดียว

```js
const task = { id: 1, title: 'Learn JS', done: false };

const { id, title } = task;

console.log(id);
console.log(title);
```

ผลลัพธ์:

```txt
1
Learn JS
```

เราใช้มันเพราะโค้ดฝั่งเซิร์ฟเวอร์มักได้ออบเจ็กต์กลับมา แล้วต้องการแค่บางฟิลด์ (field)

## 2. เปลี่ยนชื่อตอน destructuring

```js
const task = { id: 1, title: 'Learn JS' };

const { title: taskTitle } = task;

console.log(taskTitle);
```

ผลลัพธ์:

```txt
Learn JS
```

## 3. ค่า default

ถ้าฟิลด์ไม่มีอยู่ จะได้ `undefined` แต่เราใส่ค่าเริ่มต้น (default) ได้

```js
const { done = false, owner = 'Student' } = { id: 1 };

console.log(done);
console.log(owner);
```

ผลลัพธ์:

```txt
false
Student
```

## 4. Array destructuring

```js
const numbers = [10, 20, 30];

const [first, second] = numbers;

console.log(first);
console.log(second);
```

ผลลัพธ์:

```txt
10
20
```

## 5. Spread

การกระจายค่า (spread) ใช้ `...` กระจายค่าออกมา ใช้บ่อยตอนคัดลอกออบเจ็กต์หรือรวม array

```js
const task = { id: 1, title: 'Learn JS', done: false };

const updated = { ...task, done: true };

console.log(updated);
```

ผลลัพธ์:

```txt
{ id: 1, title: 'Learn JS', done: true }
```

สังเกตว่า `task` เดิมไม่เปลี่ยน เพราะการกระจายค่าสร้างออบเจ็กต์ใหม่

## 6. Rest

การเก็บค่าที่เหลือ (rest) ใช้ `...` เก็บค่าที่เหลือไว้ในตัวแปรเดียว

```js
const { id, ...rest } = { id: 1, title: 'Learn JS', done: false };

console.log(id);
console.log(rest);
```

ผลลัพธ์:

```txt
1
{ title: 'Learn JS', done: false }
```

## 7. ข้อมูลซ้อนกัน

ข้อมูลจาก API มักซ้อนหลายชั้น ต้องเข้าถึงให้ปลอดภัย

```js
const user = {
  name: 'Student',
  address: { city: 'Bangkok' },
};

console.log(user.address.city);
console.log(user.contact?.email);
```

ผลลัพธ์:

```txt
Bangkok
undefined
```

`?.` (optional chaining) คืน `undefined` แทนการโยนข้อผิดพลาด (throw error) เมื่อฟิลด์ก่อนหน้าไม่มี

## 8. ตัวอย่าง: merge ค่าที่อัปเดต

```js
const applyUpdate = (task, updates) => ({ ...task, ...updates });

const task = { id: 1, title: 'Learn JS', done: false };

console.log(applyUpdate(task, { done: true }));
console.log(applyUpdate(task, { title: 'Learn Node' }));
console.log(task);
```

ผลลัพธ์:

```txt
{ id: 1, title: 'Learn JS', done: true }
{ id: 1, title: 'Learn Node', done: false }
{ id: 1, title: 'Learn JS', done: false }
```

## โจทย์ที่ต้องทำ

สร้างไฟล์:

```txt
exercises/ch14-destructuring.js
```

ให้ทำตามนี้:

1. สร้าง `task` ที่มี `id`, `title`, `done`, และ `meta: { priority, tags }`

2. เขียนฟังก์ชัน (function) `describeTask(task)`
   - แยกค่า `title` และ `done`
   - แยกค่า `priority` จาก `meta` พร้อมค่าเริ่มต้น `'normal'`
   - คืนข้อความรูปแบบ `title - done|pending - priority`

3. เขียนฟังก์ชัน `updateTask(task, updates)`
   - ใช้การกระจายค่า คืนออบเจ็กต์ใหม่ที่รวม `updates`
   - ต้องไม่แก้ `task` เดิม

4. เขียนฟังก์ชัน `splitTask(task)`
   - ใช้การเก็บค่าที่เหลือ แยก `id` ออกมา
   - คืนออบเจ็กต์ `{ id, rest }`

5. พิมพ์ผลลัพธ์ของทั้งสามฟังก์ชัน

ตัวอย่างผลลัพธ์:

```txt
Learn JS - pending - high
{ id: 1, title: 'Learn JS', done: true, meta: { priority: 'high', tags: [ 'js' ] } }
{ id: 1, rest: { title: 'Learn JS', done: false, meta: { priority: 'high', tags: [ 'js' ] } } }
```

## วิธีรัน

```bash
node exercises/ch14-destructuring.js
```

## ผลลัพธ์ที่คาดหวัง

รันแล้วเห็นผลลัพธ์ครบสามบรรทัด และ `task` เดิมยังมี `done: false`

เสร็จแล้วพิมพ์:

```txt
ตรวจ Ch14
```
