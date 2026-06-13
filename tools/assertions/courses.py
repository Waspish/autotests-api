from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, CourseSchema, \
    GetCourseResponseSchema, CreateCourseResponseSchema, GetCoursesResponseSchema, CreateCourseRequestSchema
from tools.assertions.base import assert_equal, assert_is_true, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user


def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
    Проверяет, что фактические данные курса соответствуют ожидаемым.

    :param actual: Фактические данные курса.
    :param expected: Ожидаемые данные курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, name='id')
    assert_equal(actual.title, expected.title, name='title')
    assert_equal(actual.description, expected.description, name='description')
    assert_equal(actual.min_score, expected.min_score, name='min_score')
    assert_equal(actual.max_score, expected.max_score, name='max_score')
    assert_equal(actual.estimated_time, expected.estimated_time, name='estimated_time')

    assert_file(actual.preview_file, expected.preview_file)
    assert_user(actual.created_by_user, expected.created_by_user)


def assert_get_course_response(create_course_response: CreateCourseResponseSchema,
                               get_course_response: GetCourseResponseSchema):
    """
    Проверяет, что ответ на получение курса соответствует ответу на его создание.

    :param get_course_response: Ответ API при запросе данных курса.
    :param create_course_response: Ответ API при создании курса.
    :raises AssertionError: Если данные файла не совпадают.
    """
    assert_course(expected=create_course_response.course, actual=get_course_response.course)


def assert_get_courses_response(create_course_responses: list[CreateCourseResponseSchema],
                                get_courses_response: GetCoursesResponseSchema):
    """
    Проверяет, что ответ на получение курсов соответствует ответам на их создание.

    :param get_courses_response: Ответ API при запросе данных курсов.
    :param create_course_responses: Ответ API при создании курсов.
    :raises AssertionError: Если данные файла не совпадают.
    """
    assert_length(actual=get_courses_response.courses, expected=create_course_responses, name="courses")

    for index, create_course_response in enumerate(create_course_responses):
        assert_course(actual=get_courses_response.courses[index], expected=create_course_response.course)


def assert_update_course_response(
        request: UpdateCourseRequestSchema,
        response: UpdateCourseResponseSchema,
        course_id: str
):
    """
    Проверяет, что ответ на обновление курса соответствует запросу.

    :param request: Исходный запрос на обновление курса.
    :param response: Ответ API с данными курса.
    :param course_id: Id курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.course.title, request.title, name='title')
    assert_equal(response.course.description, request.description, name='description')
    assert_equal(response.course.min_score, request.min_score, name='min_score')
    assert_equal(response.course.max_score, request.max_score, name='max_score')
    assert_equal(response.course.estimated_time, request.estimated_time, name='estimated_time')
    assert_equal(response.course.id, course_id, name='id')

    assert_is_true(response.course.created_by_user, name='created_by_user')
    assert_is_true(response.course.preview_file, name='created_by_user')


def assert_create_course_response(request: CreateCourseRequestSchema, response: CreateCourseResponseSchema):
    """
    Проверяет, что ответ на создание курса соответствует запросу.

    :param request: Исходный запрос на создание курса.
    :param response: Ответ API с данными курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.course.title, request.title, name='title')
    assert_equal(response.course.max_score, request.max_score, name='max_score')
    assert_equal(response.course.min_score, request.min_score, name='min_score')
    assert_equal(response.course.description, request.description, name='description')
    assert_equal(response.course.estimated_time, request.estimated_time, name='estimated_time')
    assert_equal(response.course.created_by_user.id, request.created_by_user_id, name='created_by_user_id')
    assert_equal(response.course.preview_file.id, request.preview_file_id, name='preview_file_id')

    assert_is_true(response.course.id, name='id')
