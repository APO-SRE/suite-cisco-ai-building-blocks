from enum import Enum


class ModelsAdminState(str, Enum):
    DELETED = "DELETED"
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
