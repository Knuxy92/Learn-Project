# บทที่ 1: ติดตั้งและโค้ดแรก

## What JavaScript Is

JavaScript คือภาษาโปรแกรมที่ใช้บอกคอมพิวเตอร์ว่าต้องทำอะไร

เราต้องใช้มันเพราะเครื่องมือ backend อย่าง Node.js สามารถรัน JavaScript นอก browser ได้

## First Concept: `console.log`

`console.log` ใช้พิมพ์อะไรบางอย่างออกมาที่ terminal

เราต้องใช้มันเพราะมันทำให้เราเห็นว่าโค้ดของเรากำลังทำอะไรอยู่

```js
console.log('Hello World');
```

ผลลัพธ์:

```txt
Hello World
```

## Running A File

ไฟล์ `.js` คือไฟล์ JavaScript

เรารันมันด้วย Node.js แบบนี้:

```bash
node curriculum/ch01/hello-world.js
```

ผลลัพธ์:

```txt
Hello World
```

## Which File To Edit

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
