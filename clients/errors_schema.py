from typing import List, Any, Dict

from pydantic import BaseModel, ConfigDict, Field


class ValidationErrorSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    type: str
    location: List[str] = Field(alias='loc')
    message: str = Field(alias="msg")
    input: Any
    context: Dict[str, Any] = Field(alias='ctx')


class ValidationErrorResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    details: list[ValidationErrorSchema] = Field(alias='detail')


class HTTPValidationErrorSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    details: str = Field(alias='detail')
