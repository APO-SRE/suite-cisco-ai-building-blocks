from enum import Enum


class Classification(str, Enum):
    PRIVACY_VIOLATION = "PRIVACY_VIOLATION"
    RELEVANCE_VIOLATION = "RELEVANCE_VIOLATION"
    SAFETY_VIOLATION = "SAFETY_VIOLATION"
    SECURITY_VIOLATION = "SECURITY_VIOLATION"

    def __str__(self) -> str:
        return str(self.value)
