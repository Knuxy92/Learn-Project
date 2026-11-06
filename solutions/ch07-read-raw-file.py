import csv
from pathlib import Path


def count_lines(path):
    """รับเส้นทางไฟล์ คืนจำนวนบรรทัดข้อมูลโดยไม่นับบรรทัดหัวตาราง"""
    text = Path(path).read_text(encoding="utf-8")
    return max(len(text.splitlines()) - 1, 0)


def first_column(path):
    """รับเส้นทางไฟล์ CSV คืนค่าคอลัมน์แรกของทุกแถวข้อมูลโดยไม่รวมหัวตาราง"""
    with Path(path).open(encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        next(reader, None)
        return [row[0] for row in reader if row]


def write_lines(path, lines):
    """รับเส้นทางไฟล์กับลิสต์ข้อความ เขียนบรรทัดละรายการและปิดท้ายด้วยขึ้นบรรทัดใหม่"""
    text = "".join(f"{line}\n" for line in lines)
    Path(path).write_text(text, encoding="utf-8")


def read_thai_csv(path):
    """รับเส้นทางไฟล์ CSV ภาษาไทย คืนลิสต์ของดิกชันนารีแถวละหนึ่งตัว"""
    with Path(path).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


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
