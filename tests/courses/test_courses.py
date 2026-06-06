from http import HTTPStatus

import pytest

from clients.courses.courses_client import CourseClient
from clients.courses.courses_schema import CourseSchema, UpdateCourseRequestSchema, UpdateCourseResponseSchema
from tools.assertions.courses import assert_update_course_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.courses
class TestCourses:
    def test_update_course(self, function_course: CourseSchema, courses_client: CourseClient):
        request = UpdateCourseRequestSchema()
        response = courses_client.update_course_api(request=request, course_id=function_course.id)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert response.status_code == HTTPStatus.OK
        assert_update_course_response(request=request, response=response_data)

        validate_json_schema(response.json(), UpdateCourseResponseSchema.model_json_schema())
