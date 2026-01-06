from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from httpx import Response

from clients.authentication.authentication_schema import (
    LoginRequestSchema,
    LoginResponseSchema,
    RefreshRequestSchema,
)


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

    def login_api(self, request: LoginRequestSchema) -> Response:
        """Выполняет аутентификацию пользователя по email и паролю.

        POST /api/v1/authentication/login

        Запрос должен содержать корректные `email` и `password`.
        Успешный ответ возвращает access и refresh токены.

        Args:
            request (LoginRequestSchema): Данные для входа.
                См. `LoginRequestSchema` для структуры.

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
        return self.post("/api/v1/authentication/login", json=request.model_dump(by_alias=True))

    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """Обновляет access-токен с использованием refresh-токена.

        POST /api/v1/authentication/refresh

        Args:
            request (RefreshRequestSchema): Объект с `refreshToken`.

        Returns:
            httpx.Response: Ответ сервера.
                В теле (при 200 OK) — новый `accessToken` (и, опционально, новый `refreshToken`).

        Raises:
            httpx.RequestError: При сетевых ошибках.
            httpx.HTTPStatusError: При недействительном/просроченном refresh-токене (401).
        """
        return self.post("/api/v1/authentication/refresh", json=request.model_dump(by_alias=True))


    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)



def get_authentication_client() -> AuthenticationClient:
    return AuthenticationClient(client=get_public_http_client())