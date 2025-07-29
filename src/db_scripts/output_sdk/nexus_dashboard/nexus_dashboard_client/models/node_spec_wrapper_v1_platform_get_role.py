from enum import Enum


class NodeSpecWrapperV1PlatformGETRole(str, Enum):
    MASTER = "Master"
    STANDBY = "Standby"
    WORKER = "Worker"

    def __str__(self) -> str:
        return str(self.value)
