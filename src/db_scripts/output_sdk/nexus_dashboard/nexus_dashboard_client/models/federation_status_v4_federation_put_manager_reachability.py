from enum import Enum


class FederationStatusV4FederationPUTManagerReachability(str, Enum):
    DOWN = "Down"
    UP = "Up"

    def __str__(self) -> str:
        return str(self.value)
