import pytest

from clients.authentication.authentication_client import AuthenticationClient, get_authentications_client


@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_authentications_client()
