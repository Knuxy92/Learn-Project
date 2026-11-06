# บทที่ 6: ลิสต์และดิกชันนารี

## ทบทวน

บทที่แล้วเราเรียนรู้การประกาศฟังก์ชัน การส่งข้อมูลเข้าไปด้วยพารามิเตอร์ และการส่งผลลัพธ์กลับด้วย return

แต่ข้อมูลจริงไม่ได้มาเป็นค่าทีละตัว ข้อมูลหนึ่งตารางมีหลายแถว แต่ละแถวมีหลายคอลัมน์ บทนี้จะสอนโครงสร้างสองตัวที่ใช้เก็บข้อมูลแบบนั้น คือลิสต์ (list) และดิกชันนารี (dictionary)

## ลิสต์คือลำดับของค่า

ลิสต์คือลำดับของค่าที่เรียงต่อกัน สมาชิกแต่ละตัวมีตำแหน่งของตัวเอง เรียกตำแหน่งนั้นว่าดัชนี (index)

ลิสต์สำคัญเพราะข้อมูลหนึ่งคอลัมน์ เช่น ชื่อลูกค้าทั้งหมด หรือยอดใช้จ่ายทั้งหมด เก็บเป็นลิสต์ได้ตรง ๆ และเราต้องเดินผ่านทีละตัวเพื่อตรวจหรือแปลงค่า

```python
customers = [
    "Nattapong Sri",
    "Malee Wongsakul",
    "Kanya P.",
    "Anan Chaiyaporn",
]

print("จำนวนลูกค้า", len(customers))
print("คนแรก", customers[0])
print("คนสุดท้าย", customers[-1])
print("สามคนแรก", customers[:3])
```

ผลลัพธ์

```txt
จำนวนลูกค้า 4
คนแรก Nattapong Sri
คนสุดท้าย Anan Chaiyaporn
สามคนแรก ['Nattapong Sri', 'Malee Wongsakul', 'Kanya P.']
```

ดัชนีเริ่มที่ `0` ไม่ใช่ `1` ดัชนี `-1` หมายถึงตัวสุดท้าย และการตัดช่วง (slice) อย่าง `[:3]` เอาสามตัวแรกออกมาโดยไม่แตะของเดิม

## เข้าถึงสมาชิกและเดินผ่านทั้งลิสต์

เราเข้าถึงสมาชิกด้วยดัชนีเมื่อรู้ตำแหน่ง แต่เวลาทำความสะอาดข้อมูลเราแทบไม่รู้ตำแหน่งล่วงหน้า วิธีที่ใช้จริงคือเดินผ่านทุกตัวด้วย `for`

```python
customers = [
    "Nattapong Sri",
    "Malee Wongsakul",
    "Kanya P.",
]

print("คนแรก", customers[0])
print("คนสุดท้าย", customers[-1])
print("จำนวนสมาชิก", len(customers))

for name in customers:
    print("ชื่อลูกค้า", name)
```

ผลลัพธ์

```txt
คนแรก Nattapong Sri
คนสุดท้าย Kanya P.
จำนวนสมาชิก 3
ชื่อลูกค้า Nattapong Sri
ชื่อลูกค้า Malee Wongsakul
ชื่อลูกค้า Kanya P.
```

ลูป `for` วิ่งผ่านสมาชิกทุกตัวตามลำดับ ไม่ต้องรู้จำนวนล่วงหน้า ตัวแปร `name` เปลี่ยนค่าใหม่ทุกรอบและไม่คงอยู่หลังลูปจบ

คำสั่ง print แสดงค่าของสมาชิกเท่านั้น ไม่ได้แก้ไขข้อมูลในลิสต์

## เพิ่มสมาชิกด้วย append

`append` ต่อสมาชิกใหม่ไว้ท้ายลิสต์

เราใช้มันเมื่อรวมข้อมูลจากหลายแหล่งเข้าด้วยกัน เช่น อ่านไฟล์ทีละไฟล์แล้วสะสมแถวไว้ในลิสต์เดียว

```python
customers = ["Nattapong Sri", "Malee Wongsakul", "Kanya P."]

customers.append("Suda Meesuk")
print("หลังเพิ่ม", len(customers))

for name in customers:
    print(name)
```

