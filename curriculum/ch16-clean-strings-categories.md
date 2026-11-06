# บทที่ 16: ทำความสะอาดข้อความและหมวดหมู่

## ทบทวน

บทที่ 15 สอนให้เห็นค่าว่างและเติมค่าที่หายไปแล้ว

แต่การเติมค่าว่างอย่างเดียวไม่พอ เพราะค่าที่ไม่ว่างก็ยังผิดได้ เช่น `TH` กับ `Thailand` คือประเทศเดียวกัน แต่โปรแกรมมองเป็นสองค่า

บทนี้จึงจัดการกับค่าที่มีอยู่แล้วแต่เขียนไม่เหมือนกัน

## ข้อความที่ดูเหมือนกันแต่ไม่ใช่ค่าเดียวกัน

คอมพิวเตอร์เปรียบเทียบข้อความแบบตัวอักษรต่อตัวอักษร

`"paid"` กับ `"paid "` จึงไม่เท่ากัน เพราะมีช่องว่างเกินมาหนึ่งตัว

ลองนับดูว่าคอลัมน์หนึ่งมีกี่ค่าที่ไม่ซ้ำกัน

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")
print(orders["status"].nunique())
print(orders["status"].unique().tolist())
```

ผลลัพธ์

```txt
7
['cancelled', 'canceled', nan, 'Paid ', 'pending', 'paid', 'unknown', 'PAID']
```

ความจริงมีแค่สี่สถานะ คือ paid, pending, cancelled และ unknown แต่ข้อมูลบอกว่าเจ็ด

ถ้าเอาไปนับยอดตามสถานะตอนนี้ ตัวเลขจะกระจายผิดกลุ่ม

สังเกตว่า `nan` โผล่มาในรายการด้วย เพราะช่องที่ว่างในไฟล์ CSV ถูกอ่านเป็นค่าที่หายไป ไม่ใช่ข้อความว่าง

## ตัวช่วยจัดการข้อความใน Pandas

Pandas มีตัวช่วย (accessor) ชื่อ `str` สำหรับเรียกเมธอดจัดการข้อความกับทั้งคอลัมน์พร้อมกัน

มันสำคัญเพราะเราไม่ต้องเขียนลูปเอง และค่าว่างจะถูกข้ามให้อัตโนมัติ

```python
import pandas as pd

names = pd.Series(["  Somchai Jaidee  ", "Malee Wongsakul"])
print(names.str.strip().tolist())
```

ผลลัพธ์

```txt
['Somchai Jaidee', 'Malee Wongsakul']
```

## ตัดช่องว่างหัวท้าย

`str.strip()` ตัดช่องว่างที่หัวและท้ายออก

นี่คือขั้นแรกเสมอ เพราะช่องว่างที่มองไม่เห็นทำให้การเทียบข้อความพลาด

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")
names = customers["name"]

for value in names.head(4):
    print(f"[{value}]")
```

ผลลัพธ์

```txt
[  Nattapong Sri  ]
[Malee Wongsakul]
[Kanya P.]
[Anan Chaiyaporn]
```

แถวแรกมีช่องว่างสองตัวหน้าและสองตัวหลัง

```python
for value in names.str.strip().head(4):
    print(f"[{value}]")
```

ผลลัพธ์

```txt
[Nattapong Sri]
[Malee Wongsakul]
[Kanya P.]
[Anan Chaiyaporn]
```

## ยุบช่องว่างที่ซ้อนกัน

บางชื่อมีช่องว่างหลายตัวคั่นกลางคำ

`str.strip()` จัดการไม่ได้ เพราะมันแตะแค่หัวกับท้าย

ต้องใช้ `str.replace` กับรูปแบบ `\s+` ซึ่งหมายถึงช่องว่างตั้งแต่หนึ่งตัวขึ้นไป

```python
import pandas as pd

padded = pd.Series(["  Somchai   Jaidee  ", "Malee  Wongsakul"])
collapsed = padded.str.strip().str.replace(r"\s+", " ", regex=True)
print(collapsed.tolist())
```

