import pandas as pd
from helpers import import_exercise

MODULE = "ch19-quality-report.py"


def make_frame() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "customer_id": ["C1", "C2", "C2", "C4"],
            "amount": [10.0, None, 30.0, 40.0],
            "status": ["paid", "paid", "pending", ""],
        }
    )


def test_quality_report_columns_and_order():
    module = import_exercise(MODULE)
    report = module.quality_report(make_frame())

    assert list(report.columns) == ["column", "missing", "unique", "dtype"]
    assert report["column"].tolist() == ["amount", "customer_id", "status"]


def test_quality_report_counts_missing_and_unique():
    module = import_exercise(MODULE)
    report = module.quality_report(make_frame()).set_index("column")

    assert int(report.loc["amount", "missing"]) == 1
    assert int(report.loc["amount", "unique"]) == 3
    assert int(report.loc["customer_id", "missing"]) == 0
    assert int(report.loc["customer_id", "unique"]) == 3
    assert int(report.loc["status", "missing"]) == 0


def test_quality_report_dtype_is_text():
    module = import_exercise(MODULE)
    report = module.quality_report(make_frame())

    assert all(isinstance(value, str) and value for value in report["dtype"])


def test_quality_report_does_not_mutate_input():
    module = import_exercise(MODULE)
    frame = make_frame()
    before = frame.copy()

    module.quality_report(frame)

    pd.testing.assert_frame_equal(frame, before)


def test_find_duplicates_returns_all_repeated_rows():
    module = import_exercise(MODULE)
    frame = pd.DataFrame({"order_id": ["O1", "O2", "O2", "O3"], "value": [1, 2, 3, 4]})

    repeated = module.find_duplicates(frame, ["order_id"])

    assert repeated["value"].tolist() == [2, 3]


def test_find_duplicates_respects_multiple_columns():
    module = import_exercise(MODULE)
    frame = pd.DataFrame(
        {
            "order_id": ["O1", "O1", "O1"],
            "product_id": ["P1", "P1", "P2"],
        }
    )

    repeated = module.find_duplicates(frame, ["order_id", "product_id"])

    assert len(repeated) == 2


def test_find_duplicates_on_real_orders_finds_o0006():
    module = import_exercise(MODULE)
    orders, _ = module.load_raw()

    repeated = module.find_duplicates(orders, ["order_id"])

    assert len(repeated) == 3
    assert set(repeated["order_id"]) == {"O0006"}


def test_find_out_of_range_is_inclusive_at_bounds():
    module = import_exercise(MODULE)
    frame = pd.DataFrame({"quantity": [-1, 0, 1, 100, 101]})

    outside = module.find_out_of_range(frame, "quantity", 1, 100)

    assert outside["quantity"].tolist() == [-1, 0, 101]


def test_find_out_of_range_ignores_missing_values():
    module = import_exercise(MODULE)
    frame = pd.DataFrame({"quantity": [None, 5.0, 200.0]})

    outside = module.find_out_of_range(frame, "quantity", 1, 100)

    assert outside["quantity"].tolist() == [200.0]


def test_referential_issues_returns_child_orphans():
    module = import_exercise(MODULE)
    child = pd.DataFrame({"order_id": ["O1", "O2", "O3"], "customer_id": ["C1", "C9", "C2"]})
    parent = pd.DataFrame({"customer_id": ["C1", "C2"]})

    orphans = module.referential_issues(child, parent, "customer_id")

    assert orphans["order_id"].tolist() == ["O2"]
    assert list(orphans.columns) == list(child.columns)


def test_referential_issues_on_real_data_finds_c013_and_c014():
    module = import_exercise(MODULE)
    orders, customers = module.load_raw()

    orphans = module.referential_issues(orders, customers, "customer_id")

    assert len(orphans) == 5
    assert sorted(orphans["customer_id"].unique()) == ["C013", "C014"]
