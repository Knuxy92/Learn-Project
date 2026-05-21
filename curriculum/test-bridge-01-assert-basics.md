# Test Bridge 01: Assert Basics

## Why This Bridge Exists

ก่อน test database หรือ API ต้องแม่นก่อนว่า test หนึ่งตัวเขียนยังไง และ assert แต่ละแบบใช้เช็กอะไร

บทนี้จะยังไม่ใช้ SQL และยังไม่เปิด server

## Goal

ฝึก 4 อย่าง:

1. `test(...)`
2. `assert.equal(...)`
3. `assert.deepEqual(...)`
4. `assert.ok(...)`

## 1. `test(...)`

`test(...)` ใช้สร้าง test case หนึ่งตัว

```ts
import { test } from "node:test";

test("name of behavior", () => {
  // assert here
});
```

สรุป: test หนึ่งตัวควรเช็ก behavior หนึ่งเรื่องให้ชัด

## 2. `assert.equal(...)`

ใช้เช็กค่าพื้นฐาน เช่น string, number, boolean

```ts
import assert from "node:assert/strict";

assert.equal(1 + 1, 2);
assert.equal("task".toUpperCase(), "TASK");
```

สรุป: ใช้เมื่อเทียบค่าตรงๆ

## 3. `assert.deepEqual(...)`

ใช้เช็ก array หรือ object

```ts
assert.deepEqual(["a", "b"], ["a", "b"]);

assert.deepEqual(
  { id: 1, title: "Study" },
  { id: 1, title: "Study" },
);
```

สรุป: ใช้เมื่อเทียบโครงสร้างข้อมูล

## 4. `assert.ok(...)`

ใช้เช็กว่าเงื่อนไขเป็น truthy

```ts
const tasks = ["Study SQL"];

assert.ok(tasks.length > 0);
assert.ok(Array.isArray(tasks));
```

สรุป: ใช้เมื่ออยากเช็กเงื่อนไข

## Example

```ts
import { test } from "node:test";
import assert from "node:assert/strict";

const countDoneTasks = (tasks: { done: boolean }[]): number => {
  return tasks.filter((task) => task.done).length;
};

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
exercises/test-bridge-01-assert-basics.test.ts
```

ให้ทำตามนี้:

1. import:
   - `test` จาก `node:test`
   - `assert` จาก `node:assert/strict`

2. สร้าง type:

```ts
type Task = {
  id: number;
  title: string;
  done: boolean;
};
```

3. สร้าง function `countDoneTasks(tasks: Task[]): number`
   - return จำนวน task ที่ `done === true`

4. สร้าง function `findTaskTitle(tasks: Task[], id: number): string | undefined`
   - ถ้าเจอ task ให้ return `title`
   - ถ้าไม่เจอให้ return `undefined`

5. เขียน test 4 ตัว:
   - `countDoneTasks` ควรนับเฉพาะ task ที่ done
   - `findTaskTitle` ควรคืน title เมื่อเจอ id
   - `findTaskTitle` ควรคืน `undefined` เมื่อไม่เจอ id
   - tasks fixture ควรเป็น array และมีอย่างน้อย 1 item

6. ใช้ assert ให้ตรงสถานการณ์:
   - ใช้ `assert.equal(...)` กับ number/string/undefined
   - ใช้ `assert.ok(...)` กับเงื่อนไข
   - ใช้ `assert.deepEqual(...)` อย่างน้อย 1 ครั้งกับ object หรือ array

## Run

ใช้คำสั่ง:

```bash
cmd /c node --test -r ts-node/register exercises/test-bridge-01-assert-basics.test.ts
```

## Expected Outcome

เมื่อรัน test แล้วควรผ่านทุกตัว

เสร็จแล้วพิมพ์:

```txt
ตรวจ Test Bridge 01
```
