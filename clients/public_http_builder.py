from httpx import Client


def get_public_http_client() -> Client:
    """
    Фунция создает экземпляр httpx.Client с базовыми настройками.

    :return: Готовый к использованию httpx.Client.
    """
    return Client(base_url='http://127.0.0.1:8000', timeout=100)
