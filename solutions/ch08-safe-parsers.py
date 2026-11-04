import json
import tempfile
from pathlib import Path


def safe_divide(a: float, b: float) -> float | None:
    """หาร a ด้วย b คืน None เมื่อตัวหารเป็นศูนย์"""
    try:
        return a / b
    except ZeroDivisionError:
        return None


def parse_int(value) -> int | None:
    """แปลงค่าเป็นจำนวนเต็ม คืน None เมื่อแปลงไม่ได้"""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def read_text_or_default(path: str | Path, default: str = "") -> str:
    """อ่านข้อความจากไฟล์ คืน default เมื่อไฟล์ไม่มีอยู่"""
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return default


def read_json_object(path: str | Path) -> dict:
    """อ่านไฟล์ JSON ที่มีค่าเป็น object คืน dict"""
    text = Path(path).read_text(encoding="utf-8")
    data = json.loads(text)

    if not isinstance(data, dict):
        raise ValueError("JSON ต้องเป็น object")

    return data


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
        broken.write_text("[1, 2]", encoding="utf-8")
        try:
            read_json_object(broken)
        except ValueError as error:
            print(f"จับได้ {error}")
