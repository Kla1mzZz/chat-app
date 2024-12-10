from pydantic_settings import BaseSettings
from pydantic import BaseModel

class DatabaseConfig(BaseModel):
    database_url: str

class JwtConfig(BaseModel):
    secret_key: str
    algorithm: str = 'HS256'
    access_token_expire_minutes: int = 60

class Settings(BaseSettings):
    database: DatabaseConfig
    jwt: JwtConfig
    
    class Config:
        env_file = '.env'
        env_nested_delimiter='__'

settings = Settings()