# บทที่ 5: ฟังก์ชัน

## ทบทวน

บทที่แล้วเราใช้ `if / else` และ `switch` เพื่อให้โปรแกรมตัดสินใจ

บทนี้เราจะเอาโค้ดที่ใช้ซ้ำได้ไปเก็บไว้ในฟังก์ชัน (function)

## 1. Function คืออะไร

ฟังก์ชัน คือชุดคำสั่งที่ตั้งชื่อไว้ แล้วเรียกใช้ซ้ำได้

เราต้องใช้ฟังก์ชันเพราะมันช่วยลดการเขียนซ้ำและทำให้โค้ดเป็นระเบียบ

```js
function sayHello() {
  console.log('Hello');
}

sayHello();
```

ผลลัพธ์:
```txt
Hello
```

## 2. Arrow Function

ฟังก์ชันลูกศร (arrow function) คือวิธีเขียนฟังก์ชันแบบที่เราจะใช้เป็นหลักในบทต่อ ๆ ไป

เราต้องรู้มันเพราะโค้ด JavaScript สมัยใหม่ใช้รูปแบบนี้บ่อยมาก

```js
const sayHello = () => {
  console.log('Hello');
};

sayHello();
```

ผลลัพธ์:
```txt
Hello
```

## 3. Parameters และ Arguments

พารามิเตอร์ (parameter) คือชื่อช่องรับข้อมูลในฟังก์ชัน

อาร์กิวเมนต์ (argument) คือค่าจริงที่เราส่งเข้าไปตอนเรียกฟังก์ชัน

```js
const greetUser = (userName) => {
  console.log(`Hello ${userName}`);
};

greetUser('Student');
```

ผลลัพธ์:
```txt
Hello Student
```

## 4. Return Value

`return` คือการส่งค่ากลับออกมาจากฟังก์ชัน

เราต้องใช้ `return` เมื่ออยากเอาผลลัพธ์ไปใช้ต่อ

```js
const add = (firstNumber, secondNumber) => {
  return firstNumber + secondNumber;
};

console.log(add(2, 3));
```

ผลลัพธ์:
```txt
5
```

## 5. Default Parameters

พารามิเตอร์ค่าเริ่มต้น คือค่าที่ฟังก์ชันใช้เมื่อไม่ได้ส่งอาร์กิวเมนต์มา

เราต้องใช้มันเพื่อให้ฟังก์ชันมีค่าปลอดภัยตอนข้อมูลบางตัวไม่ได้ถูกส่งมา

```js
const greetUser = (userName = 'Guest') => {
  return `Hello ${userName}`;
};

console.log(greetUser());
```

ผลลัพธ์:
```txt
Hello Guest
```

## 6. Scope แบบสั้น

ขอบเขต (scope) คือพื้นที่ที่ตัวแปรถูกใช้งานได้

เราต้องเข้าใจขอบเขตเพราะตัวแปรที่สร้างในฟังก์ชันจะไม่ถูกใช้ข้างนอกฟังก์ชันโดยตรง

```js
const createMessage = () => {
  const message = 'Inside function';
  return message;
};

console.log(createMessage());
```

ผลลัพธ์:
```txt
Inside function
```

## โจทย์ที่ต้องทำ

ให้แก้ไฟล์:

```txt
exercises/ch05-utility-functions.js
```

ต้องสร้างฟังก์ชันต่อไปนี้:

1. `calculateTax(price, rate)`
   คืนค่าภาษีจาก `price * rate`

2. `formatName(firstName, lastName)`
   คืนข้อความรูปแบบ `First Last`

3. `isEven(number)`
   คืน `true` ถ้าเลขหาร 2 ลงตัว
   คืน `false` ถ้าไม่ลงตัว

4. `greetUser(userName = 'Guest')`
   คืนข้อความรูปแบบ `Hello Guest` หรือ `Hello Student`

ผลลัพธ์ที่คาดหวัง:

```txt
Tax: 70
Full name: Student Dev
Is 10 even: true
Is 7 even: false
Hello Guest
Hello Student
```

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch5
```
