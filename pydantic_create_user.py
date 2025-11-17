from pydantic import BaseModel, EmailStr, Field, ConfigDict
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    """
    Описание структуры пользователя
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    """
    Описание структуры запроса на создание пользователя.
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя
    """
    user: UserSchema


dict1 = {
    "email": "user@example.com",
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

json1 = """
{
  "email": "user@example.com",
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
"""

user1 = CreateUserRequestSchema(**dict1)
user2 = CreateUserRequestSchema.model_validate_json(json1)
user3 = CreateUserRequestSchema(
    email=user1.email,
    password=user1.password,
    last_name="string",
    first_name="string",
    middle_name="string"
)
print(user1.model_dump(by_alias=True))
print(user2.model_dump_json(by_alias=True))
print(user3.model_dump_json(by_alias=True))
print(user3)
