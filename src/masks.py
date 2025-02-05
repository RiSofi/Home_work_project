from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    card_str = str(card_number).replace(" ", "")
    # удаляем пробелы на случай передачи строки
    if len(card_str) != 16 or not card_str.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр")
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    account_str = str(account_number).replace(" ", "")
    # удаляем пробелы на случай передачи строки и преобразуем в строку
    if not account_str.isdigit():
        raise ValueError("Номер счета должен содержать только цифры.")
    if len(account_str) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры.")
    return "**" + account_str[-4:]
