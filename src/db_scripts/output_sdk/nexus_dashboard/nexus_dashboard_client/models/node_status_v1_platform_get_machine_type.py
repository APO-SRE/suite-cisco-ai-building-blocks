from enum import Enum


class NodeStatusV1PlatformGETMachineType(str, Enum):
    BAREMETAL = "BareMetal"
    UNKNOWN = "Unknown"
    VIRTUAL = "Virtual"

    def __str__(self) -> str:
        return str(self.value)
