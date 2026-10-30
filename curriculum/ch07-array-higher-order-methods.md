# บทที่ 7: เมธอดขั้นสูงของ array

## ทบทวน

บทที่แล้วเราเรียน array, index, `.length`, `.push()`, `.pop()` และ `for...of`

บทนี้เราจะใช้ method ที่ช่วยจัดการข้อมูลใน array แบบที่เจอจริงในงานบ่อยมาก

## 1. `.map()`

`.map()` ใช้เปลี่ยนข้อมูลทุกตัวใน array แล้วคืน array ใหม่

เราต้องใช้มันเมื่ออยากเอาของเดิมไปแปลงเป็นอีกรูปแบบหนึ่ง เช่นเอา object ไปดึงเฉพาะชื่อ

```js
const numbers = [1, 2, 3];
const doubledNumbers = numbers.map((number) => {
  return number * 2;
});

console.log(doubledNumbers);
```

ผลลัพธ์:

```txt
[ 2, 4, 6 ]
```

## 2. `.filter()`

`.filter()` ใช้คัดเฉพาะข้อมูลที่ตรงเงื่อนไข

เราต้องใช้มันเมื่ออยากได้ "บางตัว" จาก array

```js
const numbers = [1, 2, 3, 4];
const evenNumbers = numbers.filter((number) => {
  return number % 2 === 0;
});

console.log(evenNumbers);
```

ผลลัพธ์:

```txt
[ 2, 4 ]
```

## 3. `.find()`

`.find()` ใช้หา item ตัวแรกที่ตรงเงื่อนไข

เราต้องใช้มันเมื่ออยากได้ "ตัวเดียว" ไม่ใช่ทั้งรายการ

```js
const numbers = [3, 7, 10, 12];
const foundNumber = numbers.find((number) => {
  return number > 8;
});

console.log(foundNumber);
```

ผลลัพธ์:

```txt
10
```

## 4. `.some()`

`.some()` ใช้เช็กว่ามีอย่างน้อยหนึ่งตัวที่ตรงเงื่อนไขไหม

เราต้องใช้มันเมื่ออยากได้คำตอบเป็น `true` หรือ `false`

```js
const numbers = [1, 3, 5, 8];
const hasEvenNumber = numbers.some((number) => {
  return number % 2 === 0;
});

console.log(hasEvenNumber);
```

ผลลัพธ์:

```txt
true
```

## 5. `.every()`

`.every()` ใช้เช็กว่าทุกตัวตรงเงื่อนไขไหม

เราต้องใช้มันเมื่ออยากรู้ว่า "ทั้งหมด" ผ่านเงื่อนไขเดียวกันหรือเปล่า

```js
const numbers = [2, 4, 6];
const allEven = numbers.every((number) => {
  return number % 2 === 0;
});

console.log(allEven);
```

ผลลัพธ์:

```txt
true
```

## 6. `.reduce()`

`.reduce()` ใช้รวมข้อมูลหลายตัวให้เหลือผลลัพธ์เดียว

เราต้องใช้มันเมื่ออยากหาผลรวม นับจำนวน หรือสะสมค่าบางอย่าง

```js
const numbers = [10, 20, 30];
const total = numbers.reduce((sum, number) => {
  return sum + number;
}, 0);

console.log(total);
```

ผลลัพธ์:

```txt
60
```

## วิธีคิดง่าย ๆ

- อยากได้ array ใหม่จากทุกตัว -> `map`
- อยากคัดบางตัว -> `filter`
- อยากได้ตัวเดียว -> `find`
- อยากได้ true/false ว่ามีบ้างไหม -> `some`
- อยากได้ true/false ว่าทุกตัวใช่ไหม -> `every`
- อยากรวมให้เหลือค่าเดียว -> `reduce`

## โจทย์ที่ต้องทำ

ให้แก้ไฟล์:

```txt
exercises/ch07-product-methods.js
```

เรามี array ของสินค้า `products`

ให้ทำต่อไปนี้:

1. `productNames`
   ใช้ `map()` เอาเฉพาะชื่อสินค้าออกมา

2. `cheapProducts`
   ใช้ `filter()` เอาสินค้าที่ราคาไม่เกิน `500`

3. `foundProduct`
   ใช้ `find()` หาสินค้าที่ชื่อ `'Mouse'`

4. `hasExpensiveProduct`
   ใช้ `some()` เช็กว่ามีสินค้าที่ราคาเกิน `1000` ไหม

5. `allInStock`
   ใช้ `every()` เช็กว่าสินค้าทุกตัวมีของไหม

6. `totalPrice`
   ใช้ `reduce()` รวมราคาสินค้าทั้งหมด

ผลลัพธ์ที่คาดหวัง:

```txt
Product names: [ 'Keyboard', 'Mouse', 'Notebook' ]
Cheap products: ...
Found product: ...
Has expensive product: false
All in stock: false
Total price: 1050
```

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch7
```
