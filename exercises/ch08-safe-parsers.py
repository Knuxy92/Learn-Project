import json
import tempfile
from pathlib import Path


def safe_divide(a: float, b: float) -> float | None:
    """หาร a ด้วย b คืนผลหาร หรือ None เมื่อตัวหารเป็นศูนย์"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def parse_int(value) -> int | None:
    """แปลงค่าเป็นจำนวนเต็ม คืน None เมื่อแปลงไม่ได้"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def read_text_or_default(path: str | Path, default: str = "") -> str:
    """อ่านข้อความทั้งไฟล์ คืน default เมื่อไฟล์ไม่มีอยู่"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def read_json_object(path: str | Path) -> dict:
    """อ่านไฟล์ JSON คืน dict และโยน ValueError เมื่อค่าไม่ใช่ object"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


if __name__ == "__main__":
    print(f"safe_divide(10, 2) ได้ {safe_divide(10, 2)}")
    print(f"safe_divide(1, 0) ได้ {safe_divide(1, 0)}")
    print(f"parse_int('42') ได้ {parse_int('42')}")
    print(f"parse_int('4.2') ได้ {parse_int('4.2')}")
    print(f"parse_int(None) ได้ {parse_int(None)}")
    print(f"ไฟล์ที่ไม่มีอยู่ได้ {read_text_or_default('data/raw/ไม่มีไฟล์นี้.csv', 'none')!r}")

    with tempfile.TemporaryDirectory() as folder:
        sample = Path(folder) / "customer.json"
        sample.write_text('{"customer_id": "C001"}', encoding="utf-8")
        print(f"อ่าน JSON ได้ {read_json_object(sample)}")

        broken = Path(folder) / "list.json"
        broken.write_text(json.dumps([1, 2]), encoding="utf-8")
        try:
            read_json_object(broken)
        except ValueError as error:
            print(f"จับได้ {error}")
