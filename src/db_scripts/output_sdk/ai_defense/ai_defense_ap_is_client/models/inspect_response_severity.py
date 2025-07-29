from enum import Enum


class InspectResponseSeverity(str, Enum):
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    NONE_SEVERITY = "NONE_SEVERITY"

    def __str__(self) -> str:
        return str(self.value)
