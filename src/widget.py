from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """Функция, маскирующая номер счета/карты"""
    card_number_split = card_number.split()
    if card_number_split[0] != "Счет":
        if len(card_number_split) < 3:
            return f'{card_number_split[0]} {get_mask_card_number(card_number_split[-1])}'
        else:
            return f'{card_number_split[0]} {card_number_split[1]} {get_mask_card_number(card_number_split[-1])}'
    else:
        return f'{card_number_split[0]} {get_mask_account(card_number_split[-1])}'


print(mask_account_card("Счет 73654108430135874305"))
