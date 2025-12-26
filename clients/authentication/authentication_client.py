from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from httpx import Response
from typing import TypedDict


class LoginRequestDict(TypedDict):
    """Структура запроса для аутентификации по email и паролю.

    Attributes:
        email (str): Адрес электронной почты пользователя.
        password (str): Пароль в открытом виде (должен передаваться по HTTPS!).
    """
    email: str
    password: str


class RefreshRequestDict(TypedDict):
    """Структура запроса для обновления access-токена.

    Attributes:
        refreshToken (str): Действующий refresh token, выданный при логине.
    """
    refreshToken: str

class Token(TypedDict):
    tokenType: str
    accessToken: str
    refreshToken: str

class LoginResponseDict(TypedDict):
    token: Token

class AuthenticationClient(APIClient):
    """Клиент для работы с эндпоинтами аутентификации.

    Предоставляет типизированный и читаемый интерфейс к `/api/v1/authentication/*`.
    Наследует базовую HTTP-логику от `APIClient`.

    Пример использования:
        >>> client = AuthenticationClient(httpx.Client(base_url="https://api.example.com"))
        >>> resp = client.login_api({"email": "user@test.com", "password": "pass123"})
        >>> resp.raise_for_status()
        >>> tokens = resp.json()
    """

    def login_api(self, request: LoginRequestDict) -> Response:
        """Выполняет аутентификацию пользователя по email и паролю.

        POST /api/v1/authentication/login

        Запрос должен содержать корректные `email` и `password`.
        Успешный ответ возвращает access и refresh токены.

        Args:
            request (LoginRequestDict): Данные для входа.
                См. `LoginRequestDict` для структуры.

        Returns:
            httpx.Response: Ответ сервера.
                В теле (при 200 OK) — JSON с токенами, например:
                {
                    "accessToken": "eyJ...",
                    "refreshToken": "def502..."
                }

        Raises:
            httpx.RequestError: При сетевых ошибках.
            httpx.HTTPStatusError: При HTTP-ошибках (400, 401, 500 и т.д.).
        """
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """Обновляет access-токен с использованием refresh-токена.

        POST /api/v1/authentication/refresh

        Args:
            request (RefreshRequestDict): Объект с `refreshToken`.

        Returns:
            httpx.Response: Ответ сервера.
                В теле (при 200 OK) — новый `accessToken` (и, опционально, новый `refreshToken`).

        Raises:
            httpx.RequestError: При сетевых ошибках.
            httpx.HTTPStatusError: При недействительном/просроченном refresh-токене (401).
        """
        return self.post("/api/v1/authentication/refresh", json=request)


    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        response = self.login_api(request)
        return response.json()



def get_authentication_client() -> AuthenticationClient:
    return AuthenticationClient(client=get_public_http_client())