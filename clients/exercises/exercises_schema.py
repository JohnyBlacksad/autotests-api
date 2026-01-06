from pydantic import BaseModel, ConfigDict, Field



class GetExercisesQuerySchema(BaseModel):
    '''
    Описание структуры запроса на получение списка уроков.
    '''
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias='courseId')


class CreateExerciseRequestSchema(BaseModel):
    '''
    Описание структуры запроса на cоздание урока.
    '''
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias='courseId')
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str | None = Field(alias='estimatedTime')

class UpdateExeciseRequestSchema(BaseModel):
    '''
    Описание структуры запроса на обновление урока.
    '''
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: str | None = Field(alias='maxScore')
    min_score: str | None = Field(alias='minScore')
    order_index: str | None = Field(alias='orderIndex')
    description: str | None
    estimated_time: str | None = Field(alias='estimatedTime')


class ExerciseSchema(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')

class GetExercisesResponseSchema(BaseModel):
    exercises: list[ExerciseSchema]


class GetExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema


class CreateExerciseSchema(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')

class CreateExerciseResponseSchema(BaseModel):
    exercise: CreateExerciseSchema


class UpdateExerciseSchema(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')


class UpdateExerciseResponseSchema(BaseModel):
    exercise: UpdateExerciseSchema