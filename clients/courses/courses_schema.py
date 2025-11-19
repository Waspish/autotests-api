from pydantic import BaseModel, Field, ConfigDict

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.fakers import fake


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

    title: str = Field(default_factory=fake.sentence)
    description: str = Field(default_factory=fake.text)
    created_by_user_id: str = Field(alias="createdByUserId", default_factory=fake.uuid4)
    preview_file_id: str = Field(alias="previewFileId", default_factory=fake.uuid4)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default_factory=fake.sentence)
    description: str | None = Field(default_factory=fake.text)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)


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
