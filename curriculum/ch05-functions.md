# Chapter 5: Functions

## Recap

บทที่แล้วเราใช้ `if / else` และ `switch` เพื่อให้โปรแกรมตัดสินใจ

บทนี้เราจะเอาโค้ดที่ใช้ซ้ำได้ไปเก็บไว้ใน function

## 1. Function คืออะไร

Function คือชุดคำสั่งที่ตั้งชื่อไว้ แล้วเรียกใช้ซ้ำได้

เราต้องใช้ function เพราะมันช่วยลดการเขียนซ้ำและทำให้โค้ดเป็นระเบียบ

```js
function sayHello() {
  console.log('Hello');
}

sayHello();
```

Output:

```txt
Hello
```

## 2. Arrow Function

Arrow function คือวิธีเขียน function แบบที่เราจะใช้เป็นหลักในบทต่อ ๆ ไป

เราต้องรู้มันเพราะโค้ด JavaScript สมัยใหม่ใช้รูปแบบนี้บ่อยมาก

```js
const sayHello = () => {
  console.log('Hello');
};

sayHello();
```

Output:

```txt
Hello
```

## 3. Parameters และ Arguments

Parameter คือชื่อช่องรับข้อมูลใน function

Argument คือค่าจริงที่เราส่งเข้าไปตอนเรียก function

```js
const greetUser = (userName) => {
  console.log(`Hello ${userName}`);
};

greetUser('Knuxy92');
```

Output:

```txt
Hello Knuxy92
```

## 4. Return Value

`return` คือการส่งค่ากลับออกมาจาก function

เราต้องใช้ `return` เมื่ออยากเอาผลลัพธ์ไปใช้ต่อ

```js
const add = (firstNumber, secondNumber) => {
  return firstNumber + secondNumber;
};

console.log(add(2, 3));
```

Output:

```txt
5
```

## 5. Default Parameters

Default parameter คือค่าเริ่มต้นที่ function ใช้เมื่อไม่ได้ส่ง argument มา

เราต้องใช้มันเพื่อให้ function มีค่าปลอดภัยตอนข้อมูลบางตัวไม่ได้ถูกส่งมา

```js
const greetUser = (userName = 'Guest') => {
  return `Hello ${userName}`;
};

console.log(greetUser());
```

Output:

```txt
Hello Guest
```

## 6. Scope แบบสั้น

Scope คือพื้นที่ที่ตัวแปรสามารถถูกใช้งานได้

เราต้องเข้าใจ scope เพราะตัวแปรที่สร้างใน function จะไม่ถูกใช้ข้างนอก function โดยตรง

```js
const createMessage = () => {
  const message = 'Inside function';
  return message;
};

console.log(createMessage());
```

Output:

```txt
Inside function
```

## Guided Exercise

ให้แก้ไฟล์:

```txt
exercises/ch05-utility-functions.js
```

ต้องสร้าง function ต่อไปนี้:

1. `calculateTax(price, rate)`
   คืนค่า tax จาก `price * rate`

2. `formatName(firstName, lastName)`
   คืน string รูปแบบ `First Last`

3. `isEven(number)`
   คืน `true` ถ้าเลขหาร 2 ลงตัว
   คืน `false` ถ้าไม่ลงตัว

4. `greetUser(userName = 'Guest')`
   คืน string รูปแบบ `Hello Guest` หรือ `Hello Knuxy92`

Expected output:

```txt
Tax: 70
Full name: Knuxy Dev
Is 10 even: true
Is 7 even: false
Hello Guest
Hello Knuxy92
```

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch5
```
