# บทที่ 7: ข้อความและไฟล์

## ทบทวน

บทที่แล้วเราเก็บข้อมูลเป็นลิสต์ของดิกชันนารี แต่ข้อมูลยังถูกพิมพ์ไว้ในโค้ด

ข้อมูลจริงอยู่ในไฟล์ บทนี้จะพาจากสองทิศทาง คือทำความสะอาดข้อความที่อยู่ในแต่ละช่อง กับการอ่านและเขียนไฟล์จริงในโฟลเดอร์ `data/raw`

## ข้อความเป็นลำดับของตัวอักษร

ข้อความ (string) เก็บตัวอักษรเรียงต่อกัน เข้าถึงด้วยดัชนีได้เหมือนลิสต์ และตัดช่วงได้ด้วย slice

เราใช้ท่านี้ตอนดึงรหัสสินค้าสองตัวอักษรแรก หรือตัดปีออกจากวันที่

```python
code = "P001-KEYBOARD"

print("ทั้งข้อความ", code)
print("ตัวแรก", code[0])
print("สามตัวแรก", code[:3])
print("ห้าตัวท้าย", code[-5:])
print("จำนวนตัวอักษร", len(code))
```

ผลลัพธ์

```txt
ทั้งข้อความ P001-KEYBOARD
ตัวแรก P
สามตัวแรก P00
ห้าตัวท้าย BOARD
จำนวนตัวอักษร 13
```

ข้อความแก้ไขตรงตำแหน่งไม่ได้ ต้องสร้างข้อความใหม่เสมอ นี่คือเหตุผลที่ทุกเมธอดด้านล่างคืนค่าใหม่แทนการแก้ของเดิม

## strip ตัดช่องว่างหัวท้าย

`strip` ตัดช่องว่าง ขึ้นบรรทัดใหม่ และแท็บออกจากสองหัวท้าย

ข้อมูลจากไฟล์ CSV (comma-separated values) มักมีช่องว่างติดมาโดยเราไม่เห็น นี่คือปัญหาอันดับหนึ่งที่ทำให้ค่า `"Thailand"` กับ `" Thailand"` ถูกนับเป็นคนละค่า

```python
raw_name = "  Nattapong   Sri  "

print("ก่อนทำความสะอาด", f"[{raw_name}]")
print("หลัง strip", f"[{raw_name.strip()}]")
cleaned_name = " ".join(raw_name.split())
print(f"หลังยุบช่องว่างซ้ำ [{cleaned_name}]")
```

ผลลัพธ์

```txt
ก่อนทำความสะอาด [  Nattapong   Sri  ]
หลัง strip [Nattapong   Sri]
หลังยุบช่องว่างซ้ำ [Nattapong Sri]
```

`strip` ไม่แตะช่องว่างที่อยู่ตรงกลาง ถ้าอยากยุบช่องว่างซ้ำให้เหลือช่องเดียว ใช้ `split()` แล้วต่อกลับด้วย `" "` วิธีนี้จะนำไปใช้ซ้ำได้เมื่อเราเขียนฟังก์ชันทำความสะอาดข้อความ

## เปลี่ยนตัวพิมพ์

`lower` `upper` และ `title` เปลี่ยนตัวพิมพ์ทั้งข้อความ

เราใช้เพื่อให้ค่าเดียวกันเขียนเหมือนกันทุกแถว ก่อนจะนับหรือจับคู่ ค่าอย่าง `GOLD` กับ `gold` จะกลายเป็นค่าเดียวกันหลัง `lower`

```python
raw_country = "thailand "

print("ตัวพิมพ์เล็ก", raw_country.strip().lower())
print("ตัวพิมพ์ใหญ่", raw_country.strip().upper())
print("ขึ้นต้นคำด้วยตัวใหญ่", raw_country.strip().title())
```

ผลลัพธ์

```txt
ตัวพิมพ์เล็ก thailand
ตัวพิมพ์ใหญ่ THAILAND
ขึ้นต้นคำด้วยตัวใหญ่ Thailand
```

