import pytest
from unittest.mock import patch, Mock
from src.utils.external_api import convert_transaction_to_rub


def test_convert_rub_no_api_call():
    """Если валюта RUB — API не вызывается, сумма возвращается как есть"""
    transaction = {
        "operationAmount": {
            "amount": "1500",
            "currency": {"code": "RUB"}
        }
    }

    result = convert_transaction_to_rub(transaction)

    assert result == 1500.0


@patch("src.utils.external_api.requests.get")
@patch("src.utils.external_api.os.getenv")
def test_convert_usd_success(mock_getenv, mock_get):
    """Успешная конвертация USD → RUB через API"""

    # Мок переменной окружения
    mock_getenv.return_value = "FAKE_API_KEY"

    # Мок ответа API
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 9000.5}
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }

    result = convert_transaction_to_rub(transaction)

    assert result == 9000.5
    mock_get.assert_called_once()


@patch("src.utils.external_api.requests.get")
@patch("src.utils.external_api.os.getenv")
def test_convert_api_error(mock_getenv, mock_get):
    """Ошибка API → функция возвращает исходную сумму"""

    mock_getenv.return_value = "FAKE_API_KEY"

    mock_response = Mock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "200",
            "currency": {"code": "USD"}
        }
    }

    result = convert_transaction_to_rub(transaction)

    assert result == 200.0


@patch("src.utils.external_api.os.getenv")
def test_missing_api_key(mock_getenv):
    """Нет API ключа → возвращается исходная сумма"""

    mock_getenv.return_value = None

    transaction = {
        "operationAmount": {
            "amount": "50",
            "currency": {"code": "USD"}
        }
    }

    result = convert_transaction_to_rub(transaction)

    assert result == 50.0
