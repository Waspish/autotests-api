from typing import List

import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import ExerciseClient, get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CourseFicture
from fixtures.users import UserFixture


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema | List[CreateExerciseResponseSchema]

    @property
    def id(self) -> str:
        return self.response.exercise.id


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExerciseClient:
    return get_exercises_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(exercises_client: ExerciseClient, function_course: CourseFicture) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(course_id=function_course.id)
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)


@pytest.fixture
def function_three_exercises(
        exercises_client: ExerciseClient,
        function_course: CourseFicture,
) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(course_id=function_course.id)
    exercises_number = 3
    responses = []
    for _ in range(exercises_number):
        response = exercises_client.create_exercise(request)
        responses.append(response)

    return ExerciseFixture(request=request, response=responses)