`title` เปลี่ยนตัวแรกของทุกคำเป็นตัวใหญ่ เหมาะกับชื่อประเทศและชื่อหมวด แต่ไม่เหมาะกับอีเมล เพราะจะไปเปลี่ยนโดเมนเป็นตัวใหญ่

## replace แทนที่ข้อความ

`replace` แทนที่ทุกครั้งที่เจอ ถ้าใส่อาร์กิวเมนต์ที่สามจะจำกัดจำนวนครั้ง

เราใช้มันกับสัญลักษณ์ที่ปนมากับตัวเลข เช่น สัญลักษณ์บาทและเครื่องหมายจุลภาคในหลักพัน

```python
raw_price = "฿1,150"

print("ตัดสัญลักษณ์บาท", raw_price.replace("฿", ""))
print("ตัดบาทกับ comma", raw_price.replace("฿", "").replace(",", ""))
print("แปลงเป็นตัวเลข", float(raw_price.replace("฿", "").replace(",", "")))
```

ผลลัพธ์

```txt
ตัดสัญลักษณ์บาท 1,150
ตัดบาทกับ comma 1150
แปลงเป็นตัวเลข 1150.0
```

ต่อกันหลายครั้งแบบนี้ดูรก แต่เป็นท่ามาตรฐานที่บทที่ 17 จะเขียนใหม่ด้วย Pandas ในบรรทัดเดียว

## ตรวจรูปแบบด้วย startswith และ in

`startswith` บอกว่าข้อความขึ้นต้นด้วยชิ้นที่ให้มาหรือไม่ `in` บอกว่ามีชิ้นนั้นอยู่ข้างในหรือไม่

สองตัวนี้คืนค่าจริงเท็จ ใช้เป็นเงื่อนไขใน `if` หรือในการสร้างลิสต์แบบเข้าใจได้ทันที

```python
raw_phone = "(66) 802003004"
plus_phone = "+66801002003"

cleaned_phone = raw_phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
print("แบบมีวงเล็บ", cleaned_phone)
print("แบบมีเครื่องหมายบวก", plus_phone)
print("ขึ้นต้นด้วยรหัสประเทศ", plus_phone.startswith("+66"))
print("แทนรหัสประเทศด้วยศูนย์", plus_phone.replace("+66", "0", 1))
```

ผลลัพธ์

```txt
แบบมีวงเล็บ 66802003004
แบบมีเครื่องหมายบวก +66801002003
ขึ้นต้นด้วยรหัสประเทศ True
แทนรหัสประเทศด้วยศูนย์ 0801002003
```

เบอร์ที่ขึ้นต้นด้วย `+66` ต้องแทนที่ด้วย `0` ก่อนจึงจะยาวสิบหลักเท่ากันทุกเบอร์ ซึ่งเป็นกฎที่บทที่ 20 ใช้จริง

## split และ join

`split` แยกข้อความเป็นลิสต์ตามตัวคั่น `join` ต่อลิสต์กลับเป็นข้อความ

split และ join เป็นคู่คำสั่งที่ใช้แยกข้อความและประกอบข้อความกลับเข้าด้วยกัน

```python
line = "P001, Keyboard ,Accessory,450"

fields = line.split(",")
print("แยกด้วย comma", fields)
print("ต่อกลับ", "-".join(["P001", "Keyboard", "450"]))
print("ตัดช่องว่างแต่ละช่อง", [field.strip() for field in fields])
print("มีคำว่า Accessory หรือไม่", "Accessory" in fields)
```

ผลลัพธ์

```txt
แยกด้วย comma ['P001', ' Keyboard ', 'Accessory', '450']
ต่อกลับ P001-Keyboard-450
ตัดช่องว่างแต่ละช่อง ['P001', 'Keyboard', 'Accessory', '450']
มีคำว่า Accessory หรือไม่ True
```

