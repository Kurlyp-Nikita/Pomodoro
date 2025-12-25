from pydantic import BaseModel, Field, model_validator


class TaskShema(BaseModel):
    id: int
    name: str | None = None
    pomodoro_count: int | None = None
    category_id: int = Field(exclude=True) # исключили это поле

    class Config:
        from_attributes = True

    @model_validator(mode="after")  # @model_validator(mode="after") - валидация из документации.
    def check_name_or_pomodoro_count_none(self):  # cls - показываем что этот метод класс, @classmethod.
        if self.name is None and self.pomodoro_count is None:
            raise ValueError("name or pomodoro_count be provided")
        return self
