# Chapter 3: Operators & Expressions

## Recap

บทที่แล้วเราเรียนตัวแปรและ data types เช่น string, number, boolean, null และ undefined

บทนี้เราจะใช้ค่าพวกนั้นมาคำนวณและเปรียบเทียบ

## 1. Arithmetic Operators

Arithmetic operators คือเครื่องหมายคำนวณ เช่น บวก ลบ คูณ หาร

เราต้องใช้มันเพราะโปรแกรมมักต้องคำนวณราคา คะแนน จำนวน หรือผลรวม

```js
const price = 100;
const quantity = 3;

console.log(price * quantity);
```

Output:

```txt
300
```

ตัวที่ใช้บ่อย:

- `+` บวก
- `-` ลบ
- `*` คูณ
- `/` หาร
- `%` เอาเศษ
- `**` ยกกำลัง

## 2. Assignment Operators

Assignment operators คือเครื่องหมายที่ใช้เปลี่ยนค่าตัวแปร

เราต้องใช้มันเมื่อค่ามีการอัปเดต เช่น เพิ่มคะแนน หรือลดจำนวนสินค้า

```js
let score = 10;
score += 5;

console.log(score);
```

Output:

```txt
15
```

## 3. Comparison Operators

Comparison operators คือเครื่องหมายเปรียบเทียบค่า

เราต้องใช้มันเพื่อให้โปรแกรมตัดสินใจได้ เช่น ราคามากกว่า 1000 ไหม

```js
const age = 17;

console.log(age >= 18);
```

Output:

```txt
false
```

สำคัญ:

ใช้ `===` เป็นหลัก เพราะมันเทียบทั้งค่าและชนิดข้อมูล

```js
console.log(5 === '5');
console.log(5 == '5');
```

Output:

```txt
false
true
```

## 4. Logical Operators

Logical operators ใช้รวมเงื่อนไขหลายอัน

เราต้องใช้มันเมื่อการตัดสินใจมีมากกว่าหนึ่งเงื่อนไข

```js
const age = 20;
const hasTicket = true;

console.log(age >= 18 && hasTicket);
```

Output:

```txt
true
```

ตัวที่ใช้บ่อย:

- `&&` และ
- `||` หรือ
- `!` กลับค่า true/false

## 5. Ternary Operator

Ternary operator คือ if/else แบบสั้นที่คืนค่าออกมา

เราต้องใช้มันเมื่ออยากเลือกค่าหนึ่งจากเงื่อนไขง่าย ๆ

```js
const age = 17;
const label = age >= 18 ? 'adult' : 'minor';

console.log(label);
```

Output:

```txt
minor
```

## Guided Exercise

ให้แก้ไฟล์:

```txt
exercises/ch03-price-calculator.js
```

เป้าหมาย:

1. คำนวณ subtotal จาก `itemPrice * quantity`
2. ถ้า `quantity > 10` ให้ได้ส่วนลด 10%
3. คำนวณ final total
4. ใช้ ternary สร้างข้อความว่าได้ส่วนลดหรือไม่

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch3
```
