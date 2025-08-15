from enum import Enum


class ClusterSpecProxyServerV1PlatformGETType(str, Enum):
    HTTP = "HTTP"
    HTTPS = "HTTPS"

    def __str__(self) -> str:
        return str(self.value)
