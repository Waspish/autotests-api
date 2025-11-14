from typing import TypedDict, List

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения для курса.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения из курса.
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на получение упражнений из курса.
    """
    courseId: str


class Exercise(TypedDict):
    """
    Описание структуры упражнения.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа на список упражнений из курса.
    """
    exercises: List[Exercise]


class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на упражнение из курса.
    """
    exercise: Exercise


class ExerciseClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создание упражнения.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/exercises", json=request)

    def get_exercises_api(self, query: GetExercisesRequestDict) -> Response:
        """
        Метод получения упражнений конкретного курса по его uuid.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url="/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения по его идентификатору.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/exercises/{exercise_id}")

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения по его идентификатору.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/exercises/{exercise_id}")

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления упражнения.

        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"/api/v1/exercises/{exercise_id}", json=request)

    def create_exercise(self, request: CreateExerciseRequestDict) -> GetExercisesResponseDict:
        response = self.create_exercise_api(request=request)
        return response.json()

    def get_exercises(self, query: GetExercisesRequestDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query=query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        response = self.get_exercise_api(exercise_id=exercise_id)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> GetExerciseResponseDict:
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return response.json()


def get_exercise_client(user: AuthenticationUserDict) -> ExerciseClient:
    """
    Фунция создает экземпляр ExerciseClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExerciseClient.
    """
    return ExerciseClient(client=get_private_http_client(user))
