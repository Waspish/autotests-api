import json

from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
public_users_client = get_public_users_client()
create_user_response = public_users_client.create_user(create_user_request)
print("Create user data: ", create_user_response)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_users_client = get_private_users_client(authentication_user)

get_user_response = private_users_client.get_user(create_user_response.user.id)
get_user_response_schema = GetUserResponseSchema.model_json_schema()
print("Instance:", get_user_response.model_dump(by_alias=True))
print("Schema:", json.dumps(get_user_response_schema, indent=2))
validate_json_schema(instance=get_user_response.model_dump(by_alias=True), schema=get_user_response_schema)
