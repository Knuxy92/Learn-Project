from helpers import import_exercise


def test_describe_customer_member():
    module = import_exercise("ch02-customer-record.py")

    expected = "Somchai | 34 | 1250.50 | member"
    assert module.describe_customer("Somchai", 34, 1250.5, True) == expected


def test_describe_customer_guest():
    module = import_exercise("ch02-customer-record.py")

    assert module.describe_customer("Malee", 28, 0.0, False) == "Malee | 28 | 0.00 | guest"


def test_type_report_int():
    module = import_exercise("ch02-customer-record.py")

    assert module.type_report(3) == "int"


def test_type_report_float():
    module = import_exercise("ch02-customer-record.py")

    assert module.type_report(3.5) == "float"


def test_type_report_str():
    module = import_exercise("ch02-customer-record.py")

    assert module.type_report("x") == "str"


def test_type_report_bool():
    module = import_exercise("ch02-customer-record.py")

    assert module.type_report(True) == "bool"
