# บทที่ 9: NumPy array

## ทบทวน

บทที่แล้วเราดักข้อผิดพลาดด้วย `try` กับ `except` ทำให้ฟังก์ชันทำความสะอาดคืน `None` แทนการพัง

ตอนนี้เราจัดการข้อมูลทีละค่าได้แล้ว แต่ข้อมูลจริงมีหลักพันหลักล้านแถว

## NumPy คืออะไร

NumPy คือไลบรารีสำหรับคำนวณกับตัวเลขจำนวนมาก

หัวใจของมันคือ array ซึ่งเป็นโครงสร้างเก็บตัวเลขชนิดเดียวกันเรียงต่อกันในหน่วยความจำ

ทำไมต้องใช้ในงานทำความสะอาดข้อมูล เพราะการคำนวณทั้งคอลัมน์พร้อมกันเร็วกว่าการวนลูปทีละค่าเป็นสิบเท่าขึ้นไป และ Pandas ที่เราใช้บทหลังสร้างอยู่บน NumPy ทั้งหมด

## การนำเข้า

เรานำเข้าโดยตั้งชื่อย่อว่า `np` ซึ่งเป็นธรรมเนียมที่ทุกคนใช้ตรงกัน

```python
import numpy as np

print(np.__version__)
```

ผลลัพธ์

```txt
2.5.4
```

## array กับ list ต่างกันอย่างไร

ลิสต์เก็บอะไรก็ได้ปนกัน และบวกกันแล้วได้การต่อลิสต์

array เก็บตัวเลขชนิดเดียวกัน และบวกกันแล้วได้การบวกทีละสมาชิก

```python
import numpy as np

quantities = [3, 1, 2, 0]
prices = np.array([450.0, 1150.0, 300.0, 99.5])

print(quantities + quantities)
print(prices)
print(type(prices))
```

ผลลัพธ์

```txt
[3, 1, 2, 0, 3, 1, 2, 0]
[ 450.  1150.   300.    99.5]
<class 'numpy.ndarray'>
```

## dtype

dtype คือชนิดของตัวเลขที่ array เก็บ

array เก็บได้ชนิดเดียวทั้งก้อน ถ้าใส่จำนวนเต็มจะได้ `int64` ถ้าใส่ทศนิยมจะได้ `float64`

```python
import numpy as np

quantities = np.array([3, 1, 2, 0])
prices = np.array([450.0, 1150.0, 300.0, 99.5])

print(quantities.dtype)
print(prices.dtype)
```

ผลลัพธ์

```txt
int64
float64
```

เรื่องนี้สำคัญเพราะคอลัมน์ที่ควรเป็นตัวเลขแต่ถูกอ่านมาเป็นข้อความ จะคำนวณไม่ได้เลย

## shape, size และ ndim

สามคำนี้ตอบคำถามต่างกัน

- shape คือขนาดแต่ละมิติ
- size คือจำนวนสมาชิกทั้งหมด
- ndim คือจำนวนมิติ

```python
import numpy as np

quantities = np.array([3, 1, 2, 0])
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print(quantities.shape)
print(quantities.size)
print(quantities.ndim)

print(matrix.shape)
print(matrix.size)
print(matrix.ndim)
```

ผลลัพธ์

```txt
(4,)
4
1
(2, 3)
6
2
```

`(4,)` อ่านว่าหนึ่งมิติยาวสี่ สังเกตว่ามีลูกน้ำต่อท้าย เพราะมันคือทูเพิล (tuple) ที่มีสมาชิกตัวเดียว

## การสร้าง array

นอกจาก `np.array` ยังมีตัวช่วยสร้างที่ใช้บ่อย

```python
import numpy as np

print(np.zeros(3))
print(np.ones(2, dtype=int))
print(np.arange(0, 10, 3))
```

ผลลัพธ์

```txt
[0. 0. 0.]
[1 1]
[0 3 6 9]
```

`np.zeros` ให้ศูนย์ล้วน `np.ones` ให้หนึ่งล้วน `np.arange` ให้นับช่วงแบบก้าวหน้า

## การบังคับ dtype

เราใส่ `dtype` ตอนสร้างได้ เพื่อกำหนดชนิดตั้งแต่ต้น

การแปลง float เป็น int จะตัดทศนิยมทิ้ง ไม่ปัด

```python
import numpy as np

print(np.array([3, 1, 2], dtype=float))
print(np.array([3.7, 1.2], dtype=int))
```

ผลลัพธ์

```txt
[3. 1. 2.]
[3 1]
```

## การเข้าถึงด้วย index

array ใช้ index เหมือนลิสต์ เริ่มที่ศูนย์ และใช้ค่าติดลบเพื่อนับจากท้ายได้

```python
import numpy as np

quantities = np.array([3, 1, 2, 5, 0, 4])

print(quantities[0])
print(quantities[-1])
print(quantities[2])
```

ผลลัพธ์

```txt
3
4
2
```

## การตัดช่วงด้วย slice

slice เขียนเป็น `[start:stop:step]` โดยไม่รวมตำแหน่ง stop

```python
import numpy as np

quantities = np.array([3, 1, 2, 5, 0, 4])

print(quantities[1:4])
print(quantities[:2])
print(quantities[3:])
print(quantities[::2])
print(quantities[::-1])
```

ผลลัพธ์

```txt
[1 2 5]
[3 1]
[5 0 4]
[3 2 0]
[4 0 5 2 1 3]
```

## boolean mask

นี่คือเครื่องมือที่สำคัญที่สุดของบทนี้

การเขียน `quantities > 2` จะได้ array ของค่าจริงเท็จ ที่มีขนาดเท่ากัน

