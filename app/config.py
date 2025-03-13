from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Assistance Request Service"
    slack_webhook_url: str

    class Config:
        env_file = ".env"

settings = Settings()
