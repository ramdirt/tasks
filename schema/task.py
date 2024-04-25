from pydantic import BaseModel, Field, model_validator, field_validator, ValidationInfo


class Task(BaseModel):
    id: int | None = None
    name: str | None = None
    pomodoro_count: int | None = None
    category_id: int = Field(exclude=True)

    # before - срабатывает до инициализации класса
    # after - после инициализации, поэтому у функции будет аргрумент self

    @model_validator(mode="after")
    def check_name_or_pomodoro_count_is_not_none(self):
        if self.name is None and self.pomodoro_count is None:
            raise ValueError("name or pomodoro_count must be provided")
        print(self)
        return self