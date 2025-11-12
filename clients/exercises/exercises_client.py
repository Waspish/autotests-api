from typing import TypedDict

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
        return self.post(url="/api/v1/exercise", json=request)

    def get_exercises_api(self, query: GetExercisesRequestDict) -> Response:
        """
        Метод получения упражнений конкретного курса по его uuid.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url="/api/v1/exercise", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения по его идентификатору.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/exercise/{exercise_id}")

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения по его идентификатору.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/exercise/{exercise_id}")

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления упражнения.

        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"/api/v1/exercise/{exercise_id}", json=request)


def get_private_users_client(user: AuthenticationUserDict) -> ExerciseClient:
    """
    Фунция создает экземпляр ExerciseClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExerciseClient.
    """
    return ExerciseClient(client=get_private_http_client(user))
