import logging
import os

import pytest

from src.decorators import log

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE_PATH = os.path.join(BASE_DIR, "test_mylog.txt")


@pytest.fixture(scope="session", autouse=True)
def clean_log_file():
    """Фикстура для очистки лога перед каждым тестом."""
    if os.path.exists(LOG_FILE_PATH):
        os.remove(LOG_FILE_PATH)


def test_add_success():
    """Тест успешного выполнения add(), проверка лога."""

    @log(filename=LOG_FILE_PATH)
    def add(a, b):
        return a + b

    result = add(2, 3)

    assert result == 5

    with open(LOG_FILE_PATH, "r", encoding="utf-8") as log_file:
        log_content = log_file.read()

    assert "Calling add with args: (2, 3), kwargs: {}" in log_content
    assert "add ok, result: 5" in log_content


def test_divide_success():
    """Тест успешного выполнения divide(), проверка лога."""

    @log(filename=LOG_FILE_PATH)
    def divide(a, b):
        return a / b

    result = divide(10, 2)

    assert result == 5.0

    with open(LOG_FILE_PATH, "r", encoding="utf-8") as log_file:
        log_content = log_file.read()

    assert "Calling divide with args: (10, 2), kwargs: {}" in log_content
    assert "divide ok, result: 5.0" in log_content


def test_divide_zero_error():
    """Тест обработки ошибки ZeroDivisionError, проверка лога."""

    @log(filename=LOG_FILE_PATH)
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    with open(LOG_FILE_PATH, "r", encoding="utf-8") as log_file:
        log_content = log_file.read()

    assert "Calling divide with args: (10, 0), kwargs: {}" in log_content
    assert "divide error: ZeroDivisionError" in log_content
