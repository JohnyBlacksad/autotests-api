from pydantic import BaseModel, Field
from tools.fakers import fake

class LoginRequestSchema(BaseModel):
    """Структура запроса для аутентификации по email и паролю."""

    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class RefreshRequestSchema(BaseModel):
    """Структура запроса для обновления access-токена."""

    refresh_token: str = Field(alias='refreshToken', default_factory=fake.sentence)

class TokenSchema(BaseModel):
    '''
    Структура acess-token'а
    '''

    token_type: str = Field(alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')

class LoginResponseSchema(BaseModel):
    '''Структура ответа сервера с access токеном'''

    token: TokenSchema