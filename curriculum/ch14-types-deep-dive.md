# Chapter 14: TypeScript Types Deep Dive

## Recap

บทที่แล้วเราเริ่ม TypeScript ด้วย type annotations พื้นฐาน

บทนี้เราจะขยับไปดู types ที่ใช้จริงบ่อยขึ้นในโปรเจกต์:

- arrays
- tuples
- union types
- type aliases
- interfaces
- optional properties
- readonly

## 1. Arrays in TypeScript

เราสามารถบอก type ของ array ได้ชัดเจน

```ts
const userNames: string[] = ['Neo', 'Mint', 'Beam'];

console.log(userNames[0]);
```

Output:

```txt
Neo
```

## 2. Tuples

Tuple คือ array ที่กำหนดชนิดของแต่ละตำแหน่งไว้แน่นอน

```ts
const userEntry: [string, number] = ['Knuxy92', 17];

console.log(userEntry[0]);
console.log(userEntry[1]);
```

Output:

```txt
Knuxy92
17
```

## 3. Union Types

Union type คือค่าที่เป็นได้หลายชนิด

```ts
const userId: string | number = 'abc123';

console.log(userId);
```

Output:

```txt
abc123
```

## 4. Type Alias

Type alias ใช้ตั้งชื่อให้ shape ของข้อมูล

```ts
type Book = {
  title: string;
  pages: number;
};
```

## 5. Interface

Interface ก็ใช้กำหนด shape ของ object ได้เหมือนกัน

```ts
interface Author {
  name: string;
  age: number;
}
```

## 6. Optional and Readonly

Optional property ใช้ `?`

Readonly ใช้ `readonly`

```ts
type LibraryBook = {
  readonly id: number;
  title: string;
  authorName?: string;
};
```

## Guided Exercise

ให้แก้ไฟล์:

```txt
exercises/ch14-library-types.ts
```

ให้ทำตามนี้:

1. สร้าง `type Book`
   - `id` เป็น `readonly number`
   - `title` เป็น `string`
   - `pages` เป็น `number`
   - `genre` เป็น `'fiction' | 'non-fiction'`
   - `authorName` เป็น `string` แบบ optional

2. สร้าง `interface Library`
   - `name` เป็น `string`
   - `books` เป็น `Book[]`

3. สร้างตัวแปร `featuredBook` เป็น tuple `[string, number]`
   - เก็บ `title` กับ `pages`

4. สร้างตัวแปร `bookId` เป็น `string | number`

5. สร้าง object `library` ตาม interface `Library`

Expected output:

- พิมพ์ `featuredBook`
- พิมพ์ `bookId`
- พิมพ์ `library`

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch14
```
