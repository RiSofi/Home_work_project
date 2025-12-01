import os

import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()


def convert_transaction_to_rub(transaction):
    """
    Принимает транзакцию и возвращает сумму в рублях.
    """
    try:
        # Берём сумму транзакции
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]

        print(f"Конвертируем: {amount} {currency} -> RUB")

        # Если рубли — конвертация не нужна
        if currency == "RUB":
            print("Валюта RUB, конвертация не требуется")
            return amount

        # Получаем API ключ из .env
        api_key = os.getenv("EXCHANGE_API_KEY")

        if not api_key:
            print("Ошибка: нет API ключа! Добавьте EXCHANGE_API_KEY в файл .env")
            return amount

        # URL для API apilayer
        url = "https://api.apilayer.com/exchangerates_data/convert"

        params = {"from": currency, "to": "RUB", "amount": amount}

        headers = {"apikey": api_key}

        print(f"Делаем запрос к API...")

        # Делаем запрос с таймаутом
        response = requests.get(url, params=params, headers=headers, timeout=10)

        print(f"Статус ответа: {response.status_code}")

        # Проверяем статус ответа
        if response.status_code != 200:
            print(f"Ошибка API: {response.status_code}")
            return amount

        # Получаем JSON-ответ
        data = response.json()

        # Проверяем наличие поля result
        if "result" not in data:
            print(f"Ошибка: нет поля 'result' в ответе API")
            return amount

        result = float(data["result"])
        print(f"Успешная конвертация: {amount} {currency} = {result} RUB")

        return result

    except requests.exceptions.Timeout:
        print("Таймаут запроса к API")
        return amount
    except requests.exceptions.ConnectionError as e:
        print(f"Ошибка соединения: {e}")
        return amount
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return amount
    except KeyError as e:
        print(f"Ошибка в структуре транзакции: отсутствует поле {e}")
        return 0
    except ValueError as e:
        print(f"Ошибка преобразования числа: {e}")
        return 0
    except Exception as e:
        print(f"Ошибка конвертации: {e}")
        return 0

    # if __name__ == "__main__":
    # Тестирование функции convert_transaction_to_rub


#    print("=== ТЕСТИРОВАНИЕ КОНВЕРТАЦИИ ВАЛЮТ ===")
#
# Тест 1: Транзакция в рублях (должна вернуть ту же сумму)
#    transaction_rub = {
#        "operationAmount": {
#            "amount": "1500",
#            "currency": {"code": "RUB"}
#        }
#    }
#    print("\n--- Тест 1: RUB валюта ---")
#    result1 = convert_transaction_to_rub(transaction_rub)
#    print(f"Результат: {result1} RUB")
#
# Тест 2: Транзакция в долларах (будет конвертировать через API)
#    transaction_usd = {
#        "operationAmount": {
#            "amount": "100",
#            "currency": {"code": "USD"}
#        }
#    }
#    print("\n--- Тест 2: USD валюта ---")
#    result2 = convert_transaction_to_rub(transaction_usd)
#    print(f"Результат: {result2} RUB")
#
# Тест с реальными данными из файла
#    print("\n" + "=" * 50)
#    print("ТЕСТ С РЕАЛЬНЫМИ ДАННЫМИ:")
#    try:
#        from src.utils.load_operations import load_operations
#
#        ops = load_operations("/Users/mac/PycharmProjects/PythonProject/data/operations.json")
#
#        if ops and len(ops) > 0:
#            print(f"Загружено операций: {len(ops)}")
# Протестируем первые 2 транзакции
#            for i in range(min(2, len(ops))):
#                print(f"\n--- Реальная транзакция {i + 1} ---")
#                result = convert_transaction_to_rub(ops[i])
#                print(f"Итоговая сумма: {result:.2f} RUB")
#        else:
#            print("Файл operations.json пуст или не найден")
#
#    except ImportError:
#        print("Модуль load_operations не найден")
#    except Exception as e:
#        print(f"Ошибка при загрузке данных: {e}")
