from enum import Enum


class ClusterNodeV4FederationPUTCurrentState(str, Enum):
    ACTIVE = "Active"
    DELETED = "Deleted"
    DISCOVERING = "Discovering"
    FAILOVER = "Failover"
    INCOMPATIBLE = "Incompatible"
    INIT = "Init"
    REBOOTING = "Rebooting"
    UNDISCOVERED = "Undiscovered"
    UNHEALTHY = "Unhealthy"
    UNKNOWN = "Unknown"
    UNREGISTERED = "Unregistered"

    def __str__(self) -> str:
        return str(self.value)
