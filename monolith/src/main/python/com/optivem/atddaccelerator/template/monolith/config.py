import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Application settings
    app_name: str = "monolith"
    app_version: str = "0.0.1"
    debug: bool = False
    
    # Server settings
    host: str = "0.0.0.0"
    port: int = 8080
    
    # External API settings
    todos_api_host: str = "https://jsonplaceholder.typicode.com"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        # Map environment variables to settings
        fields = {
            'todos_api_host': {
                'env': 'TODOS_API_HOST'
            }
        }


# Global settings instance
settings = Settings()