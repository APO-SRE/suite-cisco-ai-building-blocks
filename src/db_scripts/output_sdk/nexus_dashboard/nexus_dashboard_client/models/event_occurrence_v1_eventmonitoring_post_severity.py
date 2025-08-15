from enum import Enum


class EventOccurrenceV1EventmonitoringPOSTSeverity(str, Enum):
    CRITICAL = "critical"
    MAJOR = "major"
    MINOR = "minor"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
