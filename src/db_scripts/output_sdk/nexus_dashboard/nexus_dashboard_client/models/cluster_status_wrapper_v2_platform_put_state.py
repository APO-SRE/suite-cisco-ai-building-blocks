from enum import Enum


class ClusterStatusWrapperV2PlatformPUTState(str, Enum):
    ACTIVE = "Active"
    MIGRATINGTODUALSTACK = "MigratingToDualStack"

    def __str__(self) -> str:
        return str(self.value)
