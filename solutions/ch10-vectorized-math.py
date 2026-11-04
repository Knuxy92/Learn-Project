import numpy as np


def to_baht(usd: np.ndarray, rate: float) -> np.ndarray:
    """แปลงจำนวนเงินดอลลาร์เป็นบาทด้วยอัตราแลกเปลี่ยนที่กำหนด"""
    return usd * rate


def normalize(values: np.ndarray) -> np.ndarray:
    """ปรับค่าให้อยู่ในช่วงศูนย์ถึงหนึ่ง ถ้าค่าทุกตัวเท่ากันคืนค่าศูนย์"""
    lowest = values.min()
    span = values.max() - lowest

    if span == 0:
        return np.zeros_like(values, dtype=float)

    return (values - lowest) / span


def total_with_vat(values: np.ndarray, vat: float = 0.07) -> np.ndarray:
    """บวกภาษีมูลค่าเพิ่มให้ทุกค่า"""
    return values * (1 + vat)


def clip_negative(values: np.ndarray) -> np.ndarray:
    """เปลี่ยนค่าที่ติดลบให้เป็นศูนย์ ค่าอื่นคงเดิม"""
    return np.where(values < 0, 0, values)


if __name__ == "__main__":
    usd_prices = np.array([10.0, 20.0, 35.5])
    print("ราคาเป็นบาท", to_baht(usd_prices, 35.0))

    quantities = np.array([-1, 0, 3, 5])
    print("จำนวนที่แก้ค่าติดลบแล้ว", clip_negative(quantities))

    amounts = np.array([100.0, 250.0, 1000.0])
    print("ยอดรวมภาษี", total_with_vat(amounts))

    scores = np.array([0.0, 5.0, 10.0])
    print("ค่าปรับช่วง", normalize(scores))