ผลลัพธ์

```txt
['Somchai Jaidee', 'Malee Wongsakul']
```

ต้องใส่ `regex=True` ทุกครั้ง ไม่อย่างนั้น Pandas จะหาข้อความตรงตัวแทนรูปแบบ

## ปรับตัวพิมพ์ให้เป็นมาตรฐาน

ข้อมูลเดียวกันอาจถูกพิมพ์ด้วยตัวพิมพ์ต่างกัน เช่น `GOLD`, `gold` และ `Gold`

เลือกมาตรฐานไว้หนึ่งแบบแล้วแปลงทุกค่าให้ตรงกัน

`str.lower()` ทำให้เป็นตัวพิมพ์เล็กทั้งหมด เหมาะกับสถานะและอีเมล

`str.title()` ทำให้ตัวแรกของแต่ละคำเป็นตัวพิมพ์ใหญ่ เหมาะกับชื่อคนและชื่อหมวด

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")
tiers = customers["loyalty_tier"]

print(tiers.unique().tolist())
print(tiers.str.strip().str.title().unique().tolist())
```

ผลลัพธ์

```txt
['GOLD', 'gold', 'silver', 'silver ', 'Gold', nan]
['Gold', 'Silver', nan]
```

จากห้าแบบเหลือสองแบบ บวกค่าที่หายไปหนึ่งค่า

## เติมค่าที่หายไปหลังปรับหมวดหมู่

เมื่อปรับตัวพิมพ์แล้ว ค่าว่างจะยังเป็นค่าว่าง

สำหรับคอลัมน์หมวดหมู่ ค่าที่หายไปควรมีชื่อของมันเอง เพื่อให้เห็นชัดว่าไม่ใช่ข้อมูลที่ถูกลืม

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")
tier_clean = customers["loyalty_tier"].str.strip().str.title().fillna("Unknown")
print(tier_clean.value_counts().to_string())
```

ผลลัพธ์

```txt
loyalty_tier
Silver     8
Gold       5
Unknown    1
```

## รวมชื่อเรียกที่ต่างกันด้วยดิกชันนารี

การปรับตัวพิมพ์แก้ได้เฉพาะความต่างของตัวพิมพ์

แต่ `TH` กับ `Thailand` ต่างกันที่เนื้อหา ไม่ใช่ตัวพิมพ์

วิธีที่ตรงไปตรงมาคือเขียนดิกชันนารี (dictionary) บอกว่าค่าไหนควรกลายเป็นค่าอะไร

```python
import pandas as pd

COUNTRY_ALIASES = {
    "Th": "Thailand",
    "Thailand": "Thailand",
    "La": "Laos",
    "Laos": "Laos",
}

customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")
titled = customers["country"].str.strip().str.title()
print(titled.value_counts().to_string())
```

ผลลัพธ์

```txt
country
Thailand    8
La          4
Laos        1
Th          1
```

หลังปรับตัวพิมพ์แล้วยังเหลือสี่ค่า เพราะ `TH` กลายเป็น `Th` และ `LA` กลายเป็น `La`

จากนั้นจึงเอาดิกชันนารีไปแทนที่

```python
print(titled.replace(COUNTRY_ALIASES).value_counts().to_string())
```

ผลลัพธ์

```txt
country
Thailand    9
Laos        5
```

ลำดับสำคัญมาก ต้องปรับตัวพิมพ์ก่อน แล้วค่อยแทนที่

ถ้าสลับกัน `TH` จะไม่ตรงกับคีย์ `Th` ในดิกชันนารี และจะไม่ถูกแปลง

## แปลงสถานะที่เขียนต่างกัน

สถานะมีปัญหาสองชั้น

ชั้นแรกคือตัวพิมพ์ปนกัน ชั้นที่สองคือมีสองคำที่หมายถึงสิ่งเดียวกัน คือ `canceled` กับ `cancelled`

