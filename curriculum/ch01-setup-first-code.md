# บทที่ 1: ติดตั้งและโค้ดแรก

## JavaScript คืออะไร

JavaScript คือภาษาโปรแกรมที่ใช้บอกคอมพิวเตอร์ว่าต้องทำอะไร

เราต้องใช้มันเพราะเครื่องมือฝั่งเซิร์ฟเวอร์ (backend) อย่าง Node.js รัน JavaScript นอกเบราว์เซอร์ (browser) ได้

## แนวคิดแรก: `console.log`

`console.log` ใช้พิมพ์อะไรบางอย่างออกมาที่เทอร์มินัล (terminal)

เราต้องใช้มันเพราะมันทำให้เราเห็นว่าโค้ดของเรากำลังทำอะไรอยู่

```js
console.log('Hello World');
```

ผลลัพธ์:

```txt
Hello World
```

## การรันไฟล์

ไฟล์ `.js` คือไฟล์ JavaScript

เรารันมันด้วย Node.js แบบนี้:

```bash
node curriculum/ch01/hello-world.js
```

ผลลัพธ์:

```txt
Hello World
```

## ไฟล์ที่ต้องแก้

ไฟล์ใน `curriculum/` เป็นไฟล์ตัวอย่างสำหรับอ่านและรันดู

ไฟล์ใน `exercises/` เป็นไฟล์โจทย์ที่ให้แก้และส่งตรวจ

บทนี้ให้แก้ไฟล์นี้:

```txt
exercises/ch01-first-code.js
```

## โจทย์ที่ต้องทำ

เปิด `exercises/ch01-first-code.js`

เปลี่ยนค่าในไฟล์ให้พิมพ์ออกมาเป็น:

1. ชื่อของเรา
2. อายุของเรา
3. หนึ่งประโยคที่รวมทั้งสองอย่างเข้าด้วยกัน

ตัวอย่างผลลัพธ์:

```txt
My name is Student
I am 17 years old
My name is Student and I am 17 years old.
```

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch1
```
