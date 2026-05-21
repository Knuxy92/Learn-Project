# Chapter 6: Arrays

## Recap

บทที่แล้วเราใช้ function เพื่อเก็บ logic ที่เรียกใช้ซ้ำได้

บทนี้เราจะเริ่มเก็บข้อมูลหลายชิ้นไว้ในตัวแปรเดียวด้วย array

## 1. Array คืออะไร

Array คือกล่องที่เก็บข้อมูลหลายชิ้นเรียงกันเป็นลำดับ

เราต้องใช้ array เพราะข้อมูลจริงมักมาเป็นรายการ เช่น รายการงาน รายชื่อผู้ใช้ หรือสินค้า

```js
const fruits = ['apple', 'banana', 'orange'];

console.log(fruits);
```

Output:

```txt
[ 'apple', 'banana', 'orange' ]
```

## 2. Index

Index คือเลขตำแหน่งของข้อมูลใน array

เราต้องรู้มันเพราะ JavaScript ใช้ index เพื่อดึงข้อมูลออกมาทีละตัว

สำคัญ:

- ตัวแรกอยู่ตำแหน่ง `0`
- ตัวที่สองอยู่ตำแหน่ง `1`
- ตัวที่สามอยู่ตำแหน่ง `2`

```js
const fruits = ['apple', 'banana', 'orange'];

console.log(fruits[0]);
console.log(fruits[1]);
```

Output:

```txt
apple
banana
```

## 3. `.length`

`.length` ใช้บอกจำนวนสมาชิกใน array

เราต้องใช้มันเพื่อรู้ว่ามีข้อมูลกี่ชิ้น

```js
const fruits = ['apple', 'banana', 'orange'];

console.log(fruits.length);
```

Output:

```txt
3
```

## 4. `.push()` และ `.pop()`

`.push()` ใช้เพิ่มข้อมูลต่อท้าย array

`.pop()` ใช้ลบข้อมูลตัวสุดท้ายออก

เราต้องใช้มันเพราะข้อมูลในรายการมักมีเพิ่มและมีลบ

```js
const todos = ['learn JS'];

todos.push('build project');
console.log(todos);

todos.pop();
console.log(todos);
```

Output:

```txt
[ 'learn JS', 'build project' ]
[ 'learn JS' ]
```

## 5. Loop ผ่าน array

เรามักต้องดูข้อมูลทุกตัวใน array

ตอนนี้เริ่มจาก `for...of` ก่อน เพราะอ่านง่าย

```js
const todos = ['learn JS', 'practice code'];

for (const todo of todos) {
  console.log(todo);
}
```

Output:

```txt
learn JS
practice code
```

## Guided Exercise

ให้แก้ไฟล์:

```txt
exercises/ch06-todo-array.js
```

เป้าหมาย:

1. สร้าง array ชื่อ `todos` ที่มีอย่างน้อย 3 งาน
2. พิมพ์ตัวแรกของ array
3. พิมพ์จำนวนงานทั้งหมด
4. ใช้ `.push()` เพิ่มงานใหม่ 1 งาน
5. ใช้ `.pop()` ลบงานสุดท้ายออก 1 งาน
6. ใช้ `for...of` พิมพ์งานทุกตัว

Expected output ไม่จำเป็นต้องเหมือนเป๊ะทุกตัวอักษร
แต่ต้องแสดงครบว่า:

- งานตัวแรกคืออะไร
- มีทั้งหมดกี่งาน
- หลัง push แล้วเป็นยังไง
- หลัง pop แล้วเป็นยังไง
- loop แล้วพิมพ์งานทุกตัวได้

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch6
```
