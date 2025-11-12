from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class UploadFileRequestDict(TypedDict):
    """
    Структура запроса для загрузки файла.
    """
    filename: str
    directory: str
    upload_file: str


class FilesClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """

    def get_file(self, file_id: str) -> Response:
        """
        Метод на получение файла по идентификатору.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/files/{file_id}")

    def delete_file(self, file_id: str) -> Response:
        """
        Метод на удаление файла по идентификатору.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/files/{file_id}")

    def upload_file(self, request: UploadFileRequestDict) -> Response:
        """
        Метод размещения файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            url="/api/v1/files",
            data=request,
            files={"upload_file": open(request['upload_file'], "rb")}
        )


def get_private_users_client(user: AuthenticationUserDict) -> FilesClient:
    """
    Фунция создает экземпляр FilesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))
