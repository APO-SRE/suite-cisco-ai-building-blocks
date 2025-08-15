from enum import Enum


class FederationStatusWrapperV4FederationPUTManagerReachability(str, Enum):
    DOWN = "Down"
    UP = "Up"

    def __str__(self) -> str:
        return str(self.value)
