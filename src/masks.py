def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    card_number_as_list = list(card_number)
    for index, digit in enumerate(card_number_as_list):
        if index in range(6, 12):
            card_number_as_list[index] = "*"
    masked_card_number_as_str = "".join(card_number_as_list)
    with_space = " ".join(masked_card_number_as_str[i : i + 4] for i in range(0, 16, 4))
    return with_space


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    account_number_as_list = list(account_number)
    sliced_account_number_as_list = account_number_as_list[len(account_number_as_list) - 6 :]
    for index, digit in enumerate(sliced_account_number_as_list):
        if index in [0, 1]:
            sliced_account_number_as_list[index] = "*"
    return "".join(sliced_account_number_as_list)
