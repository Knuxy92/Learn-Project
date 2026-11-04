import numpy as np
from helpers import import_exercise


def test_to_baht_multiplies_every_element():
    module = import_exercise("ch10-vectorized-math.py")

    result = module.to_baht(np.array([10, 20]), 35.0)

    assert isinstance(result, np.ndarray)
    assert result.tolist() == [350.0, 700.0]


def test_to_baht_keeps_fractional_amounts():
    module = import_exercise("ch10-vectorized-math.py")

    result = module.to_baht(np.array([1.5, 2.25]), 35.0)

    assert result.tolist() == [52.5, 78.75]


def test_normalize_spreads_values_between_zero_and_one():
    module = import_exercise("ch10-vectorized-math.py")

    result = module.normalize(np.array([0, 5, 10]))

    assert result.tolist() == [0.0, 0.5, 1.0]


def test_normalize_returns_zeros_when_all_values_equal():
    module = import_exercise("ch10-vectorized-math.py")

    result = module.normalize(np.array([3, 3, 3]))

    assert result.tolist() == [0.0, 0.0, 0.0]


def test_normalize_does_not_change_input():
    module = import_exercise("ch10-vectorized-math.py")
    values = np.array([1.0, 2.0, 3.0])

    module.normalize(values)

    assert values.tolist() == [1.0, 2.0, 3.0]


def test_total_with_vat_uses_default_rate():
    module = import_exercise("ch10-vectorized-math.py")

    result = module.total_with_vat(np.array([100.0]))

    assert result.tolist() == [107.0]


def test_total_with_vat_accepts_custom_rate():
    module = import_exercise("ch10-vectorized-math.py")

    result = module.total_with_vat(np.array([200.0, 400.0]), 0.10)

    assert np.allclose(result, [220.0, 440.0])


def test_clip_negative_turns_minus_values_into_zero():
    module = import_exercise("ch10-vectorized-math.py")

    result = module.clip_negative(np.array([-5, 3]))

    assert result.tolist() == [0, 3]


def test_clip_negative_leaves_positive_values_alone():
    module = import_exercise("ch10-vectorized-math.py")

    result = module.clip_negative(np.array([0, 7, 12]))

    assert result.tolist() == [0, 7, 12]
