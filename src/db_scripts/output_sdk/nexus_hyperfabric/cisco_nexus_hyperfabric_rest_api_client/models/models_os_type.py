from enum import Enum


class ModelsOsType(str, Enum):
    HYPER_FABRIC = "HYPER_FABRIC"
    IOS_XE = "IOS_XE"
    IOS_XR = "IOS_XR"
    LINUX = "LINUX"
    NEXUS = "NEXUS"
    WINDOWS = "WINDOWS"

    def __str__(self) -> str:
        return str(self.value)
