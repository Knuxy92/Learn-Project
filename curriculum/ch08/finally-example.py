from pathlib import Path


def read_first_line(path: Path) -> str:
    handle = None
    try:
        handle = path.open(encoding="utf-8")
        return handle.readline().rstrip("\n")
    except FileNotFoundError:
        return ""
    finally:
        if handle is not None:
            handle.close()


def count_data_rows(path: Path) -> int:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        return 0
    else:
        return max(len(lines) - 1, 0)


if __name__ == "__main__":
    products = Path("data/raw/products.csv")
    missing = Path("data/raw/ไม่มีไฟล์นี้.csv")

    print(f"แถวหัวตารางคือ {read_first_line(products)}")
    print(f"ไฟล์ที่ไม่มีอยู่ได้ {read_first_line(missing)!r}")
    print(f"products.csv มีข้อมูล {count_data_rows(products)} แถว")
    print(f"ไฟล์ที่ไม่มีอยู่ได้ {count_data_rows(missing)} แถว")

    steps = []
    try:
        steps.append("เปิดไฟล์")
        raise ValueError("ข้อมูลแถวที่ 3 ผิดรูป")
    except ValueError as error:
        steps.append(f"จัดการ {error}")
    finally:
        steps.append("ปิดไฟล์")
    print(steps)
