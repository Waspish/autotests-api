import pytest
from pydantic import BaseModel

from clients.courses.courses_client import CourseClient, get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture


class CourseFicture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema

    @property
    def id(self) -> str:
        return self.response.course.id


@pytest.fixture
def courses_client(function_user: UserFixture) -> CourseClient:
    return get_courses_client(function_user.authentication_user)


@pytest.fixture
def function_course(
        courses_client: CourseClient,
        function_file: FileFixture,
        function_user: UserFixture
) -> CourseFicture:
    request = CreateCourseRequestSchema(created_by_user_id=function_user.id, preview_file_id=function_file.id)
    response = courses_client.create_course(request)
    return CourseFicture(request=request, response=response)
