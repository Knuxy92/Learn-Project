# Chapter 2: Variables & Data Types

## Recap

บทที่แล้วเราใช้ `console.log()` เพื่อพิมพ์ข้อความออกมาที่ terminal

บทนี้เราจะเริ่มเก็บข้อมูลไว้ใน "ตัวแปร"

## 1. Variable คืออะไร

Variable คือตัวเก็บข้อมูลที่มีชื่อ เหมือนกล่องที่แปะป้ายไว้

เราต้องใช้ variable เพราะโปรแกรมต้องจำข้อมูลไว้ใช้ต่อ เช่น ชื่อ อายุ หรือสถานะผู้ใช้

```js
const userName = 'Knuxy92';

console.log(userName);
```

Output:

```txt
Knuxy92
```

## 2. `const`

`const` ใช้สร้างตัวแปรที่ไม่ควรถูก assign ค่าใหม่

เราควรใช้ `const` เป็นค่าเริ่มต้น เพราะมันช่วยกันการเผลอเปลี่ยนค่าที่ไม่ควรเปลี่ยน

```js
const userName = 'Neo';

console.log(userName);
```

Output:

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

Output:

```txt
10
```

## 4. ทำไมไม่ใช้ `var`

`var` เป็นวิธีเก่าในการสร้างตัวแปร

เราจะยังไม่ใช้ `var` เพราะมันมีปัญหาเรื่อง scope และทำให้โค้ดเดายากกว่า `const`/`let`

```js
var oldStyle = 'avoid this';

console.log(oldStyle);
```

Output:

```txt
avoid this
```

## 5. Data Types พื้นฐาน

Data type คือชนิดของข้อมูล

เราต้องรู้ data type เพราะ JavaScript จัดการ string, number, boolean, null, undefined ไม่เหมือนกัน

```js
const userName = 'Mint';
const userAge = 17;
const isStudent = true;

console.log(userName);
console.log(userAge);
console.log(isStudent);
```

Output:

```txt
Mint
17
true
```

## 6. `null` และ `undefined`

`undefined` มักหมายถึงยังไม่มีค่า ส่วน `null` มักหมายถึงตั้งใจให้ไม่มีค่า

เราต้องเข้าใจสองตัวนี้ เพราะ backend เจอข้อมูลหายหรือว่างบ่อยมาก

```js
let email;
const nickname = null;

console.log(email);
console.log(nickname);
```

Output:

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

Output:

```txt
string
number
boolean
```

## 8. Type Coercion แบบพื้นฐาน

Type coercion คือการที่ JavaScript แปลงชนิดข้อมูลให้อัตโนมัติ

เราต้องรู้เรื่องนี้ เพราะบางครั้งผลลัพธ์อาจไม่ตรงกับที่คิด

```js
console.log('5' + 3);
console.log('5' - 3);
```

Output:

```txt
53
2
```

ทำไมผลลัพธ์ต่างกัน:

- `'5' + 3` กลายเป็น string ต่อกัน
- `'5' - 3` JavaScript พยายามแปลง `'5'` เป็น number ก่อนลบ

## Guided Exercise

ให้แก้ไฟล์:

```txt
exercises/ch02-user-profile.js
```

เป้าหมาย:

1. สร้างข้อมูล profile ของตัวเอง
2. ใช้ `typeof` เช็กชนิดข้อมูล
3. ลองดู type coercion จากตัวอย่าง

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch2
```
