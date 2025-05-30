from enum import Enum


class ModelsConnectedState(str, Enum):
    CONNECTED_STATE_CONNECTED = "CONNECTED_STATE_CONNECTED"
    CONNECTED_STATE_NOT_CONNECTED = "CONNECTED_STATE_NOT_CONNECTED"

    def __str__(self) -> str:
        return str(self.value)
