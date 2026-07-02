import allure

from tools.assertions.base import assert_equal, assert_is_true
from tools.logger import get_logger

logger = get_logger("AUTHENTICATION_ASSERTIONS")


@allure.step("Check login response")
def assert_login_response(response):
    """
    Проверяет, что ответ аутентификации содержит корректные поля:
    тип токена 'bearer', а также непустые access_token и refresh_token.


    :param response: Ответ API с данными токена.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check login response")

    assert_equal(response.token.token_type, 'bearer', 'token_type')
    assert_is_true(response.token.access_token, 'access_token')
    assert_is_true(response.token.refresh_token, 'refresh_token')
