from enum import Enum


class NetworkStorageStatusV1PlatformPOSTUsageState(str, Enum):
    USAGEOVERTHRESHOLD = "UsageOverThreshold"
    USAGEUNDERTHRESHOLD = "UsageUnderThreshold"

    def __str__(self) -> str:
        return str(self.value)
