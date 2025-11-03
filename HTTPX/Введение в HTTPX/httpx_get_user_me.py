import json
import os
import sys

from dotenv import load_dotenv

import httpx

base_url = "http://127.0.0.1:8000/api/v1/"

load_dotenv()

login_payload = {
  "email": os.getenv("API_USER"),
  "password": os.getenv("API_PASSWORD")
}

if not login_payload["email"] or not login_payload["password"]:
    print("Не заданы email или password в .env")
    sys.exit(1)

with httpx.Client() as client:
    try:
        response_login = client.post(f'{base_url}authentication/login', json=login_payload)
        if response_login.status_code != 200:
            raise ValueError(f"Ошибка логина: {response_login.status_code}")
        tokens = response_login.json().get("token", {})
        access_token = tokens.get("accessToken")
        if not access_token:
            raise ValueError(f"В ответе отсутствует accessToken:\n{json.dumps(tokens, indent=2)}")
        response_me = client.get(
            f'{base_url}users/me', headers={"Authorization": f"Bearer {access_token}"}
        )
        if response_me.status_code != 200:
            raise ValueError(f"Ошибка получения данных: {response_login.status_code}")
        user_me = response_me.json().get("user", {})
        if not user_me:
            raise ValueError(f"В ответе отсутствует user object")
        print(f""
              f"------------------------------------------------------------------------------\n"
              f"JSON Ответ:\n"
              f"{json.dumps(response_me.json(), indent=4)}\n"
              f"Статус ответа: {response_me.status_code}\n"
              f"------------------------------------------------------------------------------"
              )
    except httpx.RequestError as e:
        print(f"Ошибка подключения: {e}")
    except ValueError as e:
        print(e)


