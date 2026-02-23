from pydantic import BaseModel, ConfigDict, Field
from tools.fakers import fake

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

    title: str = Field(default_factory=fake.text)
    course_id: str = Field(alias='courseId', default_factory=fake.uuid4)
    max_score: int | None = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=fake.min_score)
    order_index: int = Field(alias='orderIndex', default_factory=fake.integer)
    description: str = Field(default_factory=fake.sentence)
    estimated_time: str | None = Field(alias='estimatedTime', default_factory=fake.estimated_time)

class UpdateExeciseRequestSchema(BaseModel):
    '''
    Описание структуры запроса на обновление урока.
    '''
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default_factory=fake.text)
    max_score: int | None = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=fake.min_score)
    order_index: int | None = Field(alias='orderIndex', default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.sentence)
    estimated_time: str | None = Field(alias='estimatedTime', default_factory=fake.estimated_time)


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