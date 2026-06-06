from http import HTTPStatus

import pytest

from clients.courses.courses_client import CourseClient
from clients.courses.courses_schema import CourseSchema, UpdateCourseRequestSchema, UpdateCourseResponseSchema, \
    GetCourseResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, assert_get_course_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.courses
class TestCourses:
    def test_update_course(self, function_course: CourseSchema, courses_client: CourseClient, ):
        request = UpdateCourseRequestSchema()
        response = courses_client.update_course_api(request=request, course_id=function_course.id)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(request=request, response=response_data)

        get_response = courses_client.get_course_api(response_data.course.id)
        get_response_data = GetCourseResponseSchema.model_validate_json(get_response.text)

        assert_get_course_response(create_course_response=response_data, get_course_response=get_response_data)

        validate_json_schema(response.json(), UpdateCourseResponseSchema.model_json_schema())
