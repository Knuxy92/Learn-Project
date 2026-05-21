# Chapter 9: More on Functions & Closures

## Recap

บทที่แล้วเราเรียน object, methods, destructuring, และ spread

บทนี้เราจะอยู่กับ function ต่อ แต่จะลึกขึ้นอีกนิด โดยเฉพาะเรื่อง callback และ closure

## 1. Callback คืออะไร

Callback คือ function ที่ถูกส่งเข้าไปให้ function อื่นเรียกใช้อีกที

เราต้องรู้ callback เพราะ JavaScript ใช้มันบ่อยมาก โดยเฉพาะกับ array methods และ async code

```js
const numbers = [1, 2, 3];

numbers.forEach((number) => {
  console.log(number);
});
```

Output:

```txt
1
2
3
```

## 2. Higher-Order Function คืออะไร

Higher-order function คือ function ที่รับ function อื่นเข้ามา หรือคืน function ออกไป

เราต้องรู้มันเพราะ callback และ closures มักเกิดในรูปแบบนี้

```js
const runTask = (task) => {
  task();
};

runTask(() => {
  console.log('Task finished');
});
```

Output:

```txt
Task finished
```

## 3. Closure คืออะไร

Closure คือ function ที่ยังจำค่าจากข้างนอกตัวมันได้ แม้ function ด้านนอกจะทำงานจบไปแล้ว

เราต้องรู้มันเพราะมันช่วยให้เราเก็บ state แบบเป็นส่วนตัวได้

```js
const createCounter = () => {
  let count = 0;

  return () => {
    count += 1;
    return count;
  };
};

const counter = createCounter();

console.log(counter());
console.log(counter());
```

Output:

```txt
1
2
```

## 4. Rest Parameters

Rest parameter ใช้รับ argument หลายตัวแล้วรวมเป็น array

เราต้องใช้มันเมื่อไม่รู้ล่วงหน้าว่าจะมีค่าถูกส่งมากี่ตัว

```js
const addAll = (...numbers) => {
  return numbers.reduce((sum, number) => sum + number, 0);
};

console.log(addAll(10, 20, 30));
```

Output:

```txt
60
```

## 5. Spread in Function Calls

Spread ใน function call ใช้กระจายค่าจาก array ออกมาเป็น argument หลายตัว

เราต้องใช้มันเมื่อมีข้อมูลอยู่ใน array แต่ function ต้องการ argument แยกกัน

```js
const add = (firstNumber, secondNumber) => {
  return firstNumber + secondNumber;
};

const values = [5, 7];

console.log(add(...values));
```

Output:

```txt
12
```

## Guided Exercise

ให้แก้ไฟล์:

```txt
exercises/ch09-create-counter.js
```

ให้ทำตามนี้:

1. สร้าง function `createCounter()`
   มันต้องคืน object ที่มี:
   - `increment()`
   - `decrement()`
   - `getCount()`

2. ใช้ closure ให้ `count` ถูกเก็บไว้ภายใน `createCounter`

3. สร้าง function `sumAll(...numbers)`
   ใช้ rest parameter รับเลขหลายตัว
   และคืนผลรวม

4. สร้าง array `values = [10, 20, 30]`
   แล้วใช้ spread ส่งเข้า `sumAll`

Expected output:

```txt
Count: 0
After increment: 1
After increment again: 2
After decrement: 1
Current count: 1
Sum all: 60
```

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch9
```
