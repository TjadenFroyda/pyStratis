from typing import List
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.connectionmanager.requestmodels import *
from pystratis.api.connectionmanager.responsemodels import *


class ConnectionManager(APIRequest, metaclass=EndpointRegister):
    route = '/api/connectionmanager'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/addnode')
    def addnode(self, ipaddr: str, command: str, **kwargs) -> bool:
        """

        Args:
            ipaddr (str): The endpoint.
            command (str): Allowed commands [add, remove, onetry]
            **kwargs: Extra keyword arguments. 

        Returns:
            bool

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = AddNodeRequest(ipaddr=ipaddr, command=command)
        data = self.get(request_model, **kwargs)
        return data

    @endpoint(f'{route}/getpeerinfo')
    def getpeerinfo(self, **kwargs) -> List[PeerInfoModel]:
        """Gets the peer info.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            List[PeerInfoModel]

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return [PeerInfoModel(**x) for x in data]