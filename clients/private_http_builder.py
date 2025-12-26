from httpx import Client
from clients.authentication.authentication_client import get_authentication_client, LoginRequestDict
from typing import TypedDict

class AuthenticationUserDict(TypedDict):
    email: str
    password: str

def get_private_http_client(user: AuthenticationUserDict) -> Client:
    authontication_client = get_authentication_client()

    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    login_response = authontication_client.login(login_request)

    return Client(
        timeout=100,
        base_url='http://localhost:63897',
        headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"}
    )