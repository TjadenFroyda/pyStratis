from typing import Optional
from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import hexstr


class SetupModel(Model):
    """A SetupModel."""
    transaction_hex: Optional[hexstr] = Field(alias='transactionHex')