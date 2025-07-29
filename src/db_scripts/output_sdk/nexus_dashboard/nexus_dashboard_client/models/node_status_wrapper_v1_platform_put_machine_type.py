from enum import Enum


class NodeStatusWrapperV1PlatformPUTMachineType(str, Enum):
    BAREMETAL = "BareMetal"
    UNKNOWN = "Unknown"
    VIRTUAL = "Virtual"

    def __str__(self) -> str:
        return str(self.value)
