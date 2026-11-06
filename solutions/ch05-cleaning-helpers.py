def order_total(price, quantity):
    return price * quantity


def apply_discount(total, percent):
    return total - (total * percent / 100)


def shipping_fee(total):
    if total >= 1000:
        return 0
    return 50


print(f"ยอดรวมรายการแรก: {order_total(450, 3)}")
print(f"ยอดหลังหักส่วนลด: {apply_discount(1000, 10)}")
print(f"ค่าส่งของยอด 450: {shipping_fee(450)}")
print(f"ค่าส่งของยอด 1200: {shipping_fee(1200)}")
