from helpers import run_script


def test_first_code_prints_name_age_and_goal():
    result = run_script("ch01-first-code.py")

    assert result.returncode == 0, result.stderr
    lines = result.stdout.strip().splitlines()

    assert len(lines) == 3
    assert lines[0].startswith("ชื่อ: ")
    assert lines[1].startswith("อายุ: ")
    assert lines[1].endswith(" ปี")
    assert lines[2].startswith("เป้าหมาย: ")
