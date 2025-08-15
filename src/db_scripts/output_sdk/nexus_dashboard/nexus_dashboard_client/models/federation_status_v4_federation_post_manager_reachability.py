from enum import Enum


class FederationStatusV4FederationPOSTManagerReachability(str, Enum):
    DOWN = "Down"
    UP = "Up"

    def __str__(self) -> str:
        return str(self.value)
