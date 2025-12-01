from typing import Any


def assert_status_code(actual: int, expected: int):
    assert actual == expected, (
        f'Response status code {actual} does not match expected status code {expected}.'
    )


def assert_equal(actual: Any, expected: Any, name: str):
    assert actual == expected, (
        f'Incorrect value: {name}.\n'
        f'Actual: {actual}.\n'
        f'Expected: {expected}.\n'
    )


def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    assert actual, (
        f'Incorrect value: {name}.\n'
        f'Expected true value, but got: {actual}\n'
    )
