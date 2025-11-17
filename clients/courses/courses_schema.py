from pydantic import BaseModel, Field, ConfigDict

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    description: str
    created_by_user: UserSchema = Field(alias="createdByUser")
    preview_file: FileSchema = Field(alias="previewFile")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    estimated_time: str = Field(alias="estimatedTime")


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    description: str
    created_by_user_id: str = Field(alias="createdByUserId")
    preview_file_id: str = Field(alias="previewFileId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    estimated_time: str = Field(alias="estimatedTime")


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    description: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    estimated_time: str | None = Field(alias="estimatedTime")


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    course: CourseSchema
