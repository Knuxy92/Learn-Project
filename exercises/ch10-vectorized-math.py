import numpy as np


def to_baht(usd: np.ndarray, rate: float) -> np.ndarray:
    """รับอาร์เรย์ราคาเป็นดอลลาร์กับอัตราแลกเปลี่ยน คืนอาร์เรย์ราคาเป็นบาท"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def normalize(values: np.ndarray) -> np.ndarray:
    """รับอาร์เรย์ตัวเลข คืนอาร์เรย์ที่ปรับให้อยู่ในช่วงศูนย์ถึงหนึ่ง"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def total_with_vat(values: np.ndarray, vat: float = 0.07) -> np.ndarray:
    """รับอาร์เรย์ยอดเงินกับอัตราภาษี คืนอาร์เรย์ยอดรวมภาษี"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def clip_negative(values: np.ndarray) -> np.ndarray:
    """รับอาร์เรย์ตัวเลข คืนอาร์เรย์ที่ค่าติดลบกลายเป็นศูนย์"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


if __name__ == "__main__":
    usd_prices = np.array([10.0, 20.0, 35.5])
    print("ราคาเป็นบาท", to_baht(usd_prices, 35.0))

    quantities = np.array([-1, 0, 3, 5])
    print("จำนวนที่แก้ค่าติดลบแล้ว", clip_negative(quantities))

    amounts = np.array([100.0, 250.0, 1000.0])
    print("ยอดรวมภาษี", total_with_vat(amounts))

    scores = np.array([0.0, 5.0, 10.0])
    print("ค่าปรับช่วง", normalize(scores))
