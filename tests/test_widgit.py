from src.widgit import mask_account_card, get_date
import pytest

@pytest.mark.parametrize('card_or_account_number, expected', [('Mastercard 1111222233334444', 'Mastercard 1111 22** **** 4444'), ('счет 11112222333344445555', 'счет **5555')])
def test_mask_account_card(card_or_account_number, expected):
    assert mask_account_card(card_or_account_number) == expected

@pytest.mark.parametrize('card_or_account_number, expected', [('Unknown type 1111222233334444', 'Введите корректный тип: visa, maestro, mastercard или счет'), ('11112222333344445555', 'Введите корректный тип и номер карты или номер счета'), ('', 'Введите корректный тип и номер карты или номер счета')])
def test_mask_account_card(card_or_account_number, expected):
    with pytest.raises(ValueError) as e:
        mask_account_card(card_or_account_number)
    assert str(e.value) == expected


def test_get_date():
    assert get_date('2024-03-11T02:26:18.671407') == '11.03.2024'

def test_get_date_if_no_date(capsys, empty_date):
    get_date(empty_date)
    captured = capsys.readouterr()
    assert "Отсутствует дата операции" in captured.out
    assert get_date(empty_date) is None
