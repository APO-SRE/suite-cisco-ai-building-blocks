from enum import Enum


class SyslogSyncSpecV1PlatformGETForwardingFacility(str, Enum):
    LOCAL0 = "Local0"

    def __str__(self) -> str:
        return str(self.value)
