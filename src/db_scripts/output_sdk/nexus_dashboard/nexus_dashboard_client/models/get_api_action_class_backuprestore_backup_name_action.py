from enum import Enum


class GetApiActionClassBackuprestoreBackupNameAction(str, Enum):
    DOWNLOAD = "download"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
