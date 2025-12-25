from httpx import Client, Response, URL, QueryParams
from httpx._types import RequestData, RequestFiles
from typing import Any, Optional, Union


class APIClient:

    def __init__(self, client: Client) -> None:
        """Инициализирует API-клиент с заданным HTTP-клиентом.

        Args:
            client (httpx.Client): Предварительно настроенный экземпляр
                `httpx.Client` (например, с базовым URL, таймаутами, заголовками).
        """
        self.client = client

    def get(
        self,
        url: Union[URL, str],
        params: Optional[Union[QueryParams, dict, Any]] = None,
    ) -> Response:
        """Выполняет HTTP GET-запрос к указанному URL.

        Args:
            url (Union[httpx.URL, str]): Целевой URL. Может быть строкой
                или экземпляром `httpx.URL`.
            params (Optional[Union[httpx.QueryParams, dict]]): Параметры запроса.
                Если передан `dict`, он будет преобразован в query string.
                По умолчанию `None`.

        Returns:
            `httpx.Response`: Ответ от сервера.

        Raises:
            `httpx.RequestError`: При ошибках сети (таймаут, DNS и пр.).
            `httpx.HTTPStatusError`: При HTTP-ошибках (если вызван `.raise_for_status()`).
        """
        return self.client.get(url, params=params)

    def post(
        self,
        url: Union[URL, str],
        json: Optional[Any] = None,
        data: Optional[RequestData] = None,
        files: Optional[RequestFiles] = None,
    ) -> Response:
        """Выполняет HTTP POST-запрос к указанному URL.

        Args:
            url (Union[httpx.URL, str]): Целевой URL.
            json (Optional[Any]): Тело запроса в формате JSON.
                Автоматически сериализуется в JSON и устанавливает заголовок
                `Content-Type: application/json`.
                Должно быть сериализуемым через `json.dumps()` (dict, list и пр.).
            data (Optional[httpx.RequestData]): Данные формы (`application/x-www-form-urlencoded`)
                или raw bytes/str (`text/plain`, `application/octet-stream` и др.).
            files (Optional[httpx.RequestFiles]): Файлы для multipart-загрузки.
                См. `httpx` документацию по формату: tuple, dict, bytes и др.

        Returns:
            `httpx.Response`: Ответ от сервера.

        Raises:
            `httpx.RequestError`: При ошибках сети.
            `httpx.HTTPStatusError`: При HTTP-ошибках.
        """
        return self.client.post(url, json=json, data=data, files=files)

    def patch(
        self,
        url: Union[URL, str],
        json: Optional[Any] = None,
    ) -> Response:
        """Выполняет HTTP PATCH-запрос к указанному URL.

        Аналогично `post()`, но с методом PATCH.

        Args:
            url (Union[httpx.URL, str]): Целевой URL.
            json (Optional[Any]): Тело запроса в формате JSON.

        Returns:
            `httpx.Response`: Ответ от сервера.

        Raises:
            `httpx.RequestError`: При ошибках сети.
            `httpx.HTTPStatusError`: При HTTP-ошибках.
        """
        return self.client.patch(url, json=json)

    def delete(
        self,
        url: Union[URL, str],
    ) -> Response:
        """Выполняет HTTP DELETE-запрос к указанному URL.

        Args:
            url (Union[httpx.URL, str]): Целевой URL.

        Returns:
            `httpx.Response`: Ответ от сервера.

        Raises:
            `httpx.RequestError`: При ошибках сети.
            `httpx.HTTPStatusError`: При HTTP-ошибках.
        """
        return self.client.delete(url)