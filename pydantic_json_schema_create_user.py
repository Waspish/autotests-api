import json

from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

public_users_client = get_public_users_client()
create_user_response = public_users_client.create_user(create_user_request)
create_user_response_schema = CreateUserResponseSchema.model_json_schema()
print("Instance:", create_user_response.model_dump(by_alias=True))
print("Schema:", json.dumps(create_user_response_schema, indent=2))
validate_json_schema(instance=create_user_response.model_dump(by_alias=True), schema=create_user_response_schema)
