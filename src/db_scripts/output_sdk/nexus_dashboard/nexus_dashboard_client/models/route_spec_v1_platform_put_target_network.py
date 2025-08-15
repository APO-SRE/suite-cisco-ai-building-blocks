from enum import Enum


class RouteSpecV1PlatformPUTTargetNetwork(str, Enum):
    DATA = "Data"
    MANAGEMENT = "Management"

    def __str__(self) -> str:
        return str(self.value)
