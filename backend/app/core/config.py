from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')
    app_env: str = 'development'
    demo_mode: bool = True
    jwt_secret: str = 'demo-only-change-in-production'
    cors_origins: str = 'http://localhost:5173'
    azuracast_base_url: str = ''
    azuracast_api_key: str = ''
    azuracast_station_id: str = ''
    azuracast_stream_url: str = ''
    livekit_url: str = ''
    livekit_api_key: str = ''
    livekit_api_secret: str = ''
    radio_source_username: str = ''
    radio_source_password: str = ''
settings = Settings()
