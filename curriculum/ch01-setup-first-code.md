# บทที่ 1: ติดตั้งและโค้ดแรก

## Python คืออะไร

Python คือภาษาโปรแกรมที่อ่านง่ายและมีเครื่องมือจัดการข้อมูลอยู่ครบ

เราเลือกใช้ Python เพราะงานทำความสะอาดข้อมูลเกือบทั้งหมดใช้สองไลบรารี (library) นี้ คือ NumPy และ Pandas ซึ่งทำงานบน Python

## สิ่งที่ต้องมี

- Python 3.11 ขึ้นไป
- ตัวจัดการแพ็กเกจ `uv` หรือ `pip`

ตรวจว่ามี Python แล้วหรือยัง

```bash
python3 --version
```

ถ้าขึ้นเลขเวอร์ชันตั้งแต่ `3.11` แปลว่าใช้ได้

## ติดตั้งไลบรารีของโปรเจกต์

เข้าโฟลเดอร์โปรเจกต์แล้วสั่ง

```bash
uv sync
```

ถ้าไม่มี `uv` ใช้ `pip` แทนได้

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install numpy pandas pytest ruff
```

## แนวคิดแรก: `print`

`print` ใช้แสดงข้อความออกมาที่หน้าจอ

เราใช้มันเพราะมันทำให้เราเห็นว่าข้อมูลที่อ่านเข้ามาหน้าตาเป็นอย่างไร ก่อนจะเชื่ออะไรก็ตาม

```python
print("Hello Data")
```

ผลลัพธ์

```txt
Hello Data
```

## ตัวแปร

ตัวแปร (variable) คือชื่อที่ใช้เก็บค่าไว้ใช้ต่อ

```python
student_name = "Student"
student_age = 17

print(student_name)
print(student_age)
```

ผลลัพธ์

```txt
Student
17
```

## f-string

f-string คือข้อความที่แทรกค่าของตัวแปรเข้าไปได้ในบรรทัดเดียว

เราจะใช้มันบ่อยมากเวลาพิมพ์รายงานสรุปข้อมูล

```python
student_name = "Student"
student_age = 17

print(f"ชื่อ: {student_name}")
print(f"อายุ: {student_age} ปี")
```

ผลลัพธ์

```txt
ชื่อ: Student
อายุ: 17 ปี
```

## การรันไฟล์

ไฟล์ `.py` คือไฟล์ Python

รันด้วยคำสั่งนี้จากโฟลเดอร์โปรเจกต์

```bash
uv run python curriculum/ch01/hello-world.py
```

หรือถ้าเปิด virtual environment ไว้แล้ว

```bash
python curriculum/ch01/hello-world.py
```

## ไฟล์ที่ต้องแก้

ไฟล์ใน `curriculum/` ไว้สำหรับอ่านและรันดู

ไฟล์ใน `exercises/` เป็นโจทย์ที่ให้แก้และส่งตรวจ

บทนี้ให้แก้ไฟล์นี้

```txt
exercises/ch01-first-code.py
```

## โจทย์ที่ต้องทำ

เปิด `exercises/ch01-first-code.py`

แก้ค่าในไฟล์ให้พิมพ์ออกมาเป็น

1. ชื่อของคุณ
2. อายุของคุณ
3. เป้าหมายของคุณในหลักสูตรนี้

ตัวอย่างผลลัพธ์

```txt
ชื่อ: Student
อายุ: 17 ปี
เป้าหมาย: ทำความสะอาดข้อมูลให้พร้อมใช้
```

เมื่อเสร็จแล้วพิมพ์

```txt
ตรวจ Ch1
```
