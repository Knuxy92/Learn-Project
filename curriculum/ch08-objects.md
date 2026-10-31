# บทที่ 8: object

## ทบทวน

บทที่แล้วเราใช้เมธอด (method) ของ array เพื่อจัดการข้อมูลหลายตัว

บทนี้เราจะเรียนออบเจ็กต์ (object) ซึ่งเป็นรูปแบบข้อมูลที่ใช้บ่อยมากใน JavaScript และฝั่งเซิร์ฟเวอร์ (backend)

## 1. Object คืออะไร

ออบเจ็กต์ คือกล่องข้อมูลที่เก็บค่าเป็นคู่ `key: value`

เราต้องใช้ออบเจ็กต์เพราะข้อมูลจริงมักมีหลายฟิลด์ (field) เช่น ชื่อ อายุ ยอดเงิน หรือสถานะ

```js
const user = {
  name: 'Student',
  age: 17,
};

console.log(user);
```

ผลลัพธ์:

```txt
{ name: 'Student', age: 17 }
```

## 2. Dot Notation

การอ่านค่าด้วยจุด (dot notation) ใช้อ่านคุณสมบัติ (property) ของออบเจ็กต์

เราต้องใช้มันเพราะเป็นวิธีที่อ่านง่ายและใช้บ่อยที่สุด

```js
const user = {
  name: 'Neo',
  age: 20,
};

console.log(user.name);
console.log(user.age);
```

ผลลัพธ์:

```txt
Neo
20
```

## 3. Bracket Notation

วงเล็บเหลี่ยม (bracket notation) ใช้อ่านคุณสมบัติด้วยข้อความ (string)

เราต้องรู้มันเพราะบางครั้งชื่อคุณสมบัติมาจากตัวแปร

```js
const user = {
  name: 'Neo',
};

console.log(user['name']);
```

ผลลัพธ์:

```txt
Neo
```

## 4. Add / Change Properties

เราเพิ่มหรือแก้คุณสมบัติได้

เราต้องรู้มันเพราะออบเจ็กต์ในโปรแกรมจริงมักมีการเปลี่ยนข้อมูล

```js
const user = {
  name: 'Neo',
};

user.age = 20;
user.name = 'Mint';

console.log(user);
```

ผลลัพธ์:

```txt
{ name: 'Mint', age: 20 }
```

## 5. Methods

เมธอด คือฟังก์ชัน (function) ที่อยู่ข้างในออบเจ็กต์

เราต้องใช้มันเมื่อออบเจ็กต์ไม่ได้มีแค่ข้อมูล แต่มีพฤติกรรม (behavior) ด้วย

```js
const bankAccount = {
  owner: 'Neo',
  balance: 1000,
  getBalance() {
    return this.balance;
  },
};

console.log(bankAccount.getBalance());
```

ผลลัพธ์:

```txt
1000
```

## 6. Destructuring

การแยกค่าออกจากโครงสร้าง (destructuring) คือการดึงคุณสมบัติออกมาเก็บในตัวแปร

เราต้องใช้มันเพราะช่วยให้โค้ดสั้นและอ่านง่ายขึ้น

```js
const user = {
  name: 'Neo',
  age: 20,
};

const { name, age } = user;

console.log(name);
console.log(age);
```

ผลลัพธ์:

```txt
Neo
20
```

## 7. Spread Operator

การกระจายค่า (spread) ด้วย `{ ...obj }` ใช้คัดลอกหรือขยายออบเจ็กต์เดิม

เราต้องใช้มันเพราะช่วยสร้างออบเจ็กต์ใหม่จากของเดิมได้ง่าย

```js
const user = {
  name: 'Neo',
  age: 20,
};

const updatedUser = {
  ...user,
  age: 21,
};

console.log(updatedUser);
```

ผลลัพธ์:

```txt
{ name: 'Neo', age: 21 }
```

## โจทย์ที่ต้องทำ

ให้แก้ไฟล์:

```txt
exercises/ch08-bank-account.js
```

ให้สร้างออบเจ็กต์ชื่อ `bankAccount` ที่มี:

- `owner`
- `balance`
- `currency`

จากนั้นให้ทำตามนี้:

1. พิมพ์ชื่อเจ้าของบัญชี
2. เพิ่มคุณสมบัติ `isActive`
3. เปลี่ยน `balance` ให้มากขึ้น
4. สร้างเมธอด `deposit(amount)` ที่เพิ่มเงินเข้าไปในยอดเงิน
5. สร้างเมธอด `withdraw(amount)` ที่ลดเงินออกจากยอดเงิน
6. สร้างเมธอด `getBalance()` ที่คืนค่ายอดเงิน
7. ใช้การแยกค่าออกจากโครงสร้างดึง `owner` และ `currency`
8. ใช้การกระจายค่าสร้าง `accountSummary` จาก `bankAccount` แล้วเพิ่ม `bankName`

ผลลัพธ์ที่คาดหวัง ไม่ต้องเหมือนเป๊ะทุกตัวอักษร
แต่ต้องแสดงครบว่า:

- ชื่อเจ้าของบัญชีคืออะไร
- ยอดเงินเปลี่ยนได้
- เมธอดทำงานได้
- การแยกค่าออกจากโครงสร้างทำงานได้
- การกระจายค่าสร้างออบเจ็กต์ใหม่ได้

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch8
```
