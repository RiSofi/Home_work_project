from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция фильтрует список словарей по значению ключа 'state'"""
    result = []
    # создаем пустой список для хранения отфильтрованных данных
    for item in data:
        if "state" in item and item["state"] == state:
            # проверяем, есть ли ключ 'state' и равен ли он нужному значению
            result.append(item)
            # добавляем словарь в новый список, если он подходит
    return result


# Пример входных данных
# transactions = [
#     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
# ]

# Проверка функции
# print(filter_by_state(transactions))  # По умолчанию ищет 'EXECUTED'


def sort_by_date(data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """Функция сортирует список словарей по ключу 'date' возвращает список,
    отсортированный по дате (сортировка по умолчанию - убывание)"""
    return sorted(data, key=lambda item: datetime.fromisoformat(item["date"]), reverse=descending)


# Пример входных данных
# transactions = [
#     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
# ]

# Проверка функции
# print(sort_by_date(transactions))  # По умолчанию сортировка по убыванию
# print(sort_by_date(transactions, descending=False))  # Сортировка по возрастанию
