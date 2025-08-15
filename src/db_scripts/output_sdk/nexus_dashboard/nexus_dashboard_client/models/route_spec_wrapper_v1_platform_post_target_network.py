from enum import Enum


class RouteSpecWrapperV1PlatformPOSTTargetNetwork(str, Enum):
    DATA = "Data"
    MANAGEMENT = "Management"

    def __str__(self) -> str:
        return str(self.value)
