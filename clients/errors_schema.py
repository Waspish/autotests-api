from typing import List, Any, Dict

from pydantic import BaseModel, ConfigDict, Field


class ValidationErrorSchema(BaseModel):
    """
    Модель, описывающая структуру ошибки валидации API.
    """
    model_config = ConfigDict(populate_by_name=True)

    type: str
    location: List[str] = Field(alias='loc')
    message: str = Field(alias="msg")
    input: Any
    context: Dict[str, Any] = Field(alias='ctx')


class ValidationErrorResponseSchema(BaseModel):
    """
    Модель, описывающая структуру ответа API с ошибкой валидации.
    """
    model_config = ConfigDict(populate_by_name=True)

    details: list[ValidationErrorSchema] = Field(alias='detail')


class InternalErrorResponseSchema(BaseModel):
    """
    Модель для описания внутренней ошибки.
    """
    model_config = ConfigDict(populate_by_name=True)

    details: str = Field(alias='detail')
