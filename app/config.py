from dynaconf import Dynaconf
from pydantic import BaseModel


class APPConfig(BaseModel):
    app_port: int
    app_version: str
    app_name: str
    app_host: str
    app_mount: str
    api_key: str

class Settings(BaseModel):
    app: APPConfig


dyna_settings = Dynaconf(
    settings_files=["settings.toml"],
)

settings = Settings(app=dyna_settings["app_settings"])