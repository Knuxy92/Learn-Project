from helpers import import_exercise


def test_classify_amount_boundaries():
    module = import_exercise("ch04-classify-orders.py")

    assert module.classify_amount(499.99) == "small"
    assert module.classify_amount(500) == "medium"
    assert module.classify_amount(1999.99) == "medium"
    assert module.classify_amount(2000) == "large"


def test_count_by_status_counts_each_status():
    module = import_exercise("ch04-classify-orders.py")
    rows = [
        {"status": "paid"},
        {"status": "paid"},
        {"status": "pending"},
    ]

    assert module.count_by_status(rows) == {"paid": 2, "pending": 1}


def test_count_by_status_empty_list():
    module = import_exercise("ch04-classify-orders.py")

    assert module.count_by_status([]) == {}


def test_find_first_large_returns_first_match():
    module = import_exercise("ch04-classify-orders.py")
    rows = [{"total": 100}, {"total": 2500}, {"total": 3000}]

    assert module.find_first_large(rows) == {"total": 2500}


def test_find_first_large_returns_none_when_absent():
    module = import_exercise("ch04-classify-orders.py")

    assert module.find_first_large([{"total": 1}]) is None
