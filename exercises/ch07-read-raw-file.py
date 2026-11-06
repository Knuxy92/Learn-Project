"""โจทย์บทที่ 7 เรื่องข้อความและไฟล์

เติมโค้ดในแต่ละฟังก์ชันให้อ่านและเขียนไฟล์ได้ตามที่ docstring บอก
ไฟล์ข้อมูลจริงอยู่ในโฟลเดอร์ data/raw ของโปรเจกต์
"""

from pathlib import Path


def count_lines(path) -> int:
    """รับเส้นทางไฟล์ คืนจำนวนบรรทัดข้อมูลโดยไม่นับบรรทัดหัวตาราง"""
    return 0


def first_column(path) -> list[str]:
    """รับเส้นทางไฟล์ CSV คืนค่าคอลัมน์แรกของทุกแถวข้อมูลโดยไม่รวมหัวตาราง"""
    return []


def write_lines(path, lines):
    """รับเส้นทางไฟล์กับลิสต์ข้อความ เขียนบรรทัดละรายการและปิดท้ายด้วยขึ้นบรรทัดใหม่"""
    Path(path).write_text("", encoding="utf-8")


def read_thai_csv(path):
    """รับเส้นทางไฟล์ CSV ภาษาไทย คืนลิสต์ของดิกชันนารีแถวละหนึ่งตัว"""
    return []


def main() -> None:
    raw_dir = Path(__file__).resolve().parents[1] / "data" / "raw"

    products = raw_dir / "products.csv"
    print("จำนวนแถวสินค้า", count_lines(products))
    print("รหัสสินค้าสามตัวแรก", first_column(products)[:3])
    print()

    thai_customers = read_thai_csv(raw_dir / "customers_th.csv")
    print("ลูกค้าไทย", len(thai_customers), "คน")
    for row in thai_customers:
        print(f"{row['customer_id']} {row['name']} {row['province']}")
    print()

    sample_path = Path(__file__).resolve().parent / "sample-output.txt"
    write_lines(sample_path, ["P001", "P002"])
    print("เขียนไฟล์แล้ว", sample_path.name)
    print(sample_path.read_text(encoding="utf-8"), end="")
    sample_path.unlink()


if __name__ == "__main__":
    main()