ผลลัพธ์

```txt
หลังเพิ่ม 4
Nattapong Sri
Malee Wongsakul
Kanya P.
Suda Meesuk
```

`append` แก้ลิสต์เดิม ไม่ได้คืนลิสต์ใหม่ ถ้าไม่อยากให้ต้นฉบับเปลี่ยนต้องคัดลอกก่อนด้วย `list(customers)`

## รวมค่าด้วยฟังก์ชันในตัว

`sum`, `max`, `min` และ `len` ทำงานกับลิสต์ตัวเลขได้ทันที

สามตัวนี้คือการสรุปค่าที่เราจะเขียนเองด้วยมืออีกไม่กี่บทข้างหน้า ตอนนี้ใช้ของที่ Python ให้มาก่อน

```python
spends = [4200.0, 1850.5, 990.0, 12500.0, 640.25]

print("ยอดรวม", sum(spends))
print("ยอดมากสุด", max(spends))
print("ยอดน้อยสุด", min(spends))
print("จำนวนรายการ", len(spends))
print("ค่าเฉลี่ย", round(sum(spends) / len(spends), 2))
```

ผลลัพธ์

```txt
ยอดรวม 20180.75
ยอดมากสุด 12500.0
ยอดน้อยสุด 640.25
จำนวนรายการ 5
ค่าเฉลี่ย 4036.15
```

ถ้าลิสต์มีค่าว่างหรือค่า `None` ปนอยู่ `sum` จะพังทันที นี่เป็นเหตุผลที่ต้องทำความสะอาดค่าก่อนสรุปทุกครั้ง

## กรองด้วยการสร้างลิสต์แบบเข้าใจ

การสร้างลิสต์แบบเข้าใจ (list comprehension) คือการเขียนลูปสร้างลิสต์ใหม่ในบรรทัดเดียว รูปแบบคือวงเล็บเหลี่ยมที่ข้างในมีนิพจน์ตามด้วย `for` และ `if`

เราใช้มันกรองแถวตามเงื่อนไข ซึ่งเป็นงานที่ทำบ่อยที่สุดในขั้นทำความสะอาดข้อมูล

```python
spends = [4200.0, 1850.5, 990.0, 12500.0, 640.25]

high_spenders = [amount for amount in spends if amount >= 1000]
print("ลูกค้าที่จ่ายตั้งแต่ 1000 บาทขึ้นไป", high_spenders)
```

ผลลัพธ์

```txt
ลูกค้าที่จ่ายตั้งแต่ 1000 บาทขึ้นไป [4200.0, 1850.5, 12500.0]
```

ตัวแปร `amount` ใช้ได้แค่ในวงเล็บเหลี่ยม ไม่หลุดออกมาข้างนอก ถ้าลิสต์ใหญ่มากท่าที่สร้างลิสต์ใหม่ตรง ๆ จะเร็วกว่าลูป `append` เล็กน้อยด้วย

## เรียงลำดับด้วย sorted

`sorted` คืนลิสต์ใหม่ที่เรียงแล้ว ของเดิมไม่เปลี่ยน ต่างจาก `list.sort()` ที่แก้ของเดิม

ความต่างนี้สำคัญเพราะเรามักอยากดูข้อมูลเรียงหลายแบบจากชุดเดียว โดยไม่ต้องอ่านไฟล์ซ้ำ

```python
spends = [4200.0, 1850.5, 990.0, 12500.0, 640.25]

print("เรียงจากน้อยไปมาก", sorted(spends))
print("เรียงจากมากไปน้อย", sorted(spends, reverse=True))
print("ของเดิมไม่เปลี่ยน", spends)
```

ผลลัพธ์

```txt
เรียงจากน้อยไปมาก [640.25, 990.0, 1850.5, 4200.0, 12500.0]
เรียงจากมากไปน้อย [12500.0, 4200.0, 1850.5, 990.0, 640.25]
ของเดิมไม่เปลี่ยน [4200.0, 1850.5, 990.0, 12500.0, 640.25]
```

## ดิกชันนารีคือตารางจับคู่

