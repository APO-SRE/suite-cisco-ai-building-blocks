from enum import Enum


class SyslogSyncSpecWrapperV1PlatformPUTSeverity(str, Enum):
    ALERT = "Alert"
    CRITICAL = "Critical"

    def __str__(self) -> str:
        return str(self.value)
