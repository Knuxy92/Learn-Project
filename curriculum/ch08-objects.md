# บทที่ 8: object

## ทบทวน

บทที่แล้วเราใช้ array methods เพื่อจัดการข้อมูลหลายตัว

บทนี้เราจะเรียน object ซึ่งเป็นรูปแบบข้อมูลที่ใช้บ่อยมากใน JavaScript และ backend

## 1. Object คืออะไร

Object คือกล่องข้อมูลที่เก็บค่าเป็นคู่ `key: value`

เราต้องใช้ object เพราะข้อมูลจริงมักมีหลาย field เช่น ชื่อ อายุ ยอดเงิน หรือสถานะ

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

Dot notation ใช้อ่าน property ของ object

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

Bracket notation ใช้อ่าน property ด้วย string

เราต้องรู้มันเพราะบางครั้งชื่อ property มาจากตัวแปร

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

เราสามารถเพิ่มหรือแก้ property ได้

เราต้องรู้มันเพราะ object ในโปรแกรมจริงมักมีการเปลี่ยนข้อมูล

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

Method คือ function ที่อยู่ข้างใน object

เราต้องใช้มันเมื่อ object ไม่ได้มีแค่ข้อมูล แต่มีพฤติกรรมด้วย

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

Destructuring คือการดึง property ออกมาเก็บในตัวแปร

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

Spread operator `{ ...obj }` ใช้คัดลอกหรือขยาย object เดิม

เราต้องใช้มันเพราะช่วยสร้าง object ใหม่จากของเดิมได้ง่าย

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

ให้สร้าง object ชื่อ `bankAccount` ที่มี:

- `owner`
- `balance`
- `currency`

จากนั้นให้ทำตามนี้:

1. พิมพ์ชื่อเจ้าของบัญชี
2. เพิ่ม property `isActive`
3. เปลี่ยน `balance` ให้มากขึ้น
4. สร้าง method `deposit(amount)` ที่เพิ่มเงินเข้าไปใน balance
5. สร้าง method `withdraw(amount)` ที่ลดเงินออกจาก balance
6. สร้าง method `getBalance()` ที่คืนค่า balance
7. ใช้ destructuring ดึง `owner` และ `currency`
8. ใช้ spread operator สร้าง `accountSummary` จาก `bankAccount` แล้วเพิ่ม `bankName`

ผลลัพธ์ที่คาดหวัง ไม่ต้องเหมือนเป๊ะทุกตัวอักษร
แต่ต้องแสดงครบว่า:

- owner คืออะไร
- balance เปลี่ยนได้
- method ทำงานได้
- destructuring ทำงานได้
- spread สร้าง object ใหม่ได้

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch8
```
