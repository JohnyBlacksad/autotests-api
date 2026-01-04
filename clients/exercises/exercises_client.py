from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client

class GetExercisesQueryDict(TypedDict):
    '''
    Описание структуры запроса на получение списка уроков.
    '''

    courseId: str


class CreateExerciseRequestDict(TypedDict):
    '''
    Описание структуры запроса на cоздание урока.
    '''

    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None

class UpdateExeciseRequestDict(TypedDict):
    '''
    Описание структуры запроса на обновление урока.
    '''

    title: str | None
    maxScore: str | None
    minScore: str | None
    orderIndex: str | None
    description: str | None
    estimatedTime: str | None


class Exercise(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesResponseDict(TypedDict):
    exercises: list[Exercise]


class GetExerciseResponseDict(TypedDict):
    exercise: Exercise


class CreateExercise(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class CreateExerciseResponseDict(TypedDict):
    exercise: CreateExercise


class UpdateExercise(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseResponseDict(TypedDict):
    exercise: UpdateExercise

class ExercisesClient(APIClient):
    '''
    API клиент для работы с /api/v1/exercises
    '''

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        '''
        Метод для получения списка уроков курса

        :params query: Словарь с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        '''

        return self.get('/api/v1/exercises', params=query)


    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        '''
        Метод создания урока в курсе.

        :param request: Словарь с полями:
                        - `title`
                        - `courseId`
                        - `maxScore` (Необязательно. По умолчанию 0)
                        - `minScore` (Необязательно. По умолчанию 0)
                        - `orderIndex`
                        - `description`
                        - `estimatedTime`

        :return: Ответ от севера в виде объекта httpx.Response
        '''

        return self.post('/api/v1/exercises', json=request)

    def get_exercise_api(self, exercise_id: str) -> Response:
        '''
        Метод получения определенного урока

        :param exercise_id: Идентификатор урока
        :return: Ответ от сервера в виде объекта httpx.Response
        '''

        return self.get(f'/api/v1/exercises/{exercise_id}')

    def update_exercise_api(self, exercise_id: str, request: UpdateExeciseRequestDict) -> Response:
        '''
        Метод обновления определенного урока.

        :param exercise_id: Идентификатор урока
        :param request: Словарь с полями:
                                - `title`
                                - `maxScore`
                                - `minScore`
                                - `orderIndex`
                                - `description`
                                - `estimatedTime`

        :return: Ответ от сервера в виде объекта httpx.Response
        '''

        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        '''
        Метод удаления определенного урока.

        :param exercise_id: Идентификатор урока
        :request: Ответ от сервера в виде объекта httpx.Response
        '''

        return self.delete(f'/api/v1/exercises/{exercise_id}')

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExeciseRequestDict) -> UpdateExerciseResponseDict:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()

def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))