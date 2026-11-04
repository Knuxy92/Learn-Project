import numpy as np
from helpers import import_exercise


def test_revenue_multiplies_pair_by_pair():
    module = import_exercise("ch11-order-stats.py")

    result = module.revenue(np.array([2, 3]), np.array([100.0, 50.0]))

    assert result.tolist() == [200.0, 150.0]


def test_revenue_returns_float_for_fractional_price():
    module = import_exercise("ch11-order-stats.py")

    result = module.revenue(np.array([3]), np.array([99.5]))

    assert result.tolist() == [298.5]


def test_mask_paid_ignores_case_and_spaces():
    module = import_exercise("ch11-order-stats.py")

    result = module.mask_paid(np.array(["paid", "PAID", "pending"]))

    assert result.dtype == np.bool_
    assert result.tolist() == [True, True, False]


def test_mask_paid_strips_surrounding_spaces():
    module = import_exercise("ch11-order-stats.py")

    result = module.mask_paid(np.array([" Paid ", "paid", "cancelled"]))

    assert result.tolist() == [True, True, False]


def test_mask_paid_rejects_empty_status():
    module = import_exercise("ch11-order-stats.py")

    result = module.mask_paid(np.array(["", "paid"]))

    assert result.tolist() == [False, True]


def test_summary_returns_the_five_keys():
    module = import_exercise("ch11-order-stats.py")

    result = module.summary(np.array([10.0, 20.0, 30.0]))

    assert result == {"mean": 20.0, "median": 20.0, "min": 10.0, "max": 30.0, "sum": 60.0}


def test_summary_median_differs_from_mean():
    module = import_exercise("ch11-order-stats.py")

    result = module.summary(np.array([1.0, 2.0, 100.0]))

    assert result["mean"] == 34.333333333333336
    assert result["median"] == 2.0
    assert result["max"] == 100.0
