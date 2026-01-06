from httpx import Response
from clients.api_client import APIClient

from clients.private_http_builder import (
    AuthenticationUserSchema,
    get_private_http_client
)

from clients.exercises.exercises_schema import (
    GetExercisesQuerySchema,
    CreateExerciseRequestSchema,
    UpdateExeciseRequestSchema,
    GetExercisesResponseSchema,
    GetExerciseResponseSchema,
    CreateExerciseResponseSchema,
    UpdateExerciseResponseSchema
)


class ExercisesClient(APIClient):
    '''
    API клиент для работы с /api/v1/exercises
    '''

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        '''
        Метод для получения списка уроков курса

        :params query: Словарь с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        '''

        return self.get('/api/v1/exercises', params=query.model_dump(by_alias=True))


    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
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

        return self.post('/api/v1/exercises', json=request.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        '''
        Метод получения определенного урока

        :param exercise_id: Идентификатор урока
        :return: Ответ от сервера в виде объекта httpx.Response
        '''

        return self.get(f'/api/v1/exercises/{exercise_id}')

    def update_exercise_api(self, exercise_id: str, request: UpdateExeciseRequestSchema) -> Response:
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

        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        '''
        Метод удаления определенного урока.

        :param exercise_id: Идентификатор урока
        :request: Ответ от сервера в виде объекта httpx.Response
        '''

        return self.delete(f'/api/v1/exercises/{exercise_id}')

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExeciseRequestSchema) -> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))