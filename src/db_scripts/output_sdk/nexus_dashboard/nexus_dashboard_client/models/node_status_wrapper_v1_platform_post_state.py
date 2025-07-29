from enum import Enum


class NodeStatusWrapperV1PlatformPOSTState(str, Enum):
    ACTIVE = "Active"
    DELETED = "Deleted"
    DISCOVERING = "Discovering"
    FAILOVER = "Failover"
    INACTIVE = "Inactive"
    INCOMPATIBLE = "Incompatible"
    INIT = "Init"
    MIGRATINGTODUALSTACK = "MigratingToDualStack"
    REBOOTING = "Rebooting"
    UNDISCOVERED = "Undiscovered"
    UNHEALTHY = "Unhealthy"
    UNKNOWN = "Unknown"
    UNREGISTERED = "Unregistered"

    def __str__(self) -> str:
        return str(self.value)
