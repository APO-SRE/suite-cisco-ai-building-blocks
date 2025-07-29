from enum import Enum


class FederationStatusWrapperV4FederationGETManagerReachability(str, Enum):
    DOWN = "Down"
    UP = "Up"

    def __str__(self) -> str:
        return str(self.value)
