import pytest
from pydantic import BaseModel

from clients.authentication.authentication_client import AuthenticationClient, get_authentications_client
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self):
        return self.request.email

    @property
    def password(self):
        return self.request.password


@pytest.fixture
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()


@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_authentications_client()


@pytest.fixture
def function_user(public_users_client) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)
