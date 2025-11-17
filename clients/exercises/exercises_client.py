from httpx import Response

from clients.api_client import APIClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, GetExercisesRequestSchema, \
    UpdateExerciseRequestSchema, GetExerciseResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema


class ExerciseClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создание упражнения.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/exercises", json=request.model_dump(by_alias=True))

    def get_exercises_api(self, query: GetExercisesRequestSchema) -> Response:
        """
        Метод получения упражнений конкретного курса по его uuid.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url="/api/v1/exercises", params=query.model_dump(by_alias=True))

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

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления упражнения.

        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    def create_exercise(self, request: CreateExerciseRequestSchema) -> GetExerciseResponseSchema:
        response = self.create_exercise_api(request=request)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self, query: GetExercisesRequestSchema) -> GetExercisesRequestSchema:
        response = self.get_exercises_api(query=query)
        return GetExercisesRequestSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id=exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> GetExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return GetExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExerciseClient:
    """
    Фунция создает экземпляр ExerciseClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExerciseClient.
    """
    return ExerciseClient(client=get_private_http_client(user))
