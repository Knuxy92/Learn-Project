def order_total(price: float, quantity: int) -> float:
    """คูณราคาต่อหน่วยกับจำนวนชิ้น คืนยอดรวมเป็นทศนิยม"""
    return float(price * quantity)


def apply_discount(total: float, percent: float) -> float:
    """หักส่วนลดตามเปอร์เซ็นต์จากยอดรวม คืนยอดหลังหัก"""
    return float(total - total * percent / 100)


def is_free_shipping(total: float) -> bool:
    """ตรวจว่ายอดถึงเกณฑ์ส่งฟรีหนึ่งพันบาทหรือไม่"""
    return total >= 1000.0


if __name__ == "__main__":
    print(order_total(450, 3))
    print(order_total(300, 0))
    print(apply_discount(1000, 10))
    print(apply_discount(250, 0))
    print(is_free_shipping(1000))
    print(is_free_shipping(999.99))
