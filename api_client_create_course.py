from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
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
print("Create user data: ", create_user_response)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

create_file_request = CreateFileRequestSchema(
    filename="string.png",
    directory="stringTest",
    upload_file='./testdata/files/sponche_guard.png'
)
files_client = get_files_client(authentication_user)
create_file_response = files_client.create_file(create_file_request)
print("Create file data: ", create_file_response)

create_course_request = CreateCourseRequestSchema(
    description="Python Course Api with CI/CD, Pydantic, HTTPX",
    title="Python API Course",
    created_by_user_id=create_user_response.user.id,
    preview_file_id=create_file_response.file.id,
    max_score=100,
    min_score=10,
    estimated_time="3 weeks"
)
courses_client = get_courses_client(authentication_user)
create_course_response = courses_client.create_course(create_course_request)
print("Create course data: ", create_course_response)
