from typing import Any
from jsonschema import validate
from jsonschema.validators import Draft202012Validator

def validate_json_schema(instance: Any, schema: dict) -> None:
    '''
    Проверяет соответствует ли JSON объект (instance) заданной JSON съеме.
    :param instance: JSON данные
    :param schema: Ожидаемая JSON схема
    :raises jsonschema.exceptions.ValidationError: Если instance не соответствует схеме.
    '''
    validate(
        schema=schema,
        instance=instance,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )