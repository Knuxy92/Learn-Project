from helpers import run_script


def test_order_calculation_output():
    result = run_script("ch03-order-total.py")

    assert result.returncode == 0
    assert result.stdout.splitlines() == [
        "ยอดรวมรายการแรก: 1350",
        "ยอดหลังหักส่วนลด: 1215.0",
        "ยอดถึงเกณฑ์ส่งฟรี: True",
        "ยอดต่ำกว่าเกณฑ์ส่งฟรี: False",
    ]
