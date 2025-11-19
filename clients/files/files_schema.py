from pydantic import BaseModel, ConfigDict, HttpUrl, Field

from tools.fakers import fake


class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    filename: str
    directory: str
    url: HttpUrl


class CreateFileRequestSchema(BaseModel):
    """
    Структура запроса для загрузки файла.
    """
    model_config = ConfigDict(populate_by_name=True)

    filename: str = Field(default_factory=fake.png_file_name)
    directory: str = Field(default="tests")
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа размещения файла.
    """
    model_config = ConfigDict(populate_by_name=True)

    file: FileSchema
