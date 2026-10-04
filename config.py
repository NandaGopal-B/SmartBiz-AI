from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "SmartBiz AI"
    database_url: str = "sqlite:///./smartbiz.db"
    api_url: str = "http://127.0.0.1:8000"
    secret_key: str = "development-secret"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
