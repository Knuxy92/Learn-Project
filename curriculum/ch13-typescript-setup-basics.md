# Chapter 13: TypeScript Setup & Basics

## Recap

บทที่แล้วเราเรียน async, `fetch()`, และ `async/await`

ตอนนี้เราจะเริ่มเข้าสู่ TypeScript อย่างเป็นทางการ

## 1. TypeScript คืออะไร

TypeScript คือ JavaScript ที่เพิ่มระบบ type เข้ามา

เราต้องใช้มันเพราะมันช่วยจับ bug ได้ก่อนรันจริง และช่วยให้ editor บอกปัญหาได้ดีขึ้น

## 2. JavaScript ก่อน แล้วค่อย TypeScript

JavaScript version:

```js
const userName = 'Knuxy92';
const userAge = 17;

console.log(userName);
console.log(userAge);
```

Output:

```txt
Knuxy92
17
```

TypeScript version:

```ts
const userName: string = 'Knuxy92';
const userAge: number = 17;

console.log(userName);
console.log(userAge);
```

Output:

```txt
Knuxy92
17
```

ต่างกันตรงที่ TypeScript เพิ่ม type annotation:

- `: string`
- `: number`

## 3. Type Inference

Type inference คือการที่ TypeScript เดา type ให้เราเอง

เราต้องรู้มันเพราะไม่จำเป็นต้องใส่ type ทุกบรรทัดเสมอไป

```ts
const userName = 'Knuxy92';
const userAge = 17;
```

ตรงนี้ TypeScript ก็ยังรู้ว่า:

- `userName` เป็น string
- `userAge` เป็น number

## 4. Type Annotation ใช้ตอนไหน

เรามักใส่ type ชัด ๆ ตอน:

- function parameters
- function return values
- object types
- ตอนอยากให้โค้ดสื่อเจตนาให้ชัด

## 5. Setup ที่เราจะใช้

ในโปรเจกต์นี้เราจะใช้:

- `tsc` เพื่อ compile TypeScript
- Node.js เพื่อรัน output JS

## Guided Exercise

ให้แก้ไฟล์:

```txt
exercises/ch13-ts-variables.ts
```

ให้ทำตามนี้:

1. สร้างตัวแปร `userName` เป็น `string`
2. สร้างตัวแปร `userAge` เป็น `number`
3. สร้างตัวแปร `isStudent` เป็น `boolean`
4. สร้าง function `formatProfile`
   - รับ `name`, `age`, `isStudent`
   - คืน string รูปแบบ:
     `Knuxy92 - 17 - true`

Expected output:

```txt
Knuxy92
17
true
Knuxy92 - 17 - true
```

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch13
```