ดิกชันนารีเก็บข้อมูลเป็นคู่ระหว่างกุญแจ (key) กับค่า (value) เราเข้าถึงค่าด้วยชื่อกุญแจ ไม่ใช่ด้วยตำแหน่ง

ในงานข้อมูล หนึ่งแถวมักเก็บเป็นดิกชันนารีหนึ่งตัว โดยใช้ชื่อคอลัมน์เป็นกุญแจ ซึ่งอ่านง่ายกว่าการจำว่าคอลัมน์ที่สามคืออะไร

```python
customer = {
    "customer_id": "C001",
    "name": "Nattapong Sri",
    "country": "Thailand",
    "spend": 4200.0,
}

print("รหัส", customer["customer_id"])
print("ชื่อ", customer["name"])
print("จำนวนคีย์", len(customer))
```

ผลลัพธ์

```txt
รหัส C001
ชื่อ Nattapong Sri
จำนวนคีย์ 4
```

## เพิ่มและแก้ค่าในดิกชันนารี

การกำหนดค่าให้กุญแจที่ยังไม่มีจะเพิ่มกุญแจใหม่ ถ้ากุญแจมีอยู่แล้วจะทับค่าเดิม

ตอนทำความสะอาดเรามักเพิ่มคอลัมน์ใหม่ที่คำนวณจากของเดิม เช่น เพิ่ม `spend` หรือ `email_clean` เข้าไปในแถว

```python
customer = {"customer_id": "C001", "name": "Nattapong Sri"}

customer["email"] = "nattapong@example.com"
customer["name"] = "Nattapong Sri"
print("หลังแก้ไข", customer)
```

ผลลัพธ์

```txt
หลังแก้ไข {'customer_id': 'C001', 'name': 'Nattapong Sri', 'email': 'nattapong@example.com'}
```

## อ่านค่าที่อาจไม่มีด้วย get

ถ้าอ่านกุญแจที่ไม่มีด้วยวงเล็บเหลี่ยม โปรแกรมจะหยุดด้วย `KeyError` ทันที

`get` คืน `None` แทนการพัง และรับค่าเริ่มต้นเป็นอาร์กิวเมนต์ที่สองได้

ข้อมูลจริงมักมีคอลัมน์ไม่ครบหรือแถวบางแถวไม่มีฟิลด์นั้น `get` จึงปลอดภัยกว่าตอนอ่านข้อมูลดิบ

```python
customer = {"customer_id": "C001", "name": "Nattapong Sri"}

print("จังหวัด", customer.get("province"))
print("จังหวัด", customer.get("province", "ไม่ระบุ"))
print("มีคีย์ name หรือไม่", "name" in customer)
```

ผลลัพธ์

```txt
จังหวัด None
จังหวัด ไม่ระบุ
มีคีย์ name หรือไม่ True
```

## เดินผ่านทุกคู่ด้วย items

`items` คืนคู่กุญแจกับค่าออกมาทีละคู่ ใช้เมื่ออยากทำงานกับทั้งสองส่วนพร้อมกัน

เราใช้มันตอนพิมพ์รายงานตรวจข้อมูล หรือตอนแปลงชื่อคอลัมน์ทั้งแถว

```python
customer = {"customer_id": "C001", "name": "Nattapong Sri", "country": "Thailand"}

for key, value in customer.items():
    print(f"{key} คือ {value}")
```

ผลลัพธ์

```txt
customer_id คือ C001
name คือ Nattapong Sri
country คือ Thailand
```

## คำอธิบายชนิดข้อมูลในตัวแปร

บางตัวอย่างอาจเขียนคำอธิบายชนิดข้อมูลไว้หลังชื่อตัวแปร เช่น

~~~python
tier_counts: dict[str, int] = {}
~~~

ส่วนนี้เรียกว่า type annotation เป็นคำใบ้ให้คนอ่านและเครื่องมือตรวจโค้ดรู้ว่าตัวแปรควรเก็บอะไร ในตัวอย่างนี้ dict[str, int] หมายถึงดิกชันนารีที่ใช้ข้อความเป็นกุญแจและจำนวนเต็มเป็นค่า คำอธิบายนี้ไม่ได้แปลงค่าหรือเปลี่ยนวิธีทำงานของ Python

## นับจำนวนด้วยดิกชันนารี

