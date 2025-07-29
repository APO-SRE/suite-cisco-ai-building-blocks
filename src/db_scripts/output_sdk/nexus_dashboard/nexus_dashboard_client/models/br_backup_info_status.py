from enum import Enum


class BrBackupInfoStatus(str, Enum):
    FAILURE = "failure"
    IN_PROGRESS = "in-progress"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
