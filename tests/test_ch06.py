from helpers import import_exercise


def test_names_of_returns_names_in_order():
    module = import_exercise("ch06-customer-table.py")

    assert module.names_of([{"name": "A"}, {"name": "B"}]) == ["A", "B"]


def test_names_of_keeps_duplicates():
    module = import_exercise("ch06-customer-table.py")
    rows = [{"name": "A"}, {"name": "B"}, {"name": "A"}]

    assert module.names_of(rows) == ["A", "B", "A"]


def test_filter_by_country_keeps_matching_rows():
    module = import_exercise("ch06-customer-table.py")
    rows = [{"country": "TH"}, {"country": "LA"}]

    assert module.filter_by_country(rows, "TH") == [{"country": "TH"}]


def test_filter_by_country_returns_empty_list_when_nothing_matches():
    module = import_exercise("ch06-customer-table.py")

    assert module.filter_by_country([{"country": "TH"}], "LA") == []


def test_count_by_counts_each_value():
    module = import_exercise("ch06-customer-table.py")
    rows = [{"c": "x"}, {"c": "x"}, {"c": "y"}]

    assert module.count_by(rows, "c") == {"x": 2, "y": 1}


def test_count_by_on_empty_input():
    module = import_exercise("ch06-customer-table.py")

    assert module.count_by([], "c") == {}


def test_sort_by_spend_descending_by_default():
    module = import_exercise("ch06-customer-table.py")
    rows = [{"spend": 10}, {"spend": 30}, {"spend": 20}]

    assert module.sort_by_spend(rows) == [{"spend": 30}, {"spend": 20}, {"spend": 10}]


def test_sort_by_spend_ascending_when_requested():
    module = import_exercise("ch06-customer-table.py")
    rows = [{"spend": 10}, {"spend": 30}]

    assert module.sort_by_spend(rows, descending=False) == [{"spend": 10}, {"spend": 30}]


def test_sort_by_spend_does_not_mutate_input():
    module = import_exercise("ch06-customer-table.py")
    rows = [{"spend": 10}, {"spend": 30}]
    original = list(rows)

    module.sort_by_spend(rows)

    assert rows == original
