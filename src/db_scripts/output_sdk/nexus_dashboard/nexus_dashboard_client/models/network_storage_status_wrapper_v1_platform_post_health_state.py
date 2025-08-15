from enum import Enum


class NetworkStorageStatusWrapperV1PlatformPOSTHealthState(str, Enum):
    CRITICAL = "Critical"
    HEALTHY = "Healthy"
    MAJOR = "Major"
    MINOR = "Minor"

    def __str__(self) -> str:
        return str(self.value)
