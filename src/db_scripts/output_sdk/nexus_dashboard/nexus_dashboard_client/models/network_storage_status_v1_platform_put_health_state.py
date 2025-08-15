from enum import Enum


class NetworkStorageStatusV1PlatformPUTHealthState(str, Enum):
    CRITICAL = "Critical"
    HEALTHY = "Healthy"
    MAJOR = "Major"
    MINOR = "Minor"

    def __str__(self) -> str:
        return str(self.value)
