from typing import Any

import allure
import jsonschema
from jsonschema import Draft202012Validator

from tools.logger import get_logger

logger = get_logger("SCHEMA_ASSERTIONS")


@allure.step("Validating JSON schema")
def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Проверяет, соответсует ли JSON-объект (instance) заданной JSON-схеме (schema).

    :param instance: JSON-данные, которые нужно проверить.
    :param schema: Ожидаемая JSON-схема.
    :raises jsonschema.exceptions.ValidationError: Если instance не соответсвует schema.
    """
    logger.info("Validating JSON schema")

    jsonschema.validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )
