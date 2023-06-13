import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseSettings

dotenv_path = Path().cwd().parent / '.env'
load_dotenv(dotenv_path)


class Settings(BaseSettings):
    FIRST_SUPERUSER_EMAIL: str = os.getenv('FIRST_SUPERUSER_EMAIL')
    FIRST_SUPERUSER_PASSWORD: str = os.getenv('FIRST_SUPERUSER_PASSWORD')
    DEFAULT_PREVIEW: str = 'https://pp_urfu_test.hb.bizmrg.com/previews/default.jpg'

    # POSTGRES CREDS
    __DB_USER: str = os.getenv('DB_USER')
    __DB_PASSWORD: int = os.getenv('DB_PASSWORD')
    __DB_HOST: str = os.getenv('DB_HOST')
    __DB_PORT: int = os.getenv('DB_PORT')
    __DB_NAME: str = os.getenv('DB_NAME')
    DB_URL: str = f'postgresql://{__DB_USER}:{__DB_PASSWORD}@{__DB_HOST}:{__DB_PORT}/{__DB_NAME}'

    # VK S3 CREDS
    S3_BUCKET_NAME: str = os.getenv('S3_BUCKET_NAME')
    S3_ACCESS_KEY: str = os.getenv('S3_ACCESS_KEY')
    S3_SECRET_KEY: str = os.getenv('S3_SECRET_KEY')

    # TOKEN CONST
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = "HS256"

    class Config:
        case_sensitive = True


settings = Settings()
