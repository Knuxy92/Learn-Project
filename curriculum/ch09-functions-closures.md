# บทที่ 9: ฟังก์ชันและ closure เพิ่มเติม

## ทบทวน

บทที่แล้วเราเรียนออบเจ็กต์ (object), เมธอด (method), การแยกค่าออกจากโครงสร้าง (destructuring) และการกระจายค่า (spread)

บทนี้เราจะอยู่กับฟังก์ชัน (function) ต่อ แต่จะลึกขึ้นอีกนิด โดยเฉพาะเรื่องฟังก์ชันตอบกลับ (callback) และคลอเชอร์ (closure)

## 1. Callback คืออะไร

ฟังก์ชันตอบกลับ คือฟังก์ชันที่ถูกส่งเข้าไปให้ฟังก์ชันอื่นเรียกใช้อีกที

เราต้องรู้เรื่องฟังก์ชันตอบกลับ เพราะ JavaScript ใช้มันบ่อยมาก โดยเฉพาะกับเมธอดของ array และโค้ดอะซิงค์ (async)

```js
const numbers = [1, 2, 3];

numbers.forEach((number) => {
  console.log(number);
});
```

ผลลัพธ์:

```txt
1
2
3
```

## 2. Higher-Order Function คืออะไร

ฟังก์ชันระดับสูง (higher-order function) คือฟังก์ชันที่รับฟังก์ชันอื่นเข้ามา หรือคืนฟังก์ชันออกไป

เราต้องรู้มันเพราะฟังก์ชันตอบกลับและคลอเชอร์มักเกิดในรูปแบบนี้

```js
const runTask = (task) => {
  task();
};

runTask(() => {
  console.log('Task finished');
});
```

ผลลัพธ์:

```txt
Task finished
```

## 3. Closure คืออะไร

คลอเชอร์ คือฟังก์ชันที่ยังจำค่าจากข้างนอกตัวมันได้ แม้ฟังก์ชันด้านนอกจะทำงานจบไปแล้ว

เราต้องรู้มันเพราะมันช่วยให้เราเก็บค่าไว้ใช้เป็นการส่วนตัวได้

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

ผลลัพธ์:

```txt
1
2
```

## 4. Rest Parameters

พารามิเตอร์ที่เก็บค่าที่เหลือ (rest parameter) ใช้รับอาร์กิวเมนต์ (argument) หลายตัวแล้วรวมเป็น array

เราต้องใช้มันเมื่อไม่รู้ล่วงหน้าว่าจะมีค่าถูกส่งมากี่ตัว

```js
const addAll = (...numbers) => {
  return numbers.reduce((sum, number) => sum + number, 0);
};

console.log(addAll(10, 20, 30));
```

ผลลัพธ์:

```txt
60
```

## 5. Spread in Function Calls

การกระจายค่าในตอนเรียกฟังก์ชัน ใช้ดึงค่าจาก array ออกมาเป็นอาร์กิวเมนต์หลายตัว

เราต้องใช้มันเมื่อมีข้อมูลอยู่ใน array แต่ฟังก์ชันต้องการอาร์กิวเมนต์แยกกัน

```js
const add = (firstNumber, secondNumber) => {
  return firstNumber + secondNumber;
};

const values = [5, 7];

console.log(add(...values));
```

ผลลัพธ์:

```txt
12
```

## โจทย์ที่ต้องทำ

ให้แก้ไฟล์:

```txt
exercises/ch09-create-counter.js
```

ให้ทำตามนี้:

1. สร้างฟังก์ชัน `createCounter()`
   มันต้องคืนออบเจ็กต์ที่มี:
   - `increment()`
   - `decrement()`
   - `getCount()`

2. ใช้คลอเชอร์ให้ `count` ถูกเก็บไว้ภายใน `createCounter`

3. สร้างฟังก์ชัน `sumAll(...numbers)`
   ใช้พารามิเตอร์ที่เก็บค่าที่เหลือรับเลขหลายตัว
   และคืนผลรวม

4. สร้าง array `values = [10, 20, 30]`
   แล้วใช้การกระจายค่าส่งเข้า `sumAll`

ผลลัพธ์ที่คาดหวัง:

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
