def filter_by_state(operations: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция фильтрует операции по статусу"""
    filtered_operations = [operation for operation in operations if operation['state'] == state ]
    return filtered_operations


def sort_by_date(bank_operations: list[dict], reverse: bool = True) -> list[dict]:
    """Функция сортирует операции по дате"""
    sorted_operations = sorted(bank_operations, key=lambda x: x['date'], reverse=reverse)
    return sorted_operations

