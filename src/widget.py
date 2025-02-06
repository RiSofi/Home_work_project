from datetime import datetime
from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(full_bank_data: Union[str]) -> str:
    """Функция обрабатывает поступившую информация как о картах,
    так и о счетах и возвращает строку с замаскированным номером"""
    first_word = full_bank_data.split()

    if first_word[0] == "Счет":
        # Если это счет, то он начинается со слова 'Счет'
        masked_number = get_mask_account(first_word[-1])
        # последнее слово - номер счета
        return f"Счет {masked_number}"
    else:
        # Если это не счет, то это карта
        masked_number = get_mask_card_number(first_word[-1])
        return " ".join(first_word[:-1]) + f" {masked_number}"


def get_date(date_string: Union[str]) -> str:
    """Функция принимает строку с датой и возвращает строку в формате ДД.ММ.ГГГГ"""
    dt = datetime.fromisoformat(date_string)
    # преобразует строку в объект datetime
    return dt.strftime("%d.%m.%Y")
    # форматирует в ДД.ММ.ГГГГ


# проверка работы функций
# if __name__ == "__main__":
#     test_data = ["Visa Platinum 8990922113665229",
# "Visa Gold 5999414228426353",
# "Счет 73654108430135874305"]
#     for data in test_data:
#         print(mask_account_card(data))
#
# print(get_date("2024-03-11T02:26:18.671407"))
