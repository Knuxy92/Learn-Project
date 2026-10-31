# บทที่ 12: async ใน JavaScript

## ทบทวน

บทที่แล้วเราเรียนการจัดการข้อผิดพลาด (error) ด้วย `try`, `catch`, และ `finally`

บทนี้เราจะเริ่มเรื่องอะซิงค์ (async) ซึ่งสำคัญมาก เพราะงานจริงอย่างการส่งคำขอ (request) ผ่านเครือข่ายไม่ได้เสร็จทันที

## 1. Async คืออะไร

อะซิงค์ คือการทำงานที่ต้องรอ เช่น โหลดข้อมูลจากอินเทอร์เน็ตหรืออ่านไฟล์

เราต้องเข้าใจมันเพราะ JavaScript ไม่ควรหยุดทั้งโปรแกรมไว้แค่เพื่อรออย่างเดียว

## 2. `setTimeout`

`setTimeout` ใช้สั่งให้โค้ดบางส่วนทำงานหลังจากเวลาผ่านไป

เราจะใช้มันเพื่อดูพฤติกรรม "ไม่เสร็จทันที" ของอะซิงค์ก่อน

```js
console.log('Start');

setTimeout(() => {
  console.log('Later');
}, 1000);

console.log('End');
```

ผลลัพธ์:

```txt
Start
End
Later
```

## 3. Promise คืออะไร

พรอมิส (Promise) คือออบเจ็กต์ที่แทนงานที่ "ยังไม่เสร็จตอนนี้ แต่จะมีผลลัพธ์ภายหลัง"

เราต้องรู้มันเพราะอะซิงค์ใน JavaScript สมัยใหม่ใช้พรอมิสเป็นฐาน

```js
const promise = Promise.resolve('Done');

promise.then((result) => {
  console.log(result);
});
```

ผลลัพธ์:

```txt
Done
```

## 4. `async` / `await`

`async` / `await` คือวิธีเขียนโค้ดอะซิงค์ให้ดูเหมือนโค้ดปกติและอ่านง่ายกว่า `.then()`

เราจะใช้รูปแบบนี้เป็นหลักต่อไป

```js
const getMessage = async () => {
  return 'Hello';
};

const run = async () => {
  const message = await getMessage();
  console.log(message);
};

run();
```

ผลลัพธ์:

```txt
Hello
```

## 5. `fetch()`

`fetch()` ใช้ดึงข้อมูลจาก URL

เราต้องรู้มันเพราะฝั่งเซิร์ฟเวอร์ (backend) และฝั่งหน้าจอ (frontend) ต่างก็ต้องดึงข้อมูลจาก API บ่อยมาก

```js
const run = async () => {
  const response = await fetch('https://jsonplaceholder.typicode.com/users');
  const users = await response.json();
  console.log(users.length);
};

run();
```

ผลลัพธ์:

```txt
10
```

## โจทย์ที่ต้องทำ

ให้แก้ไฟล์:

```txt
exercises/ch12-user-fetch.js
```

ให้ทำตามนี้:

1. สร้างฟังก์ชันอะซิงค์ `getUsers()`
   - ใช้ `fetch()` ดึงข้อมูลจาก:
     `https://jsonplaceholder.typicode.com/users`
   - ใช้ `await response.json()`
   - คืน array ของผู้ใช้

2. สร้างฟังก์ชันอะซิงค์ `getUserNames()`
   - ใช้ `getUsers()`
   - คืน array ของชื่อผู้ใช้ทุกคน

3. สร้างฟังก์ชันอะซิงค์ `getUsersInCity(cityName)`
   - ใช้ `getUsers()`
   - คืนเฉพาะผู้ใช้ที่ `user.address.city === cityName`

4. สร้างฟังก์ชันอะซิงค์ `run()`
   - เรียกทั้ง 3 ฟังก์ชัน
   - console.log ผลลัพธ์ออกมา

ผลลัพธ์ที่คาดหวัง ไม่ต้องเหมือนเป๊ะทุกตัวอักษร
แต่ต้องมีครบว่า:

- จำนวนผู้ใช้
- รายชื่อผู้ใช้
- ผู้ใช้ที่อยู่ในเมืองที่เลือก

เมื่อเสร็จแล้วพิมพ์:

```txt
ตรวจ Ch12
```
