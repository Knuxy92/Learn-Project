"""โจทย์บทที่ 6 เรื่องลิสต์และดิกชันนารี

ตารางลูกค้าอยู่ในรูปลิสต์ของดิกชันนารี แต่ละแถวมีคีย์ customer_id, name, country, spend
เติมโค้ดในแต่ละฟังก์ชันให้คืนค่าตามที่ docstring บอก
"""

SAMPLE_CUSTOMERS = [
    {"customer_id": "C001", "name": "Nattapong Sri", "country": "Thailand", "spend": 4200.0},
    {"customer_id": "C002", "name": "Malee Wongsakul", "country": "Laos", "spend": 1850.5},
    {"customer_id": "C003", "name": "Kanya P.", "country": "Thailand", "spend": 990.0},
    {"customer_id": "C004", "name": "Anan Chaiyaporn", "country": "Thailand", "spend": 12500.0},
    {"customer_id": "C005", "name": "Suda Meesuk", "country": "Laos", "spend": 640.25},
    {"customer_id": "C007", "name": "Wilai Thongchai", "country": "Laos", "spend": 0.0},
]


def names_of(rows):
    """รับลิสต์ของแถว คืนลิสต์ชื่อจากคีย์ name ตามลำดับเดิม"""
    return []


def filter_by_country(rows, country):
    """รับลิสต์ของแถวกับชื่อประเทศ คืนเฉพาะแถวที่คอลัมน์ country ตรงกัน"""
    return []


def count_by(rows, key):
    """รับลิสต์ของแถวกับชื่อคอลัมน์ คืนจำนวนแถวแยกตามค่าของคอลัมน์นั้น"""
    return {}


def sort_by_spend(rows, descending=True):
    """รับลิสต์ของแถวที่ทุกแถวมีคีย์ spend คืนลิสต์ใหม่ที่เรียงตามยอดใช้จ่าย"""
    return rows


def main() -> None:
    print("ชื่อลูกค้า", names_of(SAMPLE_CUSTOMERS))

    thai_names = [row["name"] for row in filter_by_country(SAMPLE_CUSTOMERS, "Thailand")]
    print("ลูกค้าไทย", thai_names)

    print("นับตามประเทศ", count_by(SAMPLE_CUSTOMERS, "country"))
    print()

    for row in sort_by_spend(SAMPLE_CUSTOMERS):
        print(f"{row['name']:<18}{row['country']:<10}{row['spend']:>10,.2f}")


if __name__ == "__main__":
    main()
