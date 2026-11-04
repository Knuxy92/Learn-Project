def order_total(price: float, quantity: int) -> float:
    """รับราคาต่อหน่วยกับจำนวนชิ้น คืนยอดรวมก่อนหักส่วนลด"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def apply_discount(total: float, percent: float) -> float:
    """รับยอดรวมกับเปอร์เซ็นต์ส่วนลด คืนยอดหลังหักส่วนลด"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def is_free_shipping(total: float) -> bool:
    """รับยอดรวม คืนค่าจริงเมื่อยอดถึงเกณฑ์ส่งฟรีหนึ่งพันบาท"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


if __name__ == "__main__":
    print(order_total(450, 3))
    print(order_total(300, 0))
    print(apply_discount(1000, 10))
    print(apply_discount(250, 0))
    print(is_free_shipping(1000))
    print(is_free_shipping(999.99))
