import json


def load_operations(path):
    """
    Загружает список транзакций из JSON-файла.
    Если файл пустой, повреждён, не найден или содержит не список — возвращает пустой список.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Данные должны быть списком
        if isinstance(data, list):
            return data

        return []

    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return []


# if __name__ == "__main__":
#    ops = load_operations("/Users/mac/PycharmProjects/PythonProject/data/operations.json")
#    print(ops)
