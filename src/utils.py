import json
from json import JSONDecodeError


def transactions_from_json(path_to_file: str) -> list[dict]:
    """Функция через путь до JSON-файла возвращает список финансовых транзакций"""
    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            transactions = json.load(file)
            return transactions
    except JSONDecodeError:
        print("Не удалось открыть файл")
        return []
    except FileNotFoundError:
        print("Файл не найден")
        return []
