import allure

from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema
from clients.users.users_schema import CreateUserResponseSchema, UserSchema, \
    GetUserResponseSchema, CreateUserRequestSchema
from tools.assertions.base import assert_equal, assert_is_true
from tools.assertions.errors import assert_validation_error_response
from tools.logger import get_logger

logger = get_logger("USERS_ASSERTIONS")


@allure.step("Check user")
def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверяет, что фактические данные пользователя соответствуют ожидаемым.

    :param actual: Фактические данные пользователя.
    :param expected: Ожидаемые данные пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check user response")

    assert_equal(actual.email, expected.email, 'email')
    assert_equal(actual.first_name, expected.first_name, 'first_name')
    assert_equal(actual.last_name, expected.last_name, 'last_name')
    assert_equal(actual.middle_name, expected.middle_name, 'middle_name')
    assert_is_true(actual.id, 'user_id')


@allure.step("Check get user response")
def assert_get_user_response(
        get_user_response: GetUserResponseSchema,
        create_user_response: CreateUserResponseSchema
):
    """
    Проверяет, что ответ на получение пользователя соответствует ответу на его создание.

    :param get_user_response: Ответ API при запросе данных пользователя.
    :param create_user_response: Ответ API при создании пользователя.
    :raises AssertionError: Если данные файла не совпадают.
    """
    logger.info("Check get user response")

    assert_user(get_user_response.user, create_user_response.user)


@allure.step("Check create user response")
def assert_create_user_response(
        request: CreateUserRequestSchema,
        response: CreateUserResponseSchema
):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check create user response")

    assert_is_true(response.user.id, 'user_id')
    assert_equal(response.user.email, request.email, 'email')
    assert_equal(response.user.first_name, request.first_name, 'first_name')
    assert_equal(response.user.last_name, request.last_name, 'last_name')
    assert_equal(response.user.middle_name, request.middle_name, 'middle_name')


@allure.step("Check get user with incorrect user id response")
def assert_get_user_with_incorrect_user_id_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на получение пользователя с некорректным значением id
    соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Check get user with incorrect user id response")

    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type='uuid_parsing',
                location=["path", "user_id"],
                message="Input should be a valid UUID, invalid character: "
                        "expected an optional prefix of `urn:uuid:` "
                        "followed by [0-9a-fA-F-], found `i` at 1",
                input="incorrect-user-id",
                context={
                    "error": "invalid character: expected an optional prefix "
                             "of `urn:uuid:` followed by [0-9a-fA-F-], "
                             "found `i` at 1"
                }
            )
        ]
    )

    assert_validation_error_response(actual=actual, expected=expected)
