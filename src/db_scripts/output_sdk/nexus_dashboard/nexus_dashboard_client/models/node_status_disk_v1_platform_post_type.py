from enum import Enum


class NodeStatusDiskV1PlatformPOSTType(str, Enum):
    HDD = "HDD"
    SSD = "SSD"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
