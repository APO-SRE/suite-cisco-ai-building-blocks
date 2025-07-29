from enum import Enum


class FederationStatusV4FederationGETManagerReachability(str, Enum):
    DOWN = "Down"
    UP = "Up"

    def __str__(self) -> str:
        return str(self.value)