รูปแบบที่นับค่าซ้ำคือเริ่มด้วยดิกชันนารีว่าง แล้วบวกหนึ่งให้กุญแจนั้นทุกครั้งที่เจอ

เราใช้ท่านี้ตลอดหลักสูตร ตั้งแต่การนับสถานะออเดอร์ไปจนถึงการนับค่าที่หายไปในแต่ละคอลัมน์

```python
tiers = ["gold", "silver", "gold", "bronze", "gold", "silver"]

tier_counts: dict[str, int] = {}
for tier in tiers:
    tier_counts[tier] = tier_counts.get(tier, 0) + 1

print("นับตามระดับ", tier_counts)
```

ผลลัพธ์

```txt
นับตามระดับ {'gold': 3, 'silver': 2, 'bronze': 1}
```

`tier_counts.get(tier, 0)` คืน `0` เมื่อเจอกุญแจครั้งแรก แล้วเราบวกหนึ่งเก็บกลับไป ถ้าเขียนแบบนี้ลืมไม่ได้ เพราะเขียนวงเล็บเหลี่ยมตรง ๆ ครั้งแรกจะได้ `KeyError`

## ดิกชันนารีเป็นตารางค้นค่า

เมื่อกุญแจคือรหัสสินค้า ดิกชันนารีจะทำหน้าที่เหมือนตารางค้นราคา หาได้ทันทีไม่ต้องเดินหาทั้งลิสต์

```python
prices = {"P001": 450, "P002": 300, "P003": 60}

print("ราคา P002", prices["P002"])
print("คีย์ทั้งหมด", list(prices.keys()))
print("ราคาทั้งหมด", list(prices.values()))
print("ค่าเฉลี่ยราคา", sum(prices.values()) / len(prices))
```

ผลลัพธ์

```txt
ราคา P002 300
คีย์ทั้งหมด ['P001', 'P002', 'P003']
ราคาทั้งหมด [450, 300, 60]
ค่าเฉลี่ยราคา 270.0
```

## ตารางคือลิสต์ของดิกชันนารี

รวมสองโครงสร้างเข้าด้วยกันจะได้รูปที่ข้อมูลจริงใช้ คือลิสต์ของแถว โดยแต่ละแถวเป็นดิกชันนารี

รูปนี้จะเห็นซ้ำไปจนจบบทที่ 11 ก่อนที่ Pandas จะเข้ามาแทนที่

```python
rows = [
    {"name": "Nattapong Sri", "country": "Thailand", "spend": 4200.0},
    {"name": "Malee Wongsakul", "country": "Laos", "spend": 1850.5},
    {"name": "Anan Chaiyaporn", "country": "Thailand", "spend": 12500.0},
]

names = [row["name"] for row in rows]
thai_rows = [row for row in rows if row["country"] == "Thailand"]
print("ชื่อทั้งหมด", names)
print("แถวประเทศไทย", thai_rows)
```

ผลลัพธ์

```txt
ชื่อทั้งหมด ['Nattapong Sri', 'Malee Wongsakul', 'Anan Chaiyaporn']
แถวประเทศไทย [{'name': 'Nattapong Sri', 'country': 'Thailand', 'spend': 4200.0}, {'name': 'Anan Chaiyaporn', 'country': 'Thailand', 'spend': 12500.0}]
```

## เรียงแถวตามคอลัมน์

`sorted` เรียงลิสต์ของดิกชันนารีได้ถ้าเราบอกว่าดูค่าไหนผ่านอาร์กิวเมนต์ `key`

ฟังก์ชัน `lambda` คือฟังก์ชันไม่มีชื่อที่เขียนในบรรทัดเดียว ใช้ตรงนี้เพื่อบอกว่าให้เรียงตามค่า `spend`

```python
rows = [
    {"name": "Nattapong Sri", "country": "Thailand", "spend": 4200.0},
    {"name": "Malee Wongsakul", "country": "Laos", "spend": 1850.5},
    {"name": "Anan Chaiyaporn", "country": "Thailand", "spend": 12500.0},
]

by_spend = sorted(rows, key=lambda row: row["spend"], reverse=True)
for row in by_spend:
    print(f"{row['name']:<18}{row['country']:<10}{row['spend']:>10,.2f}")
```

