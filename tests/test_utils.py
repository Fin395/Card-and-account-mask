from unittest.mock import mock_open, patch

from src.utils import transactions_from_json


def test_get_transactions_success() -> None:
    """Тестирование корректного чтения файла"""
    mocked_open = mock_open(read_data='[{"id": 441945886, "state": "EXECUTED"}]')
    with patch("builtins.open", mocked_open):
        result = transactions_from_json("C:/Users/Sergei/PycharmProjects/MyProject/data/operations.json")
        assert result == [{"id": 441945886, "state": "EXECUTED"}]


def test_get_transactions_invalid_path() -> None:
    """Тестирование работы функции при ошибочно указанном пути к файлу"""
    assert transactions_from_json("C:/Users/Sergei/PycharmProjects/MyProject/operations.json") == []


def test_get_transactions_empty_file() -> None:
    """Тестирование корректного чтения файла"""
    mocked_open = mock_open(read_data=None)
    with patch("builtins.open", mocked_open):
        result = transactions_from_json("C:/Users/Sergei/PycharmProjects/MyProject/data/operations.json")
        assert result == []
