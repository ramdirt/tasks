from pydantic import BaseModel, model_validator


class UserLoginSchema(BaseModel):
    user_id: int | None = None
    access_token: str | None = None