`"Accessory" in fields` ตรวจว่าลิสต์มีสมาชิกที่เท่ากันพอดี ไม่ใช่ตรวจว่ามีข้อความย่อยอยู่ข้างใน ต่างจาก `in` ที่ใช้กับข้อความ

## จัดคอลัมน์ด้วย f-string

f-string จัดความกว้างของข้อความได้ด้วย `:<` และ `:>` ตามด้วยจำนวนช่อง และจัดตัวเลขด้วย `,` คั่นหลักพันกับ `.2f` ทศนิยมสองตำแหน่ง

เราใช้ท่านี้พิมพ์รายงานตรวจข้อมูลให้อ่านง่ายก่อนส่งต่อ

```python
print(f"{'สินค้า':<12}{'ราคา':>8}")
print(f"{'Keyboard':<12}{450:>8}")
print(f"{'Monitor':<12}{4200:>8,.2f}")
```

ผลลัพธ์

```txt
สินค้า          ราคา
Keyboard         450
Monitor     4,200.00
```

## อ่านไฟล์ทั้งไฟล์ด้วย read_text

`Path` จากโมดูล `pathlib` ใช้แทนเส้นทางไฟล์ เปิดอ่านด้วย `read_text` แล้วระบุ `encoding` ทุกครั้ง

การระบุ encoding ไว้เสมอกันปัญหาภาษาไทยเพี้ยนบนเครื่องที่ตั้งค่าเริ่มต้นต่างกัน

```python
from pathlib import Path

path = Path("data/raw/products.csv")
text = path.read_text(encoding="utf-8")
lines = text.splitlines()

print("จำนวนบรรทัดทั้งหมด", len(lines))
print("บรรทัดแรก", lines[0])
print("บรรทัดที่สอง", lines[1])
```

ผลลัพธ์

```txt
จำนวนบรรทัดทั้งหมด 9
บรรทัดแรก product_id,product_name,category,list_price
บรรทัดที่สอง P001, Keyboard ,Accessory,450
```

ไฟล์มีเก้าบรรทัด แต่มีข้อมูลแปดแถว เพราะบรรทัดแรกเป็นหัวตาราง (header) ซึ่งไม่ใช่ข้อมูล

## อ่าน CSV ด้วย csv.reader

`csv.reader` แยกแต่ละบรรทัดเป็นลิสต์ของช่องให้เอง และจัดการเรื่องเครื่องหมายจุลภาคที่อยู่ในเครื่องหมายคำพูดให้ด้วย

เราใช้มันแทนการ `split(",")` เอง เพราะข้อมูลจริงมีเครื่องหมายจุลภาคอยู่ในช่องได้

```python
import csv
from pathlib import Path

path = Path("data/raw/products.csv")

with path.open(encoding="utf-8", newline="") as handle:
    reader = csv.reader(handle)
    header = next(reader)
    rows = list(reader)

print("หัวตาราง", header)
print("จำนวนแถวข้อมูล", len(rows))
print("แถวแรก", rows[0])
```

ผลลัพธ์

```txt
หัวตาราง ['product_id', 'product_name', 'category', 'list_price']
จำนวนแถวข้อมูล 8
แถวแรก ['P001', ' Keyboard ', 'Accessory', '450']
```

`with` ปิดไฟล์ให้เองเมื่อจบ ลืมปิดไม่ได้ และ `newline=""` กันไม่ให้ Python แปลงตัวขึ้นบรรทัดใหม่ซ้ำ

## อ่าน CSV เป็นดิกชันนารีด้วย DictReader

`csv.DictReader` เอาหัวตารางไปเป็นกุญแจ แล้วคืนแถวละดิกชันนารี

รูปนี้ต่อกับบทที่ 6 ตรง ๆ เพราะ `row["product_name"]` อ่านง่ายกว่า `row[1]` มาก และไม่พังเมื่อลำดับคอลัมน์ในไฟล์เปลี่ยน

