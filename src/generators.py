from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Dict]], currency_code: str) -> Iterator[Dict[str, Dict]]:
    """Генератор, который возвращает транзакции с заданной валютой.
    Если таких транзакций нет, возвращает пустой итератор без ошибки.
    """
    filtered = (
        txn for txn in transactions if txn.get("operationAmount", {}).get("currency", {}).get("code") == currency_code
    )
    for txn in filtered:
        yield txn


def transaction_descriptions(transactions: List[Dict[str, str]]) -> Iterator[str]:
    """Генератор, возвращающий описание каждой транзакции."""
    for txn in transactions:
        yield txn.get("description", "Описание отсутствует")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, end + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[
            8:12
        ] + " " + f"{number:016d}"[12:]
