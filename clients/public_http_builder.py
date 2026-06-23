from httpx import Client

from clients.event_hooks import curl_event_hook


def get_public_http_client() -> Client:
    """
    Фунция создает экземпляр httpx.Client с базовыми настройками.

    :return: Готовый к использованию httpx.Client.
    """
    return Client(
        base_url='http://127.0.0.1:8000',
        timeout=100,
        event_hooks={"request": [curl_event_hook]}
    )
