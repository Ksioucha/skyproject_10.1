from typing import Any


def get_mask_card_number(card_number: Any) -> str:
    """Функция принимающая на вход номер карты и возвращающая ее маску"""
    if card_number.isdigit() and len(card_number) == 16:
        return card_number[:4] + " " + card_number[4:6] + "** ****" + card_number[-4:]
    else:
        return "Incorrect card number"


print(get_mask_card_number('1111222233334444'))


def get_mask_account(card_number: Any) -> str:
    """Функция, выводящая последние 4 цифры номера карты"""
    if card_number.isdigit() and len(card_number) == 16:
        return "**" + card_number[-4:]
    else:
        return "Incorrect card number"


print(get_mask_account('1111222233334444'))
