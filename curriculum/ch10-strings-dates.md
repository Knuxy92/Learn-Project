# บทที่ 10: การใช้งาน string และวันที่

## ทบทวน

บทที่แล้วเราเรียนฟังก์ชันตอบกลับ (callback), คลอเชอร์ (closure), พารามิเตอร์ที่เก็บค่าที่เหลือ (rest) และการกระจายค่า (spread) ในตอนเรียกฟังก์ชัน

บทนี้เราจะใช้สิ่งที่พบเจอบ่อยมากในโปรแกรมจริง:

- เมธอดของข้อความ (string method)
- การใช้แม่แบบข้อความ (template literal)
- พื้นฐานนิพจน์ปกติ (regex)
- พื้นฐานวันที่ (Date)

## 1. String Methods

เมธอดของข้อความ คือเครื่องมือที่ใช้จัดการข้อความ

เราต้องใช้มันเพราะข้อมูลจากผู้ใช้มักมาเป็นข้อความ เช่น ชื่อ อีเมล รหัสผ่าน หรือคำค้นหา

```js
const userName = '  knuxy92  ';

console.log(userName.trim());
console.log(userName.toUpperCase());
```

ผลลัพธ์:

```txt
knuxy92
  KNUXY92  
```

## 2. Template Literals

แม่แบบข้อความ คือการใส่ตัวแปรลงในข้อความด้วยเครื่องหมายแบ็กทิก (backtick)

เราต้องใช้มันเพราะมันอ่านง่ายกว่าการต่อข้อความยาว ๆ

```js
const firstName = 'Student';
const lastName = 'Dev';

console.log(`${firstName} ${lastName}`);
```

ผลลัพธ์:

```txt
Student Dev
```

## 3. Regex Basics

นิพจน์ปกติ คือรูปแบบสำหรับเช็กว่าข้อความตรงตามที่ต้องการไหม

เราต้องใช้มันเพราะการตรวจสอบข้อความ เช่น อีเมลหรือรหัสผ่าน มักต้องใช้รูปแบบ

```js
const email = 'test@example.com';
const emailPattern = /@/;

console.log(emailPattern.test(email));
```

ผลลัพธ์:

```txt
true
```

## 4. Date Basics

`Date` คือออบเจ็กต์ (object) ที่ใช้เก็บวันและเวลา

เราต้องใช้มันเพราะข้อมูลจริงมักมีวันที่ เช่น createdAt หรือ updatedAt

```js
const today = new Date();

console.log(today.toISOString());
```

ผลลัพธ์:

```txt
2026-04-26T...
```

## 5. โจทย์ที่ต้องทำ

ให้แก้ไฟล์:

```txt
exercises/ch10-string-validator.js
```

ให้ทำฟังก์ชันต่อไปนี้:

1. `formatUserName(userName)`
   - ใช้ `.trim()`
   - ใช้ `.toUpperCase()`

2. `isValidEmail(email)`
   - ใช้นิพจน์ปกติแบบง่าย
   - แค่เช็กว่ามี `@` และ `.`

3. `getPasswordStrength(password)`
   - ถ้าความยาวน้อยกว่า 8 ให้คืน `'weak'`
   - ถ้าความยาวตั้งแต่ 8 ขึ้นไป ให้คืน `'strong'`

4. `formatWelcomeMessage(firstName, lastName)`
   - ใช้แม่แบบข้อความ
   - คืนข้อความ `Welcome Student Dev`

5. `formatToday()`
   - สร้าง `new Date()`
   - คืนค่าจาก `.toLocaleDateString()`

ผลลัพธ์ที่คาดหวัง ไม่ต้องตรงวันที่เป๊ะ
แต่ต้องมีครบว่า:

- จัดรูปแบบชื่อผู้ใช้ได้
- อีเมลผ่านหรือไม่ผ่านได้
- ความแข็งแรงของรหัสผ่านทำงานได้
- ข้อความต้อนรับถูกต้อง
- วันที่ถูกแสดงออกมา

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch10
```
