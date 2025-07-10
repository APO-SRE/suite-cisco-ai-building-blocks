from enum import Enum


class ModelsDataType(str, Enum):
    BOOL = "BOOL"
    DURATION = "DURATION"
    INT32 = "INT32"
    INT64 = "INT64"
    JSON = "JSON"
    STRING = "STRING"
    TIME = "TIME"
    UINT32 = "UINT32"
    UINT64 = "UINT64"
    UUID = "UUID"

    def __str__(self) -> str:
        return str(self.value)
