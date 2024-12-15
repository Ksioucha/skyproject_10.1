def get_mask_card_number(card_number: str) -> str:
    """Функция принимающая на вход номер карты и возвращающая ее маску"""
    if card_number.isdigit() and len(card_number) == 16:
        return card_number[:4] + " " + card_number[4:6] + "** ****" + card_number[-4:]
    else:
        return "Incorrect card number"


print(get_mask_card_number('1111222233334444'))


def get_mask_account(card_number: str) -> str:
    """Функция, выводящая последние 4 цифры номера карты"""
    if card_number.isdigit() and len(card_number) == 20:
        return "**" + card_number[-4:]
    else:
        return "Incorrect card number"


print(get_mask_account('11112222333344445555'))


def get_date(date_month_year: str) -> str:
    """Функция для получения корректного формата даты"""
    return date_month_year[8:10] + '.' + date_month_year[5:7] + '.' + date_month_year[0:4]


print(get_date("2024-03-11T02:26:18.671407"))
