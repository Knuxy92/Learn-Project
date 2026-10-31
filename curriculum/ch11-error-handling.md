# บทที่ 11: การจัดการ error

## ทบทวน

บทที่แล้วเราเรียนเมธอดของข้อความ (string method), นิพจน์ปกติ (regex) เบื้องต้น และวันที่ (Date)

บทนี้เราจะเริ่มจัดการกับสิ่งที่ "พังได้" ในโปรแกรมอย่างเป็นระบบ

## 1. Error คืออะไร

ข้อผิดพลาด (error) คือปัญหาที่เกิดขึ้นตอนโปรแกรมรันแล้วบางอย่างทำงานไม่ได้

เราต้องรู้เรื่องข้อผิดพลาด เพราะโปรแกรมจริงไม่ได้ได้ข้อมูลที่ดีเสมอ และบางครั้งคำสั่งบางอย่างก็ล้มเหลวได้

## 2. `try` และ `catch`

`try` คือบล็อก (block) ที่เราเอาโค้ดที่อาจพังไปใส่ไว้

`catch` คือบล็อกที่ทำงานเมื่อเกิดข้อผิดพลาดใน `try`

```js
try {
  throw new Error('Something went wrong');
} catch (error) {
  console.log(error.message);
}
```

ผลลัพธ์:

```txt
Something went wrong
```

## 3. `finally`

`finally` คือบล็อกที่จะทำงานไม่ว่าจะสำเร็จหรือพัง

เราต้องใช้มันเมื่อมีสิ่งที่ควรเกิดขึ้นเสมอ เช่น ปิดการโหลด หรือพิมพ์ว่างานจบแล้ว

```js
try {
  console.log('Trying...');
} finally {
  console.log('Done');
}
```

ผลลัพธ์:

```txt
Trying...
Done
```

## 4. Error Object

ออบเจ็กต์ข้อผิดพลาด คือออบเจ็กต์ที่เก็บข้อมูลเกี่ยวกับปัญหาที่เกิดขึ้น

เราต้องรู้มันเพราะใน `catch` เรามักจะอ่าน `error.message`

```js
try {
  JSON.parse('{ bad json }');
} catch (error) {
  console.log(error.name);
  console.log(error.message);
}
```

ผลลัพธ์:

```txt
SyntaxError
...
```

## 5. Throwing Our Own Error

เราสร้างข้อผิดพลาดเองได้ด้วย `throw new Error(...)`

เราต้องใช้มันเมื่ออยากหยุดการทำงานและบอกชัดว่าข้อมูลไม่ถูกต้อง

```js
const age = -1;

if (age < 0) {
  throw new Error('Age cannot be negative');
}
```

## 6. โจทย์ที่ต้องทำ

ให้แก้ไฟล์:

```txt
exercises/ch11-safe-json.js
```

ให้ทำฟังก์ชันต่อไปนี้:

1. `safeJsonParse(jsonText)`
   - ใช้ `try/catch`
   - ถ้าแปลงข้อความสำเร็จ ให้คืนออบเจ็กต์ที่แปลงได้
   - ถ้าแปลงข้อความไม่สำเร็จ ให้คืน `{ error: 'Invalid JSON' }`

2. `getUserNameFromJson(jsonText)`
   - ใช้ `safeJsonParse`
   - ถ้าแปลงข้อความพัง หรือไม่มี `name`
     ให้คืน `'Unknown user'`
   - ถ้ามี `name`
     ให้คืนชื่อนั้น

3. `parseWithFinally(jsonText)`
   - ใช้ `try/catch/finally`
   - ถ้าแปลงข้อความสำเร็จ ให้คืนข้อมูล
   - ถ้าพัง ให้คืน `null`
   - ใน `finally` ให้พิมพ์ `'Finished parsing'`

ผลลัพธ์ที่คาดหวัง ไม่ต้องเหมือนเป๊ะทุกตัวอักษร
แต่ต้องมีครบว่า:

- แปลงข้อความ JSON ที่ดีได้
- แปลงข้อความ JSON ที่เสียแล้วไม่พังทั้งโปรแกรม
- `finally` ทำงานเสมอ

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch11
```
