import csv
from pathlib import Path

path = Path("data/raw/products.csv")
text = path.read_text(encoding="utf-8")
lines = text.splitlines()

print("จำนวนบรรทัดทั้งหมด", len(lines))
print("บรรทัดแรก", lines[0])
print("บรรทัดที่สอง", lines[1])
print()

with path.open(encoding="utf-8", newline="") as handle:
    reader = csv.reader(handle)
    header = next(reader)
    rows = list(reader)

print("หัวตาราง", header)
print("จำนวนแถวข้อมูล", len(rows))
print("แถวแรก", rows[0])
print()

with path.open(encoding="utf-8", newline="") as handle:
    dict_rows = list(csv.DictReader(handle))

print("แถวแรก", dict_rows[0])
print("ชื่อสินค้าแถวแรก", repr(dict_rows[0]["product_name"]))
print("หมวดของแถวแรก", repr(dict_rows[0]["category"]))
print()

thai_path = Path("data/raw/customers_th.csv")
print("สามไบต์แรก", thai_path.read_bytes()[:3])

with thai_path.open(encoding="utf-8-sig", newline="") as handle:
    thai_rows = list(csv.DictReader(handle))

print("จำนวนลูกค้าไทย", len(thai_rows))
for row in thai_rows:
    print(f"{row['customer_id']} {row['name']} {row['province']}")
print()

out_path = Path("curriculum/ch07/checked.txt")
selected = ["P001", "P002", "P005"]
out_path.write_text("".join(f"{pid}\n" for pid in selected), encoding="utf-8")

print("เขียนไฟล์แล้ว", out_path.name)
print(out_path.read_text(encoding="utf-8"), end="")
print(out_path.read_text(encoding="utf-8").splitlines())
out_path.unlink()
