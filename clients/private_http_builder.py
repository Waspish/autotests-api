from functools import lru_cache

from httpx import Client
from pydantic import BaseModel, EmailStr

from clients.authentication.authentication_client import get_authentications_client, LoginRequestSchema
from clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook
from config import settings


class AuthenticationUserSchema(BaseModel, frozen=True):
    """
    Модель для аутентификации пользователя.
    """
    email: EmailStr
    password: str


@lru_cache(maxsize=None)
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
        base_url=settings.http_client.client_url,
        timeout=settings.http_client.timeout,
        headers={"Authorization": f"Bearer {login_response.token.access_token}"},
        event_hooks={
            "request": [curl_event_hook, log_request_event_hook],
            "response": [log_response_event_hook]
        },
    )
