# Chapter 10: Working with Strings & Dates

## Recap

บทที่แล้วเราเรียน callback, closure, rest, และ spread ใน function calls

บทนี้เราจะใช้สิ่งที่พบเจอบ่อยมากในโปรแกรมจริง:

- string methods
- template literals
- regex basics
- Date basics

## 1. String Methods

String methods คือเครื่องมือที่ใช้จัดการข้อความ

เราต้องใช้มันเพราะข้อมูลจากผู้ใช้มักมาเป็นข้อความ เช่น ชื่อ อีเมล รหัสผ่าน หรือคำค้นหา

```js
const userName = '  knuxy92  ';

console.log(userName.trim());
console.log(userName.toUpperCase());
```

Output:

```txt
knuxy92
  KNUXY92  
```

## 2. Template Literals

Template literal คือการใส่ตัวแปรลงในข้อความด้วย backticks

เราต้องใช้มันเพราะมันอ่านง่ายกว่าการต่อ string ยาว ๆ

```js
const firstName = 'Knuxy';
const lastName = 'Dev';

console.log(`${firstName} ${lastName}`);
```

Output:

```txt
Knuxy Dev
```

## 3. Regex Basics

Regex คือ pattern สำหรับเช็กว่าข้อความตรงรูปแบบที่ต้องการไหม

เราต้องใช้มันเพราะการ validate ข้อความ เช่น อีเมลหรือรหัสผ่าน มักต้องใช้ pattern

```js
const email = 'test@example.com';
const emailPattern = /@/;

console.log(emailPattern.test(email));
```

Output:

```txt
true
```

## 4. Date Basics

`Date` คือ object ที่ใช้เก็บวันและเวลา

เราต้องใช้มันเพราะข้อมูลจริงมักมีวันที่ เช่น createdAt หรือ updatedAt

```js
const today = new Date();

console.log(today.toISOString());
```

Output:

```txt
2026-04-26T...
```

## 5. Guided Exercise

ให้แก้ไฟล์:

```txt
exercises/ch10-string-validator.js
```

ให้ทำ function ต่อไปนี้:

1. `formatUserName(userName)`
   - ใช้ `.trim()`
   - ใช้ `.toUpperCase()`

2. `isValidEmail(email)`
   - ใช้ regex แบบง่าย
   - แค่เช็กว่ามี `@` และ `.`

3. `getPasswordStrength(password)`
   - ถ้า length < 8 ให้คืน `'weak'`
   - ถ้า length >= 8 ให้คืน `'strong'`

4. `formatWelcomeMessage(firstName, lastName)`
   - ใช้ template literal
   - คืนข้อความ `Welcome Knuxy Dev`

5. `formatToday()`
   - สร้าง `new Date()`
   - คืนค่าจาก `.toLocaleDateString()`

Expected output ไม่ต้องตรงวันที่เป๊ะ
แต่ต้องมีครบว่า:

- format username ได้
- email ผ่าน/ไม่ผ่านได้
- password strength ทำงานได้
- welcome message ถูก
- date ถูกแสดงออกมา

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch10
```
