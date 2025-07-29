from enum import Enum


class NodeStatusDiskV1PlatformGETType(str, Enum):
    HDD = "HDD"
    SSD = "SSD"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
