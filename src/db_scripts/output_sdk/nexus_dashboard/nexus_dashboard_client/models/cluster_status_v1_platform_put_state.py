from enum import Enum


class ClusterStatusV1PlatformPUTState(str, Enum):
    ACTIVE = "Active"
    MIGRATINGTODUALSTACK = "MigratingToDualStack"

    def __str__(self) -> str:
        return str(self.value)
