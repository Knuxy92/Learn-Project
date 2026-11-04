from helpers import import_exercise


def test_order_total_multiplies_price_by_quantity():
    module = import_exercise("ch03-order-total.py")

    assert module.order_total(450, 3) == 1350.0


def test_order_total_zero_quantity():
    module = import_exercise("ch03-order-total.py")

    assert module.order_total(300, 0) == 0.0


def test_apply_discount_ten_percent():
    module = import_exercise("ch03-order-total.py")

    assert module.apply_discount(1000, 10) == 900.0


def test_apply_discount_zero_percent():
    module = import_exercise("ch03-order-total.py")

    assert module.apply_discount(250, 0) == 250.0


def test_is_free_shipping_at_threshold():
    module = import_exercise("ch03-order-total.py")

    assert module.is_free_shipping(1000) is True


def test_is_free_shipping_below_threshold():
    module = import_exercise("ch03-order-total.py")

    assert module.is_free_shipping(999.99) is False
