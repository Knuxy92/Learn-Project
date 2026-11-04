from pathlib import Path

import pandas as pd
from helpers import ROOT, import_exercise

CUSTOMERS_PATH = ROOT / "data" / "raw" / "customers.csv"
THAI_CUSTOMERS_PATH = ROOT / "data" / "raw" / "customers_th.csv"


def test_load_customers_reads_real_file():
    module = import_exercise("ch13-load-csv.py")

    customers = module.load_customers(CUSTOMERS_PATH)

    assert customers.shape == (14, 7)
    assert customers.loc[0, "customer_id"] == "C001"


def test_load_customers_default_path_works_from_repo_root():
    module = import_exercise("ch13-load-csv.py")

    assert module.load_customers().shape == (14, 7)


def test_load_thai_customers_keeps_header_clean():
    module = import_exercise("ch13-load-csv.py")

    thai = module.load_thai_customers(THAI_CUSTOMERS_PATH)

    assert thai.shape == (3, 4)
    assert list(thai.columns) == ["customer_id", "name", "province", "email"]
    assert thai.loc[0, "name"] == "สมชาย ใจดี"


def test_load_thai_customers_default_path_works_from_repo_root():
    module = import_exercise("ch13-load-csv.py")

    assert module.load_thai_customers().loc[0, "name"] == "สมชาย ใจดี"


def test_shape_of_returns_rows_and_columns():
    module = import_exercise("ch13-load-csv.py")

    customers = module.load_customers(CUSTOMERS_PATH)

    assert module.shape_of(customers) == (14, 7)


def test_save_clean_round_trip(tmp_path: Path):
    module = import_exercise("ch13-load-csv.py")

    customers = module.load_customers(CUSTOMERS_PATH).head(4)
    output_path = tmp_path / "customers_clean.csv"

    module.save_clean(customers, output_path)

    assert output_path.exists()
    reloaded = pd.read_csv(output_path, encoding="utf-8")
    assert reloaded.shape == (4, 7)
    assert list(reloaded.columns) == list(customers.columns)


def test_save_clean_writes_no_index_column(tmp_path: Path):
    module = import_exercise("ch13-load-csv.py")

    customers = module.load_customers(CUSTOMERS_PATH).head(2)
    output_path = tmp_path / "no_index.csv"

    module.save_clean(customers, output_path)

    header = output_path.read_text(encoding="utf-8").splitlines()[0]
    assert header.split(",")[0] == "customer_id"


def test_save_clean_preserves_thai_text(tmp_path: Path):
    module = import_exercise("ch13-load-csv.py")

    thai = module.load_thai_customers(THAI_CUSTOMERS_PATH)
    output_path = tmp_path / "thai.csv"

    module.save_clean(thai, output_path)

    reloaded = pd.read_csv(output_path, encoding="utf-8")
    assert reloaded.loc[0, "name"] == "สมชาย ใจดี"
    assert reloaded.shape == (3, 4)
