# บทที่ 13: module และการแยกไฟล์

## ทบทวน

บทที่แล้วเราเรียนอะซิงค์ (async) ด้วย `Promise`, `async` / `await` และ `fetch()`

จนถึงตอนนี้เราเขียนโค้ดอยู่ในไฟล์เดียวทั้งหมด แต่โปรแกรมจริงแยกหลายไฟล์

## 1. ทำไมต้องแยกไฟล์

โค้ดที่โตขึ้นจะเริ่มมีปัญหา:

- ไฟล์เดียวยาวจนหาโค้ดไม่เจอ
- แก้ส่วนหนึ่งไปกระทบอีกส่วนโดยไม่ตั้งใจ
- ใช้โค้ดซ้ำหลายที่แล้วต้องคัดลอกมาวาง

การแยกไฟล์ช่วยให้แต่ละไฟล์มีหน้าที่ชัด และกลับมาแก้ได้ง่าย

## 2. `export` และ `import`

ใน JavaScript สมัยใหม่ (ESM) เราใช้ `export` เพื่อส่งออกค่าไป และ `import` เพื่อดึงมาใช้

```js
// math.js
export const add = (a, b) => a + b;

export const PI = 3.14159;
```

```js
// main.js
import { add, PI } from './math.js';

console.log(add(2, 3));
console.log(PI);
```

ผลลัพธ์:

```txt
5
3.14159
```

จุดที่ต้องระวัง: ต้องใส่ `.js` ในเส้นทางไฟล์ (path) ด้วย เพราะ ESM ไม่เดานามสกุลให้

## 3. `export default`

แต่ละไฟล์มี `export default` ได้หนึ่งอัน ใช้เมื่อไฟล์นั้นมีของหลักชิ้นเดียว

```js
// greet.js
const greet = (name) => `Hello ${name}`;

export default greet;
```

```js
// main.js
import greet from './greet.js';

console.log(greet('Student'));
```

ผลลัพธ์:

```txt
Hello Student
```

ต่างกันตรงที่ `export default` ไม่ต้องใส่ `{ }` ตอนนำเข้า และตั้งชื่ออะไรก็ได้

## 4. Named export กับ default export ใช้ตอนไหน

- ไฟล์ที่มีหลายอย่างให้ใช้ (เช่น `utils.js`) ใช้การส่งออกแบบมีชื่อ (named export)
- ไฟล์ที่เป็นเรื่องเดียวจบ (เช่น `app.js`) ใช้การส่งออกค่าเริ่มต้นได้

ทั้งสองแบบใช้ร่วมกันในไฟล์เดียวได้ แต่แนะนำให้เลือกให้สม่ำเสมอทั้งโปรเจกต์

## 5. `package.json` กับ `"type": "module"`

Node.js ต้องรู้ว่าไฟล์ `.js` ของเราเป็น ESM หรือ CommonJS

ถ้าใส่ `"type": "module"` ใน `package.json` ทุกไฟล์ `.js` จะเป็น ESM

```json
{
  "name": "learn-project",
  "type": "module"
}
```

ถ้าไม่ใส่ Node จะถือว่าเป็น CommonJS ซึ่งใช้ `require()` แบบเก่า

## 6. ตัวอย่าง: แยกโค้ดเป็นสามไฟล์

```js
// tasks.js
const tasks = [
  { id: 1, title: 'Learn JS', done: false },
  { id: 2, title: 'Build API', done: false },
];

export const getAllTasks = () => tasks;

export const addTask = (title) => {
  const nextId = tasks.length === 0 ? 1 : tasks[tasks.length - 1].id + 1;
  const task = { id: nextId, title, done: false };

  tasks.push(task);
  return task;
};
```

```js
// format.js
export const formatTask = (task) => {
  const status = task.done ? 'done' : 'pending';

  return `#${task.id} ${task.title} (${status})`;
};
```

```js
// main.js
import { getAllTasks, addTask } from './tasks.js';
import { formatTask } from './format.js';

addTask('Write docs');

for (const task of getAllTasks()) {
  console.log(formatTask(task));
}
```

ผลลัพธ์:

```txt
#1 Learn JS (pending)
#2 Build API (pending)
#3 Write docs (pending)
```

## โจทย์ที่ต้องทำ

สร้างไฟล์:

```txt
exercises/ch13-modules/calculator.js
exercises/ch13-modules/formatter.js
exercises/ch13-modules/main.js
```

ให้ทำตามนี้:

1. `calculator.js` ทำการส่งออกแบบมีชื่อสองตัว:
   - `add(a, b)` คืนผลบวก
   - `multiply(a, b)` คืนผลคูณ

2. `formatter.js` ทำ `export default`:
   - `formatResult(label, value)` คืนข้อความรูปแบบ `label: value`

3. `main.js`:
   - นำเข้าทั้งสามตัว
   - คำนวณ `add(2, 3)` แล้วพิมพ์ด้วย `formatResult`
   - คำนวณ `multiply(4, 5)` แล้วพิมพ์ด้วย `formatResult`

ผลลัพธ์ที่คาดหวัง:

```txt
Sum: 5
Product: 20
```

## วิธีรัน

```bash
node exercises/ch13-modules/main.js
```

## ผลลัพธ์ที่คาดหวัง

รันแล้วเห็นสองบรรทัดตามด้านบน และไม่มีข้อผิดพลาดเรื่องโมดูล (module)

เสร็จแล้วพิมพ์:

```txt
ตรวจ Ch13
```