เอา array นั้นไปใส่ในวงเล็บเหลี่ยม จะได้เฉพาะสมาชิกที่ตำแหน่งนั้นเป็นจริง

```python
import numpy as np

quantities = np.array([3, 1, 2, 5, 0, 4])
prices = np.array([450.0, 1150.0, 300.0, 99.5, 800.0, 250.0])

mask = quantities > 2
print(mask)
print(mask.dtype)
print(prices[mask])
```

ผลลัพธ์

```txt
[ True False False  True False  True]
bool
[450.   99.5 250. ]
```

รวมสองเงื่อนไขด้วย `&` สำหรับ "และ" กับ `|` สำหรับ "หรือ" โดยต้องใส่วงเล็บทุกครั้ง

```python
import numpy as np

quantities = np.array([3, 1, 2, 5, 0, 4])
prices = np.array([450.0, 1150.0, 300.0, 99.5, 800.0, 250.0])

print(prices[(quantities > 0) & (prices < 500)])
print(quantities[quantities == 0])
```

ผลลัพธ์

```txt
[450.  300.   99.5 250. ]
[0]
```

การนับว่ามีกี่แถวที่ตรงเงื่อนไข ทำได้ด้วย `sum` เพราะค่าจริงนับเป็นหนึ่ง ค่าเท็จนับเป็นศูนย์

```python
import numpy as np

quantities = np.array([3, 1, 2, 5, 0, 4])
mask = quantities > 2

print(mask.sum())
```

ผลลัพธ์

```txt
3
```

## array สองมิติ

array ซ้อน array ได้ เกิดเป็นตารางที่มีแถวและคอลัมน์

การเข้าถึงใช้ `[แถว, คอลัมน์]` และใช้ `:` แทน "ทุกตัว"

```python
import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]])

print(matrix[0])
print(matrix[1, 2])
print(matrix[:, 0])
print(matrix[0:2, 1:3])
```

ผลลัพธ์

```txt
[1 2 3]
6
[1 4]
[[2 3]
 [5 6]]
```

`matrix[:, 0]` อ่านว่าทุกแถวในคอลัมน์แรก

## ใช้กับข้อมูลจริง

ข้อมูลราคาในไฟล์ CSV มาเป็นข้อความที่มีสัญลักษณ์บาทและ comma

ถ้าเราแปลงเป็น array ของ float ได้ การคำนวณทุกอย่างจะตามมาเอง

```python
import numpy as np


def price_array(texts: list[str]) -> np.ndarray:
    cleaned = [text.replace("฿", "").replace(",", "") for text in texts]
    return np.array(cleaned, dtype=float)


prices = price_array(["฿1,150", "450", "300.00"])
print(prices)
print(prices.dtype)
```

ผลลัพธ์

```txt
[1150.  450.  300.]
float64
```

## ตัวอย่างที่รันได้

- `curriculum/ch09/create-array-example.py` การสร้าง array และดู dtype กับ shape
- `curriculum/ch09/index-slice-example.py` การเข้าถึง การตัดช่วง และ boolean mask

รันด้วยคำสั่งนี้จากโฟลเดอร์โปรเจกต์

```bash
.venv/bin/python curriculum/ch09/create-array-example.py
```

## สรุป

| ต้องการ | ใช้ |
|---|---|
| สร้าง array | `np.array(list)` |
| ดูชนิดตัวเลข | `arr.dtype` |
| ดูขนาดแต่ละมิติ | `arr.shape` |
| นับสมาชิกทั้งหมด | `arr.size` |
| นับจำนวนมิติ | `arr.ndim` |
| สร้างศูนย์หรือหนึ่ง | `np.zeros(n)`, `np.ones(n)` |
| สร้างช่วงตัวเลข | `np.arange(start, stop, step)` |
| เลือกสมาชิกตัวเดียว | `arr[i]` |
| เลือกช่วง | `arr[start:stop:step]` |
| เลือกตามเงื่อนไข | `arr[arr > 0]` |
| รวมสองเงื่อนไข | `(arr > 0) & (arr < 10)` |

หลักที่ควรจำ

- array เก็บตัวเลขชนิดเดียวทั้งก้อน
- เงื่อนไขบน array ได้ array ของค่าจริงเท็จ
- boolean mask คือหัวใจของการกรองข้อมูลด้วย NumPy
- ข้อมูลที่อ่านจากไฟล์เป็นข้อความ ต้องแปลงเป็น float ก่อนคำนวณ

## โจทย์ที่ต้องทำ

เปิดไฟล์ `exercises/ch09-array-basics.py` แล้วเขียนสี่ฟังก์ชัน

1. `make_array(values)` สร้าง array หนึ่งมิติจากลิสต์
2. `shape_info(values)` คืนทูเพิล `(size, ndim)` ของ array
3. `select_even(values)` คืน array ของเฉพาะค่าที่หารสองลงตัว
4. `replace_negative(values, replacement=0.0)` คืน array ใหม่ที่ค่าติดลบถูกแทนด้วย `replacement` โดยไม่แก้ลิสต์ต้นฉบับ

## ผลลัพธ์ที่คาดหวัง

รันโจทย์แล้วได้แบบนี้

```txt
make_array([1, 2, 3]) ได้ [1 2 3]
dtype ของผลลัพธ์คือ int64
shape_info([1, 2, 3]) ได้ (3, 1)
select_even([1, 2, 3, 4]) ได้ [2 4]
replace_negative([1, -2, 3]) ได้ [1. 0. 3.]
```

## เสร็จแล้วพิมพ์ ตรวจ Ch9
