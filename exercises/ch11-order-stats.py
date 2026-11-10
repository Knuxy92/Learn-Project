"""แบบฝึกหัดบทที่ 11: เลือกข้อมูลและสรุปสถิติด้วย NumPy

โจทย์
เขียนฟังก์ชัน revenue, mask_paid และ summary ตามข้อกำหนดใน curriculum/ch11
ฟังก์ชัน summary ต้องคืนดิกชันนารีตามคีย์ที่โจทย์กำหนด ไม่พิมพ์ผลจากภายในฟังก์ชัน

ข้อมูลตัวอย่างและส่วนเรียกใช้งานเตรียมไว้ให้
"""

import numpy as np


def revenue(quantity: np.ndarray, price: np.ndarray) -> np.ndarray:
    """รับอาร์เรย์จำนวนกับราคาต่อหน่วย คืนอาร์เรย์ยอดเงินของแต่ละรายการ"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def mask_paid(status: np.ndarray) -> np.ndarray:
    """รับอาร์เรย์สถานะ คืนอาร์เรย์จริงเท็จที่บอกว่าแถวใดจ่ายแล้ว"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def summary(values: np.ndarray) -> dict[str, float]:
    """รับอาร์เรย์ตัวเลข คืนดิกชันที่มีคีย์ mean, median, min, max, sum"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


if __name__ == "__main__":
    quantities = np.array([2, 3, 1, 4])
    prices = np.array([450.0, 300.0, 1200.0, 89.0])
    print("ยอดต่อออเดอร์", revenue(quantities, prices))

    statuses = np.array(["paid", "PAID", " pending ", "Paid", "cancelled"])
    print("มาสก์ที่จ่ายแล้ว", mask_paid(statuses))

    amounts = np.array([900.0, 1500.0, 1200.0, 890.0])
    print("สรุปยอดขาย", summary(amounts))
