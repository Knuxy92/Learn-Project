import json

import pytest
from helpers import import_exercise


def test_safe_divide_returns_quotient():
    module = import_exercise("ch08-safe-parsers.py")

    assert module.safe_divide(10, 2) == 5.0


def test_safe_divide_by_zero_returns_none():
    module = import_exercise("ch08-safe-parsers.py")

    assert module.safe_divide(1, 0) is None


def test_parse_int_accepts_numeric_text():
    module = import_exercise("ch08-safe-parsers.py")

    assert module.parse_int("42") == 42


def test_parse_int_rejects_float_text():
    module = import_exercise("ch08-safe-parsers.py")

    assert module.parse_int("4.2") is None


def test_parse_int_rejects_none():
    module = import_exercise("ch08-safe-parsers.py")

    assert module.parse_int(None) is None


def test_read_text_or_default_returns_default_for_missing_file(tmp_path):
    module = import_exercise("ch08-safe-parsers.py")
    missing = tmp_path / "ไม่มี.csv"

    assert module.read_text_or_default(missing, "none") == "none"


def test_read_text_or_default_returns_file_content(tmp_path):
    module = import_exercise("ch08-safe-parsers.py")
    sample = tmp_path / "sample.txt"
    sample.write_text("C001,Gold", encoding="utf-8")

    assert module.read_text_or_default(sample) == "C001,Gold"


def test_read_json_object_rejects_non_object(tmp_path):
    module = import_exercise("ch08-safe-parsers.py")
    sample = tmp_path / "list.json"
    sample.write_text(json.dumps([1, 2]), encoding="utf-8")

    with pytest.raises(ValueError, match="JSON ต้องเป็น object"):
        module.read_json_object(sample)


def test_read_json_object_returns_dict(tmp_path):
    module = import_exercise("ch08-safe-parsers.py")
    sample = tmp_path / "object.json"
    sample.write_text(json.dumps({"a": 1}), encoding="utf-8")

    assert module.read_json_object(sample) == {"a": 1}


def test_read_json_object_raises_for_missing_file(tmp_path):
    module = import_exercise("ch08-safe-parsers.py")

    with pytest.raises(FileNotFoundError):
        module.read_json_object(tmp_path / "missing.json")
