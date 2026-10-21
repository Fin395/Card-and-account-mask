from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(type_and_account_or_card_number: str) -> str:
    """Функция возвращает замаскированный номер карты/счета"""
    while True:
        splitted_input = type_and_account_or_card_number.strip().split(' ')

        if len(splitted_input) !=2:
            type_and_account_or_card_number = input('Введите корректный тип и номер карты или номер счета:\n')
            continue

        card_type = splitted_input[0]
        number_part = splitted_input[-1]


        if card_type.lower() not in ['visa', 'maestro', 'счет', 'mastercard']:
           type_and_account_or_card_number = input('Введите корректный тип: visa, maestro, mastercard или счет:\n')
           continue

        if not number_part.isdigit():
            type_and_account_or_card_number = input('Номер карты или счета должен состоять только из цифр. Введите корректный номер:\n')
            continue

        if card_type == 'счет':
            if len(splitted_input) == 2 and len(number_part) == 20:
                masked_account = get_mask_account(number_part)
                return f'{card_type} {masked_account}'
            else:
                type_and_account_or_card_number = input('Номер счета должен состоять из 20 цифр. Введите корректный номер счета:\n')
                continue
        else:
            if len(number_part) == 16:
                masked_card = get_mask_card_number(number_part)
                return f'{card_type} {masked_card}'
            else:
                type_and_account_or_card_number = input('Номер карты должен состоять из 16 цифр. Введите корректный номер карты:\n')
                continue

if __name__ == "__main__":

    user_input = input("Введите тип и номер карты или номер счёта:\n")
    print(mask_account_card(user_input))
