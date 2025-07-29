from enum import Enum


class BrType(str, Enum):
    CONFIG_ONLY = "config-only"
    FULL = "full"

    def __str__(self) -> str:
        return str(self.value)
