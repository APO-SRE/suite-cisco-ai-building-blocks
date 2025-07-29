from enum import Enum


class RecordStreamV1EventmonitoringPUTStatus(str, Enum):
    COMPLETED = "Completed"
    FAILED = "Failed"

    def __str__(self) -> str:
        return str(self.value)
