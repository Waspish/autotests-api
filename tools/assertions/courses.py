from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, CourseSchema, \
    GetCourseResponseSchema
from tools.assertions.base import assert_equal, assert_is_true


def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
    Проверяет, что фактические данные файла соответствуют ожидаемым.

    :param actual: Фактические данные файла.
    :param expected: Ожидаемые данные файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.title, expected.title, name='title')
    assert_equal(actual.description, expected.description, name='description')
    assert_equal(actual.min_score, expected.min_score, name='min_score')
    assert_equal(actual.max_score, expected.max_score, name='max_score')
    assert_equal(actual.estimated_time, expected.estimated_time, name='estimated_time')

    assert_is_true(actual.id, name='id')
    assert_is_true(actual.created_by_user, name='created_by_user')
    assert_is_true(actual.preview_file, name='created_by_user')


def assert_get_course_response(create_course_response: UpdateCourseResponseSchema,
                               get_course_response: GetCourseResponseSchema):
    """
    Проверяет, что ответ на получение курса соответствует ответу на его создание.

    :param get_course_response: Ответ API при запросе данных курса.
    :param create_course_response: Ответ API при создании курса.
    :raises AssertionError: Если данные файла не совпадают.
    """
    assert_course(expected=create_course_response.course, actual=get_course_response.course)


def assert_update_course_response(request: UpdateCourseRequestSchema, response: UpdateCourseResponseSchema):
    """
    Проверяет, что ответ на обновление курса соответствует запросу.

    :param request: Исходный запрос на обновление курса.
    :param response: Ответ API с данными курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.title, response.course.title, name='title')
    assert_equal(request.description, response.course.description, name='description')
    assert_equal(request.min_score, response.course.min_score, name='min_score')
    assert_equal(request.max_score, response.course.max_score, name='max_score')
    assert_equal(request.estimated_time, response.course.estimated_time, name='estimated_time')

    assert_is_true(response.course.id, name='id')
    assert_is_true(response.course.created_by_user, name='created_by_user')
    assert_is_true(response.course.preview_file, name='created_by_user')
