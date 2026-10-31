# บทที่ 2: ตัวแปรและชนิดข้อมูล

## ทบทวน

บทที่แล้วเราใช้ `console.log()` เพื่อพิมพ์ข้อความออกมาที่เทอร์มินัล (terminal)

บทนี้เราจะเริ่มเก็บข้อมูลไว้ใน "ตัวแปร"

## 1. ตัวแปร (variable) คืออะไร

ตัวแปรคือตัวเก็บข้อมูลที่มีชื่อ เหมือนกล่องที่แปะป้ายไว้

เราต้องใช้ตัวแปรเพราะโปรแกรมต้องจำข้อมูลไว้ใช้ต่อ เช่น ชื่อ อายุ หรือสถานะผู้ใช้

```js
const userName = 'Student';

console.log(userName);
```

ผลลัพธ์:
```txt
Student
```

## 2. `const`

`const` ใช้สร้างตัวแปรที่ไม่ควรถูกกำหนดค่าใหม่

เราควรใช้ `const` เป็นค่าเริ่มต้น เพราะมันช่วยป้องกันการเผลอเปลี่ยนค่าที่ไม่ควรเปลี่ยน

```js
const userName = 'Neo';

console.log(userName);
```

ผลลัพธ์:
```txt
Neo
```

## 3. `let`

`let` ใช้สร้างตัวแปรที่เราตั้งใจจะเปลี่ยนค่าในภายหลัง

เราต้องใช้ `let` เมื่อข้อมูลมีการเปลี่ยน เช่น คะแนน จำนวนสินค้า หรือรอบการนับ

```js
let score = 0;
score = 10;

console.log(score);
```

ผลลัพธ์:
```txt
10
```

## 4. ทำไมไม่ใช้ `var`

`var` เป็นวิธีเก่าในการสร้างตัวแปร

เราจะยังไม่ใช้ `var` เพราะมันมีปัญหาเรื่องขอบเขตการใช้งาน (scope) และทำให้โค้ดเดายากกว่า `const`/`let`

```js
var oldStyle = 'avoid this';

console.log(oldStyle);
```

ผลลัพธ์:
```txt
avoid this
```

## 5. ชนิดข้อมูล (data type) พื้นฐาน

ชนิดข้อมูลคือชนิดของข้อมูล

เราต้องรู้ชนิดข้อมูลเพราะ JavaScript จัดการข้อความ (string), number, ค่าจริงเท็จ (boolean), null, undefined ไม่เหมือนกัน

```js
const userName = 'Mint';
const userAge = 17;
const isStudent = true;

console.log(userName);
console.log(userAge);
console.log(isStudent);
```

ผลลัพธ์:
```txt
Mint
17
true
```

## 6. `null` และ `undefined`

`undefined` มักหมายถึงยังไม่มีค่า ส่วน `null` มักหมายถึงตั้งใจให้ไม่มีค่า

เราต้องเข้าใจสองตัวนี้ เพราะฝั่งเซิร์ฟเวอร์เจอข้อมูลหายหรือว่างบ่อยมาก

```js
let email;
const nickname = null;

console.log(email);
console.log(nickname);
```

ผลลัพธ์:
```txt
undefined
null
```

## 7. `typeof`

`typeof` ใช้เช็กชนิดข้อมูลของค่า

เราต้องใช้มันเพื่อดูว่า JavaScript มองค่าหนึ่งเป็นชนิดอะไร

```js
console.log(typeof 'hello');
console.log(typeof 20);
console.log(typeof true);
```

ผลลัพธ์:
```txt
string
number
boolean
```

## 8. การแปลงชนิดข้อมูลอัตโนมัติ (type coercion) แบบพื้นฐาน

การแปลงชนิดข้อมูลอัตโนมัติคือการที่ JavaScript แปลงชนิดข้อมูลให้เอง

เราต้องรู้เรื่องนี้ เพราะบางครั้งผลลัพธ์อาจไม่ตรงกับที่คิด

```js
console.log('5' + 3);
console.log('5' - 3);
```

ผลลัพธ์:
```txt
53
2
```

ทำไมผลลัพธ์ต่างกัน:

- `'5' + 3` กลายเป็นข้อความต่อกัน
- `'5' - 3` JavaScript พยายามแปลง `'5'` เป็น number ก่อนลบ

## โจทย์ที่ต้องทำ

ให้แก้ไฟล์:

```txt
exercises/ch02-user-profile.js
```

เป้าหมาย:

1. สร้างข้อมูลโปรไฟล์ (profile) ของตัวเอง
2. ใช้ `typeof` เช็กชนิดข้อมูล
3. ลองดูการแปลงชนิดข้อมูลอัตโนมัติจากตัวอย่าง

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch2
```
