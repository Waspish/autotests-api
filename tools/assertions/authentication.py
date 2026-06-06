from tools.assertions.base import assert_equal, assert_is_true


def assert_login_response(response):
    """
    Проверяет, что ответ аутентификации содержит корректные поля:
    тип токена 'bearer', а также непустые access_token и refresh_token.


    :param response: Ответ API с данными токена.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.token.token_type, 'bearer', 'token_type')
    assert_is_true(response.token.access_token, 'access_token')
    assert_is_true(response.token.refresh_token, 'refresh_token')
