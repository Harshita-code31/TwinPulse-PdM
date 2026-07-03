import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

# -------------------------------------------------
# Environment File
# -------------------------------------------------

ENV_FILE = os.getenv("ENV_FILE", ".env.local")


class Settings(BaseSettings):
    # ==========================
    # Application
    # ==========================

    app_name: str
    app_version: str
    app_host: str
    app_port: int
    debug: bool

    # ==========================
    # MySQL
    # ==========================

    database_url: str
    mysql_host: str
    mysql_port: int
    mysql_database: str
    mysql_user: str
    mysql_password: str

    # ==========================
    # MQTT
    # ==========================

    mqtt_broker: str
    mqtt_port: int
    mqtt_username: str = ""
    mqtt_password: str = ""
    mqtt_topic: str

    # ==========================
    # Machine Learning
    # ==========================

    model_directory: str
    scaler_directory: str

    # ==========================
    # Logging
    # ==========================

    log_level: str
    log_directory: str

    # ==========================
    # Pydantic Settings
    # ==========================

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    """
    Load and cache application settings.
    """
    return Settings()