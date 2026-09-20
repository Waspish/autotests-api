from typing import Iterator

import pytest

from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client


@pytest.fixture
def authentication_client() -> Iterator[AuthenticationClient]:
    client = get_authentication_client()
    try:
        yield client
    finally:
        client.client.close()
