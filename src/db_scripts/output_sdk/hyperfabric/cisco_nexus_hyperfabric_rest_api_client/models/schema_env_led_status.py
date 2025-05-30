from enum import Enum


class SchemaEnvLedStatus(str, Enum):
    GREEN = "GREEN"
    OFF = "OFF"
    RED = "RED"

    def __str__(self) -> str:
        return str(self.value)
