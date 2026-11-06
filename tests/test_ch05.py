from helpers import import_exercise


def test_order_total():
    module = import_exercise("ch05-cleaning-helpers.py")
    assert module.order_total(450, 3) == 1350


def test_apply_discount():
    module = import_exercise("ch05-cleaning-helpers.py")
    assert module.apply_discount(1000, 10) == 900


def test_shipping_fee():
    module = import_exercise("ch05-cleaning-helpers.py")
    assert module.shipping_fee(450) == 50
    assert module.shipping_fee(1200) == 0
