from pystratis.core import Model


class CallByNameRequest(Model):
    """A request model for the rpc/callbyname endpoint.

    Args:
        command (str): The complete RPC command.
    """
    command: str
