from clients.courses.courses_client import CreateCourseRequestDict, get_course_client
from clients.files.files_client import get_file_client, UploadFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
public_users_client = get_public_users_client()
create_user_response = public_users_client.create_user(create_user_request)
print("Create user data: ", create_user_response)

authentication_user = AuthenticationUserDict(
    email=create_user_request["email"],
    password=create_user_request["password"]
)

upload_file_request = UploadFileRequestDict(
    filename="string.png",
    directory="stringTest",
    upload_file='./testdata/files/sponche_guard.png'
)
file_client = get_file_client(authentication_user)
create_file_response = file_client.create_file(upload_file_request)
print("Upload file data: ", create_file_response)

create_course_request = CreateCourseRequestDict(
    createdByUserId=create_user_response["user"]["id"],
    previewFileId=create_file_response["file"]["id"],
    maxScore=100,
    minScore=10,
    description="Python Course Api with CI/CD, Pydantic, HTTPX",
    estimatedTime="3 weeks",
    title="Python API Course"
)
course_client = get_course_client(authentication_user)
create_course_response = course_client.create_course(create_course_request)
print("Create course data: ", create_course_response)
