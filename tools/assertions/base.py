

def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому.

    :param actual: Фактический статус-код ответа.
    :param expected: Ожидаемый статус-код.
    :raises AssertionError: Если статус-коды не совпадают.
    """

    assert actual == expected, (
        'Некорректный статус код ответа'
        f'Ожидаемый статус код: {expected}'
        f'Возвращенный статус код: {actual}'
    )

def assert_equal(actual, expected, name):
    """
    Проверяет, что фактическое значение равно ожидаемому.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение.
    :raises AssertionError: Если фактическое значение не равно ожидаемому.
    """
    assert actual == expected, (
        f'Некорректное поле {name}'
        f'Ожидаемое значение: {expected}'
        f'Возвращенное значение: {actual}'
    )

def assert_is_true(actual, name):
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """

    assert actual, (
        f'Некорректное поле {name}'
        f'Ожидаемый статус True, но получен {actual}'
    )
