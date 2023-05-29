from typing import Optional

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"  

    DEBUGGER: bool

    PROJECT_NAME: str

    SQLALCHEMY_DATABASE_URI: str


    class Config:
        case_sensitive = True


settings = Settings()