from pathlib import Path

import pandas as pd
from helpers import import_exercise

MODULE = "ch21-final-report.py"
ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"


def cleaned_tables(module) -> tuple[dict[str, pd.DataFrame], pd.DataFrame]:
    raw = module.load_raw(RAW_DIR)
    cleaned = module.clean_all(raw)
    return cleaned, module.build_master(cleaned)


def test_load_raw_returns_three_tables():
    module = import_exercise(MODULE)

    raw = module.load_raw(RAW_DIR)

    assert sorted(raw) == ["customers", "orders", "products"]
    assert len(raw["customers"]) == 14
    assert len(raw["orders"]) == 42
    assert len(raw["products"]) == 8


def test_load_raw_uses_default_directory():
    module = import_exercise(MODULE)

    raw = module.load_raw()

    assert len(raw["customers"]) == 14


def test_clean_all_dedupes_each_table():
    module = import_exercise(MODULE)

    cleaned, _ = cleaned_tables(module)

    assert len(cleaned["customers"]) == 12
    assert len(cleaned["orders"]) == 40
    assert len(cleaned["products"]) == 8
    assert cleaned["customers"]["customer_id"].is_unique
    assert cleaned["orders"]["order_id"].is_unique


def test_clean_all_applies_canonical_normalizations():
    module = import_exercise(MODULE)

    cleaned, _ = cleaned_tables(module)

    assert set(cleaned["customers"]["country"]) == {"Thailand", "Laos"}
    assert set(cleaned["customers"]["loyalty_tier"]) == {"Gold", "Silver", "Unknown"}
    assert set(cleaned["orders"]["status"]) == {"cancelled", "paid", "pending", "unknown"}
    assert str(cleaned["orders"]["quantity"].dtype) == "Int64"
    assert str(cleaned["orders"]["unit_price"].dtype) == "Float64"


def test_build_master_has_revenue_and_one_row_per_order():
    module = import_exercise(MODULE)

    cleaned, master = cleaned_tables(module)

    assert len(master) == len(cleaned["orders"])
    assert master["order_id"].is_unique
    assert "revenue" in master.columns
    assert master.loc[master["order_id"] == "O0001", "revenue"].item() == 8400.0


def test_build_master_keeps_orders_without_customer():
    module = import_exercise(MODULE)

    _, master = cleaned_tables(module)

    assert master["customer_id"].notna().all()
    assert master["name"].isna().sum() == 5
    assert sorted(master.loc[master["name"].isna(), "customer_id"].unique()) == [
        "C013",
        "C014",
    ]


def test_customer_summary_columns_and_sorting():
    module = import_exercise(MODULE)

    _, master = cleaned_tables(module)
    summary = module.customer_summary(master)

    assert list(summary.columns) == ["customer_id", "name", "orders", "revenue"]
    assert summary["revenue"].is_monotonic_decreasing
    assert summary["customer_id"].is_unique
    assert len(summary) == 13
    assert int(summary["orders"].sum()) == len(master)


def test_customer_summary_top_row_is_c003():
    module = import_exercise(MODULE)

    _, master = cleaned_tables(module)
    summary = module.customer_summary(master)

    assert summary.iloc[0]["customer_id"] == "C003"
    assert summary.iloc[0]["orders"] == 7
    assert summary.iloc[0]["revenue"] == 13310.0


def test_monthly_summary_columns_and_sorting():
    module = import_exercise(MODULE)

    _, master = cleaned_tables(module)
    summary = module.monthly_summary(master)

    assert list(summary.columns) == ["month", "orders", "revenue"]
    assert summary["month"].is_monotonic_increasing
    assert len(summary) == 11
    assert int(summary["orders"].sum()) == len(master)
    assert summary["month"].tolist()[0] == "2025-01"
    assert summary["month"].tolist()[-1] == "2025-12"


def test_save_outputs_writes_three_files_sorted(tmp_path):
    module = import_exercise(MODULE)

    _, master = cleaned_tables(module)
    by_customer = module.customer_summary(master)
    by_month = module.monthly_summary(master)

    written = module.save_outputs(master, by_customer, by_month, tmp_path)

    assert written == ["customer_summary.csv", "master.csv", "monthly_summary.csv"]
    for name in written:
        assert (tmp_path / name).is_file()


def test_run_end_to_end_writes_all_outputs(tmp_path):
    module = import_exercise(MODULE)

    counts = module.run(RAW_DIR, tmp_path)

    assert counts["customers"] == 12
    assert counts["orders"] == 40
    assert counts["products"] == 8
    assert counts["master"] == 40
    assert counts["customer_summary"] == 13
    assert counts["monthly_summary"] == 11
    assert len(list(tmp_path.glob("*.csv"))) == 3

    master = pd.read_csv(tmp_path / "master.csv")
    assert len(master) == 40
    assert master["customer_id"].notna().all()
    assert master["order_id"].is_unique


def test_run_outputs_are_readable_and_consistent(tmp_path):
    module = import_exercise(MODULE)

    module.run(RAW_DIR, tmp_path)

    master = pd.read_csv(tmp_path / "master.csv")
    by_customer = pd.read_csv(tmp_path / "customer_summary.csv")
    by_month = pd.read_csv(tmp_path / "monthly_summary.csv")

    assert int(by_customer["orders"].sum()) == len(master)
    assert int(by_month["orders"].sum()) == len(master)
    assert by_customer["revenue"].sum() == master["revenue"].sum()
    assert by_month["revenue"].sum() == master["revenue"].sum()


def test_clean_all_keeps_iso_dates_unswapped():
    module = import_exercise(MODULE)

    raw = module.load_raw(RAW_DIR)
    cleaned = module.clean_all(raw)
    orders = cleaned["orders"].set_index("order_id")["order_date"]
    customers = cleaned["customers"].set_index("customer_id")["signup_date"]

    assert orders.loc["O0003"].strftime("%Y-%m-%d") == "2025-06-11"
    assert customers.loc["C001"].strftime("%Y-%m-%d") == "2024-11-22"
