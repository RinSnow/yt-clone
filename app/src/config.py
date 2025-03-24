from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    app_name: str = "YT Clone"
    admin_email: str
    url_test:str
    db_user:str
    db_pass:str
    db_name:str
    db_host:str
    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def get_settings():
    return Settings()