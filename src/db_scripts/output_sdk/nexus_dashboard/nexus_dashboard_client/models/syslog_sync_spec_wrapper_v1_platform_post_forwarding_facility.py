from enum import Enum


class SyslogSyncSpecWrapperV1PlatformPOSTForwardingFacility(str, Enum):
    LOCAL0 = "Local0"

    def __str__(self) -> str:
        return str(self.value)
