# ช่วงเชื่อมทดสอบ 01: พื้นฐาน assert

## ทำไมต้องมีช่วงเชื่อมนี้

ก่อน test storage หรือ API ต้องแม่นก่อนว่า test หนึ่งตัวเขียนยังไง และ assert แต่ละแบบใช้เช็กอะไร

บทนี้จะยังไม่แตะไฟล์ storage และยังไม่เปิด server

## เป้าหมาย

ฝึก 4 อย่าง:

1. `test(...)`
2. `assert.equal(...)`
3. `assert.deepEqual(...)`
4. `assert.ok(...)`

## 1. `test(...)`

`test(...)` ใช้สร้าง test หนึ่งตัว

```js
import { test } from "node:test";

test("name of behavior", () => {
  // assert here
});
```

สรุป: test หนึ่งตัวควรเช็กพฤติกรรมหนึ่งเรื่องให้ชัด

## 2. `assert.equal(...)`

ใช้เช็กค่าพื้นฐาน เช่น string, number, boolean

```js
import assert from "node:assert/strict";

assert.equal(1 + 1, 2);
assert.equal("task".toUpperCase(), "TASK");
```

สรุป: ใช้เมื่อเทียบค่าตรงๆ

## 3. `assert.deepEqual(...)`

ใช้เช็ก array หรือ object

```js
assert.deepEqual(["a", "b"], ["a", "b"]);

assert.deepEqual(
  { id: 1, title: "Study" },
  { id: 1, title: "Study" },
);
```

สรุป: ใช้เมื่อเทียบโครงสร้างข้อมูล

## 4. `assert.ok(...)`

ใช้เช็กว่าเงื่อนไขเป็น truthy

```js
const tasks = ["Study", "Review"];

assert.ok(tasks.length > 0);
assert.ok(Array.isArray(tasks));
```

สรุป: ใช้เมื่ออยากเช็กเงื่อนไข

## ตัวอย่าง

```js
import { test } from "node:test";
import assert from "node:assert/strict";

const countDoneTasks = (tasks) => tasks.filter((task) => task.done).length;

test("countDoneTasks should count only done tasks", () => {
  const result = countDoneTasks([
    { done: true },
    { done: false },
    { done: true },
  ]);

  assert.equal(result, 2);
});
```

## งานที่ต้องทำ

แก้ไฟล์:

```txt
exercises/test-bridge-01-assert-basics.test.js
```

ให้ทำตามนี้:

1. import:
   - `test` จาก `node:test`
   - `assert` จาก `node:assert/strict`

2. ใช้ fixture `tasks` ที่มีอยู่แล้วในไฟล์ เป็น array ของ object ที่มี `id`, `title`, `done`

3. สร้าง function `countDoneTasks(tasks)`
   - คืนจำนวน task ที่ `done === true`

4. สร้าง function `findTaskTitle(tasks, id)`
   - ถ้าเจอ task ให้คืน `title`
   - ถ้าไม่เจอให้คืน `undefined`

5. เขียน test 4 ตัว:
   - `countDoneTasks` ควรนับเฉพาะ task ที่ done
   - `findTaskTitle` ควรคืน title เมื่อเจอ id
   - `findTaskTitle` ควรคืน `undefined` เมื่อไม่เจอ id
   - tasks fixture ควรเป็น array และมีอย่างน้อย 1 รายการ

6. ใช้ assert ให้ตรงสถานการณ์:
   - ใช้ `assert.equal(...)` กับ number/string/undefined
   - ใช้ `assert.ok(...)` กับเงื่อนไข
   - ใช้ `assert.deepEqual(...)` อย่างน้อย 1 ครั้งกับ object หรือ array

## วิธีรัน

ใช้คำสั่ง:

```bash
node --test exercises/test-bridge-01-assert-basics.test.js
```

## ผลลัพธ์ที่คาดหวัง

เมื่อรัน test แล้วควรผ่านทุกตัว

เสร็จแล้วพิมพ์:

```txt
ตรวจ Test Bridge 01
```
