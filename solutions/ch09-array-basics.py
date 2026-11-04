import numpy as np


def make_array(values: list[float]) -> np.ndarray:
    """สร้าง array หนึ่งมิติจากลิสต์ของตัวเลข"""
    return np.array(values)


def shape_info(values: list[float]) -> tuple[int, int]:
    """คืนจำนวนสมาชิกกับจำนวนมิติของ array"""
    arr = np.array(values)
    return (arr.size, arr.ndim)


def select_even(values: list[int]) -> np.ndarray:
    """เลือกเฉพาะค่าที่หารสองลงตัว"""
    arr = np.array(values)
    return arr[arr % 2 == 0]


def replace_negative(values: list[float], replacement: float = 0.0) -> np.ndarray:
    """แทนค่าติดลบด้วย replacement โดยไม่แก้ array ต้นฉบับ"""
    arr = np.array(values, dtype=float)
    result = arr.copy()
    result[result < 0] = replacement
    return result


if __name__ == "__main__":
    print(f"make_array([1, 2, 3]) ได้ {make_array([1, 2, 3])}")
    print(f"dtype ของผลลัพธ์คือ {make_array([1, 2, 3]).dtype}")
    print(f"shape_info([1, 2, 3]) ได้ {shape_info([1, 2, 3])}")
    print(f"select_even([1, 2, 3, 4]) ได้ {select_even([1, 2, 3, 4])}")
    print(f"replace_negative([1, -2, 3]) ได้ {replace_negative([1, -2, 3])}")
