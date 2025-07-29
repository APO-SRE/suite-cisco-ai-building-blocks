from enum import Enum


class RecordStreamV1EventmonitoringGETStatus(str, Enum):
    COMPLETED = "Completed"
    FAILED = "Failed"

    def __str__(self) -> str:
        return str(self.value)
