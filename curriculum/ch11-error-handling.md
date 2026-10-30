# บทที่ 11: การจัดการ error

## ทบทวน

บทที่แล้วเราเรียน string methods, regex เบื้องต้น และ Date

บทนี้เราจะเริ่มจัดการกับสิ่งที่ "พังได้" ในโปรแกรมอย่างเป็นระบบ

## 1. Error คืออะไร

Error คือปัญหาที่เกิดขึ้นตอนโปรแกรมรันแล้วบางอย่างทำงานไม่ได้

เราต้องรู้เรื่อง error เพราะโปรแกรมจริงไม่ได้ได้ข้อมูลที่ดีเสมอ และบางครั้งคำสั่งบางอย่างก็ล้มเหลวได้

## 2. `try` และ `catch`

`try` คือ block ที่เราเอาโค้ดที่อาจพังไปใส่ไว้

`catch` คือ block ที่ทำงานเมื่อเกิด error ใน `try`

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

`finally` คือ block ที่จะทำงานไม่ว่าจะสำเร็จหรือพัง

เราต้องใช้มันเมื่อมีสิ่งที่ควรเกิดขึ้นเสมอ เช่น ปิด loading หรือพิมพ์ว่างานจบแล้ว

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

Error object คือ object ที่เก็บข้อมูลเกี่ยวกับปัญหาที่เกิดขึ้น

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

เราสามารถสร้าง error เองได้ด้วย `throw new Error(...)`

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

ให้ทำ function ต่อไปนี้:

1. `safeJsonParse(jsonText)`
   - ใช้ `try/catch`
   - ถ้า parse สำเร็จ ให้คืน object ที่ parse ได้
   - ถ้า parse ไม่สำเร็จ ให้คืน `{ error: 'Invalid JSON' }`

2. `getUserNameFromJson(jsonText)`
   - ใช้ `safeJsonParse`
   - ถ้า parse พัง หรือไม่มี `name`
     ให้คืน `'Unknown user'`
   - ถ้ามี `name`
     ให้คืนชื่อนั้น

3. `parseWithFinally(jsonText)`
   - ใช้ `try/catch/finally`
   - ถ้า parse สำเร็จ ให้คืนข้อมูล
   - ถ้าพัง ให้คืน `null`
   - ใน `finally` ให้พิมพ์ `'Finished parsing'`

ผลลัพธ์ที่คาดหวัง ไม่ต้องเหมือนเป๊ะทุกตัวอักษร
แต่ต้องมีครบว่า:

- parse JSON ที่ดีได้
- parse JSON ที่เสียแล้วไม่พังทั้งโปรแกรม
- `finally` ทำงานเสมอ

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch11
```
