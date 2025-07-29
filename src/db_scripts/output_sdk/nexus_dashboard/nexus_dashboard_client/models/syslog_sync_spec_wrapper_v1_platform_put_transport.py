from enum import Enum


class SyslogSyncSpecWrapperV1PlatformPUTTransport(str, Enum):
    TCP = "TCP"
    UDP = "UDP"

    def __str__(self) -> str:
        return str(self.value)
