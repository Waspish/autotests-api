import allure
from httpx import Response

from clients.api_client import APIClient
from clients.courses.courses_schema import CreateCourseRequestSchema, GetCoursesQuerySchema, UpdateCourseRequestSchema, \
    CreateCourseResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from tools.routes import APIRoutes


class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    @allure.step("Create course")
    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Метод создание курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url=APIRoutes.COURSES, json=request.model_dump(by_alias=True))

    @allure.step("Get courses")
    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод получения курсов конкретного пользователя по его uuid.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=APIRoutes.COURSES, params=query.model_dump(by_alias=True))

    @allure.step("Update course by id {course_id}")
    def update_course_api(self, request: UpdateCourseRequestSchema, course_id: str) -> Response:
        """
        Метод обновления курса по его идентификатору.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"{APIRoutes.COURSES}/{course_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete course by id {course_id}")
    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса по его идентификатору.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"{APIRoutes.COURSES}/{course_id}")

    @allure.step("Get course by id {course_id}")
    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса по его идентификатору.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"{APIRoutes.COURSES}/{course_id}")

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)


def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Фунция создает экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))
