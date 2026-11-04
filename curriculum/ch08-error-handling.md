# บทที่ 8: การจัดการข้อผิดพลาด

## ทบทวน

บทที่แล้วเราอ่านและเขียนไฟล์ด้วย `pathlib` และแยกข้อความด้วยเมธอดของ string

ตอนอ่านไฟล์จริง เราจะเจอสองปัญหาเกือบทุกครั้ง

- ไฟล์ที่ถูกอ้างถึงไม่มีอยู่จริง
- ค่าที่อ่านได้หน้าตาไม่เหมือนที่คาด เช่น `""` หรือ `None`

ถ้าเราไม่ดักไว้ โปรแกรมจะหยุดกลางคันและทิ้งงานที่ทำมาทั้งหมด

## ข้อผิดพลาด (error) คืออะไร

ข้อผิดพลาดคือสิ่งที่ Python โยนออกมาเมื่อคำสั่งหนึ่งทำไม่ได้

คำว่า "โยน" ตรงกับคำว่า raise ในภาษาไทยเราใช้คำว่า โยนข้อผิดพลาด

เมื่อไม่มีใครรับไว้ โปรแกรมจะหยุดทำงานทันที

ลองสั่งแบบนี้จากโฟลเดอร์โปรเจกต์

```bash
.venv/bin/python -c 'print(int("สอง"))'
```

ผลลัพธ์

```txt
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'สอง'
```

บรรทัดสุดท้ายสำคัญที่สุด มันบอกชนิดของข้อผิดพลาดคือ `ValueError` และบอกว่าอะไรผิด

## try กับ except

`try` คือบล็อกที่เราบอกว่า "ลองทำตรงนี้ก่อน"

`except` คือบล็อกที่รับข้อผิดพลาดเมื่อเกิดขึ้น

ทำไมต้องใช้ในงานทำความสะอาดข้อมูล เพราะข้อมูลดิบมีแถวเสียปนอยู่เสมอ ถ้าหนึ่งแถวพังแล้วทั้งไฟล์พังตาม เราจะทำงานไม่ได้เลย

```python
def parse_quantity_safe(text: str) -> int | None:
    try:
        return int(text)
    except ValueError:
        return None


print(f"parse_quantity_safe('3') ได้ {parse_quantity_safe('3')}")
print(f"parse_quantity_safe('') ได้ {parse_quantity_safe('')}")
print(f"parse_quantity_safe('สอง') ได้ {parse_quantity_safe('สอง')}")
```

ผลลัพธ์

```txt
parse_quantity_safe('3') ได้ 3
parse_quantity_safe('') ได้ None
parse_quantity_safe('สอง') ได้ None
```

สังเกตว่า `int("")` โยน `ValueError` และฟังก์ชันคืน `None` แทนการพัง

## จับหลายชนิดด้วยวงเล็บ

ข้อมูลดิบไม่ได้ส่งมาเป็นข้อความเสมอ บางช่องว่างมาถึงเราเป็น `None`

`int(None)` โยน `TypeError` ไม่ใช่ `ValueError`

ถ้าจับแค่ `ValueError` โปรแกรมยังพังอยู่ดี

```python
def parse_quantity_any(value) -> int | None:
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


print(f"parse_quantity_any(None) ได้ {parse_quantity_any(None)}")
print(f"parse_quantity_any('7') ได้ {parse_quantity_any('7')}")
```

ผลลัพธ์

```txt
parse_quantity_any(None) ได้ None
parse_quantity_any('7') ได้ 7
```

วงเล็บใน `except` คือการบอกว่า "จับทั้งสองชนิดนี้"

## ดูข้อความจริงของข้อผิดพลาด

ก่อนจะดัก เราควรรู้ก่อนว่าข้อผิดพลาดจริงพูดว่าอะไร

เขียน `except ... as error` แล้วพิมพ์ `error` ออกมา

```python
try:
    int("")
except ValueError as error:
    print(f"ValueError บอกว่า {error}")

try:
    int(None)
except TypeError as error:
    print(f"TypeError บอกว่า {error}")
```

