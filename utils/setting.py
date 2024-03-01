from pydantic_settings import BaseSettings, SettingsConfigDict


class Setting(BaseSettings):
    DB_NAME: str

    @property
    def DB_URL(self) -> str:
        return f"sqlite+pysqlite:///resourses/db/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file="resourses/.env")
