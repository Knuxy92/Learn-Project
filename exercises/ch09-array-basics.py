"""แบบฝึกหัดบทที่ 9: พื้นฐาน NumPy Array

โจทย์
เขียนฟังก์ชันทั้งสี่เพื่อสร้าง ตรวจสอบ เลือก และแทนค่าภายใน array
อ่านข้อกำหนดและผลลัพธ์ที่คาดหวังใน curriculum/ch09 ก่อนเริ่ม

ข้อมูลทดสอบและส่วนเรียกใช้งานเตรียมไว้ให้ เขียนวิธีทำในฟังก์ชันเอง
"""

import numpy as np


def make_array(values: list[float]) -> np.ndarray:
    """สร้าง array หนึ่งมิติจากลิสต์ของตัวเลข"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def shape_info(values: list[float]) -> tuple[int, int]:
    """คืนจำนวนสมาชิกกับจำนวนมิติเป็นคู่ลำดับ"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def select_even(values: list[int]) -> np.ndarray:
    """เลือกเฉพาะค่าที่หารสองลงตัว"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def replace_negative(values: list[float], replacement: float = 0.0) -> np.ndarray:
    """แทนค่าติดลบด้วย replacement โดยไม่แก้ array ต้นฉบับ"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


if __name__ == "__main__":
    print(f"make_array([1, 2, 3]) ได้ {make_array([1, 2, 3])}")
    print(f"dtype ของผลลัพธ์คือ {make_array([1, 2, 3]).dtype}")
    print(f"shape_info([1, 2, 3]) ได้ {shape_info([1, 2, 3])}")
    print(f"select_even([1, 2, 3, 4]) ได้ {select_even([1, 2, 3, 4])}")
    print(f"replace_negative([1, -2, 3]) ได้ {replace_negative([1, -2, 3])}")
