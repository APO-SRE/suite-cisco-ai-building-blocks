from enum import Enum


class EventRecordSpecV1EventmonitoringGETAlertState(str, Enum):
    ACTIVE = "Active"
    CLEARED = "Cleared"

    def __str__(self) -> str:
        return str(self.value)
