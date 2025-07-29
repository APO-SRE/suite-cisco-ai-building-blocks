from enum import Enum


class EventOccurrenceV1EventmonitoringGETSeverity(str, Enum):
    CRITICAL = "critical"
    MAJOR = "major"
    MINOR = "minor"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
