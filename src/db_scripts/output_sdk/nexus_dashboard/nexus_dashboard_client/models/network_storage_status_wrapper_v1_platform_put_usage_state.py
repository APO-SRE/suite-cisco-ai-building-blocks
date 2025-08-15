from enum import Enum


class NetworkStorageStatusWrapperV1PlatformPUTUsageState(str, Enum):
    USAGEOVERTHRESHOLD = "UsageOverThreshold"
    USAGEUNDERTHRESHOLD = "UsageUnderThreshold"

    def __str__(self) -> str:
        return str(self.value)
