from helpers import run_script


def test_customer_record_output():
    result = run_script("ch02-customer-record.py")

    assert result.returncode == 0
    assert result.stdout.splitlines() == [
        "ชื่อ: Somchai",
        "อายุ: 34",
        "ยอดใช้จ่าย: 1250.50 บาท",
        "เป็นสมาชิก: True",
        "ชนิดของอายุ: <class 'int'>",
        "ชนิดของยอดใช้จ่าย: <class 'float'>",
    ]
