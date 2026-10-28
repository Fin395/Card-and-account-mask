from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_account_or_card_number: str) -> str:
    """Функция возвращает замаскированный номер карты/счета"""
    splitted_number = type_and_account_or_card_number.strip().split(" ")

    if len(splitted_number) not in [2, 3]:
        raise ValueError("Введите корректный тип и номер карты или номер счета")

    card_type = splitted_number[0]
    number_part = splitted_number[-1]

    if card_type.lower() not in ["visa", "maestro", "счет", "mastercard"]:
        raise ValueError("Введите корректный тип: visa, maestro, mastercard или счет")

    if card_type.lower() == "счет":
        masked_account = get_mask_account(number_part)
        return f"{card_type} {masked_account}"

    else:
        masked_card = get_mask_card_number(number_part)
        return f"{card_type} {masked_card}"



      # while True:
    #     splitted_input = type_and_account_or_card_number.strip().split(" ")
    #
    #     if len(splitted_input) != 2:
    #         type_and_account_or_card_number = input("Введите корректный тип и номер карты или номер счета:\n")
    #         continue
    #
    #     card_type = splitted_input[0]
    #     number_part = splitted_input[-1]
    #
    #     if card_type.lower() not in ["visa", "maestro", "счет", "mastercard"]:
    #         type_and_account_or_card_number = input("Введите корректный тип: visa, maestro, mastercard или счет:\n")
    #         continue
    #
    #     if not number_part.isdigit():
    #         type_and_account_or_card_number = input(
    #             "Номер карты или счета должен состоять только из цифр. Введите корректный номер:\n"
    #         )
    #         continue
    #
    #     if card_type == "счет":
    #         if len(splitted_input) == 2 and len(number_part) == 20:
    #             masked_account = get_mask_account(number_part)
    #             return f"{card_type} {masked_account}"
    #         else:
    #             type_and_account_or_card_number = input(
    #                 "Номер счета должен состоять из 20 цифр. Введите корректный номер счета:\n"
    #             )
    #             continue
    #     else:
    #         if len(number_part) == 16:
    #             masked_card = get_mask_card_number(number_part)
    #             return f"{card_type} {masked_card}"
    #         else:
    #             type_and_account_or_card_number = input(
    #                 "Номер карты должен состоять из 16 цифр. Введите корректный номер карты:\n"
    #             )
    #             continue


def get_date(date: str) -> str:
    """Функция преобразует дату в формат 'DD.MM.YYYY'"""
    fixed_date = None

    try:
        if date:
            date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
            fixed_date = date.strftime("%d.%m.%Y")
        else:
            raise ValueError('Не указана дата операции')
    except ValueError:
        print('Отсутствует дата операции')
    finally:
        return fixed_date

if __name__ == "__main__":
    print(get_date("-07-03T18:35:29.512364"))

    print(mask_account_card('счет 11111111111111111111'))

# def validate_and_parse(raw: str):
#     """
#     Только валидация и разбор. Не делает input.
#     Возвращает (is_valid, error_message, card_type, number)
#     """
#     splitted = raw.strip().split()
#
#     if len(splitted) < 2:
#         return False, "Введите тип и номер: например, 'visa 1234...' или 'счет 123...'", None, None
#
#     card_type = splitted[0].lower()
#     number_part = splitted[-1]  # берём последнее слово как номер
#
#     allowed_types = {"visa", "maestro", "mastercard", "счет"}
#     if card_type not in allowed_types:
#         return False, f"Неверный тип. Допустимые: {', '.join(allowed_types)}.", None, None
#
#     if not number_part.isdigit():
#         return False, "Номер должен содержать только цифры.", None, None
#
#     if card_type == "счет":
#         if len(number_part) != 20:
#             return False, "Номер счёта должен состоять ровно из 20 цифр.", None, None
#         return True, None, card_type, number_part
#     else:
#         # карта: visa/maestro/mastercard
#         if len(number_part) != 16:
#             return False, "Номер карты должен состоять ровно из 16 цифр.", None, None
#         return True, None, card_type, number_part
#
#
# def mask_account_card(raw_input: str) -> str:
#     """
#     Эта функция теперь только про маскирование. Валидацию делает validate_and_parse.
#     """
#     is_valid, error, card_type, number = validate_and_parse(raw_input)
#     if not is_valid:
#         raise ValueError(error)
#
#     if card_type == "счет":
#         masked = get_mask_account(number)
#         return f"счет {masked}"
#     else:
#         masked = get_mask_card_number(number)
#         return f"{card_type} {masked}"


# if __name__ == "__main__":
#     while True:
#         user_input = input("Введите тип и номер карты или номер счёта:\n")
#
#         try:
#             result = mask_account_card(user_input)
#             print(result)
#             break  # всё ок, выходим из цикла
#         except ValueError as e:
#             print(e)
#             # continue не нужен: цикл просто продолжится и снова попросит ввод
