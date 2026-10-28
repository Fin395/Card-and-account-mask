from src.processing import filter_by_state, sort_by_date
import pytest

from tests.conftest import operations


@pytest.mark.parametrize('state, expected', [
    ('EXECUTED', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    ('CANCELED', [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
])
def test_filter_by_state(operations, state, expected):
    assert filter_by_state(operations, state) == expected

def test_filter_by_state_if_empty(empty_operations):
    assert filter_by_state(empty_operations) == []

def test_filter_by_absent_state(operations):
    assert filter_by_state(operations, state='DENIED') == []

def test_sort_by_date_reverse_true(operations):
    assert sort_by_date(operations) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

def test_sort_by_date_reverse_false(operations):
    assert sort_by_date(operations, reverse=False) == [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]

def test_sort_by_date_if_equal_dates(operations_with_equal_date):
    assert sort_by_date(operations_with_equal_date) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]