```python
import csv
from pathlib import Path

path = Path("data/raw/products.csv")

with path.open(encoding="utf-8", newline="") as handle:
    dict_rows = list(csv.DictReader(handle))

print("แถวแรก", dict_rows[0])
print(f"ชื่อสินค้าแถวแรก [{dict_rows[0]["product_name"]}]")
print(f"หมวดของแถวแรก [{dict_rows[0]["category"]}]")
```

ผลลัพธ์

```txt
แถวแรก {'product_id': 'P001', 'product_name': ' Keyboard ', 'category': 'Accessory', 'list_price': '450'}
ชื่อสินค้าแถวแรก [ Keyboard ]
หมวดของแถวแรก [Accessory]
```

ทุกค่าเป็นข้อความหมด แม้คอลัมน์ `list_price` จะดูเป็นตัวเลข การแปลงชนิดเป็นเรื่องของบทที่ 17

## ไฟล์ภาษาไทยกับ BOM

ไฟล์ `customers_th.csv` ถูกบันทึกด้วย UTF-8 ที่มี BOM (byte order mark) ซึ่งเป็นสามไบต์ลับที่วางไว้ต้นไฟล์

ถ้าเปิดด้วย `utf-8` ธรรมดา สามไบต์นี้จะไปติดอยู่หน้าชื่อคอลัมน์แรก ทำให้กุญแจกลายเป็น `"\ufeffcustomer_id"` แล้วหาไม่เจอ

```python
from pathlib import Path

path = Path("data/raw/customers_th.csv")
print("สามไบต์แรก", path.read_bytes()[:3])
```

ผลลัพธ์

```txt
สามไบต์แรก b'\xef\xbb\xbf'
```

`utf-8-sig` จะตัดสามไบต์นั้นทิ้งให้เองเมื่ออ่าน และเติมกลับให้เมื่อเขียน

```python
import csv
from pathlib import Path

path = Path("data/raw/customers_th.csv")

with path.open(encoding="utf-8-sig", newline="") as handle:
    thai_rows = list(csv.DictReader(handle))

print("จำนวนลูกค้าไทย", len(thai_rows))
for row in thai_rows:
    print(f"{row['customer_id']} {row['name']} {row['province']}")
```

ผลลัพธ์

```txt
จำนวนลูกค้าไทย 3
C001 สมชาย ใจดี กรุงเทพมหานคร
C002 นัฐพงษ์ ศรี เชียงใหม่
C003 มาลี วงศ์สกุล ขอนแก่น
```

## เขียนไฟล์ด้วย write_text

`write_text` เขียนข้อความทั้งก้อนลงไฟล์ ทับของเดิมถ้ามีอยู่แล้ว

เราใช้มันเขียนผลลัพธ์ที่ผ่านการตรวจแล้ว เพื่อให้รอบถัดไปอ่านต่อได้โดยไม่ต้องคำนวณซ้ำ

```python
from pathlib import Path

out_path = Path("curriculum/ch07/checked.txt")
selected = ["P001", "P002", "P005"]
out_path.write_text("".join(f"{pid}\n" for pid in selected), encoding="utf-8")

print("เขียนไฟล์แล้ว", out_path.name)
print(out_path.read_text(encoding="utf-8"), end="")
out_path.unlink()
```

ผลลัพธ์

```txt
เขียนไฟล์แล้ว checked.txt
P001
P002
P005
```

แบบที่ใช้ในที่นี้คือ `"".join(f"{pid}\n" ...)` ซึ่งปิดท้ายทุกบรรทัดรวมถึงบรรทัดสุดท้ายด้วย ถ้าใช้ `"\n".join(...)` แทน ไฟล์จะไม่มีขึ้นบรรทัดใหม่ปิดท้าย และหลายเครื่องมืออ่านไฟล์จะถือว่าบรรทัดสุดท้ายยังไม่จบ

## อ่านกลับเพื่อตรวจ

หลังเขียนแล้วควรอ่านกลับมาเทียบ วิธีนี้จับปัญหาบรรทัดหายหรือ encoding ผิดได้ทันที

