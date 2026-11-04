import numpy as np


def revenue(quantity: np.ndarray, price: np.ndarray) -> np.ndarray:
    """คูณจำนวนกับราคาต่อหน่วยทีละคู่"""
    return np.asarray(quantity) * np.asarray(price)


def mask_paid(status: np.ndarray) -> np.ndarray:
    """คืนมาสก์จริงเท็จของแถวที่สถานะเป็น paid โดยไม่สนตัวพิมพ์และช่องว่าง"""
    cleaned = np.strings.lower(np.strings.strip(np.asarray(status, dtype=str)))
    return cleaned == "paid"


def summary(values: np.ndarray) -> dict[str, float]:
    """สรุปค่าสถิติพื้นฐานห้าตัว"""
    numbers = np.asarray(values, dtype=float)

    return {
        "mean": float(numbers.mean()),
        "median": float(np.median(numbers)),
        "min": float(numbers.min()),
        "max": float(numbers.max()),
        "sum": float(numbers.sum()),
    }


if __name__ == "__main__":
    quantities = np.array([2, 3, 1, 4])
    prices = np.array([450.0, 300.0, 1200.0, 89.0])
    print("ยอดต่อออเดอร์", revenue(quantities, prices))

    statuses = np.array(["paid", "PAID", " pending ", "Paid", "cancelled"])
    print("มาสก์ที่จ่ายแล้ว", mask_paid(statuses))

    amounts = np.array([900.0, 1500.0, 1200.0, 890.0])
    print("สรุปยอดขาย", summary(amounts))
