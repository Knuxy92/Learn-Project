customer = {
    "customer_id": "C001",
    "name": "Nattapong Sri",
    "country": "Thailand",
    "spend": 4200.0,
}

print("รหัส", customer["customer_id"])
print("ชื่อ", customer["name"])
print("จำนวนคีย์", len(customer))
print()

customer = {"customer_id": "C001", "name": "Nattapong Sri"}

customer["email"] = "nattapong@example.com"
customer["name"] = "Nattapong Sri"
print("หลังแก้ไข", customer)
print()

customer = {"customer_id": "C001", "name": "Nattapong Sri"}

print("จังหวัด", customer.get("province"))
print("จังหวัด", customer.get("province", "ไม่ระบุ"))
print("มีคีย์ name หรือไม่", "name" in customer)
print()

customer = {"customer_id": "C001", "name": "Nattapong Sri", "country": "Thailand"}

for key, value in customer.items():
    print(f"{key} คือ {value}")
print()

tiers = ["gold", "silver", "gold", "bronze", "gold", "silver"]

tier_counts: dict[str, int] = {}
for tier in tiers:
    tier_counts[tier] = tier_counts.get(tier, 0) + 1

print("นับตามระดับ", tier_counts)
print()

prices = {"P001": 450, "P002": 300, "P003": 60}

print("ราคา P002", prices["P002"])
print("คีย์ทั้งหมด", list(prices.keys()))
print("ราคาทั้งหมด", list(prices.values()))
print("ค่าเฉลี่ยราคา", sum(prices.values()) / len(prices))
print()

rows = [
    {"name": "Nattapong Sri", "country": "Thailand", "spend": 4200.0},
    {"name": "Malee Wongsakul", "country": "Laos", "spend": 1850.5},
    {"name": "Anan Chaiyaporn", "country": "Thailand", "spend": 12500.0},
]

by_spend = sorted(rows, key=lambda row: row["spend"], reverse=True)
for row in by_spend:
    print(f"{row['name']:<18}{row['country']:<10}{row['spend']:>10,.2f}")
print()

rows = [
    {"name": "Nattapong Sri", "country": "Thailand", "spend": 4200.0},
    {"name": "Malee Wongsakul", "country": "Laos", "spend": 1850.5},
    {"name": "Anan Chaiyaporn", "country": "Thailand", "spend": 12500.0},
]

names = [row["name"] for row in rows]
thai_rows = [row for row in rows if row["country"] == "Thailand"]
print("ชื่อทั้งหมด", names)
print("แถวประเทศไทย", thai_rows)
