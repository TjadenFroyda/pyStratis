from pydantic import Field, conint
from pystratis.api import Model


class GetConnectionInfoModel(Model):
    """A GetConnectionInfoModel."""
    signalr_uri: str = Field(alias='signalRUri')
    signalr_port: conint(ge=0) = Field(alias='signalRPort')
