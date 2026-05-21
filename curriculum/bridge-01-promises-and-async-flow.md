# Bridge 01: Promises and Async Flow

## Why This Bridge Exists

ช่วง `Ch21` และ `Ch22` เราเริ่มใช้ของพวกนี้จริงแล้ว:

- `readFile(...)`
- `writeFile(...)`
- `fetch(...)`
- `server.close(...)`
- `after(...)`
- `async / await`

นายใช้งานมันได้แล้วในเชิงรูปแบบ

แต่ยังมีจุดที่ต้องทำให้แน่นก่อนเข้าสายหลักถัดไป:

- Promise คืออะไรจริง ๆ
- ทำไมบางอย่าง `await` ได้ บางอย่างไม่ได้
- ทำไม callback API ต้อง wrap เป็น Promise ก่อน
- cleanup ของ test ควรรออะไรบ้าง

ดังนั้นบทนี้เป็น "บทคั่น"

ไม่ใช่การเปลี่ยนสาย

แต่เป็นการอุด prerequisite ให้แน่นก่อนกลับเข้าสาย backend หลัก

## Entry Point

เราเข้าบทนี้หลังจาก:

- `Ch22` ผ่านแล้ว
- เริ่มเจอคำถามเรื่อง `Promise`, `await`, `server.close`, `after`

สรุปคือ:

- เข้าตรงนี้เพราะเริ่มใช้ async ของจริงมากขึ้น
- ถ้าไม่หยุดอธิบายตรงนี้ ต่อไปจะเริ่มใช้แบบจำมากกว่าเข้าใจ

## Exit Point

เราจะออกจากบทคั่นนี้เมื่อทำได้ครบ:

1. อธิบายได้ว่า Promise คือ "ค่าที่จะมาในอนาคต"
2. แยกได้ว่าอะไรคืนค่าเป็น `Promise<T>` และอะไรเป็น `T`
3. เข้าใจว่า `await` ใช้กับ promise ไม่ใช่ callback ตรง ๆ
4. wrap callback API เช่น `server.close(...)` เป็น Promise ได้
5. อ่าน flow ของ async cleanup ได้เอง

เมื่อครบ 5 ข้อนี้ จะกลับเข้าสายหลักได้

## Return to Main Line

หลังจบบทนี้ เราจะกลับเข้าสายหลักที่:

- `Ch23 - SQLite Basics`

เหตุผล:

- หลังจากรู้ Promise ชัด จะอ่าน code ฝั่ง database ง่ายขึ้นมาก
- API ของ database ใน Node มัก async
- ถ้า Promise ยังไม่แม่น การ debug DB flow จะยากกว่าจำเป็น

## Main Line After This Bridge

ลำดับถัดจากนี้:

1. `Bridge 01 - Promises and Async Flow`
2. `Ch23 - SQLite Basics`
3. `Ch24 - Task API with SQLite`
4. `Ch25 - Query Layer and DB Refactor`
5. `Ch26 - API Testing with Database`

## Why We Do Not Skip This

ถ้าข้ามบทนี้เลย ปัญหาที่จะเจอใน database/testing ต่อไปคือ:

- ไม่เข้าใจว่าทำไม query ต้อง `await`
- ไม่เข้าใจว่าทำไม setup/teardown ต้องรอ
- งงว่า value ไหนเป็น promise และ value ไหนเป็นค่าจริง
- แก้ bug แบบลองผิดลองถูกมากเกินไป

## Lesson Goal

บทนี้จะเน้น 4 อย่าง:

1. Promise states
2. `async` function return type
3. callback -> promise wrapping
4. cleanup flow with `after()`

## Example 1: Promise as Future Value

```ts
const getMessage = async (): Promise<string> => {
  return "done";
};

const run = async (): Promise<void> => {
  const message = await getMessage();
  console.log(message);
};
```

## Example 2: Value vs Promise

```ts
const getTasks = async (): Promise<string[]> => {
  return ["a", "b"];
};

const tasksPromise = getTasks();
const tasks = await getTasks();
```

ตรงนี้:

- `tasksPromise` = `Promise<string[]>`
- `tasks` = `string[]`

## Example 3: Wrap Callback API

```ts
await new Promise<void>((resolve, reject) => {
  server.close((error) => {
    if (error) reject(error);
    else resolve();
  });
});
```

## Guided Exercise

ให้แก้ไฟล์:

```txt
exercises/bridge-01-promises.ts
```

ให้ทำตามนี้:

1. สร้าง `wait(ms)` ที่คืน `Promise<string>`
   - ใช้ `setTimeout`
   - เมื่อครบเวลาให้ `resolve("done")`

2. สร้าง `getTaskTitles()` ที่คืน `Promise<string[]>`
   - คืน array string 2 ตัว

3. สร้าง `closeServer(server)` ที่คืน `Promise<void>`
   - wrap `server.close(...)`

4. สร้าง function `runDemo()`
   - `await wait(100)`
   - `await getTaskTitles()`
   - พิมพ์ผลออกมา

5. ตอบใน comment สั้น ๆ ในไฟล์นี้:
   - อะไรคือ `Promise<string[]>`
   - อะไรคือ `string[]`

## Expected Output

ประมาณนี้:

```txt
done
Task count: 2
```

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Bridge 01
```
