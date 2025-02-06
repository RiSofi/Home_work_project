from typing import Union
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(full_bank_data: str) -> str:
    '''Функция обрабатывает поступившую информация как о картах, так и о счетах и возвращает строку с замаскированным номером'''
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


if __name__ == "__main__":
    test_data = ["Visa Platinum 8990922113665229",
"Visa Gold 5999414228426353",
"Счет 73654108430135874305"]
    for data in test_data:
        print(mask_account_card(data))




