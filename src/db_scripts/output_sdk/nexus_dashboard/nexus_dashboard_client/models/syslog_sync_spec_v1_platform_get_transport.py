from enum import Enum


class SyslogSyncSpecV1PlatformGETTransport(str, Enum):
    TCP = "TCP"
    UDP = "UDP"

    def __str__(self) -> str:
        return str(self.value)
