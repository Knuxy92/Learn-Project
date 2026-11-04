import numpy as np


def price_array(texts: list[str]) -> np.ndarray:
    cleaned = [text.replace("฿", "").replace(",", "") for text in texts]
    return np.array(cleaned, dtype=float)


if __name__ == "__main__":
    quantities = np.array([3, 1, 2, 0])
    prices = np.array([450.0, 1150.0, 300.0, 99.5])

    print(f"quantities คือ {quantities}")
    print(f"prices คือ {prices}")
    print(f"ชนิดของ quantities คือ {type(quantities)}")
    print(f"dtype ของ quantities คือ {quantities.dtype}")
    print(f"dtype ของ prices คือ {prices.dtype}")
    print(f"shape ของ quantities คือ {quantities.shape}")
    print(f"size ของ quantities คือ {quantities.size}")
    print(f"ndim ของ quantities คือ {quantities.ndim}")

    print(f"บังคับ dtype float ได้ {np.array([3, 1, 2], dtype=float)}")
    print(f"บังคับ dtype int ได้ {np.array([3.7, 1.2], dtype=int)}")

    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"matrix คือ {matrix}")
    print(f"shape ของ matrix คือ {matrix.shape}")
    print(f"ndim ของ matrix คือ {matrix.ndim}")

    print(f"zeros คือ {np.zeros(3)}")
    print(f"ones แบบ int คือ {np.ones(2, dtype=int)}")
    print(f"arange คือ {np.arange(0, 10, 3)}")

    prices_from_text = price_array(["฿1,150", "450", "300.00"])
    print(f"ลิสต์ข้อความกลายเป็น {prices_from_text}")
    print(f"dtype ของผลลัพธ์คือ {prices_from_text.dtype}")

    print(f"array ว่างคือ {np.array([])}")
    print(f"array ว่างมี size {np.array([]).size}")
