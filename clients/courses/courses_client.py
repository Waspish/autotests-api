from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CourseClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    class CreateCourseRequestDict(TypedDict):
        """
        Описание структуры запроса на создание курса.
        """
        title: str
        maxScore: int
        minScore: int
        description: str
        estimatedTime: str
        previewFileId: str
        createdByUserId: str

    class UpdateCourseRequestDict(TypedDict):
        """
        Описание структуры запроса на обновление курса.
        """
        title: str | None
        maxScore: str | None
        minScore: str | None
        description: str | None
        estimatedTime: str | None

    class GetCoursesQueryDict(TypedDict):
        """
        Описание структуры запроса на получение курса.
        """
        userId: str

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Метод создание курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/courses", json=request)

    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Метод получения курсов конкретного пользователя по его uuid.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url="/api/v1/courses", params=query)

    def update_course_api(self, request: UpdateCourseRequestDict, course_id: str) -> Response:
        """
        Метод обновления курса по его идентификатору.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"/api/v1/courses/{course_id}", json=request)

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
