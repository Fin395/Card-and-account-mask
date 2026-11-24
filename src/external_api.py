import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_transaction_amount(transaction: dict) -> float:
    """Через внешний API получаем текущий курс валют и конвертируем сумму операции в рубли"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        transaction_amount = transaction["operationAmount"]["amount"]
    else:
        url = "https://api.apilayer.com/exchangerates_data/convert"

        payload = {
            "amount": transaction["operationAmount"]["amount"],
            "from": transaction["operationAmount"]["currency"]["code"],
            "to": "RUB",
        }
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers, params=payload)
        if response.status_code != 200:
            raise RuntimeError(f"API вернул {response.status_code}: {response.text[:200]}")

        try:
            transaction_amount = response.json()["result"]
        except requests.exceptions.JSONDecodeError:
            raise RuntimeError(f"Ответ не JSON: {response.text[:200]}")
    return transaction_amount


transaction = {
    "id": 390558607,
    "state": "EXECUTED",
    "date": "2019-02-12T00:08:07.524972",
    "operationAmount": {"amount": "16796.95", "currency": {"name": "USD", "code": "USD"}},
}

print(get_transaction_amount(transaction))
