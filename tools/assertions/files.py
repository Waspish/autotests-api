from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, FileSchema, \
    GetFileResponseSchema
from tools.assertions.base import assert_equal, assert_is_true
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response


def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
    Проверяет, что ответ на создание файла соответствует запросу.

    :param request: Исходный запрос на создание файла.
    :param response: Ответ API с данными файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    # Формируем ожидаемую ссылку на загруженный файл
    expected_url = f'http://localhost:8000/static/{request.directory}/{request.filename}'

    assert_equal(response.file.directory, request.directory, 'directory')
    assert_equal(response.file.filename, request.filename, 'filename')
    assert_equal(str(response.file.url), expected_url, 'url')
    assert_is_true(response.file.id, 'id')


def assert_file(actual: FileSchema, expected: FileSchema):
    """
    Проверяет, что фактические данные файла соответствуют ожидаемым.

    :param actual: Фактические данные файла.
    :param expected: Ожидаемые данные файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, 'id')
    assert_equal(actual.filename, expected.filename, 'filename')
    assert_equal(actual.url, expected.url, 'url')
    assert_equal(actual.directory, expected.directory, 'directory')


def assert_get_file_response(create_file_response: CreateFileResponseSchema, get_file_response: GetFileResponseSchema):
    """
    Проверяет, что ответ на получение файла соответствует ответу на его создание.

    :param get_file_response: Ответ API при запросе данных файла.
    :param create_file_response: Ответ API при создании файла.
    :raises AssertionError: Если данные файла не совпадают.
    """
    assert_file(expected=create_file_response.file, actual=get_file_response.file)


def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем файла соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type='string_too_short',
                location=["body", "filename"],
                message="String should have at least 1 character",
                input="",
                context={"min_length": 1}
            )
        ]
    )

    assert_validation_error_response(actual=actual, expected=expected)


def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым значением директории соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type='string_too_short',
                location=["body", "directory"],
                message="String should have at least 1 character",
                input="",
                context={"min_length": 1}
            )
        ]
    )

    assert_validation_error_response(actual=actual, expected=expected)


def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если файл не найден на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "File not found"
    """
    # Ожидаемое сообщение об ошибке, если файл не найден
    expected = InternalErrorResponseSchema(details="File not found")
    # Используем ранее созданную функцию для проверки внутренней ошибки
    assert_internal_error_response(actual=actual, expected=expected)


def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на получение файла с некорретным значением id соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type='uuid_parsing',
                location=["path", "file_id"],
                message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` "
                        "followed by [0-9a-fA-F-], found `i` at 1",
                input="incorrect-file-id",
                context={
                    "error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], "
                             "found `i` at 1"}
            )
        ]
    )

    assert_validation_error_response(actual=actual, expected=expected)
