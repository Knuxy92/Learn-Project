import numpy as np

if __name__ == "__main__":
    quantities = np.array([3, 1, 2, 5, 0, 4])

    print(f"quantities คือ {quantities}")
    print(f"ตัวแรกคือ {quantities[0]}")
    print(f"ตัวสุดท้ายคือ {quantities[-1]}")
    print(f"ช่วง 1 ถึง 3 คือ {quantities[1:4]}")
    print(f"สองตัวแรกคือ {quantities[:2]}")
    print(f"ตั้งแต่ตัวที่ 3 คือ {quantities[3:]}")
    print(f"ข้ามทีละสองคือ {quantities[::2]}")
    print(f"ย้อนกลับคือ {quantities[::-1]}")

    prices = np.array([450.0, 1150.0, 300.0, 99.5, 800.0, 250.0])
    print(f"ราคาที่จำนวนมากกว่าสองคือ {prices[quantities > 2]}")
    print(f"ราคาที่อยู่ระหว่าง 0 กับ 500 คือ {prices[(quantities > 0) & (prices < 500)]}")
    print(f"แถวที่จำนวนเป็นศูนย์คือ {quantities[quantities == 0]}")

    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"matrix แถวแรกคือ {matrix[0]}")
    print(f"สมาชิกแถวที่ 2 คอลัมน์ที่ 3 คือ {matrix[1, 2]}")
    print(f"คอลัมน์แรกทุกแถวคือ {matrix[:, 0]}")
    print(f"บล็อก 2 คูณ 2 คือ {matrix[0:2, 1:3]}")

    selected = prices[quantities > 2]
    print(f"ผลลัพธ์ที่เลือกได้มี shape {selected.shape}")
    print(f"ผลลัพธ์ที่เลือกได้มี size {selected.size}")

    mask = quantities > 2
    print(f"mask คือ {mask}")
    print(f"dtype ของ mask คือ {mask.dtype}")
    print(f"นับค่าจริงด้วย sum ได้ {mask.sum()}")
