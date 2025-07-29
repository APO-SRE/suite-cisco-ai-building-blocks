from enum import Enum


class SeverityConditionV1EventmonitoringPOSTSeverity(str, Enum):
    CRITICAL = "critical"
    MAJOR = "major"
    MINOR = "minor"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
