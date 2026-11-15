from datetime import datetime
from functools import wraps


def log(filename=None):
    """Создаем декоратор для логирования работы функции"""
    def wrapper(func):
        """Создаем вспомогательную функцию для формирования замыкания"""
        @wraps(func)
        def inner(*args, **kwargs):
            """Создаем замыкание"""
            status = 'ok'
            error_message = ''
            result = None
            start_log_text = f'Начало работы функции {func.__name__}: {datetime.now()}'
            print(start_log_text)

            try:
                result = func(*args, **kwargs)
            except Exception as e:
                status = 'error'
                error_message = f'{type(e).__name__}: {e}'
            finally:
                finish_log_text = f'Окончание работы функции {func.__name__}: {datetime.now()}'
                status_log_text = f'{func.__name__} {status}: {error_message}'
                print(finish_log_text)
                print(status_log_text)
                if filename:
                    with open(f'{filename}', 'w', encoding='utf-8') as file:
                        file.write(f'{start_log_text}\n{finish_log_text}\n{status_log_text}')

            return result
        return inner
    return wrapper

# @log('log.txt')
# def add_two(n):
#     return n+2
#
# print(add_two(5))

