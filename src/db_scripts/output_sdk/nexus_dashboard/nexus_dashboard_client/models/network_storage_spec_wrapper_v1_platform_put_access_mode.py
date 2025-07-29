from enum import Enum


class NetworkStorageSpecWrapperV1PlatformPUTAccessMode(str, Enum):
    READONLY = "ReadOnly"
    READWRITE = "ReadWrite"

    def __str__(self) -> str:
        return str(self.value)
