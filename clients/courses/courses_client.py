from httpx import Response

from clients.api_client import APIClient
from clients.courses.courses_schema import CreateCourseRequestSchema, GetCoursesQuerySchema, UpdateCourseRequestSchema, \
    CreateCourseResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema


class CourseClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Метод создание курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/courses", json=request.model_dump(by_alias=True))

    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод получения курсов конкретного пользователя по его uuid.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url="/api/v1/courses", params=query.model_dump(by_alias=True))

    def update_course_api(self, request: UpdateCourseRequestSchema, course_id: str) -> Response:
        """
        Метод обновления курса по его идентификатору.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"/api/v1/courses/{course_id}", json=request.model_dump(by_alias=True))

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса по его идентификатору.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/courses/{course_id}")

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса по его идентификатору.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)


def get_courses_client(user: AuthenticationUserSchema) -> CourseClient:
    """
    Фунция создает экземпляр CourseClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CourseClient.
    """
    return CourseClient(client=get_private_http_client(user))
