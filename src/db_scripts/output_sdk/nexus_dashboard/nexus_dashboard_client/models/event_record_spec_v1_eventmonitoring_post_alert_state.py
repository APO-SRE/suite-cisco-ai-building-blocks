from enum import Enum


class EventRecordSpecV1EventmonitoringPOSTAlertState(str, Enum):
    ACTIVE = "Active"
    CLEARED = "Cleared"

    def __str__(self) -> str:
        return str(self.value)