```python
from pathlib import Path

out_path = Path("curriculum/ch07/checked.txt")
out_path.write_text("P001\nP002\n", encoding="utf-8")
print(out_path.read_text(encoding="utf-8").splitlines())
out_path.unlink()
```

ผลลัพธ์

```txt
['P001', 'P002']
```

## สรุป

| อยากทำอะไร | เขียนแบบนี้ |
|---|---|
| ตัดช่องว่างหัวท้าย | `text.strip()` |
| ยุบช่องว่างซ้ำ | `" ".join(text.split())` |
| ทำเป็นตัวเล็ก | `text.lower()` |
| ทำเป็นตัวใหญ่ | `text.upper()` |
| ขึ้นต้นคำด้วยตัวใหญ่ | `text.title()` |
| แทนข้อความ | `text.replace(old, new)` |
| ตรวจคำนำหน้า | `text.startswith(prefix)` |
| หาตำแหน่ง | `text.find(part)` |
| แยกเป็นลิสต์ | `text.split(",")` |
| ต่อกลับเป็นข้อความ | `",".join(items)` |
| อ่านไฟล์ | `Path(p).read_text(encoding="utf-8")` |
| อ่านทีละบรรทัด | `text.splitlines()` |
| อ่าน CSV เป็นลิสต์ | `csv.reader` |
| อ่าน CSV เป็นดิกชันนารี | `csv.DictReader` |
| อ่านไฟล์ไทย | `encoding="utf-8-sig"` |
| เขียนไฟล์ | `Path(p).write_text(text, encoding="utf-8")` |

กฎที่ต้องจำ

- ข้อความแก้ตรงตำแหน่งไม่ได้ ทุกเมธอดคืนค่าใหม่
- ระบุ `encoding` ทุกครั้งที่เปิดไฟล์ ไม่มีข้อยกเว้น
- ไฟล์ที่มี BOM ต้องใช้ `utf-8-sig` ไม่งั้นชื่อคอลัมน์แรกจะเพี้ยน
- `csv.DictReader` คืนทุกค่าเป็นข้อความ ต้องแปลงชนิดเอง
- บรรทัดแรกของ CSV คือหัวตาราง ไม่ใช่ข้อมูล ต้องข้ามเสมอ

## โจทย์ที่ต้องทำ

เปิด `exercises/ch07-read-raw-file.py` แล้วเติมสี่ฟังก์ชันนี้

1. `count_lines(path)` คืนจำนวนบรรทัดข้อมูลโดยไม่นับหัวตาราง
2. `first_column(path)` คืนค่าคอลัมน์แรกของทุกแถวข้อมูลเป็นลิสต์
3. `write_lines(path, lines)` เขียนข้อความบรรทัดละรายการ ปิดท้ายด้วยขึ้นบรรทัดใหม่
4. `read_thai_csv(path)` อ่านไฟล์ CSV ภาษาไทยด้วย `utf-8-sig` แล้วคืนลิสต์ของดิกชันนารี

ไฟล์ที่ใช้ทดสอบคือ `data/raw/products.csv` `data/raw/customers.csv` และ `data/raw/customers_th.csv`

## ผลลัพธ์ที่คาดหวัง

รันด้วยคำสั่งนี้จากโฟลเดอร์โปรเจกต์

```cmd
python exercises/ch07-read-raw-file.py
```

ต้องได้ผลแบบนี้

```txt
จำนวนแถวสินค้า 8
รหัสสินค้าสามตัวแรก ['P001', 'P002', 'P003']

ลูกค้าไทย 3 คน
C001 สมชาย ใจดี กรุงเทพมหานคร
C002 นัฐพงษ์ ศรี เชียงใหม่
C003 มาลี วงศ์สกุล ขอนแก่น

เขียนไฟล์แล้ว sample-output.txt
P001
P002
```

ตรวจงานตัวเองด้วย

```cmd
python -m pytest tests/test_ch07.py
```

## เสร็จแล้วพิมพ์ ตรวจ Ch7
