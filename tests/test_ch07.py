from pathlib import Path

from helpers import ROOT, import_exercise

RAW_DIR = ROOT / "data" / "raw"


def test_count_lines_excludes_header_on_real_file():
    module = import_exercise("ch07-read-raw-file.py")

    assert module.count_lines(RAW_DIR / "products.csv") == 8


def test_count_lines_on_tmp_file(tmp_path):
    module = import_exercise("ch07-read-raw-file.py")
    path = tmp_path / "sample.csv"
    path.write_text("id,name\n1,A\n2,B\n", encoding="utf-8")

    assert module.count_lines(path) == 2


def test_count_lines_on_header_only_file(tmp_path):
    module = import_exercise("ch07-read-raw-file.py")
    path = tmp_path / "empty.csv"
    path.write_text("id,name\n", encoding="utf-8")

    assert module.count_lines(path) == 0


def test_first_column_skips_header():
    module = import_exercise("ch07-read-raw-file.py")

    assert module.first_column(RAW_DIR / "customers.csv")[0] == "C001"


def test_first_column_returns_every_row(tmp_path):
    module = import_exercise("ch07-read-raw-file.py")
    path = tmp_path / "sample.csv"
    path.write_text("id,name\nP001,A\nP002,B\n", encoding="utf-8")

    assert module.first_column(path) == ["P001", "P002"]


def test_write_lines_writes_one_line_each(tmp_path):
    module = import_exercise("ch07-read-raw-file.py")
    path = tmp_path / "out.txt"

    module.write_lines(path, ["P001", "P002"])

    assert path.read_text(encoding="utf-8") == "P001\nP002\n"


def test_write_lines_keeps_thai_text(tmp_path):
    module = import_exercise("ch07-read-raw-file.py")
    path = tmp_path / "out.txt"

    module.write_lines(path, ["สมชาย", "มาลี"])

    assert path.read_text(encoding="utf-8").splitlines() == ["สมชาย", "มาลี"]


def test_write_lines_handles_empty_list(tmp_path):
    module = import_exercise("ch07-read-raw-file.py")
    path = tmp_path / "out.txt"

    module.write_lines(path, [])

    assert path.read_text(encoding="utf-8") == ""


def test_read_thai_csv_reads_bom_file():
    module = import_exercise("ch07-read-raw-file.py")
    rows = module.read_thai_csv(RAW_DIR / "customers_th.csv")

    assert len(rows) == 3
    assert rows[0]["name"] == "สมชาย ใจดี"
    assert rows[0]["province"] == "กรุงเทพมหานคร"


def test_read_thai_csv_returns_dict_rows(tmp_path):
    module = import_exercise("ch07-read-raw-file.py")
    path = tmp_path / "thai.csv"
    path.write_text(
        "customer_id,name\nC001,สมชาย ใจดี\n",
        encoding="utf-8-sig",
    )

    rows = module.read_thai_csv(path)

    assert rows == [{"customer_id": "C001", "name": "สมชาย ใจดี"}]


def test_read_thai_csv_uses_key_names_from_header(tmp_path):
    module = import_exercise("ch07-read-raw-file.py")
    path = tmp_path / "thai.csv"
    path.write_text("customer_id,province\nC002,เชียงใหม่\n", encoding="utf-8-sig")

    rows = module.read_thai_csv(path)

    assert list(rows[0]) == ["customer_id", "province"]
    assert rows[0]["province"] == "เชียงใหม่"


def test_paths_accept_plain_strings():
    module = import_exercise("ch07-read-raw-file.py")

    assert module.count_lines(str(Path(RAW_DIR / "products.csv"))) == 8
