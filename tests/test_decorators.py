from src.decorators import log


def test_log_return():
    """Проверяем, что декоратор корректно возвращает результат работы функции"""
    @log()
    def add_two(x):
        """Создаем функцию для проверки работы декоратора"""
        return x+2

    result = add_two(2)
    assert result == 4

def test_log_capture(capsys):
    """Проверяем вывод результата работы функции в консоль при отсутствии файла"""
    @log()
    def add_two(x):
        """Создаем функцию для проверки работы декоратора"""
        return x+2

    add_two(2)
    captured = capsys.readouterr()
    assert 'add_two ok' in captured.out

def test_log_in_file():
    """Проверка записи результата работы функции в файл"""
    @log('my_file.txt')
    def add_two(x):
        """Создаем функцию для проверки работы декоратора"""
        return x + 2

    add_two(2)

    with open('my_file.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    assert 'add_two ok' in content

def test_log_console_if_exception(capsys):
    """Проверяем вывод ошибки в консоль"""
    @log('my_file.txt')
    def add_two(x):
        """Создаем функцию для проверки работы декоратора"""
        return x + 2

    add_two('2')
    captured = capsys.readouterr()
    assert 'add_two error' in captured.out
    assert 'TypeError' in captured.out
