# บทที่ 16: pattern ขั้นสูงใน TypeScript

## ทบทวน

บทที่แล้วเราเรียน function ที่มี type, generics, และ utility types

บทนี้เราจะเริ่มเข้า patterns ที่สำคัญมากใน TypeScript:

- narrowing
- type guards
- discriminated union
- `unknown` vs `any`
- แนวคิดการแยก module แบบเบื้องต้น

## 1. Narrowing

Narrowing คือการที่ TypeScript ค่อย ๆ รู้ type แคบลงหลังจากเราเช็กบางอย่าง

```ts
const printValue = (value: string | number): void => {
  if (typeof value === 'string') {
    console.log(value.toUpperCase());
    return;
  }

  console.log(value.toFixed(2));
};

printValue('hello');
printValue(12.5);
```

ผลลัพธ์:

```txt
HELLO
12.50
```

## 2. Type Guard

Type guard คือ function ที่ช่วยบอก TypeScript ว่าค่าหนึ่งเป็น type อะไร

```ts
const isString = (value: unknown): value is string => {
  return typeof value === 'string';
};

console.log(isString('hello'));
console.log(isString(123));
```

ผลลัพธ์:

```txt
true
false
```

## 3. `unknown` vs `any`

- `any` = ปล่อยผ่านได้เกือบทุกอย่าง
- `unknown` = ยังไม่รู้ type จึงต้องเช็กก่อนใช้

เราควรเลือกใช้ `unknown` เพราะปลอดภัยกว่า

## 4. Discriminated Union

Discriminated union คือ union ที่มี field กลางเอาไว้บอกชนิดของข้อมูล

```ts
type Result =
  | { status: 'success'; data: string }
  | { status: 'error'; error: string };

const printResult = (result: Result): void => {
  if (result.status === 'success') {
    console.log(result.data);
    return;
  }

  console.log(result.error);
};
```

## โจทย์ที่ต้องทำ

ให้แก้ไฟล์:

```txt
exercises/ch16-event-system.ts
```

ให้ทำตามนี้:

1. สร้าง `type UserEvent`
   - `{ type: 'login'; userName: string }`
   - `{ type: 'logout'; userId: number }`
   - `{ type: 'error'; message: string }`

2. สร้าง function `printEvent(event: UserEvent)`
   - ใช้ narrowing จาก `event.type`
   - ถ้า `login` ให้พิมพ์ `Login: <userName>`
   - ถ้า `logout` ให้พิมพ์ `Logout: <userId>`
   - ถ้า `error` ให้พิมพ์ `Error: <message>`

3. สร้าง type guard `isString(value: unknown): value is string`

4. สร้าง function `safeUpperCase(value: unknown): string`
   - ถ้าเป็น string ให้คืนตัวพิมพ์ใหญ่
   - ถ้าไม่ใช่ ให้คืน `'NOT A STRING'`

5. สร้าง `type EventHandler = (event: UserEvent) => void`

6. สร้างตัวแปร `handleEvent` ตาม type `EventHandler`
   - ให้มันเรียก `printEvent(event)`

ผลลัพธ์ที่คาดหวัง:

- `Login: Student`
- `Logout: 17`
- `Error: Something went wrong`
- `HELLO`
- `NOT A STRING`

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch16
```
