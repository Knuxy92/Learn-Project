# บทที่ 15: ฟังก์ชันและ generics ใน TypeScript

## ทบทวน

บทที่แล้วเราเรียน type aliases, interfaces, tuples, unions, optional properties, และ readonly

บทนี้เราจะเอา TypeScript ไปใช้กับ function ให้ชัดขึ้น และเริ่ม generic แบบเบื้องต้น

## 1. Typing Function Parameters and Return Values

เราสามารถบอก type ของ parameter และค่าที่ function คืนได้

```ts
const add = (firstNumber: number, secondNumber: number): number => {
  return firstNumber + secondNumber;
};

console.log(add(2, 3));
```

ผลลัพธ์:

```txt
5
```

## 2. Function Type Expression

Function type expression คือการตั้ง type ให้ “รูปร่างของ function”

```ts
type MathFn = (firstNumber: number, secondNumber: number) => number;

const multiply: MathFn = (firstNumber, secondNumber) => {
  return firstNumber * secondNumber;
};

console.log(multiply(4, 5));
```

ผลลัพธ์:

```txt
20
```

## 3. Generic Function

Generic คือ function ที่ใช้ได้กับหลาย type แต่ยังปลอดภัยเรื่อง type

```ts
const firstItem = <T>(items: T[]): T | undefined => {
  return items[0];
};

console.log(firstItem(['a', 'b', 'c']));
console.log(firstItem([10, 20, 30]));
```

ผลลัพธ์:

```txt
a
10
```

หมายเหตุ:

ใน TypeScript แบบเข้ม (`strict`) `items[0]` อาจเป็น `undefined` ได้ถ้า array ว่าง

ดังนั้น type ที่ปลอดภัยกว่าจะเป็น:

```ts
T | undefined
```

## 4. Utility Types

Utility types คือ type ที่ TypeScript เตรียมไว้ให้ใช้บ่อย ๆ

ตัวอย่าง:

```ts
type User = {
  id: number;
  name: string;
  age: number;
};

type UserPreview = Pick<User, 'id' | 'name'>;
type UserWithoutAge = Omit<User, 'age'>;
```

`Pick` = เลือกบาง field

`Omit` = ตัดบาง field ออก

## โจทย์ที่ต้องทำ

ให้แก้ไฟล์:

```txt
exercises/ch15-storage.ts
```

ให้ทำตามนี้:

1. สร้าง `type MathFn`
   - รับ number 2 ตัว
   - คืน number

2. สร้าง function `subtract` โดยใช้ `MathFn`

3. สร้าง generic function `firstItem<T>(items: T[]): T`
   - ให้ปรับเป็น `T | undefined`
   - คืน item ตัวแรกของ array

4. สร้าง `type User`
   - `id`
   - `name`
   - `email`
   - `age`

5. สร้าง `type UserPreview = Pick<User, 'id' | 'name'>`

6. สร้าง `type UserWithoutEmail = Omit<User, 'email'>`

7. สร้างตัวแปร `userPreview` และ `userWithoutEmail`

ผลลัพธ์ที่คาดหวัง:

- `subtract(10, 3)` ได้ `7`
- `firstItem(['a', 'b', 'c'])` ได้ `'a'`
- `firstItem([10, 20, 30])` ได้ `10`
- `userPreview` มีแค่ `id` กับ `name`
- `userWithoutEmail` ไม่มี `email`

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch15
```
