# บทที่ 16: JSON และการตรวจข้อมูล

## ทบทวน

บทที่แล้วเราเรียน built-in module ของ Node.js และเขียนไฟล์ JSON แล้ว

บทนี้เราจะโฟกัสเรื่อง JSON และการตรวจข้อมูลก่อนใช้งานจริง

## 1. JSON คืออะไร

JSON (JavaScript Object Notation) คือรูปแบบข้อความสำหรับแลกเปลี่ยนข้อมูล

backend ใช้ JSON สองทางหลัก:

- รับข้อมูลจาก client เข้ามาเป็น request body
- ส่งข้อมูลกลับไปเป็น response body

ข้อจำกัดที่ต้องรู้:

- key ต้องเป็น string อยู่ในเครื่องหมายคำพูดคู่
- ไม่มี `undefined`, function หรือ comment
- ค่าได้แค่ string, number, boolean, null, array, object

## 2. `JSON.stringify` และ `JSON.parse`

```js
const task = { id: 1, title: 'Learn JS', done: false };

const text = JSON.stringify(task);
const back = JSON.parse(text);

console.log(text);
console.log(back);
```

ผลลัพธ์:

```txt
{"id":1,"title":"Learn JS","done":false}
{ id: 1, title: 'Learn JS', done: false }
```

## 3. `JSON.parse` พังได้

ถ้าข้อความไม่ใช่ JSON ที่ถูกต้อง `JSON.parse` จะ throw error

```js
try {
  JSON.parse('{ bad json }');
} catch (error) {
  console.log('parse failed');
  console.log(error.name);
}
```

ผลลัพธ์:

```txt
parse failed
SyntaxError
```

ดังนั้นทุกครั้งที่ parse ข้อมูลจากภายนอก ต้องเตรียมรับ error

## 4. ตรวจชนิดข้อมูล

JavaScript เป็นภาษา dynamic เราจึงต้องตรวจเองว่า field ที่ได้มาถูกชนิด

```js
const isValidTask = (value) => {
  if (typeof value !== 'object' || value === null) return false;
  if (typeof value.title !== 'string') return false;
  if (value.done !== undefined && typeof value.done !== 'boolean') return false;

  return true;
};

console.log(isValidTask({ title: 'Learn JS' }));
console.log(isValidTask({ title: 123 }));
console.log(isValidTask(null));
```

ผลลัพธ์:

```txt
true
false
false
```

จุดที่พลาดบ่อย: `typeof null` คืน `'object'` จึงต้องเช็ก `value === null` แยก

## 5. ตรวจ array

```js
const isValidTaskList = (value) => {
  if (!Array.isArray(value)) return false;

  return value.every(isValidTask);
};
```

`Array.isArray` เชื่อถือได้กว่า `typeof` เพราะ `typeof []` คืน `'object'`

## 6. แปลงค่าที่มาจาก URL

ค่าใน `req.params` และ query string เป็น string เสมอ ต้องแปลงเอง

```js
const toId = (value) => {
  const id = Number(value);

  return Number.isInteger(id) && id > 0 ? id : null;
};

console.log(toId('12'));
console.log(toId('abc'));
console.log(toId('-3'));
```

ผลลัพธ์:

```txt
12
null
null
```

## 7. ตัวอย่าง: ตรวจ payload ก่อนสร้าง task

```js
const parseCreateTaskBody = (body) => {
  if (typeof body !== 'object' || body === null) {
    return { error: 'Body must be an object' };
  }

  const { title, done } = body;

  if (typeof title !== 'string' || title.trim() === '') {
    return { error: 'Title is required' };
  }

  if (done !== undefined && typeof done !== 'boolean') {
    return { error: 'Done must be a boolean' };
  }

  return { value: { title: title.trim(), done: done ?? false } };
};

console.log(parseCreateTaskBody({ title: '  Learn JS  ' }));
console.log(parseCreateTaskBody({ title: '' }));
console.log(parseCreateTaskBody({ title: 'X', done: 'yes' }));
```

ผลลัพธ์:

```txt
{ value: { title: 'Learn JS', done: false } }
{ error: 'Title is required' }
{ error: 'Done must be a boolean' }
```

## โจทย์ที่ต้องทำ

สร้างไฟล์:

```txt
exercises/ch16-json-validation.js
```

ให้ทำตามนี้:

1. เขียน function `safeParse(text)`
   - คืน `{ ok: true, value }` เมื่อ parse สำเร็จ
   - คืน `{ ok: false, error: 'Invalid JSON' }` เมื่อ parse ไม่สำเร็จ

2. เขียน function `isValidTask(value)`
   - `value` ต้องเป็น object ที่ไม่ใช่ `null`
   - `title` ต้องเป็น string ที่ไม่ว่างหลัง `trim()`
   - `done` ถ้ามี ต้องเป็น boolean

3. เขียน function `parseTaskList(text)`
   - ใช้ `safeParse`
   - ถ้า parse ไม่ผ่าน คืน `{ ok: false, error }`
   - ถ้าข้อมูลไม่ใช่ array หรือมี item ที่ไม่ผ่าน `isValidTask` คืน `{ ok: false, error: 'Invalid task list' }`
   - ถ้าผ่าน คืน `{ ok: true, value }`

4. เขียน function `toId(value)`
   - คืน integer ที่มากกว่า 0
   - ถ้าไม่ใช่ คืน `null`

5. ทดสอบด้วยข้อมูลดีและข้อมูลเสีย อย่างละ 2 เคส แล้วพิมพ์ผลลัพธ์

ตัวอย่างผลลัพธ์:

```txt
{ ok: true, value: [ { id: 1, title: 'Learn JS', done: false } ] }
{ ok: false, error: 'Invalid JSON' }
{ ok: false, error: 'Invalid task list' }
12
null
```

## วิธีรัน

```bash
node exercises/ch16-json-validation.js
```

## ผลลัพธ์ที่คาดหวัง

รันแล้วไม่ throw error และเห็นผลลัพธ์ทั้งกรณีผ่านและไม่ผ่าน

เสร็จแล้วพิมพ์:

```txt
ตรวจ Ch16
```
