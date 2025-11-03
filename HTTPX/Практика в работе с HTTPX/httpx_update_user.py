import httpx

from tools.fakers import get_random_email

create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=create_user_payload)
print(create_user_response.status_code)
create_user_response_data = create_user_response.json()

login_user_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_user_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_user_payload)
print(login_user_response.status_code)
login_user_response_data = login_user_response.json()

update_user_payload = {
    "email": get_random_email(),
    "lastName": "string",
    "firstName": "Olga",
    "middleName": "string"
}
update_user_headers = {
    "Authorization": f"Bearer {login_user_response_data['token']['accessToken']}"
}

update_user_response = httpx.patch(f"http://127.0.0.1:8000/api/v1/users/{create_user_response_data['user']['id']}",
                                   json=update_user_payload, headers=update_user_headers)
print(update_user_response.status_code)
update_user_response_data = update_user_response.json()
