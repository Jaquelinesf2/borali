from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Informações gerais da aplicação
    APP_NAME: str = "Borali API"
    APP_DESCRIPTION: str = "API do aplicativo de transporte estilo Uber"
    APP_VERSION: str = "0.1.0"

    # Versionamento da API
    API_V1_PREFIX: str = "/api/v1"

    class Config:
        env_file = ".env"


# Instância única de configuração
settings = Settings()
