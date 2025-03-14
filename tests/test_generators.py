import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_existing_currency(transactions):
    """Тест на выборку транзакций в USD."""
    result = list(filter_by_currency(transactions, "USD"))
    expected = [transactions[0], transactions[1], transactions[3]]
    assert result == expected


def test_filter_missing_currency(transactions):
    """Тест на случай, когда транзакции в указанной валюте отсутствуют."""
    result = list(filter_by_currency(transactions, "JPY"))
    assert result == []


def test_empty_list():
    """Тест на случай, когда список транзакций пустой."""
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_partial_missing_keys():
    """Тест на транзакции с отсутствующими ключами 'operationAmount' или 'currency'."""
    broken_transactions = [
        {"id": 4, "state": "EXECUTED", "date": "2023-01-04T13:00:00"},
        {
            "id": 5,
            "state": "EXECUTED",
            "date": "2023-01-05T14:00:00",
            "operationAmount": {"amount": "400.00"},  # Нет currency
        },
    ]
    result = list(filter_by_currency(broken_transactions, "USD"))
    assert result == []


def test_transaction_descriptions(transactions):
    """Проверка корректного вывода описаний."""
    result = list(transaction_descriptions(transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert result == expected


def test_missing_description():
    """Проверка на случай отсутствия ключа 'description'."""
    transactions = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2},  # Нет description
        {"id": 3, "description": "Оплата услуг"},
    ]

    result = list(transaction_descriptions(transactions))
    expected = ["Перевод организации", "Описание отсутствует", "Оплата услуг"]

    assert result == expected


def test_empty_list_descriptions():
    """Проверка на пустой список транзакций."""
    result = list(transaction_descriptions([]))
    assert result == []


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"]),
    ],
)
def test_card_number_generator(start, end, expected):
    """Проверяет, что генератор выдает номера карт в заданном диапазоне и корректно их форматирует."""
    assert list(card_number_generator(start, end)) == expected


@pytest.mark.parametrize(
    "start, end",
    [
        (0, 0),  # Граничный случай: минимальное значение
        (1016 - 1, 1016 - 1),  # Граничный случай: максимальное 16-значное число
    ],
)
def test_card_number_generator_edge_cases(start, end):
    """Проверяет корректность обработки крайних значений."""
    generated = list(card_number_generator(start, end))
    assert len(generated) == 1
    assert all(len(card) == 19 for card in generated)  # Проверка формата XXXX XXXX XXXX XXXX


@pytest.mark.parametrize(
    "start, end",
    [
        (5, 1),  # Некорректный диапазон: start > end
        (0, -5),  # Отрицательный диапазон
    ],
)
def test_card_number_generator_invalid_range(start, end):
    """Проверяет, что генератор корректно завершает работу при некорректном диапазоне."""
    assert list(card_number_generator(start, end)) == []
