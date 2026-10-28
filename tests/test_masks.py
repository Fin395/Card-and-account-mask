from src.masks import get_mask_card_number, get_mask_account
import pytest


@pytest.mark.parametrize('card_number, expected', [
    ('7777888899994444', '7777 88** **** 4444')])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize('card_number, expected', [
    ('777788889999444', 'Номер карты должен состоять из 16 цифр'), ('777788889999444д', 'Номер карты должен состоять из 16 цифр')])
def test_get_mask_card_number_wrong_length_and_symbols(card_number, expected):
    with pytest.raises(ValueError) as e:
        get_mask_card_number(card_number)
    assert str(e.value) == expected


@pytest.mark.parametrize('account_number, expected', [
    ('77778888999944443333', '**3333')])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize('account_number, expected', [
    ('777788889999444', 'Номер счета должен состоять из 20 цифр'), ('77778888999944443333222д', 'Номер счета должен состоять из 20 цифр')])
def test_get_mask_account_wrong_length_and_symbols(account_number, expected):
    with pytest.raises(ValueError) as e:
        get_mask_account(account_number)
    assert str(e.value) == expected
