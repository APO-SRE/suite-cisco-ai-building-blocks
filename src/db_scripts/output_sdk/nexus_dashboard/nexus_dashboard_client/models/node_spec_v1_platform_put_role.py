from enum import Enum


class NodeSpecV1PlatformPUTRole(str, Enum):
    MASTER = "Master"
    STANDBY = "Standby"
    WORKER = "Worker"

    def __str__(self) -> str:
        return str(self.value)
