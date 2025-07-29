from enum import Enum


class ClusterStatusWrapperV1PlatformGETState(str, Enum):
    ACTIVE = "Active"
    MIGRATINGTODUALSTACK = "MigratingToDualStack"

    def __str__(self) -> str:
        return str(self.value)
