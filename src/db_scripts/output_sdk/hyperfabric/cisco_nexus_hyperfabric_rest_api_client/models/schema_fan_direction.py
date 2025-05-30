from enum import Enum


class SchemaFanDirection(str, Enum):
    EXHAUST = "EXHAUST"
    INTAKE = "INTAKE"

    def __str__(self) -> str:
        return str(self.value)
