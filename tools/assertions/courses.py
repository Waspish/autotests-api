from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema
from tools.assertions.base import assert_equal, assert_is_true


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