ผลลัพธ์

```txt
ValueError บอกว่า invalid literal for int() with base 10: ''
TypeError บอกว่า int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
```

ข้อความนี้เป็นของ Python ไม่ใช่ของเรา เราพิมพ์ดูตอนพัฒนาได้ แต่ไม่ควรเอาไปโชว์ผู้ใช้ตรง ๆ

## จับเฉพาะที่คาดไว้

`except Exception` จับได้ทุกอย่าง แต่ทำให้เราไม่รู้ว่าอะไรผิดจริง

หลักคือจับเฉพาะชนิดที่เรารู้ว่าจะเกิด และจัดการมันได้

```python
def lookup_tier(tiers: dict[str, str], customer_id: str) -> str:
    try:
        return tiers[customer_id]
    except KeyError:
        return "Unknown"


tiers = {"C001": "Gold", "C002": "Silver"}
print(f"lookup_tier('C001') ได้ {lookup_tier(tiers, 'C001')}")
print(f"lookup_tier('C999') ได้ {lookup_tier(tiers, 'C999')}")
```

ผลลัพธ์

```txt
lookup_tier('C001') ได้ Gold
lookup_tier('C999') ได้ Unknown
```

`KeyError` เกิดเมื่อคีย์ (key) ไม่มีในดิกชันนารี

## โยนข้อผิดพลาดเองด้วย raise

บางครั้งข้อมูลไม่ได้ทำให้ Python พัง แต่ผิดกฎทางธุรกิจของเรา

เช่น จำนวนสินค้าต้องมากกว่าศูนย์

กรณีแบบนี้เราโยนข้อผิดพลาดเอง เพื่อให้คนเรียกฟังก์ชันรู้ว่าข้อมูลใช้ไม่ได้

```python
def require_positive_quantity(text: str) -> int:
    quantity = int(text)
    if quantity <= 0:
        raise ValueError(f"จำนวนต้องมากกว่าศูนย์ แต่ได้ {quantity}")
    return quantity


print(f"require_positive_quantity('2') ได้ {require_positive_quantity('2')}")
try:
    require_positive_quantity("0")
except ValueError as error:
    print(f"จับได้ {error}")
```

ผลลัพธ์

```txt
require_positive_quantity('2') ได้ 2
จับได้ จำนวนต้องมากกว่าศูนย์ แต่ได้ 0
```

ข้อความใน `ValueError` เป็นของเราเอง เราจึงเขียนให้อ่านรู้เรื่องได้

## finally

`finally` คือบล็อกที่ทำงานเสมอ ไม่ว่าข้างในจะสำเร็จหรือพัง

ใช้เมื่อมีอะไรต้องคืนทรัพยากร เช่น ปิดไฟล์

```python
from pathlib import Path


def read_first_line(path: Path) -> str:
    handle = None
    try:
        handle = path.open(encoding="utf-8")
        return handle.readline().rstrip("\n")
    except FileNotFoundError:
        return ""
    finally:
        if handle is not None:
            handle.close()


products = Path("data/raw/products.csv")
missing = Path("data/raw/ไม่มีไฟล์นี้.csv")

print(f"แถวหัวตารางคือ {read_first_line(products)}")
print(f"ไฟล์ที่ไม่มีอยู่ได้ {read_first_line(missing)!r}")
```

ผลลัพธ์

```txt
แถวหัวตารางคือ product_id,product_name,category,list_price
ไฟล์ที่ไม่มีอยู่ได้ ''
```

ไฟล์ถูกปิดทุกครั้ง ไม่ว่าจะอ่านสำเร็จหรือไม่

## else ใน try

`else` ทำงานเมื่อ `try` สำเร็จโดยไม่มีข้อผิดพลาด

เราใช้มันเพื่อแยก "โค้ดที่อาจพัง" ออกจาก "โค้ดที่ทำต่อเมื่อไม่พัง"

