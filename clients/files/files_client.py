from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient

class CreateFileRequestDict(TypedDict):
    '''
    Описание структуры запроса на создание файла.
    '''

    fileName: str
    directory: str
    upload_file: str

class FilesClient(APIClient):
    '''
    API клиент для работы с /api/v1/files
    '''

    def get_file_api(self, file_id: str) -> Response:
        '''
        Метод получения файла

        :param file_id: Идентификатор файла
        :return: Ответ от сервера в виду объекта httpx.Response
        '''

        return self.get(f'/api/v1/files/{file_id}')

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        '''
        Метод создания файла

        :param request: Словарь с fileName, directory, upload_file
        :return: Ответ от сервера в виду объекта httpx.Response
        '''
        payload = {
            'upload_file': open(request['upload_file'], 'rb')
        }

        return self.post('/api/v1/files', data=request, files=payload)

    def delete_file_api(self, file_id: str) -> Response:
        '''
        Метод удаления файла
        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        '''

        return self.delete(f'/api/v1/files/{file_id}')