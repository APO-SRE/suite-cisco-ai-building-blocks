from enum import Enum


class ClusterSpecV2PlatformPUTNetworkMode(str, Enum):
    DUALSTACK = "DualStack"
    SINGLESTACK_IPV4 = "SingleStack-IPV4"
    SINGLESTACK_IPV6 = "SingleStack-IPV6"

    def __str__(self) -> str:
        return str(self.value)
