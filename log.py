import httpx

from clients.authentication.authentication_client import AuthenticationClient, LoginRequestDict


def authentication(user: LoginRequestDict):
    client = AuthenticationClient(httpx.Client())
    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    client.login_api(login_request)


authentication({'email': '', 'password': ''})
