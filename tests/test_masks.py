from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7000552279664064", "7000 55** **** 4064"),
        ("1234567812345678", "1234 56** **** 5678"),
        ("5434567829847592", "5434 56** **** 7592"),
    ],
)
def test_get_mask_card_number_valid(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "card_number",
    [
        "1234 5678 1234",
        "abcd567812345678",
        "abcdkasdjnbgjbhg",
        "12345678123456789",
        "2738469" "",
        " ",
        None,
    ],
)
def test_get_mask_card_number_invalid(card_number: Any) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("27592747582", "**7582"),
        ("8372605816948251", "**8251"),
        ("454305", "**4305"),
    ],
)
def test_get_mask_account_valid(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "account_number",
    [
        "hpr65324092356",
        "abcdkasdjnbgjbhg",
        "323",
        "1834",
        "83749",
        "1",
        "",
        " ",
        None,
    ],
)
def test_get_mask_account_invalid(account_number: int | str) -> None:
    with pytest.raises(ValueError):
        get_mask_account(account_number)