```python
import pandas as pd

STATUS_ALIASES = {"canceled": "cancelled"}

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")
print(orders["status"].value_counts(dropna=False).to_string())
```

ผลลัพธ์

```txt
status
pending      8
cancelled    7
canceled     6
Paid         6
NaN          5
unknown      5
paid         4
PAID         1
```

แปดค่าที่แตกต่าง แต่จริง ๆ มีแค่สี่ความหมาย

```python
status = orders["status"].str.strip().str.lower().replace(STATUS_ALIASES)
status = status.mask(status.isna() | status.eq(""), "unknown")
print(status.value_counts().to_string())
```

ผลลัพธ์

```txt
status
cancelled    13
paid         11
unknown      10
pending       8
```

`mask` ใช้แทนที่เฉพาะตำแหน่งที่เงื่อนไขเป็นจริง

เงื่อนไขคือเป็นค่าว่างหรือเป็นข้อความว่าง เพราะข้อมูลจากไฟล์ CSV อาจมาได้ทั้งสองแบบ

## ปรับชื่อหมวดสินค้า

คอลัมน์หมวดสินค้ามีปัญหาเดียวคือตัวพิมพ์ปนกัน จึงใช้ `strip` กับ `title` พอ

```python
import pandas as pd

products = pd.read_csv("data/raw/products.csv", encoding="utf-8")
print(products["category"].unique().tolist())
print(products["category"].str.strip().str.title().unique().tolist())
```

ผลลัพธ์

```txt
['Accessory', 'accessory', 'Stationery', 'display', 'furniture', 'Display', 'stationery']
['Accessory', 'Stationery', 'Display', 'Furniture']
```

## สรุป

| ปัญหา | เมธอด | หมายเหตุ |
|---|---|---|
| ช่องว่างหัวท้าย | `str.strip()` | ทำก่อนเสมอ |
| ช่องว่างซ้อนกลางคำ | `str.replace(r"\s+", " ", regex=True)` | ต้องใส่ `regex=True` |
| ตัวพิมพ์ปน | `str.lower()` หรือ `str.title()` | เลือกให้ตรงกับชนิดข้อมูล |
| ชื่อเรียกต่างกัน | `Series.replace(dict)` | ปรับตัวพิมพ์ก่อนแล้วค่อยแทนที่ |
| ค่าหายในหมวดหมู่ | `fillna` หรือ `mask` | ใส่ชื่อเช่น Unknown หรือ unknown |

## โจทย์ที่ต้องทำ

เปิด `exercises/ch16-normalize-text.py`

เขียนสี่ฟังก์ชันนี้

1. `clean_name` รับคอลัมน์ชื่อ คืนคอลัมน์ที่ตัดช่องว่างหัวท้าย ยุบช่องว่างซ้อน และปรับเป็นคำขึ้นต้น
2. `normalize_country` รับคอลัมน์ประเทศ คืนคอลัมน์ที่มีแค่ Thailand กับ Laos
3. `normalize_status` รับคอลัมน์สถานะ คืนคอลัมน์ตัวพิมพ์เล็กที่ canceled รวมเป็น cancelled และค่าว่างเป็น unknown
4. `normalize_category` รับคอลัมน์หมวดสินค้า คืนคอลัมน์ที่ตัดช่องว่างและปรับเป็นคำขึ้นต้น

ฟังก์ชันต้องคืนค่า ไม่พิมพ์ออกมา และต้องไม่แก้คอลัมน์ต้นฉบับ

## ผลลัพธ์ที่คาดหวัง

```txt
['Nattapong Sri', 'Malee Wongsakul', 'Kanya P.', 'Anan Chaiyaporn', 'Suda Meesuk']
['Thailand', 'Laos']
['cancelled', 'unknown', 'paid', 'pending']
['Accessory', 'Stationery', 'Display', 'Furniture']
```

## เสร็จแล้วพิมพ์ ตรวจ Ch16
