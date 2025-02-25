import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card(correct_bank_data: list[tuple[str, str]]) -> None:
    for input_data, expected_output in correct_bank_data:
        assert mask_account_card(input_data) == expected_output


@pytest.mark.parametrize(
    "input_data",
    [
        "6442680986443212",
        "SomeText",
        "",
        None,
    ],
)
def test_mask_account_card_invalid(input_data: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(input_data)


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("0001-01-01T00:00:00", "01.01.0001"),
        ("9999-12-31T23:59:59", "31.12.9999"),
    ],
)
def test_case(date_string: str, expected: str) -> None:
    result = get_date(date_string)
    assert result == expected


# Тест для обработки некорректных строк
@pytest.mark.parametrize(
    "invalid_date_string",
    [
        "invalid-date",
        "",
    ],
)
def test_invalid_date(invalid_date_string: str) -> None:
    with pytest.raises(ValueError):
        get_date(invalid_date_string)


# Тест для обработки строк с пробелами и лишними символами
def test_non_standard_format() -> None:
    date_string = " 2024-03-11T02:26:18.671407 "
    result = get_date(date_string.strip())
    assert result == "11.03.2024"
