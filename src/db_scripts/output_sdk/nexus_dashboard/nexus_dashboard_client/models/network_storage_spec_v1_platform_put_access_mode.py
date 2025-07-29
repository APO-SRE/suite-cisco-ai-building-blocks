from enum import Enum


class NetworkStorageSpecV1PlatformPUTAccessMode(str, Enum):
    READONLY = "ReadOnly"
    READWRITE = "ReadWrite"

    def __str__(self) -> str:
        return str(self.value)
