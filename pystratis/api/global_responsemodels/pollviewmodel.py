from typing import Optional, List
from pydantic import Field, conint
from pystratis.core import PubKey
from pystratis.core.types import uint256
from pystratis.api import Model


class PollViewModel(Model):
    """A PollViewModel."""
    is_pending: bool = Field(alias='IsPending')
    is_executed: bool = Field(alias='IsExecuted')
    poll_id: int = Field(alias='Id')
    poll_voted_in_favor_blockdata_hash: Optional[uint256] = Field(alias='PollVotedInFavorBlockDataHash')
    poll_voted_in_favor_blockdata_height: Optional[conint(ge=0)] = Field(alias='PollVotedInFavorBlockDataHeight')
    poll_start_favor_blockdata_hash: Optional[uint256] = Field(alias='PollStartFavorBlockDataHash')
    poll_start_favor_blockdata_height: Optional[conint(ge=0)] = Field(alias='PollStartFavorBlockDataHeight')
    poll_executed_blockdata_hash: Optional[uint256] = Field(alias='PollExecutedBlockDataHash')
    poll_executed_blockdata_height: Optional[conint(ge=0)] = Field(alias='PollExecutedBlockDataHeight')
    pubkeys_hex_voted_in_favor: List[PubKey] = Field(alias='PubKeysHexVotedInFavor')
    voting_data_string: str = Field(alias='VotingDataString')