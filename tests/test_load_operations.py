import json
from unittest.mock import mock_open, patch
from src.utils.load_operations import load_operations


def test_load_operations_valid_json():
    """Корректный список — должен вернуться список"""

    fake_json = '[{"id": 1, "amount": 100}]'

    with patch("builtins.open", mock_open(read_data=fake_json)):
        with patch("json.load", return_value=[{"id": 1, "amount": 100}]):
            result = load_operations("fake_path.json")

    assert result == [{"id": 1, "amount": 100}]


def test_load_operations_empty_file():
    """Пустой файл → должно вернуться []"""

    with patch("builtins.open", mock_open(read_data="")):
        with patch("json.load", side_effect=json.JSONDecodeError("msg", "doc", 0)):
            result = load_operations("fake.json")

    assert result == []


def test_load_operations_not_list():
    """JSON содержит не список → []"""

    fake_json = '{"id": 1}'

    with patch("builtins.open", mock_open(read_data=fake_json)):
        with patch("json.load", return_value={"id": 1}):
            result = load_operations("fake.json")

    assert result == []


def test_load_operations_file_not_found():
    """Файл не найден → []"""

    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_operations("missing.json")

    assert result == []
