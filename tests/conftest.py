from typing import Any

import pytest


@pytest.fixture
def valid_card_numbers() -> list[tuple[str, str]]:
    return [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7000552279664064", "7000 55** **** 4064"),
        ("1234567812345678", "1234 56** **** 5678"),
    ]


@pytest.fixture
def invalid_card_numbers() -> list[str | None]:
    return [
        "1234 5678 1234",
        "abcd567812345678",
        "12345678123456789",
        "",
        None,
    ]


@pytest.fixture
def valid_mask_account() -> list[tuple[str, str]]:
    return [
        ("73654108430135874305", "**4305"),
        ("27592747582", "**7582"),
        ("8372605816948251", "**8251"),
    ]


@pytest.fixture
def invalid_mask_account() -> list[str | None]:
    return [
        "hpr65324092356",
        "323",
        "",
        None,
    ]


@pytest.fixture
def correct_bank_data() -> list[tuple[str, str]]:
    return [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ]


@pytest.fixture
def incorrect_bank_data() -> list[str | None]:
    return [
        "6442680986443212",
        "SomeText",
        "",
        None,
    ]


@pytest.fixture
def valid_date_type() -> list[tuple[str, str]]:
    return [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("0001-01-01T00:00:00", "01.01.0001"),
        ("9999-12-31T23:59:59", "31.12.9999"),
    ]


@pytest.fixture
def invalid_date_type() -> list[str]:
    return [
        "invalid-date",
        "",
    ]


@pytest.fixture
def filter_by_state_data() -> list[dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