```python
from pathlib import Path


def count_data_rows(path: Path) -> int:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        return 0
    else:
        return max(len(lines) - 1, 0)


print(f"products.csv มีข้อมูล {count_data_rows(Path('data/raw/products.csv'))} แถว")
print(f"ไฟล์ที่ไม่มีอยู่ได้ {count_data_rows(Path('data/raw/ไม่มีไฟล์นี้.csv'))} แถว")
```

ผลลัพธ์

```txt
products.csv มีข้อมูล 8 แถว
ไฟล์ที่ไม่มีอยู่ได้ 0 แถว
```

## ภาพรวมลำดับการทำงาน

ตัวอย่างนี้ทำให้เห็นลำดับทั้งสี่ส่วนในครั้งเดียว

```python
steps = []
try:
    steps.append("เปิดไฟล์")
    raise ValueError("ข้อมูลแถวที่ 3 ผิดรูป")
except ValueError as error:
    steps.append(f"จัดการ {error}")
finally:
    steps.append("ปิดไฟล์")

print(steps)
```

ผลลัพธ์

```txt
['เปิดไฟล์', 'จัดการ ข้อมูลแถวที่ 3 ผิดรูป', 'ปิดไฟล์']
```

## ตัวอย่างที่รันได้

- `curriculum/ch08/try-except-example.py` รวมทุกกรณีของ `try` กับ `except` และ `raise`
- `curriculum/ch08/finally-example.py` เรื่อง `finally` กับ `else` และการปิดไฟล์

รันด้วยคำสั่งนี้จากโฟลเดอร์โปรเจกต์

```bash
.venv/bin/python curriculum/ch08/try-except-example.py
```

## สรุป

| ต้องการ | ใช้ |
|---|---|
| ลองทำโค้ดที่อาจพัง | `try` |
| รับข้อผิดพลาดชนิดที่คาดไว้ | `except ValueError` |
| รับหลายชนิดพร้อมกัน | `except (ValueError, TypeError)` |
| ดูข้อความจริงของข้อผิดพลาด | `except ValueError as error` |
| ทำงานเสมอไม่ว่าจะพังหรือไม่ | `finally` |
| ทำงานเมื่อไม่พังเท่านั้น | `else` |
| แจ้งว่าข้อมูลผิดกฎ | `raise ValueError("...")` |

หลักที่ควรจำ

- จับเฉพาะชนิดที่รู้ว่าจะเกิด
- ฟังก์ชันที่ใช้ทำความสะอาดข้อมูลมักคืน `None` เมื่อแปลงไม่ได้ ดีกว่าโยนข้อผิดพลาด
- ฟังก์ชันที่ตรวจกฎทางธุรกิจควรโยนข้อผิดพลาด เพื่อให้ผู้เรียกตัดสินใจเอง

## โจทย์ที่ต้องทำ

เปิดไฟล์ `exercises/ch08-safe-parsers.py` แล้วเขียนสี่ฟังก์ชัน

1. `safe_divide(a, b)` คืนผลหาร หรือ `None` เมื่อ `b` เป็นศูนย์
2. `parse_int(value)` คืนจำนวนเต็ม หรือ `None` เมื่อแปลงไม่ได้
3. `read_text_or_default(path, default="")` อ่านข้อความทั้งไฟล์ หรือคืน `default` เมื่อไฟล์ไม่มี
4. `read_json_object(path)` อ่านไฟล์ JSON คืน `dict` และโยน `ValueError` ข้อความ `JSON ต้องเป็น object` เมื่อค่าไม่ใช่ object

## ผลลัพธ์ที่คาดหวัง

รันโจทย์แล้วได้แบบนี้

```txt
safe_divide(10, 2) ได้ 5.0
safe_divide(1, 0) ได้ None
parse_int('42') ได้ 42
parse_int('4.2') ได้ None
parse_int(None) ได้ None
ไฟล์ที่ไม่มีอยู่ได้ 'none'
อ่าน JSON ได้ {'customer_id': 'C001'}
จับได้ JSON ต้องเป็น object
```

## เสร็จแล้วพิมพ์ ตรวจ Ch8
