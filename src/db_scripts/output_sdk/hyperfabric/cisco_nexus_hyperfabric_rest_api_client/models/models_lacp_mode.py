from enum import Enum


class ModelsLacpMode(str, Enum):
    LACP_ACTIVE = "LACP_ACTIVE"
    LACP_OFF = "LACP_OFF"
    LACP_PASSIVE = "LACP_PASSIVE"

    def __str__(self) -> str:
        return str(self.value)
