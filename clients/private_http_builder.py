from httpx import Client
from pydantic import BaseModel

from clients.authentication.authentication_client import get_authentications_client, LoginRequestSchema


class AuthenticationUserSchema(BaseModel):
    email: str
    password: str


def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Фунция создает экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    authentication_client = get_authentications_client()

    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentication_client.login(login_request)

    return Client(
        base_url='http://127.0.0.1:8000',
        timeout=100,
        headers={"Authorization": f"Bearer {login_response.token.access_token}"},
    )
