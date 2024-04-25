from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GOOGLE_TOKEN_ID: str = "asdSUIHsdgen8yayghegrnGsdgu"
    SQLITE_DB_NAME: str = "tasks.sqlite"