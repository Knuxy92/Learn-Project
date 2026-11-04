import pandas as pd
import pytest
from helpers import import_exercise


@pytest.fixture(scope="module")
def module():
    return import_exercise("ch16-normalize-text.py")


def test_clean_name_trims_and_collapses(module):
    result = module.clean_name(pd.Series(["  somchai   jaidee "]))

    assert result.tolist() == ["Somchai Jaidee"]


def test_clean_name_keeps_missing(module):
    result = module.clean_name(pd.Series(["  Nattapong Sri  ", None]))

    assert result.tolist()[0] == "Nattapong Sri"
    assert pd.isna(result.tolist()[1])


def test_normalize_country_maps_aliases(module):
    result = module.normalize_country(pd.Series(["TH", "thailand ", "Laos", "LA"]))

    assert result.tolist() == ["Thailand", "Thailand", "Laos", "Laos"]


def test_normalize_country_leaves_unknown_missing(module):
    result = module.normalize_country(pd.Series(["TH", None]))

    assert result.tolist()[0] == "Thailand"
    assert pd.isna(result.tolist()[1])


def test_normalize_status_lowers_and_unifies(module):
    result = module.normalize_status(pd.Series(["PAID", "paid ", "canceled", ""]))

    assert result.tolist() == ["paid", "paid", "cancelled", "unknown"]


def test_normalize_status_fills_missing(module):
    result = module.normalize_status(pd.Series(["pending", None]))

    assert result.tolist() == ["pending", "unknown"]


def test_normalize_category_title_cases(module):
    result = module.normalize_category(pd.Series(["accessory", "Display", " furniture "]))

    assert result.tolist() == ["Accessory", "Display", "Furniture"]


def test_normalize_category_keeps_missing(module):
    result = module.normalize_category(pd.Series(["accessory", None]))

    assert result.tolist()[0] == "Accessory"
    assert pd.isna(result.tolist()[1])


def test_functions_do_not_mutate_input(module):
    source = pd.Series(["  somchai   jaidee "])
    module.clean_name(source)

    assert source.tolist() == ["  somchai   jaidee "]


def test_clean_name_works_on_real_customers(module):
    customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")
    result = module.clean_name(customers["name"])

    assert result.iloc[0] == "Nattapong Sri"
    assert not result.str.contains("  ").any()


def test_normalize_status_on_real_orders_has_four_values(module):
    orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")
    result = module.normalize_status(orders["status"])

    assert sorted(result.unique().tolist()) == ["cancelled", "paid", "pending", "unknown"]
    assert result.isna().sum() == 0
