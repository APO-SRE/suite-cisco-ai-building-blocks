from enum import Enum


class BrStatusOperation(str, Enum):
    BACKUP = "backup"
    NONE = "none"
    RESTORE = "restore"

    def __str__(self) -> str:
        return str(self.value)
