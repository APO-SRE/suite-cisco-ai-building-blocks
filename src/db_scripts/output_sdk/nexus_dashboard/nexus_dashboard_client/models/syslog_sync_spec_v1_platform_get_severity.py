from enum import Enum


class SyslogSyncSpecV1PlatformGETSeverity(str, Enum):
    ALERT = "Alert"
    CRITICAL = "Critical"

    def __str__(self) -> str:
        return str(self.value)
