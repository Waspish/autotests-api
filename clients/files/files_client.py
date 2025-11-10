from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class FilesClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """

    class UploadFileRequestDict(TypedDict):
        """
        Структура запроса для загрузки файла.
        """
        filename: str
        directory: str
        upload_file: str

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
