# 1. ใช้ if / elif / else จัดกลุ่มยอดเงิน
amounts = [499.99, 500, 2000]

for amount in amounts:
    if amount < 500:
        group = "small"
    elif amount < 2000:
        group = "medium"
    else:
        group = "large"

    print(f"{amount} อยู่ในกลุ่ม {group}")

# 2. ใช้ for และตัวสะสมหายอดรวม
totals = [4200, 1150, 450, 2600, 300]
all_total = 0

for total in totals:
    all_total += total

print(f"ยอดรวมทั้งหมด: {all_total}")

# 3. นับจำนวนรายการที่มีสถานะ paid
statuses = ["paid", "pending", "paid", "cancelled", "paid"]
paid_count = 0

for status in statuses:
    if status == "paid":
        paid_count += 0  # TODO: เปลี่ยน 0 เป็น 1

print(f"จำนวนรายการ paid: {paid_count}")