ผลลัพธ์

```txt
Anan Chaiyaporn   Thailand   12,500.00
Nattapong Sri     Thailand    4,200.00
Malee Wongsakul   Laos        1,850.50
```

ถ้าแถวไหนไม่มีคีย์ `spend` โค้ดนี้จะพังด้วย `KeyError` การเรียงจึงต้องทำหลังตรวจว่าไม่มีค่าหายไปแล้วเท่านั้น

## สรุป

| อยากทำอะไร | เขียนแบบนี้ |
|---|---|
| นับสมาชิก | `len(items)` |
| เอาตัวแรก | `items[0]` |
| เอาตัวสุดท้าย | `items[-1]` |
| เอาสองตัวแรก | `items[:2]` |
| เพิ่มท้ายลิสต์ | `items.append(value)` |
| กรองสมาชิก | `[x for x in items if condition]` |
| แปลงทุกตัว | `[f(x) for x in items]` |
| เรียงลิสต์ใหม่ | `sorted(items)` |
| เรียงลิสต์ของแถว | `sorted(rows, key=lambda r: r["col"])` |
| อ่านค่าดิกชันนารี | `row["col"]` |
| อ่านแบบไม่พัง | `row.get("col", default)` |
| เดินทุกคู่ | `for k, v in row.items()` |
| นับค่าซ้ำ | `counts[k] = counts.get(k, 0) + 1` |

กฎที่ต้องจำ

- ดัชนีเริ่มที่ `0` และ `-1` คือตัวสุดท้าย
- `sorted` คืนลิสต์ใหม่ ส่วน `list.sort()` แก้ของเดิม
- ลิสต์ที่ส่งเข้าไปในฟังก์ชันแล้วแก้ข้างใน จะกระทบของเดิม ให้คัดลอกก่อนถ้าไม่ต้องการ
- อ่านดิกชันนารีด้วย `[]` เมื่อมั่นใจว่ามีคีย์ ใช้ `get` เมื่อไม่มั่นใจ
- ตารางข้อมูลใน Python คือลิสต์ของดิกชันนารี

## โจทย์ที่ต้องทำ

เปิด `exercises/ch06-customer-table.py` แล้วเติมสี่ฟังก์ชันนี้

1. `names_of(rows)` คืนลิสต์ชื่อจากคีย์ `name` ตามลำดับเดิม
2. `filter_by_country(rows, country)` คืนเฉพาะแถวที่คอลัมน์ `country` ตรงกับค่าที่ส่งมา
3. `count_by(rows, key)` คืนดิกชันนารีที่นับว่าค่าแต่ละค่าในคอลัมน์นั้นโผล่กี่ครั้ง
4. `sort_by_spend(rows, descending=True)` คืนลิสต์ใหม่ที่เรียงตามคีย์ `spend` และไม่แก้ลิสต์เดิม

ข้อมูลตัวอย่างอยู่ในตัวแปร `SAMPLE_CUSTOMERS` ท้ายไฟล์มีบล็อก `if __name__ == "__main__":` ไว้รันดูผล

## ผลลัพธ์ที่คาดหวัง

รันด้วยคำสั่งนี้จากโฟลเดอร์โปรเจกต์

```cmd
python exercises/ch06-customer-table.py
```

ต้องได้ผลแบบนี้

```txt
ชื่อลูกค้า ['Nattapong Sri', 'Malee Wongsakul', 'Kanya P.', 'Anan Chaiyaporn', 'Suda Meesuk', 'Wilai Thongchai']
ลูกค้าไทย ['Nattapong Sri', 'Kanya P.', 'Anan Chaiyaporn']
นับตามประเทศ {'Thailand': 3, 'Laos': 3}

Anan Chaiyaporn   Thailand   12,500.00
Nattapong Sri     Thailand    4,200.00
Malee Wongsakul   Laos        1,850.50
Kanya P.          Thailand      990.00
Suda Meesuk       Laos          640.25
Wilai Thongchai   Laos            0.00
```

ตรวจงานตัวเองด้วย

```cmd
python -m pytest tests/test_ch06.py
```

## เสร็จแล้วพิมพ์ ตรวจ Ch6
