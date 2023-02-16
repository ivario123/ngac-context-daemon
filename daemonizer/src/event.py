from typing import Type
from NgacApi.ngac import NGAC
NGAC_URL = "http://130.240.200.92:8001"

class Event:
    """
    A marker class for all events
    """
    NGAC = NGAC(policy_server_url=NGAC_URL,token="admin_token")

    def trigger(self):
        """
        Called when the timeout is reached
        """
        pass

    def __init__(self) -> None:
        pass


class EventGroup:
    """
    A marker class for all event groups
    """
    mapping: dict[str, Type[Event]] = {}
    """
    Resolves type for each contained event
    """

    def __init__(self, event: Type[Event]) -> None:
        self.event = event()
