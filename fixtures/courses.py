from typing import List

import pytest
from pydantic import BaseModel

from clients.courses.courses_client import CoursesClient, get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture


class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema

    @property
    def id(self) -> str:
        return self.response.course.id


class CoursesFixture(BaseModel):
    request: List[CreateCourseRequestSchema]
    response: List[CreateCourseResponseSchema]


@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(function_user.authentication_user)


@pytest.fixture
def function_course(
        courses_client: CoursesClient,
        function_file: FileFixture,
        function_user: UserFixture
) -> CourseFixture:
    request = CreateCourseRequestSchema(created_by_user_id=function_user.id, preview_file_id=function_file.id)
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)


@pytest.fixture
def function_three_courses(
        courses_client: CoursesClient,
        function_file: FileFixture,
        function_user: UserFixture
) -> CoursesFixture:
    courses_number = 3
    responses = []
    requests = []
    for _ in range(courses_number):
        request = CreateCourseRequestSchema(created_by_user_id=function_user.id, preview_file_id=function_file.id)
        response = courses_client.create_course(request)
        requests.append(request)
        responses.append(response)

    return CoursesFixture(request=requests, response=responses)
