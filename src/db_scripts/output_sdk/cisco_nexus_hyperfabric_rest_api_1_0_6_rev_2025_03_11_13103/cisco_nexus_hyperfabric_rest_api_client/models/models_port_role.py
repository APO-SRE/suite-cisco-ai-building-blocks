from enum import Enum


class ModelsPortRole(str, Enum):
    FABRIC_PORT = "FABRIC_PORT"
    HOST_PORT = "HOST_PORT"
    LAG_PORT = "LAG_PORT"
    ROUTED_PORT = "ROUTED_PORT"
    UNUSED_PORT = "UNUSED_PORT"

    def __str__(self) -> str:
        return str(self.value)
