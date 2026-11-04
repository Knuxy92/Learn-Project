from pathlib import Path

import pandas as pd
from helpers import import_exercise

MODULE = "ch20-clean-pipeline.py"
ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"


def raw_frame(name: str) -> pd.DataFrame:
    return pd.read_csv(RAW_DIR / name, dtype=str, encoding="utf-8")


def test_clean_customers_dedupes_keep_last():
    module = import_exercise(MODULE)

    cleaned = module.clean_customers(raw_frame("customers.csv"))

    assert len(cleaned) == 12
    assert cleaned["customer_id"].is_unique
    last_c003 = cleaned.loc[cleaned["customer_id"] == "C003", "name"].item()
    assert last_c003 == "Malee Wongsakul"


def test_clean_customers_normalizes_columns():
    module = import_exercise(MODULE)

    cleaned = module.clean_customers(raw_frame("customers.csv"))

    assert set(cleaned["country"]) == {"Thailand", "Laos"}
    assert set(cleaned["loyalty_tier"]) == {"Gold", "Silver", "Unknown"}
    assert cleaned["email"].str.lower().eq(cleaned["email"]).all()
    assert str(cleaned["signup_date"].dtype).startswith("datetime64")
    assert cleaned.loc[cleaned["customer_id"] == "C001", "name"].item() == "Nattapong Sri"


def test_clean_customers_keeps_phone_as_ten_digits_or_missing():
    module = import_exercise(MODULE)

    cleaned = module.clean_customers(raw_frame("customers.csv"))
    phones = cleaned["phone"].dropna()

    assert phones.str.fullmatch(r"0\d{9}").all()
    assert len(phones) == 11


def test_clean_orders_dedupes_keep_last():
    module = import_exercise(MODULE)

    cleaned = module.clean_orders(raw_frame("orders.csv"))

    assert len(cleaned) == 40
    assert cleaned["order_id"].is_unique


def test_clean_orders_parses_types_and_status():
    module = import_exercise(MODULE)

    cleaned = module.clean_orders(raw_frame("orders.csv"))

    assert str(cleaned["quantity"].dtype) == "Int64"
    assert str(cleaned["unit_price"].dtype) == "Float64"
    assert str(cleaned["order_date"].dtype).startswith("datetime64")
    assert set(cleaned["status"]) == {"cancelled", "paid", "pending", "unknown"}
    assert cleaned["unit_price"].isna().sum() == 3


def test_clean_orders_drops_rows_without_keys():
    module = import_exercise(MODULE)

    frame = pd.DataFrame(
        {
            "order_id": ["O1", "O2", "O3", ""],
            "customer_id": ["C1", None, "C2", "C3"],
            "product_id": ["P1", "P2", "", "P3"],
            "quantity": ["1", "2", "3", "4"],
            "unit_price": ["10", "20", "30", "40"],
            "order_date": ["2025-01-01"] * 4,
            "status": ["paid"] * 4,
        }
    )

    cleaned = module.clean_orders(frame)

    assert cleaned["order_id"].tolist() == ["O1"]


def test_clean_products_normalizes_names_and_categories():
    module = import_exercise(MODULE)

    cleaned = module.clean_products(raw_frame("products.csv"))

    assert len(cleaned) == 8
    assert set(cleaned["category"]) == {"Accessory", "Stationery", "Display", "Furniture"}
    assert cleaned["product_name"].tolist()[0] == "Keyboard"


def test_build_master_joins_and_computes_revenue():
    module = import_exercise(MODULE)

    customers = module.clean_customers(raw_frame("customers.csv"))
    orders = module.clean_orders(raw_frame("orders.csv"))
    products = module.clean_products(raw_frame("products.csv"))
    master = module.build_master(orders, customers, products)

    assert list(master.columns) == module.MASTER_COLUMNS
    assert len(master) == 40
    assert master["order_id"].is_unique
    first = master.loc[master["order_id"] == "O0001"].iloc[0]
    assert first["revenue"] == 8400.0
    assert first["product_name"] == "Monitor"


def test_build_master_leaves_orphan_customers_without_name():
    module = import_exercise(MODULE)

    customers = module.clean_customers(raw_frame("customers.csv"))
    orders = module.clean_orders(raw_frame("orders.csv"))
    products = module.clean_products(raw_frame("products.csv"))
    master = module.build_master(orders, customers, products)

    orphans = master.loc[master["name"].isna(), "customer_id"].unique()
    assert sorted(orphans) == ["C013", "C014"]


def test_run_pipeline_writes_files_and_returns_counts(tmp_path):
    module = import_exercise(MODULE)

    counts = module.run_pipeline(RAW_DIR, tmp_path)

    assert counts == {"customers": 12, "orders": 40, "products": 8, "master": 40}
    assert (tmp_path / "master.csv").exists()
    assert (tmp_path / "customers_clean.csv").exists()
    assert len(pd.read_csv(tmp_path / "master.csv")) == 40


def test_run_pipeline_creates_output_directory(tmp_path):
    module = import_exercise(MODULE)

    target = tmp_path / "nested" / "out"
    module.run_pipeline(RAW_DIR, target)

    assert target.is_dir()
    assert (target / "master.csv").is_file()


def test_clean_orders_keeps_iso_dates_unswapped():
    module = import_exercise(MODULE)

    cleaned = module.clean_orders(raw_frame("orders.csv"))
    by_id = cleaned.set_index("order_id")["order_date"]

    assert by_id.loc["O0003"].strftime("%Y-%m-%d") == "2025-06-11"
    assert by_id.loc["O0008"].strftime("%Y-%m-%d") == "2025-01-09"


def test_clean_customers_keeps_iso_dates_unswapped():
    module = import_exercise(MODULE)

    cleaned = module.clean_customers(raw_frame("customers.csv"))
    by_id = cleaned.set_index("customer_id")["signup_date"]

    assert by_id.loc["C001"].strftime("%Y-%m-%d") == "2024-11-22"
    assert by_id.loc["C010"].strftime("%Y-%m-%d") == "2024-03-05"
