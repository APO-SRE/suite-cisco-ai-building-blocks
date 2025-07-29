from enum import Enum


class BrRestoreRequestType(str, Enum):
    CONFIG_ONLY = "config-only"
    FULL = "full"

    def __str__(self) -> str:
        return str(self.value)
