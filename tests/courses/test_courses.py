from http import HTTPStatus

import pytest

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, GetCoursesQuerySchema, \
    GetCoursesResponseSchema, CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.courses import CourseFicture
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, assert_get_courses_response, \
    assert_create_course_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.courses
class TestCourses:
    def test_get_courses(self, courses_client: CoursesClient, function_course: CourseFicture,
                         function_user: UserFixture):
        request = GetCoursesQuerySchema(user_id=function_user.id)
        response = courses_client.get_courses_api(request)
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response([function_course.response], response_data)

        validate_json_schema(response.json(), GetCoursesResponseSchema.model_json_schema())

    def test_get_three_courses(self, courses_client: CoursesClient, function_three_courses: CourseFicture,
                               function_user: UserFixture):
        request = GetCoursesQuerySchema(user_id=function_user.id)
        response = courses_client.get_courses_api(request)
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response([*function_three_courses.response], response_data)

        validate_json_schema(response.json(), GetCoursesResponseSchema.model_json_schema())

    def test_update_course(self, function_course: CourseFicture, courses_client: CoursesClient):
        request = UpdateCourseRequestSchema()
        response = courses_client.update_course_api(request=request, course_id=function_course.id)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(request=request, response=response_data, course_id=function_course.id)

        validate_json_schema(response.json(), UpdateCourseResponseSchema.model_json_schema())

    def test_create_course(self, courses_client: CoursesClient, function_file: FileFixture,
                           function_user: UserFixture):
        request = CreateCourseRequestSchema(created_by_user_id=function_user.id, preview_file_id=function_file.id)
        response = courses_client.create_course_api(request=request)
        response_data = CreateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_course_response(request=request, response=response_data)

        validate_json_schema(response.json(), CreateCourseResponseSchema.model_json_schema())
