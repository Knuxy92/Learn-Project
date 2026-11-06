def safe_divide(a, b):
    """หาร a ด้วย b คืน None เมื่อ b เป็นศูนย์"""
    # TODO: ใช้ try / except จัดการกรณีหารด้วยศูนย์
    return None


def parse_int(value):
    """แปลงค่าเป็นจำนวนเต็ม ถ้าแปลงไม่ได้ให้คืน None"""
    # TODO: ใช้ try / except จัดการ ValueError และ TypeError
    return None


def read_text_or_default(path, default=""):
    """อ่านไฟล์ข้อความ ถ้าไม่มีไฟล์ให้คืน default"""
    # TODO: ใช้ try / except จัดการ FileNotFoundError
    return default


def read_json_object(path):
    """อ่าน JSON และตรวจว่าค่าหลักเป็น dict ถ้าไม่ใช่ให้ raise ValueError"""
    # TODO: อ่าน JSON และตรวจชนิดข้อมูล
    return {}


if __name__ == "__main__":
    print(f"safe_divide(10, 2) ได้ {safe_divide(10, 2)}")
    print(f"safe_divide(1, 0) ได้ {safe_divide(1, 0)}")
    print(f"parse_int('42') ได้ {parse_int('42')}")
    print(f"parse_int('4.2') ได้ {parse_int('4.2')}")
    print(f"parse_int(None) ได้ {parse_int(None)}")
    print(f"ไฟล์ที่ไม่มีอยู่ได้ {read_text_or_default('missing.txt', 'none')!r}")
