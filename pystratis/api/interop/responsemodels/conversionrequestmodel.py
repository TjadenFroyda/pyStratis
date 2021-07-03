from typing import Optional
from pydantic import Field, conint
from pystratis.core import Model, ConversionRequestType
from pystratis.core.types import Address, Money, uint256


class ConversionRequestModel(Model):
    """A ConversionRequestModel."""
    request_id: Optional[uint256] = Field(alias='requestId')
    request_type: Optional[ConversionRequestType] = Field(alias='requestType')
    request_status: Optional[conint(ge=0)] = Field(alias='requestStatus')
    block_height: Optional[conint(ge=0)] = Field(alias='blockHeight')
    destination_address: Optional[Address] = Field(alias='destinationAddress')
    amount: Optional[Money]
    processed: Optional[bool]
