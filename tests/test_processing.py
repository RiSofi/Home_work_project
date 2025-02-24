from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(filter_by_state_data: list[dict[str, Any]]) -> None:
    result = filter_by_state(filter_by_state_data, "EXECUTED")
    expected = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert result == expected


def test_filter_by_state_no_match(filter_by_state_data: list[dict[str, Any]]) -> None:
    """Проверяем случаи, когда нет элементов с указанным статусом"""
    result = filter_by_state(filter_by_state_data, "PENDING")
    assert result == []


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("PENDING", []),  # Нет элементов с таким статусом
        ("", []),  # Пустая строка в качестве статуса
    ],
)
def test_filter_by_state_parametrized(
    filter_by_state_data: list[dict[str, Any]], state: str, expected: list[dict[str, Any]]
) -> None:
    """Проверка фильтрации по разным статусам"""
    result = filter_by_state(filter_by_state_data, state)
    assert result == expected


def test_sort_by_date_descending(filter_by_state_data: list[dict[str, Any]]) -> None:
    """Проверяем сортировку по убыванию"""
    result = sort_by_date(filter_by_state_data)
    expected = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert result == expected


def test_sort_by_date_ascending(filter_by_state_data: list[dict[str, Any]]) -> None:
    """Проверяем сортировку по возрастанию"""
    result = sort_by_date(filter_by_state_data, descending=False)
    expected = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    assert result == expected


def test_sort_by_date_same_dates() -> None:
    """Проверяем сортировку при одинаковых датах"""
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2023-05-01T12:00:00.000000"},
        {"id": 2, "state": "CANCELED", "date": "2023-05-01T12:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2023-05-01T12:00:00.000000"},
    ]
    result = sort_by_date(data)
    assert result == data  # Порядок должен остаться тем же


def test_sort_by_date_invalid_format() -> None:
    """Проверяем обработку некорректных форматов дат"""
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03 18:35:29"},  # Нет 'T'
        {"id": 2, "state": "CANCELED", "date": "2018/06/30 02:08:58"},  # Неправильный разделитель
        {"id": 3, "state": "EXECUTED", "date": "June 30, 2018 02:08:58"},  # Нестандартный формат
    ]
    with pytest.raises(ValueError):
        sort_by_date(data)
