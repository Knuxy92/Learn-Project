from helpers import run_script


def test_classify_orders_output():
    result = run_script("ch04-classify-orders.py")

    assert result.returncode == 0
    assert result.stdout.splitlines() == [
        "499.99 อยู่ในกลุ่ม small",
        "500 อยู่ในกลุ่ม medium",
        "2000 อยู่ในกลุ่ม large",
        "ยอดรวมทั้งหมด: 8700",
        "จำนวนรายการ paid: 3",
    ]
