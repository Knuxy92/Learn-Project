# บทที่ 4: การควบคุมทิศทาง

## ทบทวน

บทที่แล้วเราใช้ตัวดำเนินการ (operator) เพื่อคำนวณและเปรียบเทียบค่า

บทนี้เราจะให้โปรแกรม "ตัดสินใจ" จากเงื่อนไข

## 1. `if`

`if` คือคำสั่งที่ให้โค้ดบางส่วนทำงานเมื่อเงื่อนไขเป็น `true`

เราต้องใช้ `if` เพราะโปรแกรมจริงต้องเลือกทำสิ่งต่างกันตามข้อมูล

```js
const score = 80;

if (score >= 50) {
  console.log('pass');
}
```

ผลลัพธ์:
```txt
pass
```

## 2. `else`

`else` คือทางเลือกเมื่อเงื่อนไขของ `if` ไม่เป็นจริง

เราต้องใช้ `else` เพื่อบอกว่า "ถ้าไม่ใช่แบบนี้ ให้ทำอีกแบบ"

```js
const score = 40;

if (score >= 50) {
  console.log('pass');
} else {
  console.log('fail');
}
```

ผลลัพธ์:
```txt
fail
```

## 3. `else if`

`else if` ใช้เมื่อมีเงื่อนไขหลายระดับ

เราต้องใช้มันเมื่อผลลัพธ์มีมากกว่า 2 แบบ เช่น เกรด A/B/C/D/F

```js
const score = 75;

if (score >= 80) {
  console.log('A');
} else if (score >= 70) {
  console.log('B');
} else {
  console.log('C or lower');
}
```

ผลลัพธ์:
```txt
B
```

## 4. `switch`

`switch` ใช้เลือกทางจากค่าหนึ่งค่าที่มีหลายกรณี (case)

เราจะใช้มันเมื่อเทียบค่าเดียวกับหลายตัวเลือก เช่น บทบาท (role) หรือสถานะ

```js
const role = 'admin';

switch (role) {
  case 'admin':
    console.log('full access');
    break;
  default:
    console.log('limited access');
}
```

ผลลัพธ์:
```txt
full access
```

## 5. ค่าจริง (truthy) และค่าเท็จ (falsy)

ค่าจริง/ค่าเท็จคือวิธีที่ JavaScript มองค่าต่าง ๆ เป็นเหมือน `true` หรือ `false`

เราต้องรู้มันเพราะ `if` ไม่ได้ใช้แค่ค่าจริงเท็จ (boolean) ตรง ๆ เท่านั้น

ค่าเท็จมี 6 ตัวที่ควรจำ:

- `false`
- `0`
- `''`
- `null`
- `undefined`
- `NaN`

```js
const userName = '';

if (userName) {
  console.log('has name');
} else {
  console.log('missing name');
}
```

ผลลัพธ์:
```txt
missing name
```

## 6. การลัดวงจร (short-circuit) แบบง่าย

การลัดวงจรคือการใช้ `&&` หรือ `||` เพื่อเลือกค่าหรือหยุดเช็กเร็วขึ้น

เราต้องรู้มันเพราะโค้ด JavaScript จริงใช้บ่อยมาก

```js
const nickname = '';
const displayName = nickname || 'Anonymous';

console.log(displayName);
```

ผลลัพธ์:
```txt
Anonymous
```

## โจทย์ที่ต้องทำ

ให้แก้ไฟล์:

```txt
exercises/ch04-grade-calculator.js
```

เป้าหมาย:

1. ใช้ `if / else if / else` เพื่อคำนวณเกรด (grade) ตามตารางด้านล่าง
2. ใช้ `switch` เพื่อสร้างข้อความตามเกรดตามตารางด้านล่าง
3. ใช้ค่าจริง/ค่าเท็จเพื่อตรวจว่ามี `studentName` ไหม
4. ใช้การลัดวงจรตั้งชื่อที่แสดง (display name) ถ้าชื่อว่าง

## กติกาการให้เกรด

ให้ใช้กฎนี้:

| คะแนน | เกรด |
|---|---|
| `score >= 90` | `A` |
| `score >= 80` | `B` |
| `score >= 70` | `C` |
| `score >= 60` | `D` |
| ต่ำกว่า `60` | `F` |

## กติกาข้อความ

ให้ใช้ข้อความนี้:

| เกรด | ข้อความ |
|---|---|
| `A` | `Excellent work` |
| `B` | `Great job` |
| `C` | `Good effort` |
| `D` | `Needs improvement` |
| `F` | `Keep practicing` |

## ค่าการทดสอบที่ต้องใช้

ให้ใช้ค่าทดสอบนี้ตอนส่งตรวจ:

```js
const studentName = 'Student';
const score = 85;
```

ผลลัพธ์ที่คาดหวัง:

```txt
Student: Student
Score: 85
Grade: B
Message: Great job
```

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch4
```
