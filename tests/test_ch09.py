import numpy as np
from helpers import import_exercise


def test_make_array_returns_numeric_array():
    module = import_exercise("ch09-array-basics.py")
    result = module.make_array([1, 2, 3])

    assert isinstance(result, np.ndarray)
    assert np.issubdtype(result.dtype, np.number)
    assert result.tolist() == [1, 2, 3]


def test_shape_info_reports_size_and_dimension():
    module = import_exercise("ch09-array-basics.py")

    assert module.shape_info([1, 2, 3]) == (3, 1)


def test_select_even_keeps_even_values():
    module = import_exercise("ch09-array-basics.py")
    result = module.select_even([1, 2, 3, 4])

    assert result.tolist() == [2, 4]


def test_select_even_returns_array():
    module = import_exercise("ch09-array-basics.py")

    assert isinstance(module.select_even([1, 2, 3, 4]), np.ndarray)


def test_replace_negative_uses_default_replacement():
    module = import_exercise("ch09-array-basics.py")
    result = module.replace_negative([1, -2, 3])

    assert result.tolist() == [1.0, 0.0, 3.0]


def test_replace_negative_accepts_custom_replacement():
    module = import_exercise("ch09-array-basics.py")
    result = module.replace_negative([-5.0, 2.0], replacement=-1.0)

    assert result.tolist() == [-1.0, 2.0]


def test_replace_negative_does_not_mutate_input():
    module = import_exercise("ch09-array-basics.py")
    values = [1.0, -2.0, 3.0]

    module.replace_negative(values)

    assert values == [1.0, -2.0, 3.0]


def test_replace_negative_returns_array():
    module = import_exercise("ch09-array-basics.py")

    assert isinstance(module.replace_negative([1.0, -2.0]), np.ndarray)


def test_make_array_empty_list_has_zero_size():
    module = import_exercise("ch09-array-basics.py")

    assert module.make_array([]).size == 0


def test_shape_info_handles_float_input():
    module = import_exercise("ch09-array-basics.py")

    assert module.shape_info([1.5, 2.5]) == (2, 1)


def test_select_even_returns_empty_array_when_none_match():
    module = import_exercise("ch09-array-basics.py")

    assert module.select_even([1, 3, 5]).size == 0
