from enum import Enum


class NodeSpecV1PlatformGETRole(str, Enum):
    MASTER = "Master"
    STANDBY = "Standby"
    WORKER = "Worker"

    def __str__(self) -> str:
        return str(self.value)
